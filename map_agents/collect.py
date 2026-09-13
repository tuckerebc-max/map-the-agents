"""Bounded public collectors: the backing catalog feed and immutable GitHub source snapshots.

All network traffic goes through an injected transport under byte/time/request/retry budgets.
A token, if configured, is sent only to api.github.com. Redirects are refused. Fetched bytes are
stored as data for the wiki kernel; nothing fetched is ever executed or interpreted as commands.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, urlsplit

from . import core, intake

API_HOST = "api.github.com"
RAW_HOST = "raw.githubusercontent.com"
PUBLISHED_URL = "https://alltheagents.org/agents.json"
ALLOWED_HOSTS = {API_HOST, RAW_HOST, "alltheagents.org"}
CATALOG_REPO = "prime-radiant-inc/alltheagents.org"
CATALOG_PATH = "_data/agents.json"
CATALOG_LABEL = "alltheagents.org-backing"
CATALOG_FIELDS = ("name", "slug", "category", "url", "source_code_url", "description", "license", "source_urls")
SUPPORTED_CLASSES = {"agent", "multiplexer", "agent-sdk"}
CURSOR_FILE = "state/catalog-cursor.json"
PUBLISHED_FILE = "state/catalog-published.json"
FEED_DIR = "catalog/feeds/alltheagents.org"
SOURCE_DIR = "sources/github"
BLOB_CACHE_DIR = "state/blob-cache"
SNAPSHOT_FILE = "snapshot.json"
RCW_MANIFEST = "manifest.json"
RCW_SUFFIXES = {".md", ".txt", ".html", ".htm"}
DOC_SUFFIXES = {".md", ".txt", ".rst", ".markdown"}
DOC_DIRS = ("docs/", "doc/")
SOURCE_SUFFIXES = DOC_SUFFIXES | RCW_SUFFIXES | {
    ".py", ".ts", ".tsx", ".js", ".mjs", ".go", ".rs", ".java", ".kt", ".rb", ".cs", ".sh",
    ".toml", ".yaml", ".yml", ".json", ".cfg", ".ini",
}
README_NAMES = ("README.md", "README.markdown", "README.rst", "README.txt", "README")
MAX_FEED_BYTES = 8_000_000
MAX_API_BYTES = 4_000_000
MAX_DESCRIPTION = 300
MAX_OMITTED_LISTED = 200
MAX_PATH_CHARS = 512
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
RESERVED_DEVICES = re.compile(r"(?i)^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\..*)?$")
UNSAFE_CHARS = re.compile(r"[\x00-\x1f\x7f\\:*?\"<>|]")
SLUG_STRIP = re.compile(r"[^a-z0-9._-]+")


class CollectError(core.WorkbenchError):
    code = 8


class BudgetExceeded(CollectError):
    code = 9


class FetchFailed(CollectError):
    pass


class PrivateRepo(CollectError):
    pass


class InvalidPath(CollectError):
    pass


class MalformedPayload(CollectError):
    pass


class IntegrityError(CollectError):
    pass


class TransportError(Exception):
    """Raised by a transport for connection-level failures; retried within the budget."""


@dataclass(frozen=True)
class Response:
    status: int
    body: bytes
    headers: dict = field(default_factory=dict)


@dataclass
class Budget:
    """Finite network allowance for one collector call."""

    max_bytes: int = 12_000_000
    max_seconds: float = 120.0
    max_requests: int = 60
    retries: int = 2
    bytes_used: int = 0
    requests: int = 0
    started: float = field(default_factory=time.monotonic)

    def remaining_seconds(self) -> float:
        return self.max_seconds - (time.monotonic() - self.started)

    def summary(self) -> dict:
        return {"bytes_used": self.bytes_used, "max_bytes": self.max_bytes, "requests": self.requests,
                "max_requests": self.max_requests, "max_seconds": self.max_seconds, "retries": self.retries}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # noqa: D401 - urllib hook
        return None


def urllib_transport(url: str, headers: dict, timeout: float, max_bytes: int) -> Response:
    """Default transport: one GET, no redirect following, reads at most max_bytes."""
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.build_opener(_NoRedirect).open(request, timeout=timeout) as resp:
            return Response(resp.status, resp.read(max_bytes), dict(resp.headers))
    except urllib.error.HTTPError as exc:
        return Response(exc.code, exc.read(max_bytes), dict(exc.headers))
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise TransportError(type(exc).__name__) from exc


class Fetcher:
    """Budgeted GET client. Errors carry only public locators, never headers or tokens."""

    def __init__(self, transport, budget: Budget | None, token: str | None) -> None:
        self.transport, self.budget, self._token = transport, budget or Budget(), token

    def get_bytes(self, url: str, max_bytes: int, accept: str = "application/vnd.github+json") -> bytes:
        parts = urlsplit(url)
        host = (parts.hostname or "").lower()
        if parts.scheme != "https" or host not in ALLOWED_HOSTS:
            raise CollectError(f"host-not-allowed: {host or '?'}")
        locator = f"{parts.scheme}://{host}{parts.path}"
        headers = {"User-Agent": "map-agents-collector", "Accept": accept}
        if self._token and host == API_HOST:
            headers["Authorization"] = f"Bearer {self._token}"
        budget, attempts = self.budget, 0
        while True:
            # Every attempt re-derives its allowance: failed bodies consume bytes and time too.
            allowance = budget.max_bytes - budget.bytes_used
            if allowance <= 0:
                raise BudgetExceeded(f"byte-budget exhausted before {locator}")
            bound = min(max_bytes, allowance)  # max_bytes may be 0: a zero-byte blob is a valid exact size
            remaining = budget.remaining_seconds()
            if remaining <= 0:
                raise BudgetExceeded(f"time-budget exhausted before {locator}")
            if budget.requests >= budget.max_requests:
                raise BudgetExceeded(f"request-budget exhausted before {locator}")
            budget.requests += 1
            attempts += 1
            try:
                resp = self.transport(url, headers, min(remaining, 30.0), bound + 1)
            except TransportError as exc:
                resp, failure = None, f"transport-{exc}"
            else:
                budget.bytes_used += len(resp.body)
                if len(resp.body) > bound:
                    if bound < max_bytes:
                        raise BudgetExceeded(f"byte-budget exceeded at {locator} (http-{resp.status})")
                    raise MalformedPayload(f"oversized-payload over {bound} bytes: {locator}")
                failure = f"http-{resp.status}" if resp.status >= 500 else None
            if budget.remaining_seconds() <= 0:
                raise BudgetExceeded(f"time-budget exceeded during {locator}")
            if failure is None:
                break
            if attempts > budget.retries:
                raise FetchFailed(f"{failure} after {attempts} attempts: {locator}")
        if 300 <= resp.status < 400:
            raise FetchFailed(f"redirect-refused http-{resp.status}: {locator}")
        if resp.status in (403, 429):
            raise FetchFailed(f"http-{resp.status} forbidden-or-rate-limited: {locator}")
        if resp.status != 200:
            raise FetchFailed(f"http-{resp.status}: {locator}")
        return resp.body

    def get_json(self, url: str, max_bytes: int = MAX_API_BYTES) -> object:
        try:
            return json.loads(self.get_bytes(url, max_bytes).decode("utf-8"))
        except (ValueError, UnicodeDecodeError) as exc:
            raise MalformedPayload(f"not-json: {urlsplit(url).path}") from exc


def _token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or None


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha(data: bytes) -> str:
    """Git object identity: sha1 over the 'blob <len>\\0' header plus the bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _load_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_bytes().decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise core.CorruptState(f"{path} is not valid JSON") from exc
    return data if isinstance(data, dict) else None


def _resolve_head(fetch: Fetcher, key: str) -> tuple[dict, str, str, str | None]:
    """Return (repo metadata, default branch, commit SHA, commit date) for a public repository."""
    meta = fetch.get_json(f"https://{API_HOST}/repos/{key}")
    if not isinstance(meta, dict) or not isinstance(meta.get("default_branch"), str):
        raise MalformedPayload(f"repository metadata malformed: {key}")
    if meta.get("private") is not False:
        raise PrivateRepo(f"not a public repository: {key}")
    branch = meta["default_branch"]
    info = fetch.get_json(f"https://{API_HOST}/repos/{key}/branches/{quote(branch, safe='')}")
    commit = info.get("commit") if isinstance(info, dict) else None
    sha = commit.get("sha") if isinstance(commit, dict) else None
    if not isinstance(sha, str) or not SHA_RE.match(sha):
        raise MalformedPayload(f"branch commit malformed: {key}")
    inner = commit.get("commit") or {}
    date = ((inner.get("committer") or {}).get("date")) if isinstance(inner, dict) else None
    return meta, branch, sha, date if isinstance(date, str) else None


# --------------------------------------------------------------------------- catalog

def _parse_catalog(raw: bytes) -> list[dict]:
    try:
        data = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise MalformedPayload(f"catalog feed is not JSON: {CATALOG_PATH}") from exc
    if not isinstance(data, list):
        raise MalformedPayload("catalog feed must be a JSON array")
    for n, entry in enumerate(data):
        if not isinstance(entry, dict) or any(k not in entry for k in CATALOG_FIELDS):
            raise MalformedPayload(f"catalog entry {n} lacks required fields")
        if not isinstance(entry["slug"], str) or not entry["slug"] or not isinstance(entry["category"], str):
            raise MalformedPayload(f"catalog entry {n} has invalid slug/category")
    return sorted(data, key=lambda e: e["slug"])


def _catalog_source(entry: dict, sha: str, via: str) -> dict:
    desc = entry.get("description") if isinstance(entry.get("description"), str) else ""
    return {
        "kind": "catalog", "catalog": CATALOG_LABEL, "slug": entry["slug"], "name": entry.get("name"),
        "category": entry["category"], "license": entry.get("license"), "description": desc[:MAX_DESCRIPTION],
        "repo_field": via, "commit": sha, "locator": f"https://github.com/{CATALOG_REPO}/blob/{sha}/{CATALOG_PATH}",
    }


def _entry_key(entry: dict) -> tuple[str, str] | None:
    """(repo key, field used): source_code_url first, then the public url as a fallback."""
    for name in ("source_code_url", "url"):
        url = entry.get(name)
        if isinstance(url, str) and url:
            key, _canonical, _reason = intake.normalize(url)
            if key:
                return key, name
    return None


def _published(fetch: Fetcher, backing_entries: int) -> dict:
    raw = fetch.get_bytes(PUBLISHED_URL, MAX_FEED_BYTES, accept="application/json")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise MalformedPayload("published index is not JSON") from exc
    if not isinstance(data, list):
        raise MalformedPayload("published index must be a JSON array")
    return {"url": PUBLISHED_URL, "digest": _sha256(raw), "entries": len(data), "backing_entries": backing_entries}


def catalog(root: Path, limit: int, transport=None, budget: Budget | None = None, published: bool = False) -> dict:
    """Process up to `limit` backing-catalog entries per call, resuming from state/catalog-cursor.json.

    All fetches (head, feed, optional published index) complete before any canonical write. A failed
    optional published fetch is reported in `published` with ok=false; the backing intake still lands.
    """
    root = Path(root)
    if not isinstance(limit, int) or limit <= 0:
        raise CollectError("limit must be a positive integer")
    fetch = Fetcher(transport or urllib_transport, budget, _token())
    with core.writer_lock(root):
        core.init_locked(root)
        cursor = _load_json(root / CURSOR_FILE) or {}
        _meta, branch, sha, _date = _resolve_head(fetch, CATALOG_REPO)
        feed_dir = root / FEED_DIR / sha
        _safe_storage(root, feed_dir)
        feed_path = feed_dir / "agents.json"
        cached = feed_path.exists()
        raw = feed_path.read_bytes() if cached else fetch.get_bytes(
            f"https://{RAW_HOST}/{CATALOG_REPO}/{sha}/{CATALOG_PATH}", MAX_FEED_BYTES, accept="application/json")
        digest = _sha256(raw)
        if cached and (_load_json(feed_dir / "feed.json") or {}).get("digest") != digest:
            raise IntegrityError("cached catalog digest differs from its capture record")
        entries = _parse_catalog(raw)  # a malformed feed raises here, before any state changes
        pub: dict | None = None
        if published:
            try:
                pub = {"ok": True, **_published(fetch, len(entries))}
            except core.WorkbenchError as exc:
                pub = {"ok": False, "error": type(exc).__name__, "code": exc.code, "message": str(exc)}
        if not cached:
            core.atomic_write_bytes(feed_path, raw)
            core.write_if_changed(feed_dir / "feed.json", core.dump_json({
                "repo": CATALOG_REPO, "path": CATALOG_PATH, "branch": branch, "commit": sha, "digest": digest,
                "bytes": len(raw), "entries": len(entries),
                "locator": f"https://github.com/{CATALOG_REPO}/blob/{sha}/{CATALOG_PATH}"}))
        version_changed = cursor.get("commit") != sha
        if version_changed:
            cursor = {"repo": CATALOG_REPO, "path": CATALOG_PATH, "commit": sha, "digest": digest,
                      "entries": len(entries), "next_index": 0}
        start = int(cursor.get("next_index", 0))
        batch = entries[start:start + limit]
        by_category: dict[str, int] = {}
        keys = {e["slug"]: _entry_key(e) for e in entries}
        for entry in entries:
            by_category[entry["category"]] = by_category.get(entry["category"], 0) + 1
        totals = {"entries": len(entries), "by_category": dict(sorted(by_category.items())),
                  "no_repo": sum(1 for k in keys.values() if k is None),
                  "via_url_fallback": sum(1 for k in keys.values() if k and k[1] == "url"),
                  "unique_repos": len({k[0] for k in keys.values() if k}),
                  "unsupported_category": sum(1 for e in entries if e["category"] not in SUPPORTED_CLASSES)}
        repos = core.load_repos(root)
        processed = {"attached": 0, "no_repo": 0, "unsupported_category": 0, "new_repos": []}
        for entry in batch:
            found = keys[entry["slug"]]
            if found is None:
                processed["no_repo"] += 1
                continue
            key, via = found
            record = repos.get(key)
            if record is None:
                record = repos[key] = intake.new_record(key, f"https://github.com/{key}")
                processed["new_repos"].append(key)
            if entry["category"] in SUPPORTED_CLASSES:
                intake._add_unique(record["classes"], entry["category"])
            else:
                processed["unsupported_category"] += 1
            intake._add_unique(record["origins"], CATALOG_LABEL)
            source = _catalog_source(entry, sha, via)
            slot = next((i for i, s in enumerate(record["sources"])
                         if s.get("kind") == "catalog" and s.get("slug") == entry["slug"]), None)
            if slot is None:
                record["sources"].append(source)
            else:
                record["sources"][slot] = source
            processed["attached"] += 1
        cursor["next_index"] = start + len(batch)
        changed = core.save_repos(root, repos)
        core.write_if_changed(root / CURSOR_FILE, core.dump_json(cursor))
        if pub and pub["ok"]:
            core.write_if_changed(root / PUBLISHED_FILE, core.dump_json({k: v for k, v in pub.items() if k != "ok"}))
            pub["discrepancy"] = pub["entries"] != len(entries)
            pub["note"] = "published index and backing feed are recorded separately; counts are not reconciled"
        result = {
            "root": str(root), "catalog": CATALOG_LABEL, "commit": sha, "branch": branch, "digest": digest,
            "feed": (feed_path.relative_to(root)).as_posix(), "feed_cached": cached, "version_changed": version_changed,
            "processed": len(batch), "range": [start, start + len(batch)], "backlog": len(entries) - cursor["next_index"],
            "batch": processed, "totals": totals, "changed": changed, "budget": fetch.budget.summary(),
        }
        if pub is not None:
            result["published"] = pub
    return result


# --------------------------------------------------------------------------- snapshot

def path_problem(path: object) -> str | None:
    """Why a repository path is unsafe to store, or None. Portable across Windows and POSIX."""
    if not isinstance(path, str) or not path or len(path) > MAX_PATH_CHARS:
        return "empty-or-too-long"
    if path.startswith(("/", "~")) or UNSAFE_CHARS.search(path) or "%" in path:
        return "absolute-or-unsafe-characters"
    for segment in path.split("/"):
        if segment in ("", ".", "..") or segment.lower() == ".git":
            return "dot-or-empty-segment"
        if segment != segment.rstrip(" .") or RESERVED_DEVICES.match(segment):
            return "windows-alias-or-device"
    if Path(path).suffix.lower() not in SOURCE_SUFFIXES:
        return "unsupported-file-type"
    return None


def _check_paths(paths: list[str] | None) -> list[str]:
    out: list[str] = []
    for raw in paths or []:
        problem = path_problem(raw)
        if problem:
            raise InvalidPath(f"path rejected ({problem}): {raw if isinstance(raw, str) else '?'}"[:200])
        if raw not in out:
            out.append(raw)
    return out


def storage_name(path: str) -> str:
    """Deterministic flat storage name: <slug>-<sha256(path)[:12]><rcw suffix>. No directories, no
    case or suffix collisions (README.md vs readme.md, x.py vs x.py.txt); original path stays in metadata."""
    suffix = Path(path).suffix.lower()
    suffix = suffix if suffix in RCW_SUFFIXES else ".txt"
    slug = SLUG_STRIP.sub("-", Path(path).name.lower()).strip("-.")[:40] or "file"
    return f"{slug}-{_sha256(path.encode('utf-8'))[:12]}{suffix}"


def _contained(base: Path, target: Path) -> bool:
    try:
        return target.parent == base and not target.is_symlink() and target.resolve().is_relative_to(base.resolve())
    except OSError:
        return False


def _safe_storage(root: Path, target: Path) -> None:
    """Reject redirected storage components below the caller's chosen corpus root."""
    root, target = root.absolute(), target.absolute()
    if not target.is_relative_to(root) or not target.resolve().is_relative_to(root.resolve()):
        raise InvalidPath("storage path is outside the corpus root")
    for part in (target, *target.parents):
        if part == root:
            break
        if part.is_symlink() or part.is_junction():
            raise InvalidPath("storage path contains a symbolic link or junction")


def _select(blobs: dict[str, dict], explicit: list[str], max_files: int, max_bytes: int) -> tuple[list[str], list[dict]]:
    """Order: README, explicit paths, root docs, docs/ trees. Budgets omit, never silently drop."""
    lower = {p.lower(): p for p in blobs}
    readme = next((n for n in README_NAMES if n in blobs), None) or next(
        (lower[n.lower()] for n in README_NAMES if n.lower() in lower), None)
    root_docs = sorted(p for p in blobs if "/" not in p and Path(p).suffix.lower() in DOC_SUFFIXES)
    dir_docs = sorted(p for p in blobs if p.lower().startswith(DOC_DIRS) and Path(p).suffix.lower() in DOC_SUFFIXES)
    ordered: list[str] = []
    for path in ([readme] if readme else []) + explicit + root_docs + dir_docs:
        if path not in ordered:
            ordered.append(path)
    selected, omitted, used = [], [], 0
    for path in ordered:
        size = int(blobs[path].get("size") or 0)
        problem = path_problem(path)
        if problem:
            omitted.append({"path": path[:MAX_PATH_CHARS], "size": size, "reason": f"unsafe-path:{problem}"})
        elif not isinstance(blobs[path].get("sha"), str) or not SHA_RE.match(blobs[path]["sha"]):
            omitted.append({"path": path, "size": size, "reason": "missing-blob-sha"})
        elif len(selected) >= max_files:
            omitted.append({"path": path, "size": size, "reason": "file-budget"})
        elif used + size > max_bytes:
            omitted.append({"path": path, "size": size, "reason": "byte-budget"})
        else:
            selected.append(path)
            used += size
    return selected, omitted


def _verified(data: bytes, git_sha: str, size: int, label: str) -> bytes:
    if len(data) != size or git_blob_sha(data) != git_sha:
        raise IntegrityError(f"blob-mismatch (git sha or size): {label}")
    return data


def _obtain_blob(root: Path, fetch: Fetcher, full_name: str, sha: str, path: str, git_sha: str, size: int) -> bytes:
    """Bytes for one blob: verified state cache first, otherwise a bounded raw fetch at the exact SHA."""
    cache = root / BLOB_CACHE_DIR / full_name.lower() / git_sha
    _safe_storage(root, cache)
    if cache.exists():
        return _verified(cache.read_bytes(), git_sha, size, f"cache {git_sha[:12]}")
    data = fetch.get_bytes(f"https://{RAW_HOST}/{full_name}/{sha}/{quote(path, safe='/')}", size, accept="text/plain")
    _verified(data, git_sha, size, f"download {path}")
    core.atomic_write_bytes(cache, data)
    return data


def _collect_snapshot(root: Path, fetch: Fetcher, key: str, max_files: int, max_bytes: int, explicit: list[str]) -> dict:
    owner, name = key.split("/")
    meta, branch, sha, date = _resolve_head(fetch, key)
    full_name = meta.get("full_name") if isinstance(meta.get("full_name"), str) else key
    spdx = (meta.get("license") or {}).get("spdx_id") if isinstance(meta.get("license"), dict) else None
    tree = fetch.get_json(f"https://{API_HOST}/repos/{key}/git/trees/{sha}?recursive=1")
    if not isinstance(tree, dict) or not isinstance(tree.get("tree"), list):
        raise MalformedPayload(f"tree malformed: {key}@{sha[:12]}")
    blobs = {t["path"]: t for t in tree["tree"] if isinstance(t, dict) and t.get("type") == "blob" and isinstance(t.get("path"), str)}
    truncated = bool(tree.get("truncated"))
    for path in explicit:
        if path not in blobs:
            raise InvalidPath(f"path not in tree (truncated={truncated}): {path}")
    selected, omitted = _select(blobs, explicit, max_files, max_bytes)
    commit_dir = root / SOURCE_DIR / owner / name / sha
    _safe_storage(root, commit_dir)
    known_bad: set[str] = set()
    for prior_snapshot in sorted(commit_dir.glob(f"*/{SNAPSHOT_FILE}")):
        known_bad |= {o["path"] for o in (_load_json(prior_snapshot) or {}).get("omitted", []) if o.get("reason") == "not-utf8"}
    staged: list[tuple[str, bytes, str]] = []
    for path in selected:
        size, git_sha = int(blobs[path].get("size") or 0), blobs[path]["sha"]
        if path in known_bad:
            omitted.append({"path": path, "size": size, "reason": "not-utf8"})
            continue
        data = _obtain_blob(root, fetch, full_name, sha, path, git_sha, size)
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            omitted.append({"path": path, "size": size, "reason": "not-utf8"})
            continue
        staged.append((path, data, text))
    # The selection identity is the exact inspected file set at this commit; a different set gets its
    # own package directory, so earlier packages keep their bytes and rcw evidence stays valid.
    selection = [{"path": p, "git_sha": blobs[p]["sha"]} for p, _d, _t in staged]
    snapshot_id = _sha256(core.dump_json({"commit": sha, "files": selection}))[:16]
    snap_dir = commit_dir / snapshot_id
    _safe_storage(root, snap_dir)
    prior = _load_json(snap_dir / SNAPSHOT_FILE) or {}
    prior_digests = {f["path"]: f["sha256"] for f in prior.get("files", []) if isinstance(f, dict)}
    files: list[dict] = []
    for path, data, text in staged:
        stored = storage_name(path)
        target = snap_dir / stored
        if not _contained(snap_dir, target):
            raise InvalidPath(f"storage escapes snapshot directory: {stored}")
        digest = _sha256(data)
        if path in prior_digests and prior_digests[path] != digest:
            raise IntegrityError(f"manifest-digest-mismatch: {path}")
        if target.exists():
            _verified(target.read_bytes(), blobs[path]["sha"], len(data), f"stored {stored}")
        else:
            core.atomic_write_bytes(target, data)
        files.append({
            "path": path, "stored": stored, "size": len(data), "sha256": digest, "git_sha": blobs[path]["sha"],
            "lines": len(text.splitlines()),
            "url": f"https://github.com/{full_name}/blob/{sha}/{quote(path, safe='/')}",
            "raw_url": f"https://{RAW_HOST}/{full_name}/{sha}/{quote(path, safe='/')}",
        })
    members = [{"path": f["stored"], "metadata": {
        "title": f"{full_name}/{f['path']} @ {sha[:12]}", "creator": owner, "date": date, "source_type": "webpage",
        "access": "public", "url": f["url"],
        "identifiers": {"repository": key, "commit": sha, "path": f["path"], "git_sha": f["git_sha"], "snapshot_id": snapshot_id},
    }} for f in files]
    rel_dir = snap_dir.relative_to(root).as_posix()
    manifest = {
        "snapshot_id": snapshot_id, "dir": rel_dir, "package": f"{rel_dir}/{RCW_MANIFEST}",
        "repo": key, "full_name": full_name, "url": f"https://github.com/{full_name}", "default_branch": branch,
        "commit": sha, "commit_date": date, "tree_sha": tree.get("sha"), "license": spdx,
        "budgets": {"max_files": max_files, "max_bytes": max_bytes, "bytes_stored": sum(f["size"] for f in files)},
        "files": files, "omitted": omitted[:MAX_OMITTED_LISTED], "omitted_count": len(omitted), "explicit_paths": explicit,
        "selection": {"candidates": len(files) + len(omitted), "stored": len(files), "omitted": len(omitted),
                      "complete": not omitted},
        "repository": {"tree_truncated": truncated, "tree_blobs": len(blobs), "complete": not truncated},
    }
    if files:
        core.write_if_changed(snap_dir / RCW_MANIFEST, core.dump_json(
            {"complete": True, "title": f"{full_name} @ {sha} [{snapshot_id}]", "files": members}))
    if not prior:
        core.write_if_changed(snap_dir / SNAPSHOT_FILE, core.dump_json(manifest))
    return {**manifest, "reused": bool(prior)}


def snapshot(root: Path, repo: str, max_files: int, max_bytes: int, paths: list[str] | None = None,
             transport=None, budget: Budget | None = None) -> dict:
    """Store an immutable, budgeted text snapshot of a public repository's default-branch head."""
    root = Path(root)
    key, canonical, reason = intake.normalize(f"https://github.com/{repo}")
    if not key:
        raise InvalidPath(f"repository rejected: {reason or 'not-github'}")
    explicit = _check_paths(paths)
    if not isinstance(max_files, int) or max_files <= 0 or not isinstance(max_bytes, int) or max_bytes <= 0:
        raise CollectError("max_files and max_bytes must be positive integers")
    fetch = Fetcher(transport or urllib_transport, budget, _token())
    with core.writer_lock(root):
        core.init_locked(root)
        repos = core.load_repos(root)
        record = repos.setdefault(key, intake.new_record(key, canonical))
        try:
            manifest = _collect_snapshot(root, fetch, key, max_files, max_bytes, explicit)
        except core.WorkbenchError as exc:
            # Prior snapshots stay on disk; the record states that this refresh failed and why.
            record["freshness"] = "refresh-failed"
            record["last_error"] = {"code": type(exc).__name__, "message": str(exc), "locator": canonical}
            if record["status"] == "discovered":
                record["status"] = "blocked"
            core.save_repos(root, repos)
            raise
        sha, snap_id = manifest["commit"], manifest["snapshot_id"]
        record.pop("last_error", None)
        record["latest_commit"] = sha
        record["latest_snapshot_id"] = snap_id
        record["latest_snapshot"] = {"snapshot_id": snap_id, "commit": sha, "dir": manifest["dir"],
                                     "snapshot": f"{manifest['dir']}/{SNAPSHOT_FILE}", "package": manifest["package"]}
        if record["status"] in ("discovered", "blocked", "snapshotted"):
            record["status"] = "snapshotted"
        indexed = record.get("indexed_snapshot_id")
        record["freshness"] = "pending" if indexed is None else ("current" if indexed == snap_id else "stale")
        intake._add_unique(record["sources"], {"kind": "snapshot", **record["latest_snapshot"]})
        changed = core.save_repos(root, repos)
    return {"root": str(root), "repo": key, "commit": sha, "snapshot_id": snap_id, "dir": manifest["dir"],
            "package": manifest["package"], "files_stored": len(manifest["files"]), "omitted_count": manifest["omitted_count"],
            "omitted": manifest["omitted"], "selection": manifest["selection"], "repository": manifest["repository"],
            "reused": manifest["reused"], "license": manifest["license"], "status": record["status"],
            "freshness": record["freshness"], "changed": changed, "budget": fetch.budget.summary()}
