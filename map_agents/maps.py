"""Compact, source-linked navigation and search over the catalog and validated dossiers.

build(root) never reads catalog blurbs as fact and never invents facets: every claim it renders comes from
wiki.load_dossier, which already validated it against the kernel's claims/slices/sources tables and the
snapshot bytes. A repo with no dossier is shown as a lead or a pending snapshot, never as analyzed code. A
dossier that fails validation is reported by name and excluded from the usable "known" evidence count.

The bounded main index and per-repo orientation pages stay small by linking, not truncating: every class,
every agent, every component/pattern claim, every facet gap and every freshness state has a full, paginated
detail page under map/ so a reader can always reach every repository and every claim without opening JSON or
a raw source file, even at a corpus of thousands of repositories.

query(root, ...) then searches only the generated map/ Markdown (never sources/, never wiki/data/, and not the
kernel's own wiki/pages/ archive unless explicitly requested) with deterministic scoring, an excerpt centered on
the matched terms, and a real completeness flag instead of a silent file-count cutoff.
"""

from __future__ import annotations

import re
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from . import core, wiki

MAP_DIR = "map"
NOTES_SUFFIX = ".notes.md"
DETAIL_SUFFIX = ".detail.md"
AGENTS_CORPUS = "AGENTS_CORPUS.md"
INDEX_WORD_LIMIT = 2000
REPO_WORD_LIMIT = 500
COMPONENT_FACETS = ("specifications", "components", "design-choices", "interfaces")
PATTERN_FACETS = ("workflows", "skills-patterns", "orchestration")
STATUS_ORDER = ("discovered", "snapshotted", "distilled", "blocked")
FRESHNESS_ORDER = ("current", "pending", "stale", "refresh-failed")
TAG_INLINE_CAP = 6          # origins/projects shown inline on a repo page before "+N more, see detail page"
CLASS_PREVIEW_CAP = 20      # class names previewed on the main index before linking to the full class index
AGENT_PREVIEW_CAP = 20      # repos previewed on the main index before linking to the full agent index
NAV_PREVIEW_CAP = 15        # component/pattern claims previewed on the main index
FRESHNESS_PREVIEW_CAP = 20  # stale/refresh-failed repos previewed on the main index
MAX_CLAIMS_PER_FACET = 2    # claims sampled per facet on a repo's orientation page
MAX_QUERY_FILE_BYTES = 200_000
MAX_QUERY_FILES = 100_000   # a safety ceiling, not a silent truncation of the real corpus
BUILD_FILE = "map/build.json"
_WORD_RE = re.compile(r"[a-z0-9]+")


def _word_count(text: str) -> int:
    return len(text.split())


def _tokenize(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "uncategorized"


def _owner_name(key: str) -> tuple[str, str]:
    owner, name = key.split("/")
    return owner, name


def _repo_page_rel(key: str) -> str:
    owner, name = _owner_name(key)
    return f"{MAP_DIR}/repos/{owner}/{name}.md"


def _notes_rel(key: str) -> str:
    owner, name = _owner_name(key)
    return f"{MAP_DIR}/repos/{owner}/{name}{NOTES_SUFFIX}"


def _detail_rel(key: str) -> str:
    owner, name = _owner_name(key)
    return f"{MAP_DIR}/repos/{owner}/{name}{DETAIL_SUFFIX}"


def _from_map(rel: str) -> str:
    """Path relative to map/index.md for a link inside map/index.md."""
    return rel[len(MAP_DIR) + 1:]


def _repo_link_from_section(key: str) -> str:
    """Path relative to a page under map/<section>/... for a link to that repo's orientation page."""
    owner, name = _owner_name(key)
    return f"../repos/{owner}/{name}.md"


def _repo_link_from_root(key: str) -> str:
    """Root-relative path, for use from AGENTS_CORPUS.md or other corpus-root files."""
    return _repo_page_rel(key)


def _up_to_root_from_repo_page() -> str:
    """map/repos/<owner>/<name>.md sits three directories below the corpus root."""
    return "../../../"


def _evidence_link(loc: dict) -> str:
    """A real clickable Markdown link to the immutable GitHub blob range, not a plain path#Lline string."""
    text = f"{loc['path']}#L{loc['line_start']}-L{loc['line_end']}"
    return f"[{text}]({loc['url']})"


def _bounded_tags(label: str, values: list[str], cap: int = TAG_INLINE_CAP) -> str:
    values = values or []
    shown = ", ".join(values[:cap]) if values else "none"
    extra = len(values) - cap
    return f"{label}: {shown}" + (f" (+{extra} more; full list in the detail page)" if extra > 0 else "")


def _bound_by_lines(lines: list[str], limit: int, note: str) -> list[str]:
    """Keep whole lines while the cumulative word count stays within limit; never cut a line in half."""
    total = _word_count("\n".join(lines))
    if total <= limit:
        return lines
    kept: list[str] = []
    used = 0
    note_words = _word_count(note)
    for line in lines:
        w = _word_count(line)
        if used + w > limit - note_words:
            break
        kept.append(line)
        used += w
    kept.append(note)
    return kept


# ---------------------------------------------------------------- repo pages


def _render_repo_detail(key: str, record: dict, dossier: dict | None) -> str:
    """Unbounded detail page: full origins/projects tags and, when present, every claim in every facet."""
    lines = [f"# {key} -- full detail", "", f"[Back to orientation]({Path(_repo_page_rel(key)).name})", "",
              "## Origins", "", *[f"- {v}" for v in record.get('origins', [])], "",
              "## Projects", "", *[f"- {v}" for v in record.get('projects', [])], ""]
    if dossier is None:
        lines.append("No distilled dossier is available for this repository yet.")
    else:
        lines.append(f"Full evidence record (JSON): [{record['dossier']}]({_up_to_root_from_repo_page()}{record['dossier']})")
        lines.append("")
        by_facet: dict[str, list[dict]] = {}
        for c in dossier["claims"]:
            by_facet.setdefault(c["facet"], []).append(c)
        for facet in wiki.FACETS:
            claims = by_facet.get(facet, [])
            lines.append(f"## {facet} ({len(claims)} claim(s))")
            lines.append("")
            if not claims:
                lines.append("- unknown (no source-linked claim submitted for this facet)")
            for c in claims:
                links = ", ".join(_evidence_link(loc) for loc in c["locators"])
                lines.append(f"- [{c['kind']}/{c['basis']}] {c['text']} -- evidence: {links} (`{c['claim_id']}`)")
            lines.append("")
        if dossier.get("superseded_claim_ids"):
            lines.append(f"Superseded claim IDs (kept as history): {', '.join(dossier['superseded_claim_ids'])}")
            lines.append("")
    return "\n".join(lines) + "\n"


def _render_repo_page(key: str, record: dict, dossier: dict | None) -> str:
    owner, name = _owner_name(key)
    status, freshness = record.get("status", "discovered"), record.get("freshness", "pending")
    detail_link = f"[full detail]({name}{DETAIL_SUFFIX})"
    notes_link = f"[notes]({name}{NOTES_SUFFIX})"
    header = [
        f"# {key}", "",
        f"Status: {status} - Freshness: {freshness}",
        f"Catalog classes: {', '.join(record.get('classes') or []) or 'none recorded'}",
        _bounded_tags("Origins", record.get("origins")) + " - " + _bounded_tags("Projects", record.get("projects")),
    ]
    latest = record.get("latest_snapshot")
    if isinstance(latest, dict):
        header.append(f"Latest snapshot: commit {latest['commit'][:12]} @ {latest['snapshot_id']}")
    if record.get("last_error"):
        err = record["last_error"]
        header.append(f"Last collection error: {err.get('code')}: {str(err.get('message'))[:160]}")
    if record.get("dossier_problem"):
        header.append(f"Dossier validation failed and its claims are not shown here: {record['dossier_problem']}")
        header.append("This repository is excluded from the map's `known` evidence count until it is re-applied.")
    header.append("")
    footer = ["", f"Metadata and full claim list: {detail_link}", f"Human notes ({notes_link}, never overwritten by build)",
              "", "[Back to map index](../../index.md)"]
    if dossier is None:
        body = ["## Evidence", ""]
        if status == "discovered":
            body.append("This is an intake lead only. No source snapshot or code has been analyzed.")
        elif status == "blocked":
            body.append("Collection is blocked; no distilled evidence exists yet.")
        else:
            body.append(f"Status is `{status}`; a snapshot exists but no dossier has been distilled and applied yet.")
        body += ["", "## Facets", "", "All facets are pending (no distilled, evidence-checked claims yet).", ""]
        return "\n".join(_bound_by_lines(header + body,
                         REPO_WORD_LIMIT - _word_count("\n".join(footer)),
                         f"More metadata: {detail_link}") + footer) + "\n"
    n_claims = len(dossier["claims"])
    n_gaps = len(dossier["gaps"])
    body = ["## Summary (orientation draft, not independently verified)", "", dossier["summary"], "",
            "## Facets", "", f"{n_claims} claim(s) across {len(wiki.FACETS) - n_gaps} facet(s); {n_gaps} facet(s) unknown.", ""]
    reserved = _word_count("\n".join(header + body + footer))
    budget = REPO_WORD_LIMIT - reserved
    by_facet: dict[str, list[dict]] = {}
    for c in dossier["claims"]:
        by_facet.setdefault(c["facet"], []).append(c)
    facet_lines: list[str] = []
    omitted = 0
    for facet in wiki.FACETS:
        claims = by_facet.get(facet, [])
        if not claims:
            facet_lines.append(f"- {facet}: unknown (no source-linked claim submitted for this facet)")
            continue
        facet_lines.append(f"- {facet} ({len(claims)} claim(s)):")
        shown = 0
        for c in claims:
            links = ", ".join(_evidence_link(loc) for loc in c["locators"])
            entry = f"  - [{c['kind']}/{c['basis']}] {c['text']} -- evidence: {links}"
            if shown < MAX_CLAIMS_PER_FACET and _word_count(entry) <= budget:
                facet_lines.append(entry)
                budget -= _word_count(entry)
                shown += 1
            else:
                omitted += 1
    if omitted:
        facet_lines.append(f"\n({omitted} additional claim(s) omitted for length; see {detail_link} for every claim.)")
    else:
        facet_lines.append(f"\nEvery claim for this repository is shown above and in {detail_link}.")
    return "\n".join(_bound_by_lines(header + body + facet_lines,
                     REPO_WORD_LIMIT - _word_count("\n".join(footer)),
                     f"More evidence: {detail_link}") + footer) + "\n"


# ---------------------------------------------------------------- secondary, unbounded navigation pages


def _render_agents_index(repos: dict) -> str:
    lines = ["# Agents -- full index", "", f"{len(repos)} repositories.", "", "[Back to map index](../index.md)", ""]
    for key in sorted(repos):
        r = repos[key]
        lines.append(f"- [{key}]({_repo_link_from_section(key)}) -- status={r.get('status')}, freshness={r.get('freshness')}")
    return "\n".join(lines) + "\n"


def _render_classes_index(by_class: dict[str, list[str]]) -> str:
    lines = ["# Classes -- full index", "", "[Back to map index](../index.md)", ""]
    for cls in sorted(by_class):
        lines.append(f"- [{cls}]({_slugify(cls)}.md) ({len(by_class[cls])} repo(s))")
    return "\n".join(lines) + "\n"


def _render_class_page(cls: str, members: list[str]) -> str:
    lines = [f"# Class: {cls}", "", "[Back to classes index](index.md)", "[Back to map index](../index.md)", ""]
    for key in sorted(members):
        lines.append(f"- [{key}]({_repo_link_from_section(key)})")
    return "\n".join(lines) + "\n"


def _render_nav_index(title: str, claims: list[tuple[str, dict]]) -> str:
    lines = [f"# {title} -- full index", "", "[Back to map index](../index.md)", ""]
    if not claims:
        lines.append("- No source-backed claims yet for this category.")
    for key, c in sorted(claims, key=lambda kc: (kc[0], kc[1]["claim_id"])):
        links = ", ".join(_evidence_link(loc) for loc in c["locators"])
        lines.append(f"- [{key}]({_repo_link_from_section(key)}) [{c['kind']}/{c['basis']}] {c['text']} -- evidence: {links}")
    return "\n".join(lines) + "\n"


def _render_gaps_index(gap_repos: dict[str, list[str]]) -> str:
    lines = ["# Gaps -- full index", "", "[Back to map index](../index.md)", ""]
    for facet in wiki.FACETS:
        missing = gap_repos.get(facet, [])
        if missing:
            lines.append(f"- [{facet}]({facet}.md): missing in {len(missing)} distilled repo(s)")
        else:
            lines.append(f"- {facet}: no gaps across distilled repos")
    return "\n".join(lines) + "\n"


def _render_gap_page(facet: str, repos_missing: list[str]) -> str:
    lines = [f"# Gap: {facet}", "", "[Back to gaps index](index.md)", "[Back to map index](../index.md)", "",
             f"{len(repos_missing)} distilled repo(s) have no source-linked claim for `{facet}`.", ""]
    for key in sorted(repos_missing):
        lines.append(f"- [{key}]({_repo_link_from_section(key)})")
    return "\n".join(lines) + "\n"


def _render_freshness_index(repos: dict) -> str:
    lines = ["# Freshness -- full index", "", "[Back to map index](../index.md)", ""]
    by_fresh: dict[str, list[str]] = defaultdict(list)
    for key, r in repos.items():
        by_fresh[r.get("freshness", "pending")].append(key)
    for state in FRESHNESS_ORDER:
        keys = sorted(by_fresh.get(state, []))
        lines.append(f"## {state} ({len(keys)})")
        lines.append("")
        for key in keys:
            r = repos[key]
            reason = r.get("last_error", {}).get("code") if r.get("last_error") else ""
            suffix = f" -- {reason}" if reason else ""
            lines.append(f"- [{key}]({_repo_link_from_section(key)}){suffix}")
        lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- main index and pointer


def _render_index(repos: dict, by_status: Counter, by_freshness: Counter, by_class: dict,
                   component_claims: list, pattern_claims: list, gap_repos: dict[str, list[str]],
                   stale_keys: list[str], invalid_keys: list[str]) -> str:
    total = len(repos)
    known = by_status.get("distilled", 0) - len(invalid_keys)
    lines = [
        "# Map the Agents -- Observatory index", "",
        f"Coverage: {known} of {total} known/total (distilled with kernel-applied, currently valid evidence).", "",
        "Status counts: " + (", ".join(f"{s}={by_status[s]}" for s in STATUS_ORDER if by_status.get(s)) or "none"), "",
        "Freshness counts: " + (", ".join(f"{f}={by_freshness[f]}" for f in FRESHNESS_ORDER if by_freshness.get(f)) or "none"), "",
        "Navigation: " + " | ".join(f"[{s}]({s}/index.md)" for s in
            ("classes", "agents", "components", "patterns", "gaps", "freshness")), "",
    ]
    if invalid_keys:
        lines.append("Invalid dossiers (excluded from `known` until re-applied): " +
                      ", ".join(f"[{k}]({_from_map(_repo_page_rel(k))})" for k in sorted(invalid_keys)))
        lines.append("")
    lines += ["## Classes", "", f"Full index: [classes/index.md](classes/index.md) ({len(by_class)} class(es)).", ""]
    for cls in sorted(by_class)[:CLASS_PREVIEW_CAP]:
        lines.append(f"- [{cls}](classes/{_slugify(cls)}.md) ({len(by_class[cls])} repo(s))")
    if len(by_class) > CLASS_PREVIEW_CAP:
        lines.append(f"- ... {len(by_class) - CLASS_PREVIEW_CAP} more; see classes/index.md")
    if not by_class:
        lines.append("- No catalog classes recorded yet.")
    lines += ["", "## Agents", "", f"Full index: [agents/index.md](agents/index.md) ({total} repo(s)).", ""]
    for key in sorted(repos)[:AGENT_PREVIEW_CAP]:
        r = repos[key]
        lines.append(f"- [{key}]({_from_map(_repo_page_rel(key))}) -- status={r.get('status')}, freshness={r.get('freshness')}")
    if total > AGENT_PREVIEW_CAP:
        lines.append(f"- ... {total - AGENT_PREVIEW_CAP} more; see agents/index.md")
    lines += ["", "## Components", "", "Full index: [components/index.md](components/index.md).", ""]
    lines += _preview_nav(component_claims)
    lines += ["", "## Patterns", "", "Full index: [patterns/index.md](patterns/index.md).", ""]
    lines += _preview_nav(pattern_claims)
    lines += ["", "## Gaps", "", "Full index: [gaps/index.md](gaps/index.md).", ""]
    any_gap = False
    for facet in wiki.FACETS:
        if gap_repos.get(facet):
            any_gap = True
            lines.append(f"- [{facet}](gaps/{facet}.md): missing in {len(gap_repos[facet])} distilled repo(s)")
    if not any_gap:
        lines.append("- No gap data yet (no valid distilled repos)." if known == 0 else "- No facet gaps across valid distilled repos.")
    lines += ["", "## Freshness", "", "Full index: [freshness/index.md](freshness/index.md).", ""]
    if stale_keys:
        for key in sorted(stale_keys)[:FRESHNESS_PREVIEW_CAP]:
            r = repos[key]
            reason = r.get("last_error", {}).get("code") if r.get("last_error") else r.get("freshness")
            lines.append(f"- [{key}]({_from_map(_repo_page_rel(key))}): {r.get('freshness')} ({reason})")
        if len(stale_keys) > FRESHNESS_PREVIEW_CAP:
            lines.append(f"- ... {len(stale_keys) - FRESHNESS_PREVIEW_CAP} more; see freshness/index.md")
    else:
        lines.append("- No stale or refresh-failed repos.")
    return "\n".join(_bound_by_lines(lines, INDEX_WORD_LIMIT,
                     "(index truncated at the word budget; see the linked full indexes under map/ for every entry)")) + "\n"


def _preview_nav(claims: list[tuple[str, dict]]) -> list[str]:
    if not claims:
        return ["- No source-backed claims yet for this category."]
    ordered = sorted(claims, key=lambda kc: (kc[0], kc[1]["claim_id"]))
    lines = []
    for key, c in ordered[:NAV_PREVIEW_CAP]:
        links = ", ".join(_evidence_link(loc) for loc in c["locators"])
        lines.append(f"- [{key}]({_from_map(_repo_page_rel(key))}) [{c['kind']}/{c['basis']}] {c['text']} -- evidence: {links}")
    if len(ordered) > NAV_PREVIEW_CAP:
        lines.append(f"- ... {len(ordered) - NAV_PREVIEW_CAP} more; see the full index above")
    return lines


def _render_pointer() -> str:
    return "\n".join([
        "# AGENTS_CORPUS", "",
        "Generated pointer into the Observatory map. Do not hand-edit; rebuild with "
        "`python -m map_agents --root ROOT build`.", "",
        f"- Main index: [{MAP_DIR}/index.md]({MAP_DIR}/index.md)",
        f"- Classes: [{MAP_DIR}/index.md#classes]({MAP_DIR}/index.md#classes) (full: [{MAP_DIR}/classes/index.md]({MAP_DIR}/classes/index.md))",
        f"- Agents: [{MAP_DIR}/index.md#agents]({MAP_DIR}/index.md#agents) (full: [{MAP_DIR}/agents/index.md]({MAP_DIR}/agents/index.md))",
        f"- Components: [{MAP_DIR}/index.md#components]({MAP_DIR}/index.md#components) (full: [{MAP_DIR}/components/index.md]({MAP_DIR}/components/index.md))",
        f"- Patterns: [{MAP_DIR}/index.md#patterns]({MAP_DIR}/index.md#patterns) (full: [{MAP_DIR}/patterns/index.md]({MAP_DIR}/patterns/index.md))",
        f"- Gaps: [{MAP_DIR}/index.md#gaps]({MAP_DIR}/index.md#gaps) (full: [{MAP_DIR}/gaps/index.md]({MAP_DIR}/gaps/index.md))",
        f"- Freshness: [{MAP_DIR}/index.md#freshness]({MAP_DIR}/index.md#freshness) (full: [{MAP_DIR}/freshness/index.md]({MAP_DIR}/freshness/index.md))", "",
    ]) + "\n"


def _paginate(rel: str, text: str) -> dict[str, str]:
    """Small sibling pages preserve complete Markdown lines and relative evidence links."""
    lines = text.splitlines()
    if _word_count(text) <= 1800:
        return {rel: text}
    chunks, chunk, words = [], [], 0
    for line in lines:
        size = _word_count(line)
        if words + size > 1750 and chunk:
            chunks.append(chunk)
            chunk, words = [], 0
        chunk.append(line)
        words += size
    if chunk:
        chunks.append(chunk)
    path = Path(rel)
    paths = [rel] + [path.with_name(f"{path.stem}.page-{n}.md").as_posix() for n in range(2, len(chunks) + 1)]
    output = {}
    for i, chunk in enumerate(chunks):
        nav = [f"[First page]({path.name})"]
        if i:
            nav.append(f"[Previous]({Path(paths[i-1]).name})")
        if i + 1 < len(chunks):
            nav.append(f"[Next]({Path(paths[i+1]).name})")
        title = lines[0] if i else ""
        output[paths[i]] = title + f"\n\nPage {i+1} of {len(chunks)}. " + " | ".join(nav) + "\n\n" + "\n".join(chunk) + "\n"
    return output


def _digest(value: object) -> str:
    return hashlib.sha256(core.dump_json(value)).hexdigest()


def build(root: Path) -> dict:
    """Render the bounded index/orientation pages plus unbounded linked detail pages under map/, and AGENTS_CORPUS.md.

    Reads catalog/repos.json and, for every `distilled` record, the validated dossier via wiki.load_dossier
    (never a raw catalog blurb). A dossier that fails validation is named on its repo's page and excluded
    from `known`/component/pattern/gap accounting; the run still completes and reports `invalid_dossiers`.
    Writes are atomic and no-op when bytes are unchanged; a pre-existing notes file is created once and never
    overwritten again.
    """
    root = Path(root)
    with core.writer_lock(root):
        core.init_locked(root)
        repos = core.load_repos(root)
        by_status: Counter = Counter()
        by_freshness: Counter = Counter()
        by_class: dict[str, list[str]] = defaultdict(list)
        component_claims: list[tuple[str, dict]] = []
        pattern_claims: list[tuple[str, dict]] = []
        gap_repos: dict[str, list[str]] = defaultdict(list)
        stale_keys: list[str] = []
        invalid_keys: list[str] = []
        written: list[str] = []
        unchanged = 0
        rendered: dict[str, str] = {}
        file_repos: dict[str, str] = {}

        def _put(rel: str, text: str, repo: str | None = None) -> None:
            pages = {rel: text} if rel in (AGENTS_CORPUS, "map/index.md") or (repo and rel.endswith(f"/{repo.split('/')[1]}.md")) else _paginate(rel, text)
            rendered.update(pages)
            if repo:
                file_repos.update({p: repo for p in pages})

        for key in sorted(repos):
            record = dict(repos[key])
            by_status[record.get("status", "discovered")] += 1
            by_freshness[record.get("freshness", "pending")] += 1
            for cls in record.get("classes") or ["uncategorized"]:
                by_class[cls].append(key)
            if record.get("freshness") in ("stale", "refresh-failed"):
                stale_keys.append(key)
            dossier = None
            if record.get("status") == "distilled" and record.get("dossier"):
                try:
                    dossier = wiki.load_dossier(root, key)
                except core.WorkbenchError as exc:
                    record["dossier_problem"] = f"{type(exc).__name__}: {exc}"
                    invalid_keys.append(key)
            notes_path = root / _notes_rel(key)
            if not notes_path.is_file():
                core.atomic_write_bytes(notes_path, f"# Notes for {key}\n\n(human-owned; the map build never overwrites this file)\n".encode("utf-8"))
            _put(_repo_page_rel(key), _render_repo_page(key, record, dossier), key)
            _put(_detail_rel(key), _render_repo_detail(key, record, dossier), key)
            if dossier:
                for c in dossier["claims"]:
                    if c["facet"] in COMPONENT_FACETS:
                        component_claims.append((key, c))
                    if c["facet"] in PATTERN_FACETS:
                        pattern_claims.append((key, c))
                for g in dossier["gaps"]:
                    gap_repos[g["facet"]].append(key)

        _put(f"{MAP_DIR}/agents/index.md", _render_agents_index(repos))
        _put(f"{MAP_DIR}/classes/index.md", _render_classes_index(by_class))
        for cls, members in by_class.items():
            _put(f"{MAP_DIR}/classes/{_slugify(cls)}.md", _render_class_page(cls, members))
        _put(f"{MAP_DIR}/components/index.md", _render_nav_index("Components", component_claims))
        _put(f"{MAP_DIR}/patterns/index.md", _render_nav_index("Patterns", pattern_claims))
        _put(f"{MAP_DIR}/gaps/index.md", _render_gaps_index(gap_repos))
        for facet, missing in gap_repos.items():
            _put(f"{MAP_DIR}/gaps/{facet}.md", _render_gap_page(facet, missing))
        _put(f"{MAP_DIR}/freshness/index.md", _render_freshness_index(repos))
        _put(f"{MAP_DIR}/index.md", _render_index(repos, by_status, by_freshness, by_class, component_claims,
                                                    pattern_claims, gap_repos, stale_keys, invalid_keys))
        _put(AGENTS_CORPUS, _render_pointer())
        for rel, text in rendered.items():
            if core.write_if_changed(root / rel, text.encode("utf-8")):
                written.append(rel)
            else:
                unchanged += 1
        manifest = {"schema_version": 1, "catalog_digest": _digest(repos),
                    "files": sorted(p for p in rendered if p.startswith("map/")),
                    "file_repos": file_repos, "records": repos}
        if core.write_if_changed(root / BUILD_FILE, core.dump_json(manifest)):
            written.append(BUILD_FILE)
        else:
            unchanged += 1

    gap_counts = {f: len(v) for f, v in gap_repos.items()}
    return {
        "root": str(root), "repos": len(repos), "known": by_status.get("distilled", 0) - len(invalid_keys),
        "total": len(repos), "written": sorted(written), "unchanged": unchanged,
        "by_status": dict(sorted(by_status.items())), "by_freshness": dict(sorted(by_freshness.items())),
        "gaps": dict(sorted(gap_counts.items())), "stale": sorted(stale_keys), "invalid_dossiers": sorted(invalid_keys),
    }


# ---------------------------------------------------------------- query


def _searchable_files(root: Path, include_archive: bool) -> tuple[list[Path], bool]:
    """Generated Markdown only: map/ orientation and detail pages, excluding human-owned notes.

    The kernel's own wiki/pages/ archive is excluded by default because an archived page cannot be
    reliably re-labelled with the repository's current freshness/status without re-reading source; pass
    include_archive=True to add it (results from it never carry repo/status/freshness fields and are
    marked historical). Returns (files, complete) where complete is False only if MAX_QUERY_FILES, a
    safety ceiling far above any realistic corpus, was actually reached.
    """
    root = Path(root)
    files: list[Path] = []
    base = root / MAP_DIR
    if (root / BUILD_FILE).is_file():
        manifest = json.loads((root / BUILD_FILE).read_bytes())
        files.extend(root / p for p in manifest["files"] if p.startswith("map/") and ".." not in Path(p).parts)
    elif base.is_dir():
        files.extend(sorted(p for p in base.rglob("*.md") if p.is_file() and not p.name.endswith(NOTES_SUFFIX)))
    if include_archive:
        archive = root / wiki.WIKI_DIR / "pages"
        if archive.is_dir():
            files.extend(sorted(p for p in archive.rglob("*.md") if p.is_file()))
    complete = len(files) <= MAX_QUERY_FILES
    return files[:MAX_QUERY_FILES], complete


def _read_bounded(path: Path, max_bytes: int) -> tuple[bytes, bool]:
    with open(path, "rb") as fh:
        data = fh.read(max_bytes + 1)
    return (data[:max_bytes], True) if len(data) > max_bytes else (data, False)


def _excerpt(body: str, terms: list[str], max_chars: int) -> str:
    """A window centered on the first matched term, not just the file's opening bytes. Never exceeds max_chars."""
    if max_chars <= 0:
        return ""
    if len(body) <= max_chars:
        return body
    lower = body.lower()
    pos = min((lower.find(t) for t in terms if lower.find(t) != -1), default=-1)
    if pos == -1:
        return body[:max_chars]
    mark = "... "
    budget = max(0, max_chars - 2 * len(mark))
    start = max(0, pos - budget // 3)
    end = min(len(body), start + budget)
    start = max(0, end - budget)
    prefix = mark if start > 0 else ""
    suffix = mark if end < len(body) else ""
    return (prefix + body[start:end] + suffix)[:max_chars]


def query(root: Path, text: str, limit: int = 10, max_chars: int = 4000, include_archive: bool = False) -> dict:
    """Deterministic term-frequency search over generated map/ Markdown, bounded by limit and max_chars.

    Every file is read with a bounded read() (max_bytes+1), never a full read followed by slicing. `complete`
    is False if the corpus exceeded the safety ceiling MAX_QUERY_FILES, so an empty result set is never
    presented as corpus-wide coverage without that flag.
    """
    root = Path(root)
    if limit <= 0 or max_chars <= 0:
        raise core.WorkbenchError("limit and max_chars must be positive")
    terms = sorted(set(_tokenize(text)))
    files, complete = _searchable_files(root, include_archive)
    repos = core.load_repos(root) if (root / core.REPOS_FILE).is_file() else {}
    manifest = json.loads((root / BUILD_FILE).read_bytes()) if (root / BUILD_FILE).is_file() else {}
    stale_view = manifest.get("catalog_digest") != _digest(repos)
    scored: list[tuple[int, str, str, bool]] = []
    if terms:
        for path in files:
            if not path.is_file():
                complete = False
                continue
            data, truncated_read = _read_bounded(path, MAX_QUERY_FILE_BYTES)
            complete = complete and not truncated_read
            body = data.decode("utf-8", "replace")
            counts = Counter(_tokenize(body))
            score = sum(counts.get(t, 0) for t in terms)
            if score > 0:
                scored.append((score, path.relative_to(root).as_posix(), body, truncated_read))
                if len(scored) > 2 * limit:
                    scored.sort(key=lambda t: (-t[0], t[1]))
                    del scored[limit:]
    scored.sort(key=lambda t: (-t[0], t[1]))
    results: list[dict] = []
    used = 0
    for score, rel, body, truncated_read in scored:
        if len(results) >= limit or used >= max_chars:
            break
        snippet = _excerpt(body.strip(), terms, max_chars - used)
        used += len(snippet)
        entry = {"path": rel, "score": score, "excerpt": snippet,
                 "truncated": truncated_read or len(snippet) < len(body.strip()), "stale_view": stale_view}
        parts = Path(rel).parts
        if rel in manifest.get("file_repos", {}):
            key = manifest["file_repos"][rel]
            record = manifest["records"].get(key)
            if record:
                entry["repo"] = key
                entry["status"] = record.get("status")
                entry["freshness"] = record.get("freshness")
        elif rel.startswith(f"{wiki.WIKI_DIR}/pages/"):
            entry["archive"] = True
            entry["note"] = "kernel-generated historical wiki page; not labelled with current catalog freshness"
        results.append(entry)
    return {
        "root": str(root), "query": text, "terms": terms, "files_scanned": len(files), "complete": complete,
        "stale_view": stale_view,
        "results": results, "total_chars": used, "limit": limit, "max_chars": max_chars,
    }
