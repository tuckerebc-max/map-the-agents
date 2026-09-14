"""Behavioral tests for the directory layer: capture, resolve, render. Offline, frozen fixtures.

PAGE_NANOCLAW mirrors the live shape observed at
https://raw.githubusercontent.com/prime-radiant-inc/alltheagents.org/0709cccb49aff08a4b10beb95a214005a810a363/agents/nanoclaw.md
(read-only bounded GET, 2026-09-13): a YAML list for `platforms`, "yes (details)"-shaped feature
strings, a `model_providers` sentence, and a rich `what_makes_it_special` field plus a full body.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import collect, core, directory, maps
from test_collect import API, CAT, RAW, SHA1, SHA2, FakeTransport, entry, head_routes, js

PAGE_NANOCLAW = """---
name: "NanoClaw Page"
slug: "nanoclaw"
category: "multiplexer"
maker: "nanocoai"
license: "MIT"
url: "https://github.com/nanocoai/nanoclaw"
source_code_url: "https://github.com/nanocoai/nanoclaw"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
language: "TypeScript"
mcp_support: "no"
plugin_support: "yes (skills system, customization by forking)"
subagents: "yes (multi-agent support, per-agent containers)"
hooks: "no"
model_providers: "Anthropic (Claude Agent SDK), Codex, OpenCode, Ollama"
install_method: "git clone, pnpm install"
what_makes_it_special: "Lightweight, containerized alternative that runs agents in isolated Docker containers."
---

NanoClaw is a self-hosted personal AI assistant harness with per-agent Docker containers.
"""

PAGE_URLFALLBACK = """---
name: UrlFallback Page
slug: urlfallback
category: agent
maker: page-maker
url: https://github.com/orgu/urlfallback
---

A page whose only repo hint is the plain `url` field, not `source_code_url`.
"""

PAGE_PAGESONLY = """---
name: "[Pages] Only"
slug: pagesonly
category: agent
maker: "`backtick` maker"
mcp_support: yes
what_makes_it_special: "Click [here](javascript:alert(1)) or see <script>evil()</script> for details."
---

Body with an injected `](evil)` sequence and a bare https://example.com/evil link attempt.
"""

PAGE_NO_FRONTMATTER = "Just a body, no frontmatter delimiters at all.\n"
PAGE_BAD_YAML = "---\nname: [unterminated\n---\nbody\n"


def backing_entries() -> list[dict]:
    return [
        entry("Nanoclaw", "agent", "https://github.com/nanocoai/nanoclaw", slug="nanoclaw",
              subagents="no", platforms=[], model_providers="OpenAI only", plan_mode=None,
              description="backing nanoclaw description"),
        entry("BackingOnly", "agent", "https://github.com/orgb/backingonly", slug="backingonly"),
        entry("NoRepo", "agent", None, slug="norepo", url="https://example.org/norepo"),
    ]


def published_entries() -> list[dict]:
    return [
        {"name": "Nanoclaw", "slug": "nanoclaw", "category": "agent-sdk", "maker": "pub-maker", "license": "Apache-2.0",
         "language": "Python", "stars": "10", "description": "published nanoclaw description"},
        {"name": "PubOnly", "slug": "pubonly", "category": "agent", "maker": "pub-maker-2", "license": "MIT",
         "language": "Go", "stars": "3", "description": "published only entry"},
    ]


def tree_entry(path: str, body: bytes | None = None, git_sha: str | None = None, size: int | None = None) -> dict:
    body = b"" if body is None else body
    return {"path": path, "type": "blob", "sha": git_sha or collect.git_blob_sha(body), "size": size if size is not None else len(body)}


def build_routes(sha: str, tree_items: list[dict], page_bodies: dict[str, bytes], published: list[dict] | None = None,
                  backing: list[dict] | None = None, truncated: bool = False) -> dict:
    routes = {**head_routes(CAT, sha), collect.PUBLISHED_URL: js(published if published is not None else published_entries()),
              f"{RAW}/{CAT}/{sha}/{collect.CATALOG_PATH}": js(backing if backing is not None else backing_entries()),
              f"{API}/repos/{CAT}/git/trees/{sha}?recursive=1": js({"sha": "t" * 40, "truncated": truncated, "tree": tree_items})}
    for path, body in page_bodies.items():
        routes[f"{RAW}/{CAT}/{sha}/{collect.quote(path, safe='/')}"] = collect.Response(200, body)
    return routes


def seed_catalog(tmp_path: Path, sha: str = SHA1, backing: list[dict] | None = None) -> FakeTransport:
    t = FakeTransport(build_routes(sha, [], {}, backing=backing))
    collect.catalog(tmp_path, 10, transport=t)
    return t


def full_tree(sha: str) -> list[dict]:
    return [
        tree_entry("agents/nanoclaw.md", PAGE_NANOCLAW.encode()),
        tree_entry("agents/urlfallback.md", PAGE_URLFALLBACK.encode()),
        tree_entry("agents/pagesonly.md", PAGE_PAGESONLY.encode()),
        tree_entry("agents/../evil.md", b"x", git_sha="z" * 40),  # unsafe path
        tree_entry("agents/bad.md", b"x", git_sha="not-a-sha"),   # unsafe sha shape
        {"path": "agents/dirlike", "type": "tree", "sha": "d" * 40},
        {"path": "README.md", "type": "blob", "sha": "e" * 40, "size": 1},
    ]


def full_pages() -> dict[str, bytes]:
    return {"agents/nanoclaw.md": PAGE_NANOCLAW.encode(), "agents/urlfallback.md": PAGE_URLFALLBACK.encode(),
            "agents/pagesonly.md": PAGE_PAGESONLY.encode()}


def _capture_all(tmp_path: Path, sha: str = SHA1, backing: list[dict] | None = None,
                  published: list[dict] | None = None, tree_items: list[dict] | None = None,
                  pages: dict[str, bytes] | None = None, truncated: bool = False) -> None:
    seed_catalog(tmp_path, sha, backing=backing)
    t = FakeTransport(build_routes(sha, tree_items if tree_items is not None else full_tree(sha),
                                    pages if pages is not None else full_pages(), published=published,
                                    backing=backing, truncated=truncated))
    directory.capture(tmp_path, 50, transport=t)


# --------------------------------------------------------------------------- capture


def test_capture_requires_a_catalog_cursor_first(tmp_path: Path) -> None:
    with pytest.raises(directory.DirectoryError, match="run `catalog`"):
        directory.capture(tmp_path, 10, transport=FakeTransport({}))
    assert not (tmp_path / directory.DIR_CURSOR_FILE).exists()


def test_capture_resumes_persists_truncated_flag_and_publishes_content_addressed(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    t = FakeTransport(build_routes(SHA1, full_tree(SHA1), full_pages(), truncated=True))
    first = directory.capture(tmp_path, 1, transport=t)
    assert first["pages_total"] == 3 and first["unsafe_pages"] == 2
    assert first["tree_truncated"] is True
    assert first["processed"] == 1 and first["backlog"] == 2
    second = directory.capture(tmp_path, 1, transport=t)
    third = directory.capture(tmp_path, 1, transport=t)
    assert third["backlog"] == 0
    assert sorted(first["newly_captured"] + second["newly_captured"] + third["newly_captured"]) == \
        ["nanoclaw", "pagesonly", "urlfallback"]
    pointer = json.loads((tmp_path / directory.PUBLISHED_POINTER_FILE).read_text())
    stored = tmp_path / directory.PUBLISHED_STORE_DIR / pointer["digest"] / "agents.json"
    assert stored.is_file() and json.loads(stored.read_text()) == published_entries()
    before = (tmp_path / directory.DIR_CURSOR_FILE).read_bytes()
    raw_calls_before = len(t.urls(collect.RAW_HOST))
    fourth = directory.capture(tmp_path, 5, transport=t)
    assert fourth["processed"] == 0 and fourth["backlog"] == 0
    assert (tmp_path / directory.DIR_CURSOR_FILE).read_bytes() == before
    assert len(t.urls(collect.RAW_HOST)) == raw_calls_before, "no re-fetch of already-captured pages"
    assert len([c for c in t.calls if "git/trees" in c["url"]]) == 1, "tree fetched once at an unchanged commit"
    view = directory.resolve(tmp_path)
    assert view["tree_truncated"] is True


def test_capture_records_byte_hash_mismatch_and_detects_tampered_cache_on_reuse(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    tampered = full_pages()
    tampered["agents/nanoclaw.md"] = b"tampered bytes that do not match the declared git blob sha"
    t = FakeTransport(build_routes(SHA1, full_tree(SHA1), tampered))
    result = directory.capture(tmp_path, 10, transport=t)
    assert result["newly_failed"] == ["nanoclaw"]
    assert set(result["newly_captured"]) == {"pagesonly", "urlfallback"}
    assert not directory._page_path(tmp_path, SHA1, "nanoclaw").is_file()
    cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    assert "nanoclaw" in cursor["failures"]
    fixed = FakeTransport(build_routes(SHA1, full_tree(SHA1), full_pages()))
    healed = directory.capture(tmp_path, 10, transport=fixed)
    assert healed["newly_captured"] == ["nanoclaw"] and healed["failures"] == 0
    # Now corrupt an already-captured page directly on disk: a future capture() must fail loudly, not
    # silently re-download over it or silently keep serving the tampered bytes.
    good_path = directory._page_path(tmp_path, SHA1, "pagesonly")
    original = good_path.read_bytes()
    good_path.write_bytes(original + b"tampered-suffix")
    with pytest.raises(collect.IntegrityError, match="do not match recorded git blob sha"):
        directory.capture(tmp_path, 10, transport=fixed)
    assert good_path.read_bytes() != original, "corruption reported, not silently repaired"


def test_capture_stops_on_budget_exhaustion_without_marking_unattempted_pages_failed(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    t = FakeTransport(build_routes(SHA1, full_tree(SHA1), full_pages()))
    tight = collect.Budget(max_requests=2)  # tree(1) + published(1) exhausts before any page fetch
    result = directory.capture(tmp_path, 10, transport=t, budget=tight)
    assert result["newly_captured"] == [] and result["newly_failed"] == []
    assert result["stopped"] is not None and "BudgetExceeded" in result["stopped"]
    assert result["failures"] == 0, "no page was actually attempted, so none is stamped a network failure"
    assert result["backlog"] == result["pages_total"]
    cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    assert cursor["failures"] == {}
    # A follow-up call with a full budget makes real progress from where the stop left off.
    healthy = directory.capture(tmp_path, 10, transport=FakeTransport(build_routes(SHA1, full_tree(SHA1), full_pages())))
    assert healthy["backlog"] == 0 and healthy["stopped"] is None


def test_capture_stops_on_rate_limit_without_failing_remaining_pages(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    routes = build_routes(SHA1, full_tree(SHA1), full_pages())
    first_page_url = f"{RAW}/{CAT}/{SHA1}/{collect.quote('agents/nanoclaw.md', safe='/')}"
    routes[first_page_url] = collect.Response(429, b"")
    result = directory.capture(tmp_path, 10, transport=FakeTransport(routes))
    assert result["stopped"] is not None and "429" in result["stopped"]
    assert result["newly_failed"] == [] and result["failures"] == 0
    assert result["backlog"] == result["pages_total"], "the page that hit 429 stays pending, not marked failed"


def test_capture_fetch_failure_is_a_per_item_failure_not_a_raise(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    routes = build_routes(SHA1, full_tree(SHA1), full_pages())
    routes[f"{RAW}/{CAT}/{SHA1}/{collect.quote('agents/pagesonly.md', safe='/')}"] = collect.Response(404, b"")
    result = directory.capture(tmp_path, 10, transport=FakeTransport(routes))
    assert "pagesonly" in result["newly_failed"]
    view = directory.resolve(tmp_path)
    assert "pagesonly" in view["failed_pages"] and "pagesonly" not in view["missing_pages"]


# --------------------------------------------------------------------------- resolve: union, no-repo, url fallback


def test_resolve_union_membership_published_backing_and_pages_only(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    assert set(entries) == {"nanoclaw", "backingonly", "norepo", "pubonly", "pagesonly", "urlfallback"}
    assert entries["pubonly"]["membership"] == {"published": True, "backing": False, "pages": False}
    assert entries["backingonly"]["membership"] == {"published": False, "backing": True, "pages": False}
    assert entries["pagesonly"]["membership"] == {"published": False, "backing": False, "pages": True}


def test_resolve_no_repo_entry_is_explicit_not_absent_capability(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    assert entries["norepo"]["repo_key"] is None
    rendered, _ = directory._render_entry(entries["norepo"])
    assert "repository source unavailable" in rendered and "not an absence of capability" in rendered


def test_resolve_exposes_normalized_lead_even_when_not_tracked(tmp_path: Path) -> None:
    # urlfallback exists only as a site page (never seen by `catalog`), so its normalized repo is a
    # genuine lead the parent can intake, not yet a tracked repository record in this corpus.
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    untracked = entries["urlfallback"]
    assert untracked["repo_key"] == "orgu/urlfallback" and untracked["repo_tracked"] is False
    rendered, _ = directory._render_entry(untracked)
    assert "[orgu/urlfallback](https://github.com/orgu/urlfallback)" in rendered
    assert "not yet tracked in this corpus" in rendered
    tracked = entries["nanoclaw"]
    assert tracked["repo_key"] == "nanocoai/nanoclaw" and tracked["repo_tracked"] is True
    tracked_rendered, _ = directory._render_entry(tracked)
    assert "[nanocoai/nanoclaw](../../repos/nanocoai/nanoclaw.md)" in tracked_rendered


def test_resolve_preserves_url_fallback_like_the_collector(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    fb = entries["urlfallback"]
    assert fb["repo_key"] == "orgu/urlfallback" and fb["repo_field"] == "url" and fb["repo_source"] == "page"


# --------------------------------------------------------------------------- resolve: broad conflicts


def test_resolve_conflicts_cover_features_interface_model_providers_and_category(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    nc = entries["nanoclaw"]
    assert nc["conflicts"]["category"] == {"published": "agent-sdk", "backing": "agent", "page": "multiplexer"}
    assert nc["conflicts"]["subagents"] == {"published": None, "backing": "no", "page": "yes (multi-agent support, per-agent containers)"}
    assert "interface" in nc["conflicts"]
    assert nc["conflicts"]["interface"]["page"] == (("CLI", "Desktop", "Web"), "git clone, pnpm install")
    assert nc["conflicts"]["interface"]["backing"] == ((), "npm")
    assert "model_providers" in nc["conflicts"]
    rendered, overflow = directory._render_entry(nc)
    assert "Discrepancy between directory sources" in rendered
    assert overflow is not None, "more than five discrepant fields must overflow to a linked detail page"
    assert "full conflict detail" in rendered
    assert "category" in overflow and "subagents" in overflow


def test_resolve_feature_states_distinguish_unknown_no_and_yes_with_detail(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    nc = directory.resolve(tmp_path)["entries"]["nanoclaw"]
    assert nc["features"]["mcp_support"]["state"] == "no"
    assert nc["features"]["subagents"]["state"] == "yes"
    assert nc["features"]["subagents"]["value"] == "yes (multi-agent support, per-agent containers)"
    assert nc["features"]["plan_mode"]["state"] == "unknown"
    view = directory.render(tmp_path)
    feature_pages = {p: t for p, t in view["pages"].items() if p.startswith(f"{directory.MAP_DIR}/features/") and p.endswith(".md")
                     and "index" not in p}
    subagents_page = next(t for p, t in feature_pages.items() if "subagents" in t.lower() and "Directory feature: subagents" in t)
    assert "nanoclaw" in subagents_page, "'yes (details)' counts as a positive feature in navigation"


# --------------------------------------------------------------------------- resolve: unsafe paths, malformed pages


def test_resolve_unsafe_paths_are_excluded_and_reported(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    view = directory.resolve(tmp_path)
    assert len(view["unsafe_pages"]) == 2
    assert {u["reason"] for u in view["unsafe_pages"]} == {"unsafe-path-or-sha"}
    assert "evil" not in view["entries"] and "bad" not in view["entries"]


def test_resolve_malformed_or_missing_frontmatter_is_a_gap_not_a_raise(tmp_path: Path) -> None:
    tree = [tree_entry("agents/nofm.md", PAGE_NO_FRONTMATTER.encode()), tree_entry("agents/badyaml.md", PAGE_BAD_YAML.encode())]
    pages = {"agents/nofm.md": PAGE_NO_FRONTMATTER.encode(), "agents/badyaml.md": PAGE_BAD_YAML.encode()}
    _capture_all(tmp_path, tree_items=tree, pages=pages, backing=[], published=[])
    view = directory.resolve(tmp_path)
    assert view["malformed_pages"]["nofm"] == "no-frontmatter-block"
    assert view["malformed_pages"]["badyaml"].startswith("invalid-yaml")
    entries = view["entries"]
    assert entries["nofm"]["page_error"] == "no-frontmatter-block"
    rendered, _ = directory._render_entry(entries["nofm"])
    assert "Gap: this entry's site page could not be fully read" in rendered


def test_resolve_detects_tampered_cache_without_raising(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    page_path = directory._page_path(tmp_path, SHA1, "urlfallback")
    page_path.write_bytes(page_path.read_bytes() + b"tampered")
    view = directory.resolve(tmp_path)
    assert view["malformed_pages"]["urlfallback"] == "cache-tampered"
    assert "urlfallback" not in view["missing_pages"]


def test_resolve_flags_published_and_backing_integrity_problems(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    pointer = json.loads((tmp_path / directory.PUBLISHED_POINTER_FILE).read_text())
    stored = tmp_path / directory.PUBLISHED_STORE_DIR / pointer["digest"] / "agents.json"
    stored.write_bytes(stored.read_bytes().replace(b"published", b"altered!!"))
    view = directory.resolve(tmp_path)
    assert view["published_integrity_error"] == "published-digest-mismatch"
    assert view["counts"]["published"] == 0, "tampered published content must never be published as fact"
    feed_path = tmp_path / collect.FEED_DIR / SHA1 / "agents.json"
    feed_path.write_bytes(feed_path.read_bytes().replace(b"backing", b"altered!!"))
    view2 = directory.resolve(tmp_path)
    assert view2["backing_integrity_error"] == "backing-digest-mismatch"
    assert view2["counts"]["backing"] == 0


def test_resolve_is_safe_against_a_tampered_commit_or_digest_pointer(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    cursor["commit"] = "../../../etc/passwd"
    (tmp_path / directory.DIR_CURSOR_FILE).write_text(json.dumps(cursor))
    view = directory.resolve(tmp_path)
    assert view["commit"] is None and view["counts"]["backing"] == 0 and view["counts"]["pages"] == 0
    pointer_path = tmp_path / directory.PUBLISHED_POINTER_FILE
    bad_pointer = json.loads(pointer_path.read_text())
    bad_pointer["digest"] = "../../escape"
    pointer_path.write_text(json.dumps(bad_pointer))
    view2 = directory.resolve(tmp_path)
    assert view2["counts"]["published"] == 0
    assert not any(p.is_relative_to(tmp_path) is False for p in tmp_path.rglob("*"))


def test_resolve_is_read_only_and_safe_before_any_capture(tmp_path: Path) -> None:
    core.init(tmp_path)
    view = directory.resolve(tmp_path)
    assert view["entries"] == {} and view["counts"]["union"] == 0
    assert not (tmp_path / directory.DIR_CURSOR_FILE).exists()


# --------------------------------------------------------------------------- render: collisions, escaping, budgets


def test_render_collision_resistant_entry_and_group_filenames(tmp_path: Path) -> None:
    pages = {"agents/a.b.md": b"---\nname: A.B\nslug: a.b\ncategory: x\n---\nbody\n",
             "agents/a-b.md": b"---\nname: A-B\nslug: a-b\ncategory: x\n---\nbody\n",
             "agents/index.md": b"---\nname: Index Entry\nslug: index\ncategory: x\n---\nbody\n"}
    tree = [tree_entry(path, body) for path, body in pages.items()]
    _capture_all(tmp_path, tree_items=tree, pages=pages, backing=[], published=[])
    out = directory.render(tmp_path)
    stems = {directory._entry_stem("a.b"), directory._entry_stem("a-b"), directory._entry_stem("index")}
    assert len(stems) == 3, "three distinct raw slugs must never collide onto the same filename"
    for stem in stems:
        assert f"{directory.MAP_DIR}/entries/{stem}.md" in out["pages"]
    section_index = out["pages"][f"{directory.MAP_DIR}/entries/index.md"]
    assert "full entry index" in section_index, "the 'index' slug's own page must not overwrite the section index"
    assert "Index Entry" not in section_index or f"({directory._entry_stem('index')}.md)" in section_index
    for stem in stems:
        assert f"({stem}.md)" in section_index


def test_render_group_name_collisions_preserve_every_group(tmp_path: Path) -> None:
    backing = [entry("One", "cat a", "https://github.com/org1/one", slug="one"),
               entry("Two", "cat-a", "https://github.com/org2/two", slug="two")]
    _capture_all(tmp_path, backing=backing, published=[], tree_items=[], pages={})
    out = directory.render(tmp_path)
    class_files = {p for p in out["pages"] if p.startswith(f"{directory.MAP_DIR}/classes/") and "index" not in p}
    assert len(class_files) == 2, "two distinct category strings that slugify identically must get distinct pages"
    all_text = "".join(out["pages"][p] for p in class_files)
    assert "one" in all_text and "two" in all_text


def test_render_escapes_untrusted_markdown_in_names_and_descriptions(tmp_path: Path) -> None:
    tree = [tree_entry("agents/pagesonly.md", PAGE_PAGESONLY.encode())]
    pages = {"agents/pagesonly.md": PAGE_PAGESONLY.encode()}
    _capture_all(tmp_path, tree_items=tree, pages=pages, backing=[], published=[])
    out = directory.render(tmp_path)
    stem = directory._entry_stem("pagesonly")
    text = out["pages"][f"{directory.MAP_DIR}/entries/{stem}.md"]
    assert "[here](javascript:alert(1))" not in text, "unescaped brackets must never form a live link"
    assert "<script>evil()</script>" not in text, "raw HTML must be neutralized"
    assert "\\[here\\]" in text
    assert "\\<script\\>" in text
    assert "\\`backtick\\`" in text


def test_render_entry_page_stays_within_400_words_including_everything(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    for slug, e in entries.items():
        rendered, _overflow = directory._render_entry(e)
        assert directory._word_count(rendered) <= directory.ENTRY_WORD_LIMIT, slug


def test_render_source_references_are_real_markdown_links(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    rendered, _ = directory._render_entry(entries["nanoclaw"])
    sources_line = next(line for line in rendered.splitlines() if line.startswith("Sources:"))
    assert "](https://" in sources_line
    import re as _re
    # Every URL in the sources line must be the target of a markdown link, i.e. immediately preceded by "(".
    assert all(sources_line[m.start() - 1] == "(" for m in _re.finditer(r"https?://", sources_line))


def test_render_uses_page_body_and_what_makes_it_special_over_truncated_published_description(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    entries = directory.resolve(tmp_path)["entries"]
    nc = entries["nanoclaw"]
    assert "self-hosted personal AI assistant harness" in nc["description"]
    assert nc["description_source"].startswith("captured site page body")
    assert nc["highlight"] and "containerized alternative" in nc["highlight"]
    rendered, _ = directory._render_entry(nc)
    assert "Highlight (site page `what_makes_it_special`)" in rendered
    assert "containerized alternative" in rendered
    assert "self-hosted personal AI assistant harness" in rendered


# --------------------------------------------------------------------------- build/query integration


def test_build_integrates_directory_pages_into_manifest_and_index_links(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    result = maps.build(tmp_path)
    assert result["directory"]["union"] == 6
    manifest = json.loads((tmp_path / maps.BUILD_FILE).read_text())
    assert any(p.startswith(f"{directory.MAP_DIR}/") for p in manifest["files"])
    assert "directory_digest" in manifest
    index_text = (tmp_path / "map/index.md").read_text(encoding="utf-8")
    assert "directory/index.md" in index_text and "## Directory" in index_text


def test_build_is_a_no_op_on_unchanged_directory_state(tmp_path: Path) -> None:
    _capture_all(tmp_path)
    first = maps.build(tmp_path)
    assert any(p.startswith(f"{directory.MAP_DIR}/") for p in first["written"])
    second = maps.build(tmp_path)
    assert not any(p.startswith(f"{directory.MAP_DIR}/") for p in second["written"])


def test_query_reports_stale_view_after_a_new_directory_capture_until_rebuild(tmp_path: Path) -> None:
    seed_catalog(tmp_path)
    t = FakeTransport(build_routes(SHA1, full_tree(SHA1), full_pages()))
    directory.capture(tmp_path, 1, transport=t)  # partial: only one page captured so far
    maps.build(tmp_path)
    fresh = maps.query(tmp_path, "nanoclaw")
    assert fresh["stale_view"] is False
    # Capturing the rest of the already-known pages changes state/directory-cursor.json without touching
    # any repo record at all.
    directory.capture(tmp_path, 50, transport=t)
    stale = maps.query(tmp_path, "nanoclaw")
    assert stale["stale_view"] is True, "a new directory capture alone must invalidate the generated view"
    maps.build(tmp_path)
    healed = maps.query(tmp_path, "nanoclaw")
    assert healed["stale_view"] is False


def test_repo_only_corpus_without_any_directory_capture_stays_unaffected(tmp_path: Path) -> None:
    """Standalone repo-record behavior (no `directory` ever run) must not regress."""
    t = FakeTransport(build_routes(SHA1, [], {}, backing=[entry("Solo", "agent", "https://github.com/org-solo/solo", slug="solo")]))
    collect.catalog(tmp_path, 10, transport=t)
    result = maps.build(tmp_path)
    assert result["directory"]["union"] == 0
    query_result = maps.query(tmp_path, "solo")
    assert query_result["stale_view"] is False
    second = maps.build(tmp_path)
    assert second["written"] == []


# --------------------------------------------------------------------------- long legitimate slugs (live-shaped)

# Real observed live-capture slug (87 chars), currently only reachable via the backing feed's fallback,
# excluded under the old 80-char SLUG_RE ceiling. Real _TEMPLATE.md is an intentionally-excluded non-entry.
LONG_SLUG = "setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit"
PAGE_LONG = f"---\nname: Long Slug Entry\nslug: {LONG_SLUG}\ncategory: agent\n---\n\nA legitimately long site slug.\n"
PAGE_TEMPLATE = b"---\nname: Template\nslug: _TEMPLATE\ncategory: agent\n---\n\nTemplate scaffold, not a real entry.\n"


def test_long_legitimate_slug_is_captured_with_stable_short_storage(tmp_path: Path) -> None:
    assert len(LONG_SLUG) > directory.STORAGE_SLUG_CEILING
    seed_catalog(tmp_path)
    tree = [tree_entry(f"agents/{LONG_SLUG}.md", PAGE_LONG.encode()), tree_entry("agents/_TEMPLATE.md", PAGE_TEMPLATE)]
    t = FakeTransport(build_routes(SHA1, tree, {f"agents/{LONG_SLUG}.md": PAGE_LONG.encode(), "agents/_TEMPLATE.md": PAGE_TEMPLATE}))
    result = directory.capture(tmp_path, 10, transport=t)
    assert LONG_SLUG in result["newly_captured"]
    assert result["unsafe_pages"] == 1  # only _TEMPLATE.md, not the long legitimate slug
    stored = directory._page_path(tmp_path, SHA1, LONG_SLUG)
    assert stored.is_file()
    assert stored.name != f"{LONG_SLUG}.md", "a legitimately long slug must not be stored under an unbounded filename"
    assert len(stored.name) < len(LONG_SLUG)
    assert stored.read_bytes() == PAGE_LONG.encode()
    # _TEMPLATE remains an intentionally excluded non-entry: charset/case reject it regardless of length.
    cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    assert any(u["path"] == "agents/_TEMPLATE.md" for u in cursor["unsafe"])
    view = directory.resolve(tmp_path)
    assert LONG_SLUG in view["entries"] and "_TEMPLATE" not in view["entries"]
    assert view["entries"][LONG_SLUG]["name"] == "Long Slug Entry"


def test_storage_name_hash_integrity_and_old_mapping_preserved() -> None:
    short = "a" * directory.STORAGE_SLUG_CEILING
    boundary_plus_one = "b" * (directory.STORAGE_SLUG_CEILING + 1)
    assert directory._page_storage_name(short) == f"{short}.md", "unchanged for every slug at/under the old ceiling"
    hashed = directory._page_storage_name(boundary_plus_one)
    assert hashed != f"{boundary_plus_one}.md"
    assert hashed == directory._page_storage_name(boundary_plus_one), "deterministic: same slug, same filename every time"
    other_long = "c" * (directory.STORAGE_SLUG_CEILING + 1)
    assert hashed != directory._page_storage_name(other_long), "two distinct long slugs must not collide"
    assert len(hashed) < 120


def test_policy_bump_forces_exactly_one_tree_refetch_and_reuses_prior_pages(tmp_path: Path) -> None:
    """A dcursor saved by pre-widening code (no path_policy_version, the long slug filed as unsafe) must
    heal on the next capture(): exactly one real tree refetch, the long slug reclassified into `pages`,
    and the already-captured short-slug page reused rather than re-downloaded."""
    seed_catalog(tmp_path)
    old_tree = full_tree(SHA1)  # nanoclaw/urlfallback/pagesonly already legitimately captured
    t1 = FakeTransport(build_routes(SHA1, old_tree, full_pages()))
    directory.capture(tmp_path, 50, transport=t1)
    old_cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    assert "path_policy_version" in old_cursor
    # Simulate a cursor saved by the pre-widening code: no version stamp, and the long slug was recorded
    # unsafe (as the old, narrower SLUG_RE would have done) instead of missing entirely.
    del old_cursor["path_policy_version"]
    old_cursor["unsafe"] = old_cursor["unsafe"] + [{"path": f"agents/{LONG_SLUG}.md", "reason": "unsafe-path-or-sha"}]
    (tmp_path / directory.DIR_CURSOR_FILE).write_text(json.dumps(old_cursor))
    nanoclaw_before = directory._page_path(tmp_path, SHA1, "nanoclaw").read_bytes()
    new_tree = old_tree + [tree_entry(f"agents/{LONG_SLUG}.md", PAGE_LONG.encode())]
    t2 = FakeTransport(build_routes(SHA1, new_tree, {**full_pages(), f"agents/{LONG_SLUG}.md": PAGE_LONG.encode()}))
    result = directory.capture(tmp_path, 50, transport=t2)
    assert len([c for c in t2.calls if "git/trees" in c["url"]]) == 1, "the version bump forces exactly one real refetch"
    assert LONG_SLUG in result["newly_captured"]
    assert directory._page_path(tmp_path, SHA1, "nanoclaw").read_bytes() == nanoclaw_before, "prior captured page reused, not re-fetched"
    assert len([c for c in t2.urls(collect.RAW_HOST) if "nanoclaw" in c]) == 0, "no re-download of an already-good page"
    new_cursor = json.loads((tmp_path / directory.DIR_CURSOR_FILE).read_text())
    assert new_cursor["path_policy_version"] == directory.PATH_POLICY_VERSION
    assert not any(u["path"].endswith(LONG_SLUG + ".md") for u in new_cursor["unsafe"]), "reconciled out of the unsafe list"
    # A further call at the same commit must not refetch the tree again.
    t3 = FakeTransport(build_routes(SHA1, new_tree, {**full_pages(), f"agents/{LONG_SLUG}.md": PAGE_LONG.encode()}))
    directory.capture(tmp_path, 50, transport=t3)
    assert len([c for c in t3.calls if "git/trees" in c["url"]]) == 0
