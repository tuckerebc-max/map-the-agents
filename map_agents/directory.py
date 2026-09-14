"""Bounded capture and rendering of the alltheagents.org site directory.

The published feed (https://alltheagents.org/agents.json, 828 entries as observed 2026-09-13) carries
no repository URLs. The immutable backing feed already captured by `collect.catalog` at
catalog/feeds/alltheagents.org/<sha>/agents.json is richer but is keyed by slug, not every slug has a
resolvable repository, and a handful of published slugs are missing from it entirely. Those missing
slugs still have a complete Markdown/frontmatter page at `agents/<slug>.md` in the very same site
repository tree, at the same immutable commit (observed live shape: real frontmatter carries
`platforms` as a list, "yes (details)"-shaped feature strings, `model_providers`, and a rich
`what_makes_it_special` field alongside a full Markdown body -- see
agents/nanoclaw.md at 0709cccb49aff08a4b10beb95a214005a810a363).

`capture` fetches the site tree and every page's bytes, verified against the Git blob SHA, through the
shared bounded Fetcher, and stops issuing new requests on budget exhaustion or a 403/429 rather than
stamping every unattempted page a failure. `resolve` then builds one read-only, no-network view keyed
by the union of published/backing/page slugs, re-verifying every cached byte before trusting it and
surfacing (not silently resolving) any cross-source discrepancy. `render` turns that view into small,
source-linked, Markdown-escaped pages that `maps.build` folds into the generated map.

A repo_key is only ever a `source_code_url` or `url` fallback already present in the backing feed or a
page's frontmatter, normalized the same way `intake.normalize`/`collect._entry_key` do elsewhere; it is
exposed even when this corpus has not tracked that repository yet (`repo_tracked=False`), so a parent
process can intake it, but the renderer only links into `map/repos/` when the repository is tracked.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError

from . import collect, core, intake

DIRECTORY_REPO = collect.CATALOG_REPO
PAGES_PREFIX = "agents/"
PAGES_SUFFIX = ".md"
DIR_CURSOR_FILE = "state/directory-cursor.json"
PUBLISHED_POINTER_FILE = "state/directory-published.json"
PUBLISHED_STORE_DIR = "catalog/directory/published"
PAGE_STORE_DIR = "catalog/directory/pages"
MAP_DIR = "map/directory"
PUBLISHED_FIELDS = ("name", "slug", "category", "maker", "license", "language", "stars", "description")
FEATURE_FIELDS = ("mcp_support", "plugin_support", "claude_code_plugin", "subagents", "hooks", "plan_mode")
SCALAR_FIELDS = ("name", "category", "maker", "license", "language", "model_providers")
MAX_PUBLISHED_BYTES = 8_000_000
MAX_PAGE_BYTES = 200_000
ENTRY_WORD_LIMIT = 400
HIGHLIGHT_WORD_CAP = 60
NAV_PAGE_WORD_LIMIT = 1800
ROOT_WORD_LIMIT = 2000
CONFLICT_INLINE_CAP = 5
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,199}$")
STORAGE_SLUG_CEILING = 81  # the old SLUG_RE's max length; slugs at or below this keep their exact old filename
STORAGE_PREFIX_LEN = 40    # readable prefix length for a hashed long-slug filename; keeps paths portable
PATH_POLICY_VERSION = 2    # bump forces exactly one tree refetch at an otherwise-unchanged commit (see _resolve_tree)
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.DOTALL)
_MD_UNSAFE_RE = re.compile(r"[\\`\[\]<>]")
EMPTY_INTERFACE = ((), None)
_yaml = YAML(typ="safe", pure=True)


class DirectoryError(core.WorkbenchError):
    code = 10


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-") or "unlabeled"


def _md_escape(value: object) -> str:
    """Neutralize Markdown link/code/HTML syntax in untrusted directory text before it is rendered."""
    if value is None:
        return ""
    text = str(value).replace("\r", " ").replace("\n", " ")
    return _MD_UNSAFE_RE.sub(lambda m: "\\" + m.group(0), text)


def _safe_page_slug(path: str) -> str | None:
    """The slug for an `agents/<slug>.md` tree path, or None if the path/slug is not safe to store."""
    if collect.path_problem(path) is not None or not path.startswith(PAGES_PREFIX) or not path.endswith(PAGES_SUFFIX):
        return None
    slug = path[len(PAGES_PREFIX):-len(PAGES_SUFFIX)]
    return slug if SLUG_RE.match(slug) else None


def _valid_page_meta(p: object) -> bool:
    """Defensive re-validation of one cached tree entry; a tampered state file must not build an unsafe path."""
    return (isinstance(p, dict) and isinstance(p.get("path"), str) and isinstance(p.get("slug"), str)
            and isinstance(p.get("git_sha"), str) and bool(collect.SHA_RE.match(p["git_sha"]))
            and isinstance(p.get("size"), int) and p["size"] >= 0 and _safe_page_slug(p["path"]) == p["slug"])


def _safe_digest(d: object) -> bool:
    return isinstance(d, str) and bool(HEX64_RE.match(d))


def _safe_commit(commit: object) -> str | None:
    return commit if isinstance(commit, str) and collect.SHA_RE.match(commit) else None


def _bytes_ok(data: bytes, git_sha: str, size: int) -> bool:
    return len(data) == size and collect.git_blob_sha(data) == git_sha


def _page_dir(root: Path, commit: str) -> Path:
    return Path(root) / PAGE_STORE_DIR / commit


def _page_storage_name(slug: str) -> str:
    """Stable on-disk filename for a captured page.

    Unchanged for every slug at or below the old 80-character ceiling, so every previously captured page
    keeps its exact old path and is reused without a re-download. A legitimate longer slug (real observed
    site data includes an 87-character one) is hashed-and-shortened instead of rejected or stored under an
    unbounded filename; the full real slug is never lost, only recorded in metadata rather than the path.
    """
    if len(slug) <= STORAGE_SLUG_CEILING:
        return f"{slug}.md"
    return f"{slug[:STORAGE_PREFIX_LEN]}-{hashlib.sha256(slug.encode('utf-8')).hexdigest()[:16]}.md"


def _page_path(root: Path, commit: str, slug: str) -> Path:
    return _page_dir(root, commit) / _page_storage_name(slug)


def _entry_stem(slug: str) -> str:
    """Collision-resistant, stable filename stem: two different raw slugs never collide after slugifying."""
    return f"{_slugify(slug)}-{hashlib.sha256(slug.encode('utf-8')).hexdigest()[:10]}"


def _group_file(name: object) -> str:
    return f"{_slugify(name)}-{hashlib.sha256(str(name).encode('utf-8')).hexdigest()[:10]}.md"


def _word_count(text: str) -> int:
    return len(text.split())


def _paginate(rel: str, lines: list[str], limit: int = NAV_PAGE_WORD_LIMIT) -> dict[str, str]:
    """Whole-line pagination with First/Previous/Next nav; mirrors maps._paginate for map/directory pages."""
    text = "\n".join(lines) + "\n"
    if _word_count(text) <= limit:
        return {rel: text}
    chunks: list[list[str]] = []
    chunk: list[str] = []
    words = 0
    for line in lines[1:]:
        size = _word_count(line)
        if words + size > limit - 50 and chunk:
            chunks.append(chunk)
            chunk, words = [], 0
        chunk.append(line)
        words += size
    if chunk:
        chunks.append(chunk)
    path = Path(rel)
    paths = [rel] + [path.with_name(f"{path.stem}.page-{n}.md").as_posix() for n in range(2, len(chunks) + 1)]
    out: dict[str, str] = {}
    for i, part in enumerate(chunks):
        nav = [f"[First page]({path.name})"]
        if i:
            nav.append(f"[Previous]({Path(paths[i - 1]).name})")
        if i + 1 < len(chunks):
            nav.append(f"[Next]({Path(paths[i + 1]).name})")
        header = lines[0] if lines else ""
        out[paths[i]] = header + f"\n\nPage {i + 1} of {len(chunks)}. " + " | ".join(nav) + "\n\n" + "\n".join(part) + "\n"
    return out


def state_digest(root: Path) -> str:
    """A digest of the directory layer's own state, so a fresh capture invalidates a stale generated view
    even when no repository record changed. Absent state hashes to a fixed value, so a corpus that never
    ran `directory` is never spuriously marked stale by this digest alone."""
    root = Path(root)
    parts = [(root / rel).read_bytes() if (root / rel).is_file() else b"<absent>"
             for rel in (DIR_CURSOR_FILE, PUBLISHED_POINTER_FILE, collect.CURSOR_FILE)]
    return _sha256(b"\x00".join(parts))


# --------------------------------------------------------------------------- repository identity aliases
#
# catalog/repository-aliases.json is a parent-verified, externally produced record of GitHub repository
# renames (schema: {"schema_version": 1, "resolutions": [{"requested_repo", "resolved_repo",
# "github_repository_id", "html_url", "authority", "observed_at", "outcome", "private"}, ...]}). It is
# read-only here: never edited, never used to invent a resolution GitHub did not actually report. Only
# outcome == "resolved" rows participate; a numeric id is the only rename-stable join key, so it is
# required. Shared by directory entries (to link a renamed lead to its canonical repo dossier) and by
# maps.py (to show "Formerly: ..." on a repo page), so it lives here rather than duplicated in both.

ALIASES_FILE = "catalog/repository-aliases.json"


def _valid_alias_row(row: object) -> bool:
    if not isinstance(row, dict) or row.get("outcome") != "resolved":
        return False
    gid = row.get("github_repository_id")
    if not isinstance(gid, int) or isinstance(gid, bool) or gid <= 0:
        return False
    return isinstance(row.get("requested_repo"), str) and isinstance(row.get("resolved_repo"), str)


def load_aliases(root: Path) -> dict:
    """Read-only union of catalog/repository-aliases.json, keyed for lookup by either end of a rename.

    Malformed rows (bad shape, non-numeric id, an outcome other than "resolved") are dropped, never
    coerced into a displayed alias. Two rows that resolve the same former identity to two different
    canonical repos keep the first one seen rather than overwriting silently.
    """
    try:
        data = collect._load_json(Path(root) / ALIASES_FILE)
    except core.CorruptState:
        data = None  # not valid JSON at all: treated exactly like an absent file, never invented or raised
    by_former: dict[str, dict] = {}
    by_canonical: dict[str, list[dict]] = defaultdict(list)
    if not isinstance(data, dict) or not isinstance(data.get("resolutions"), list):
        return {"by_former": by_former, "by_canonical": dict(by_canonical)}
    for row in data["resolutions"]:
        if not _valid_alias_row(row):
            continue
        former_key, _c1, _r1 = intake.normalize(f"https://github.com/{row['requested_repo']}")
        canonical_key, _c2, _r2 = intake.normalize(f"https://github.com/{row['resolved_repo']}")
        if not former_key or not canonical_key:
            continue
        html_url = row.get("html_url")
        html_url = html_url if isinstance(html_url, str) and html_url else f"https://github.com/{canonical_key}"
        record = {"former": former_key, "canonical": canonical_key, "github_repository_id": row["github_repository_id"],
                  "authority": row.get("authority") if isinstance(row.get("authority"), str) else None,
                  "html_url": html_url, "observed_at": row.get("observed_at") if isinstance(row.get("observed_at"), str) else None}
        if former_key in by_former and by_former[former_key]["canonical"] != canonical_key:
            continue
        by_former[former_key] = record
        if canonical_key != former_key:
            by_canonical[canonical_key].append(record)
    return {"by_former": by_former, "by_canonical": dict(by_canonical)}


def aliases_digest(root: Path) -> str:
    """Digest of the raw alias file bytes, so a refreshed alias file invalidates a stale generated view."""
    path = Path(root) / ALIASES_FILE
    return _sha256(path.read_bytes() if path.is_file() else b"<absent>")


def repo_identity(key: str, record: dict, aliases: dict) -> dict:
    """Merge a repo record's own collector-attached identity with the externally verified alias file.

    Prefers the record's own `github_repository_id`/`aliases` (added by the collector when it has them)
    but never invents a rename the alias file does not support. `renamed_to` is set only when this
    record's own key is itself a former identity that GitHub reports has moved elsewhere.
    """
    own_id = record.get("github_repository_id")
    own_id = own_id if isinstance(own_id, int) and not isinstance(own_id, bool) and own_id > 0 else None
    own_formers = [f for f in (record.get("aliases") or []) if isinstance(f, str) and f]
    as_former = aliases["by_former"].get(key)
    former_records = aliases["by_canonical"].get(key, [])
    github_id = own_id or (as_former["github_repository_id"] if as_former else None) or \
        (former_records[0]["github_repository_id"] if former_records else None)
    formers = list(dict.fromkeys(own_formers + [f["former"] for f in former_records]))
    renamed_to = as_former if (as_former and as_former["canonical"] != key) else None
    return {"github_repository_id": github_id, "formers": formers, "renamed_to": renamed_to}


# --------------------------------------------------------------------------- capture


def _parse_published(raw: bytes) -> dict[str, dict]:
    try:
        data = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise collect.MalformedPayload("published index is not JSON") from exc
    if not isinstance(data, list):
        raise collect.MalformedPayload("published index must be a JSON array")
    by_slug: dict[str, dict] = {}
    for n, entry in enumerate(data):
        if not isinstance(entry, dict) or any(k not in entry for k in PUBLISHED_FIELDS):
            raise collect.MalformedPayload(f"published entry {n} lacks a required field")
        slug = entry["slug"]
        if not isinstance(slug, str) or not slug:
            raise collect.MalformedPayload(f"published entry {n} has an invalid slug")
        if slug in by_slug:
            raise collect.MalformedPayload(f"published index contains duplicate slug {slug!r}")
        by_slug[slug] = entry
    return by_slug


def _resolve_tree(root: Path, fetch: collect.Fetcher, commit: str, cached: dict) -> tuple[list[dict], list[dict], bool]:
    """(pages, unsafe, truncated) for agents/*.md at `commit`; reused from cache only when the commit AND
    the path-safety policy both match. A `path_policy_version` bump (e.g. a widened safe slug length)
    forces exactly one real refetch even at an unchanged commit, so a page a stale cache once rejected as
    unsafe under an older, narrower policy is reconsidered instead of being silently declared covered."""
    if (cached.get("commit") == commit and cached.get("path_policy_version") == PATH_POLICY_VERSION
            and isinstance(cached.get("pages"), list) and isinstance(cached.get("unsafe"), list)):
        pages = [p for p in cached["pages"] if _valid_page_meta(p)]
        return pages, cached["unsafe"], bool(cached.get("truncated"))
    tree = fetch.get_json(f"https://{collect.API_HOST}/repos/{DIRECTORY_REPO}/git/trees/{commit}?recursive=1")
    if not isinstance(tree, dict) or not isinstance(tree.get("tree"), list):
        raise collect.MalformedPayload(f"directory tree malformed: {DIRECTORY_REPO}@{commit[:12]}")
    truncated = bool(tree.get("truncated"))
    pages, unsafe = [], []
    for item in tree["tree"]:
        if not isinstance(item, dict) or item.get("type") != "blob":
            continue
        path = item.get("path")
        if not isinstance(path, str) or not path.startswith(PAGES_PREFIX) or not path.endswith(PAGES_SUFFIX):
            continue
        slug = _safe_page_slug(path)
        git_sha = item.get("sha")
        if slug is None or not isinstance(git_sha, str) or not collect.SHA_RE.match(git_sha):
            unsafe.append({"path": path[:collect.MAX_PATH_CHARS], "reason": "unsafe-path-or-sha"})
            continue
        pages.append({"path": path, "slug": slug, "git_sha": git_sha, "size": int(item.get("size") or 0)})
    pages.sort(key=lambda p: p["slug"])
    return pages, unsafe, truncated


def _rate_limited(exc: collect.FetchFailed) -> bool:
    return "forbidden-or-rate-limited" in str(exc)


def capture(root: Path, limit: int, transport=None, budget: collect.Budget | None = None) -> dict:
    """Process up to `limit` pending agents/*.md pages this call, resuming from state/directory-cursor.json.

    Always fetches the published index fresh (bounded, content-addressed by digest, hash-verified before
    reuse); the site page tree is refetched only when the backing-feed commit has changed, and its
    `truncated` flag is persisted so a partial GitHub tree listing is never reported as full coverage.
    Every previously captured page is re-verified against its recorded Git blob SHA before being treated
    as already done; a mismatch raises immediately rather than being silently reused or re-downloaded
    over good bytes. A per-item fetch/verify failure is recorded against its slug and does not abort the
    batch, but hitting the network/time/request budget or a 403/429 stops issuing further requests this
    call instead of stamping every remaining, never-attempted page a failure.
    """
    root = Path(root)
    if not isinstance(limit, int) or limit <= 0:
        raise DirectoryError("limit must be a positive integer")
    fetch = collect.Fetcher(transport or collect.urllib_transport, budget, collect._token())
    with core.writer_lock(root):
        core.init_locked(root)
        catalog_cursor = collect._load_json(root / collect.CURSOR_FILE) or {}
        commit = _safe_commit(catalog_cursor.get("commit"))
        if commit is None:
            raise DirectoryError("no backing-feed commit recorded yet; run `catalog` at least once first")
        dcursor = collect._load_json(root / DIR_CURSOR_FILE) or {}
        pages, unsafe, truncated = _resolve_tree(root, fetch, commit, dcursor)
        pub_raw = fetch.get_bytes(collect.PUBLISHED_URL, MAX_PUBLISHED_BYTES, accept="application/json")
        published = _parse_published(pub_raw)  # malformed published data raises before any write
        digest = _sha256(pub_raw)
        store_dir = root / PUBLISHED_STORE_DIR / digest
        existing = store_dir / "agents.json"
        collect._safe_storage(root, store_dir)
        if existing.exists():
            if _sha256(existing.read_bytes()) != digest:
                raise collect.IntegrityError(f"cached published index at digest {digest[:12]} does not match its own name")
        else:
            core.atomic_write_bytes(existing, pub_raw)
            core.write_if_changed(store_dir / "index.json", core.dump_json(
                {"url": collect.PUBLISHED_URL, "digest": digest, "entries": len(published)}))
        core.write_if_changed(root / PUBLISHED_POINTER_FILE, core.dump_json(
            {"url": collect.PUBLISHED_URL, "digest": digest, "entries": len(published)}))
        known_slugs = {p["slug"] for p in pages}
        failures = {slug: reason for slug, reason in (dcursor.get("failures") or {}).items() if slug in known_slugs}
        page_dir = _page_dir(root, commit)
        status: dict[str, bool] = {}
        for p in pages:
            path = _page_path(root, commit, p["slug"])
            if not path.is_file():
                status[p["slug"]] = False
                continue
            if not _bytes_ok(path.read_bytes(), p["git_sha"], p["size"]):
                raise collect.IntegrityError(f"cached directory page bytes do not match recorded git blob sha: {p['slug']}")
            status[p["slug"]] = True
        pending_idx = [i for i, p in enumerate(pages) if not status[p["slug"]]]
        cache_fresh = dcursor.get("commit") == commit and dcursor.get("path_policy_version") == PATH_POLICY_VERSION
        start = min(int(dcursor.get("next_index", 0)), len(pages)) if cache_fresh else 0
        order = [i for i in pending_idx if i >= start] + [i for i in pending_idx if i < start]
        picked = order[:limit]
        newly_captured, newly_failed, stopped = [], [], None
        stop_at = None
        for i in picked:
            p = pages[i]
            url = f"https://{collect.RAW_HOST}/{DIRECTORY_REPO}/{commit}/{quote(p['path'], safe='/')}"
            try:
                data = fetch.get_bytes(url, min(p["size"], MAX_PAGE_BYTES) if p["size"] else MAX_PAGE_BYTES, accept="text/plain")
                if not _bytes_ok(data, p["git_sha"], p["size"]):
                    raise collect.IntegrityError(f"blob-mismatch: {p['path']}")
            except collect.BudgetExceeded as exc:
                stopped, stop_at = f"{type(exc).__name__}: {exc}", i
                break
            except collect.FetchFailed as exc:
                if _rate_limited(exc):
                    stopped, stop_at = f"{type(exc).__name__}: {exc}", i
                    break
                failures[p["slug"]] = f"{type(exc).__name__}: {exc}"
                newly_failed.append(p["slug"])
                continue
            except core.WorkbenchError as exc:
                failures[p["slug"]] = f"{type(exc).__name__}: {exc}"
                newly_failed.append(p["slug"])
                continue
            collect._safe_storage(root, page_dir)
            core.atomic_write_bytes(_page_path(root, commit, p["slug"]), data)
            failures.pop(p["slug"], None)
            newly_captured.append(p["slug"])
        next_index = stop_at if stop_at is not None else ((picked[-1] + 1) if picked else start)
        dcursor = {"repo": DIRECTORY_REPO, "commit": commit, "path_policy_version": PATH_POLICY_VERSION,
                   "pages": pages, "unsafe": unsafe, "truncated": truncated, "next_index": next_index, "failures": failures}
        core.write_if_changed(root / DIR_CURSOR_FILE, core.dump_json(dcursor))
        captured_count = sum(1 for p in pages if status[p["slug"]] or p["slug"] in newly_captured)
    return {
        "root": str(root), "commit": commit, "pages_total": len(pages), "unsafe_pages": len(unsafe),
        "tree_truncated": truncated, "captured": captured_count, "backlog": len(pages) - captured_count,
        "processed": len(newly_captured) + len(newly_failed), "newly_captured": newly_captured,
        "newly_failed": newly_failed, "stopped": stopped, "failures": len(failures),
        "published": {"url": collect.PUBLISHED_URL, "digest": digest, "entries": len(published)},
        "budget": fetch.budget.summary(),
    }


# --------------------------------------------------------------------------- resolve


def _load_published(root: Path) -> tuple[dict[str, dict], dict, str | None]:
    pointer = collect._load_json(root / PUBLISHED_POINTER_FILE)
    if not pointer or not _safe_digest(pointer.get("digest")):
        return {}, {}, None
    path = root / PUBLISHED_STORE_DIR / pointer["digest"] / "agents.json"
    collect._safe_storage(root, path.parent)
    if not path.is_file():
        return {}, pointer, "published-store-missing"
    raw = path.read_bytes()
    if _sha256(raw) != pointer["digest"]:
        return {}, pointer, "published-digest-mismatch"
    try:
        return _parse_published(raw), pointer, None
    except collect.MalformedPayload as exc:
        return {}, pointer, f"published-malformed: {exc}"


def _load_backing(root: Path, commit: str) -> tuple[dict[str, dict], str | None]:
    feed_dir = root / collect.FEED_DIR / commit
    path = feed_dir / "agents.json"
    if not path.is_file():
        return {}, None
    raw = path.read_bytes()
    meta = collect._load_json(feed_dir / "feed.json") or {}
    if isinstance(meta.get("digest"), str) and _sha256(raw) != meta["digest"]:
        return {}, "backing-digest-mismatch"
    try:
        entries = collect._parse_catalog(raw)
    except collect.MalformedPayload as exc:
        return {}, f"backing-malformed: {exc}"
    return {e["slug"]: e for e in entries}, None


def _parse_frontmatter(text: str) -> tuple[dict | None, str, str | None]:
    """(frontmatter, body, error). A missing/invalid frontmatter block is an explicit gap, not a raise."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text, "no-frontmatter-block"
    try:
        data = _yaml.load(match.group(1))
    except YAMLError as exc:
        return None, match.group(2), f"invalid-yaml: {exc}"
    if not isinstance(data, dict):
        return None, match.group(2), "frontmatter-not-a-mapping"
    return data, match.group(2), None


def _read_verified(root: Path, commit: str, p: dict) -> bytes | None:
    """None if never captured; raises IntegrityError if present but no longer matching its recorded hash."""
    path = _page_path(root, commit, p["slug"])
    if not path.is_file():
        return None
    data = path.read_bytes()
    if not _bytes_ok(data, p["git_sha"], p["size"]):
        raise collect.IntegrityError(f"cached page bytes do not match recorded git blob sha: {p['slug']}")
    return data


def _load_pages(root: Path, commit: str, pages_meta: list[dict]) -> tuple[dict[str, dict], dict[str, str]]:
    parsed: dict[str, dict] = {}
    malformed: dict[str, str] = {}
    for p in pages_meta:
        try:
            data = _read_verified(root, commit, p)
        except collect.IntegrityError:
            malformed[p["slug"]] = "cache-tampered"
            continue
        if data is None:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            malformed[p["slug"]] = "not-utf8"
            continue
        frontmatter, body, error = _parse_frontmatter(text)
        if error:
            malformed[p["slug"]] = error
        parsed[p["slug"]] = {"frontmatter": frontmatter or {}, "body": body.strip(), "path": p["path"], "error": error}
    return parsed, malformed


def _repo_from(entry: dict | None) -> tuple[str | None, str | None, str | None]:
    """(repo key, field, canonical url) via source_code_url then url fallback -- matches collect._entry_key."""
    if not isinstance(entry, dict):
        return None, None, None
    for name in ("source_code_url", "url"):
        url = entry.get(name)
        if isinstance(url, str) and url:
            key, canonical, _reason = intake.normalize(url)
            if key:
                return key, name, canonical
    return None, None, None


def _interface_of(e: dict | None) -> tuple[tuple[str, ...], str | None]:
    if not isinstance(e, dict):
        return EMPTY_INTERFACE
    platforms = e.get("platforms")
    if isinstance(platforms, list):
        plist = tuple(sorted(str(p) for p in platforms if isinstance(p, (str, int, float))))
    elif isinstance(platforms, str) and platforms:
        plist = (platforms,)
    else:
        plist = ()
    install = e.get("install_method")
    install = install if isinstance(install, str) and install else None
    return (plist, install)


def _feature_state(value: object) -> str:
    if value in (None, ""):
        return "unknown"
    s = str(value).strip().lower()
    if s.startswith("yes"):
        return "yes"
    if s.startswith("no"):
        return "no"
    return "reported"


def _first_differing(*values: object) -> bool:
    present = [v for v in values if v not in (None, "")]
    return len({json.dumps(v, sort_keys=True) for v in present}) > 1


def _build_entry(slug: str, pub: dict | None, back: dict | None, page: dict | None, pub_pointer: dict,
                  commit: str | None, repos: dict, aliases: dict) -> dict:
    page_fm = page["frontmatter"] if page else None

    def pick(*sources: tuple[dict | None, str]) -> object:
        for src, key in sources:
            if isinstance(src, dict) and src.get(key) not in (None, ""):
                return src.get(key)
        return None

    name = pick((page_fm, "name"), (back, "name"), (pub, "name")) or slug
    category = pick((page_fm, "category"), (back, "category"), (pub, "category"))
    maker = pick((page_fm, "maker"), (back, "maker"), (pub, "maker"))
    license_ = pick((page_fm, "license"), (back, "license"), (pub, "license"))
    language = pick((page_fm, "language"), (back, "language"), (pub, "language"))
    model_providers = pick((page_fm, "model_providers"), (back, "model_providers"), (pub, "model_providers"))
    i_page, i_back = _interface_of(page_fm), _interface_of(back)
    interface = i_page if i_page != EMPTY_INTERFACE else i_back

    features: dict[str, dict] = {}
    for f in FEATURE_FIELDS:
        pv, bv, gv = (pub or {}).get(f), (back or {}).get(f), (page_fm or {}).get(f)
        value = gv if gv not in (None, "") else (bv if bv not in (None, "") else pv)
        features[f] = {"value": value, "state": _feature_state(value), "published": pv, "backing": bv, "page": gv}

    repo_back_key, repo_back_field, _ = _repo_from(back)
    repo_page_key, repo_page_field, _ = _repo_from(page_fm)
    if repo_back_key:
        repo_key, repo_field, repo_source = repo_back_key, repo_back_field, "backing"
    elif repo_page_key:
        repo_key, repo_field, repo_source = repo_page_key, repo_page_field, "page"
    else:
        repo_key, repo_field, repo_source = None, None, None

    conflicts: dict[str, dict] = {}
    for field in SCALAR_FIELDS:
        got = (pub.get(field) if isinstance(pub, dict) else None, back.get(field) if isinstance(back, dict) else None,
               page_fm.get(field) if isinstance(page_fm, dict) else None)
        if _first_differing(*got):
            conflicts[field] = {"published": got[0], "backing": got[1], "page": got[2]}
    for f in FEATURE_FIELDS:
        got = (features[f]["published"], features[f]["backing"], features[f]["page"])
        if _first_differing(*got):
            conflicts[f] = {"published": got[0], "backing": got[1], "page": got[2]}
    if i_back != EMPTY_INTERFACE and i_page != EMPTY_INTERFACE and i_back != i_page:
        conflicts["interface"] = {"published": None, "backing": i_back, "page": i_page}
    if repo_back_key and repo_page_key and repo_back_key != repo_page_key:
        conflicts["repo_identity"] = {"published": None, "backing": repo_back_key, "page": repo_page_key}

    body_text = (page or {}).get("body") or ""
    highlight = (page_fm or {}).get("what_makes_it_special")
    highlight = highlight if isinstance(highlight, str) and highlight else None
    pub_desc = (pub or {}).get("description") if isinstance((pub or {}).get("description"), str) else None
    back_desc = (back or {}).get("description") if isinstance((back or {}).get("description"), str) else None
    if body_text:
        description, description_source = body_text, f"captured site page body ({page['path']})"
    elif highlight:
        description, description_source = highlight, "site page `what_makes_it_special`"
    elif pub_desc:
        description, description_source = pub_desc, "published index `description`"
    elif back_desc:
        description, description_source = back_desc, "backing feed `description`"
    else:
        description, description_source = "", None
    extra_highlight = highlight if highlight and highlight != description else None

    locators: dict[str, tuple[str, str]] = {}
    if pub is not None and _safe_digest(pub_pointer.get("digest")):
        locators["published"] = (f"published index (sha256:{pub_pointer['digest'][:12]})", collect.PUBLISHED_URL)
    if back is not None and commit:
        locators["backing"] = (f"backing feed @ {commit[:12]}",
                                f"https://github.com/{collect.CATALOG_REPO}/blob/{commit}/{collect.CATALOG_PATH}")
    if page is not None and commit:
        locators["page"] = (f"site page @ {commit[:12]}",
                             f"https://github.com/{collect.CATALOG_REPO}/blob/{commit}/{quote(page['path'], safe='/')}")

    # If this lead's own normalized key is a former identity that GitHub reports has moved, offer the
    # canonical repo dossier (when it is actually tracked here) while keeping the original lead visible.
    alias_hit = aliases["by_former"].get(repo_key) if repo_key else None
    repo_canonical_key = alias_hit["canonical"] if (alias_hit and alias_hit["canonical"] != repo_key) else None

    return {
        "slug": slug, "name": name, "category": category, "maker": maker, "license": license_, "language": language,
        "model_providers": model_providers, "interface": {"platforms": interface[0], "install_method": interface[1]},
        "features": features, "membership": {"published": pub is not None, "backing": back is not None, "pages": page is not None},
        "conflicts": conflicts, "repo_key": repo_key, "repo_field": repo_field, "repo_source": repo_source,
        "repo_tracked": bool(repo_key and repo_key in repos),
        "repo_canonical_key": repo_canonical_key, "repo_canonical_tracked": bool(repo_canonical_key and repo_canonical_key in repos),
        "repo_alias": alias_hit if repo_canonical_key else None,
        "description": description, "description_source": description_source, "highlight": extra_highlight,
        "page_error": (page or {}).get("error"), "locators": locators,
    }


def resolve(root: Path) -> dict:
    """Read-only union of published/backing/page slugs. No network; safe to call at any time.

    Every cached page's bytes are re-verified against its recorded Git blob SHA before its frontmatter or
    body is trusted; a mismatch is reported per-slug as a gap, never silently published. The published
    and backing stores are likewise hash-checked against their own recorded digests before use.
    """
    root = Path(root)
    dcursor = collect._load_json(root / DIR_CURSOR_FILE) or {}
    commit = _safe_commit(dcursor.get("commit"))
    pages_meta = [p for p in (dcursor.get("pages") or []) if _valid_page_meta(p)] if isinstance(dcursor.get("pages"), list) else []
    published, pub_pointer, pub_error = _load_published(root)
    backing, backing_error = _load_backing(root, commit) if commit else ({}, None)
    parsed_pages, malformed_pages = _load_pages(root, commit, pages_meta) if commit else ({}, {})
    repos = core.load_repos(root)
    aliases = load_aliases(root)
    slugs = sorted(set(published) | set(backing) | set(parsed_pages))
    entries = {slug: _build_entry(slug, published.get(slug), backing.get(slug), parsed_pages.get(slug),
                                   pub_pointer, commit, repos, aliases) for slug in slugs}
    failures = dict(dcursor.get("failures") or {})
    attempted = {p["slug"] for p in pages_meta}
    captured = set(parsed_pages) | set(malformed_pages)
    missing_pages = sorted(s for s in attempted if s not in captured and s not in failures)
    failed_pages = sorted(s for s in attempted if s in failures)
    return {
        "root": str(root), "commit": commit, "entries": entries,
        "counts": {"published": len(published), "backing": len(backing), "pages": len(parsed_pages),
                   "union": len(slugs), "with_repo": sum(1 for e in entries.values() if e["repo_key"]),
                   "tracked_repo": sum(1 for e in entries.values() if e["repo_tracked"]),
                   "renamed_leads": sum(1 for e in entries.values() if e["repo_canonical_key"]),
                   "conflicts": sum(1 for e in entries.values() if e["conflicts"])},
        "tree_truncated": bool(dcursor.get("truncated")),
        "unsafe_pages": dcursor.get("unsafe") or [], "malformed_pages": malformed_pages,
        "missing_pages": missing_pages, "failed_pages": failed_pages,
        "published_integrity_error": pub_error, "backing_integrity_error": backing_error,
    }


# --------------------------------------------------------------------------- render


def _evidence_marker(entry: dict) -> str:
    members = [k for k, v in entry["membership"].items() if v]
    return f"{members[0]}-only" if len(members) == 1 else "+".join(members)


def _render_interface(interface: dict) -> str:
    parts = []
    if interface.get("platforms"):
        parts.append("platforms=" + ", ".join(_md_escape(p) for p in interface["platforms"]))
    if interface.get("install_method"):
        parts.append("install=" + _md_escape(interface["install_method"]))
    return "; ".join(parts) if parts else "unknown"


def _render_repo_lines(entry: dict) -> list[str]:
    if entry["repo_key"] is None:
        return ["No repository record: repository source unavailable in this directory capture, not an absence of capability.", ""]
    lead = f"[{entry['repo_key']}](https://github.com/{entry['repo_key']}) (source: {entry['repo_source']}, field: `{entry['repo_field']}`)"
    if entry["repo_canonical_key"]:
        alias = entry["repo_alias"]
        gid = f"github id {alias['github_repository_id']}" if alias.get("github_repository_id") else "no github id recorded"
        if entry["repo_canonical_tracked"]:
            c_owner, c_name = entry["repo_canonical_key"].split("/")
            return [f"Repository map entry (renamed): original lead {lead} now resolves to "
                     f"[{entry['repo_canonical_key']}](../../repos/{c_owner}/{c_name}.md) "
                     f"({gid}, verified [{alias['html_url']}]({alias['html_url']})).", ""]
        return [f"Repository lead (renamed, not yet tracked under the new identity): {lead} now resolves to "
                 f"[{entry['repo_canonical_key']}](https://github.com/{entry['repo_canonical_key']}) "
                 f"({gid}, verified [{alias['html_url']}]({alias['html_url']})).", ""]
    owner, name = entry["repo_key"].split("/")
    if entry["repo_tracked"]:
        return [f"Repository map entry: [{entry['repo_key']}](../../repos/{owner}/{name}.md) "
                 f"(source: {entry['repo_source']}, field: `{entry['repo_field']}`).", ""]
    return [f"Repository lead (normalized, not yet tracked in this corpus): {lead}.", ""]


def _render_conflicts(entry: dict, stem: str) -> tuple[list[str], str | None]:
    conflicts = entry["conflicts"]
    if not conflicts:
        return [], None
    items = sorted(conflicts.items())
    inline, overflow = items[:CONFLICT_INLINE_CAP], items[CONFLICT_INLINE_CAP:]
    lines = ["Discrepancy between directory sources (not overwritten):", ""]
    for field, vals in inline:
        lines.append(f"- {field}: published={_md_escape(vals.get('published'))}, backing={_md_escape(vals.get('backing'))}, "
                      f"page={_md_escape(vals.get('page'))}")
    overflow_text = None
    if overflow:
        overflow_rel = f"{stem}.conflicts.md"
        lines.append(f"- ... {len(overflow)} more discrepant field(s); see [full conflict detail]({overflow_rel})")
        detail = [f"# Directory conflicts: {_md_escape(entry['name'])} (`{_md_escape(entry['slug'])}`)", "",
                  f"[Back to entry]({stem}.md)", "", "All discrepant fields (not overwritten):", ""]
        for field, vals in items:
            detail.append(f"- {field}: published={_md_escape(vals.get('published'))}, backing={_md_escape(vals.get('backing'))}, "
                           f"page={_md_escape(vals.get('page'))}")
        overflow_text = "\n".join(detail) + "\n"
    lines.append("")
    return lines, overflow_text


def _source_links(entry: dict) -> list[str]:
    return [f"[{label}]({url})" for label, url in entry["locators"].values()]


def _render_entry(entry: dict) -> tuple[str, str | None]:
    stem = _entry_stem(entry["slug"])
    head = [f"# {_md_escape(entry['name'])} (`{_md_escape(entry['slug'])}`)", "",
            "[Back to directory index](../index.md)", "", f"Directory membership: {_evidence_marker(entry)}.", "",
            f"- Category: {_md_escape(entry['category']) if entry['category'] else 'unknown'}",
            f"- Provider/maker: {_md_escape(entry['maker']) if entry['maker'] else 'unknown'}",
            f"- License: {_md_escape(entry['license']) if entry['license'] else 'unknown'}",
            f"- Language: {_md_escape(entry['language']) if entry['language'] else 'unknown'}",
            f"- Interface: {_render_interface(entry['interface'])}",
            f"- Model providers: {_md_escape(entry['model_providers']) if entry['model_providers'] else 'unknown'}",
            "- Feature flags (directory-reported):"]
    for field, v in entry["features"].items():
        shown = _md_escape(v["value"]) if v["state"] != "unknown" else "unknown"
        head.append(f"  - {field}: {shown} ({v['state']})")
    head.append("")
    head += _render_repo_lines(entry)
    conflict_lines, overflow_text = _render_conflicts(entry, stem)
    head += conflict_lines
    if entry["page_error"]:
        head += [f"Gap: this entry's site page could not be fully read ({entry['page_error']}).", ""]
    sources = _source_links(entry)
    sources_line = "Sources: " + ("; ".join(sources) if sources else "none recorded")
    desc_header = ["## Description", ""]
    reserved = _word_count("\n".join(head + desc_header + [sources_line]))
    budget = max(0, ENTRY_WORD_LIMIT - reserved)
    desc_lines: list[str] = []
    if entry["highlight"]:
        words = _md_escape(entry["highlight"]).split()
        prefix = "Highlight (site page `what_makes_it_special`): "
        take = min(len(words), HIGHLIGHT_WORD_CAP, max(0, budget - _word_count(prefix) - 1))
        if take:
            desc_lines.append(prefix + " ".join(words[:take]) +
                               (" ..." if take < len(words) else ""))
            budget = max(0, budget - _word_count(desc_lines[-1]))
            desc_lines.append("")
    if entry["description"]:
        words = _md_escape(entry["description"]).split()
        label = entry["description_source"] or "directory catalog text"
        prefix = f"({label}, not a verified repo-code finding)"
        take = min(len(words), max(0, budget - _word_count(prefix) - 1))
        if take:
            desc_lines.append(prefix)
            desc_lines.append(" ".join(words[:take]) + (" ..." if take < len(words) else ""))
    elif not desc_lines and budget >= 3:
        desc_lines.append("(no description recorded)")
    body = "\n".join(head + desc_header + desc_lines + [sources_line]) + "\n"
    return body, overflow_text


def _render_index(view: dict) -> str:
    c = view["counts"]
    lines = [
        "# Directory -- alltheagents.org catalog layer", "",
        f"Union of {c['union']} slug(s): published={c['published']}, backing={c['backing']}, pages={c['pages']}.",
        f"{c['with_repo']} entry(ies) resolve a normalized repository lead ({c['tracked_repo']} already tracked "
        f"in this corpus); {c['conflicts']} have at least one cross-source discrepancy.", "",
        "All facts on this page are attributed to the directory catalog, not to inspected repository code.", "",
        "Navigation: " + " | ".join(f"[{s}]({s}/index.md)" for s in ("entries", "classes", "providers", "features")), "",
    ]
    if view["tree_truncated"]:
        lines.append("Warning: the last site-tree listing was truncated by GitHub's API; page coverage below is partial.")
    if view["missing_pages"]:
        lines.append(f"{len(view['missing_pages'])} known site page(s) not yet attempted; run `directory` again to resume.")
    if view["failed_pages"]:
        lines.append(f"{len(view['failed_pages'])} site page(s) failed to fetch or verify; run `directory` again to retry.")
    if view["unsafe_pages"]:
        lines.append(f"{len(view['unsafe_pages'])} site path(s) rejected as unsafe and excluded from capture.")
    if view["malformed_pages"]:
        lines.append(f"{len(view['malformed_pages'])} captured page(s) have malformed frontmatter or failed cache verification.")
    if view.get("published_integrity_error"):
        lines.append(f"Published index integrity problem: {view['published_integrity_error']} (published facts withheld).")
    if view.get("backing_integrity_error"):
        lines.append(f"Backing feed integrity problem: {view['backing_integrity_error']} (backing facts withheld).")
    lines += ["", "[Back to map index](../index.md)"]
    return "\n".join(lines) + "\n"


def _render_group_index(title: str, groups: dict[str, list[str]]) -> str:
    lines = [f"# Directory -- {title}", "", "[Back to directory index](../index.md)", ""]
    for name in sorted(groups, key=str):
        lines.append(f"- [{_md_escape(name)}]({_group_file(name)}) ({len(groups[name])} entrie(s))")
    if not groups:
        lines.append("- none recorded")
    return "\n".join(lines) + "\n"


def _render_group_page(title: str, name: object, slugs: list[str]) -> list[str]:
    lines = [f"# Directory {title}: {_md_escape(name)}", "", "[Back to index](index.md)", "[Back to directory index](../index.md)", ""]
    for slug in sorted(slugs):
        lines.append(f"- [{_md_escape(slug)}](../entries/{_entry_stem(slug)}.md)")
    return lines


def render(root: Path) -> dict:
    """Render map/directory/** from the resolved union view. Returns pages for maps.build to fold in."""
    root = Path(root)
    view = resolve(root)
    entries = view["entries"]
    pages: dict[str, str] = {}
    pages.update(_paginate(f"{MAP_DIR}/index.md", _render_index(view).splitlines(), limit=ROOT_WORD_LIMIT))
    entries_lines = ["# Directory -- full entry index", "", "[Back to directory index](../index.md)", ""]
    for slug in sorted(entries):
        e = entries[slug]
        stem = _entry_stem(slug)
        entries_lines.append(f"- [{_md_escape(e['name'])} (`{_md_escape(slug)}`)]({stem}.md) -- {_evidence_marker(e)}")
        text, overflow = _render_entry(e)
        pages[f"{MAP_DIR}/entries/{stem}.md"] = text
        if overflow:
            pages[f"{MAP_DIR}/entries/{stem}.conflicts.md"] = overflow
    pages.update(_paginate(f"{MAP_DIR}/entries/index.md", entries_lines))
    by_class: dict[str, list[str]] = defaultdict(list)
    by_provider: dict[str, list[str]] = defaultdict(list)
    by_feature: dict[str, list[str]] = defaultdict(list)
    for slug, e in entries.items():
        by_class[e["category"] or "uncategorized"].append(slug)
        by_provider[e["maker"] or "unknown"].append(slug)
        for feat, v in e["features"].items():
            if v["state"] == "yes":
                by_feature[feat].append(slug)
    pages.update(_paginate(f"{MAP_DIR}/classes/index.md", _render_group_index("classes", by_class).splitlines(), limit=ROOT_WORD_LIMIT))
    for name, slugs in by_class.items():
        pages.update(_paginate(f"{MAP_DIR}/classes/{_group_file(name)}", _render_group_page("class", name, slugs)))
    pages.update(_paginate(f"{MAP_DIR}/providers/index.md", _render_group_index("providers", by_provider).splitlines(), limit=ROOT_WORD_LIMIT))
    for name, slugs in by_provider.items():
        pages.update(_paginate(f"{MAP_DIR}/providers/{_group_file(name)}", _render_group_page("provider", name, slugs)))
    pages.update(_paginate(f"{MAP_DIR}/features/index.md", _render_group_index("features", by_feature).splitlines(), limit=ROOT_WORD_LIMIT))
    for name, slugs in by_feature.items():
        pages.update(_paginate(f"{MAP_DIR}/features/{_group_file(name)}", _render_group_page("feature", name, slugs)))
    return {"pages": pages, "counts": view["counts"], "commit": view["commit"], "tree_truncated": view["tree_truncated"],
            "missing_pages": len(view["missing_pages"]), "failed_pages": len(view["failed_pages"]),
            "malformed_pages": len(view["malformed_pages"])}


# --------------------------------------------------------------------------- lead intake

INGEST_ORIGIN = "directory-resolve"
INGEST_PROJECT = "directory-intake"


def ingest_new_leads(root: Path, limit: int = 50) -> dict:
    """Send normalized public repo keys already resolved by `resolve()` into canonical catalog intake.

    A directory-only lead (published/page-sourced, no backing-feed counterpart) would otherwise stay a
    generated page forever with no catalog record. This is read-only over `resolve()`'s already-verified
    view: no raw body/private text, no other URL is ever followed, and a lead whose normalized key is
    already tracked -- directly, or through a verified alias whose canonical is already tracked -- is
    filtered out, not re-invented. Candidates beyond `limit` are reported `deferred`, not silently
    dropped; because the filter is "already tracked", a later call naturally advances past whatever a
    prior call already ingested, without needing a separate cursor.
    """
    root = Path(root)
    if not isinstance(limit, int) or limit <= 0:
        raise DirectoryError("limit must be a positive integer")
    view = resolve(root)
    repos = core.load_repos(root)
    candidates: list[str] = []
    for slug in sorted(view["entries"]):
        e = view["entries"][slug]
        key = e.get("repo_key")
        if not key or key in repos:
            continue
        if e.get("repo_canonical_key") and e.get("repo_canonical_tracked"):
            continue  # a verified alias already resolves to a tracked canonical repo
        candidates.append(key)
    candidates = sorted(set(candidates))
    picked, deferred = candidates[:limit], candidates[limit:]
    result = {"root": str(root), "candidates": len(candidates), "picked": len(picked), "deferred": len(deferred),
              "new_repos": [], "accepted": [], "changed": False}
    if picked:
        text = "\n".join(f"https://github.com/{key}" for key in picked)
        ingested = intake.ingest(root, text, INGEST_ORIGIN, INGEST_PROJECT)
        result.update(new_repos=ingested["new_repos"], accepted=ingested["accepted"], changed=ingested["changed"])
    return result
