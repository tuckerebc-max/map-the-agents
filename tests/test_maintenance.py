"""Behavioral tests for the bounded directory-capture + scoped-audit integration in hosted maintenance.

Offline throughout: FakeTransport serves only explicitly declared routes, so any unexpected network
call 404s. Does not repeat kernel prepare/apply setup already covered elsewhere; targets only the
new orchestration boundary in scripts/run_maintenance.py.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import collect, core, directory, wiki, workers
from scripts import run_maintenance as hosted
from test_collect import API, CAT, RAW, SHA1, entry, head_routes, js, repo_routes
from test_directory import PAGE_NANOCLAW, PAGE_URLFALLBACK, backing_entries, build_routes, published_entries, tree_entry
from test_map_review import alias_row, write_aliases


def test_directory_capture_reaches_generated_map_and_reports_backlog_honestly(tmp_path):
    root = tmp_path / "c"
    tree = [tree_entry("agents/nanoclaw.md", PAGE_NANOCLAW.encode())]
    routes = build_routes(SHA1, tree, {"agents/nanoclaw.md": PAGE_NANOCLAW.encode()})
    t = _FakeTransport(routes)
    result = hosted.run(root, tmp_path / "summary.json",
                        limits=workers.Limits(catalog_entries=10, max_repos=0), transport=t)
    assert "directory" in result and "skipped" not in result["directory"]
    dcap = result["directory"]
    assert dcap["pages_total"] == 1 and dcap["captured"] == 1 and dcap["backlog"] == 0
    assert dcap["newly_captured"] == 1 and dcap["failures"] == 0
    assert result["publishable"] is True and result["status"] == "validated"
    assert (root / "map/directory/index.md").is_file()
    entry_files = list((root / "map/directory/entries").glob("*.md"))
    assert any("nanoclaw" in f.read_text(encoding="utf-8").lower() for f in entry_files), \
        "the newly captured directory page must reach the generated map, not just internal state"


def test_directory_capture_limit_leaves_an_honest_backlog(tmp_path):
    """<=25 pages per run: with more pages than the limit, backlog/failures must be reported, not hidden."""
    root = tmp_path / "c"
    pages = {f"agents/item{i}.md": f"---\nname: Item{i}\nslug: item{i}\ncategory: agent\n---\nbody\n".encode() for i in range(3)}
    tree = [tree_entry(p, b) for p, b in pages.items()]
    routes = build_routes(SHA1, tree, pages)
    t = _FakeTransport(routes)
    orig_limit = hosted.DIRECTORY_LIMIT
    hosted.DIRECTORY_LIMIT = 2
    try:
        result = hosted.run(root, tmp_path / "summary.json",
                            limits=workers.Limits(catalog_entries=10, max_repos=0), transport=t)
    finally:
        hosted.DIRECTORY_LIMIT = orig_limit
    dcap = result["directory"]
    assert dcap["pages_total"] == 3 and dcap["processed"] == 2 and dcap["backlog"] == 1
    assert result["status"] == "validated"  # a truthful backlog is not itself a failure


def test_missing_catalog_cursor_is_an_honest_skip_not_a_publish_block(tmp_path):
    root = tmp_path / "c"
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert result["directory"] == {"skipped": result["directory"]["skipped"]}
    assert "no backing-feed commit" in result["directory"]["skipped"]
    assert result["publishable"] is True and result["status"] == "validated"


def test_directory_integrity_error_is_never_swallowed(tmp_path, monkeypatch):
    root = tmp_path / "c"
    tree = [tree_entry("agents/nanoclaw.md", PAGE_NANOCLAW.encode())]
    routes = build_routes(SHA1, tree, {"agents/nanoclaw.md": PAGE_NANOCLAW.encode()})
    t = _FakeTransport(routes)

    def _tampered_capture(*a, **kw):
        raise collect.IntegrityError("simulated tampered directory cache")
    monkeypatch.setattr(hosted.directory, "capture", _tampered_capture)
    result = hosted.run(root, tmp_path / "summary.json",
                        limits=workers.Limits(catalog_entries=10, max_repos=0), transport=t)
    assert result["publishable"] is False
    assert result["error"] == "IntegrityError"
    assert result["stage"] == "directory"


def test_audit_defaults_to_full_scope_until_wiki_audit_supports_repos(tmp_path):
    root = tmp_path / "c"
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert result["audit_scope"] == "full"
    assert "audit_scoped_repos" not in result


def _partitioned_changed_repo_root(tmp_path: Path):
    """A repo whose record is actually mutated by workers.maintain's own snapshot stage (not by intake,
    which happens before the before/after diff), under a partitioned wiki layout."""
    root = tmp_path / "c"
    core.init(root)
    core.atomic_write_bytes(root / wiki.LAYOUT_FILE, core.dump_json({"schema_version": wiki.LAYOUT_SCHEMA, "layout": "partitioned"}))
    from map_agents import intake
    intake.ingest(root, "https://github.com/example/changed", "test", "navy-yard")
    t = _FakeTransport(repo_routes("example/changed", SHA1, {"README.md": b"hello\n"}))
    return root, t


def test_orchestration_passes_changed_keys_once_audit_supports_repos_and_layout_is_partitioned(tmp_path, monkeypatch):
    root, t = _partitioned_changed_repo_root(tmp_path)
    seen = {}

    def fake_audit(root_, level, repos=None):
        seen["repos"] = repos
        return {"ok": True, "level": level}
    monkeypatch.setattr(hosted.wiki, "audit", fake_audit)
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=1), transport=t)
    assert result["audit_scope"] == "scoped"
    assert seen["repos"] == ["example/changed"]
    assert result["audit_scoped_repos"] == 1
    assert result["publishable"] is True


def test_failed_scoped_audit_blocks_publication(tmp_path, monkeypatch):
    root, t = _partitioned_changed_repo_root(tmp_path)
    monkeypatch.setattr(hosted.wiki, "audit", lambda root_, level, repos=None: {"ok": False, "level": level})
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=1), transport=t)
    assert result["publishable"] is False
    assert result["audit_scope"] == "scoped" and result["audit_ok"] is False
    assert result["stage"] == "audit"


def test_full_dossier_validation_failure_blocks_publication_even_when_scoped_audit_passes(tmp_path, monkeypatch):
    root = tmp_path / "c"
    core.init(root)
    monkeypatch.setattr(hosted.wiki, "audit", lambda root_, level: {"ok": True, "level": level})
    real_build = hosted.maps.build
    def fake_build(root_):
        result = real_build(root_)
        return {**result, "invalid_dossiers": ["some/repo"]}
    monkeypatch.setattr(hosted.maps, "build", fake_build)
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert result["publishable"] is False
    assert result["audit_ok"] is True  # the scoped/full kernel audit alone said ok
    assert result["map"]["invalid_dossiers"] == ["some/repo"]  # maps.build's own full validation still caught it
    assert result["stage"] == "audit"


def test_workflow_tracks_directory_cursor_and_published_state():
    text = (Path(__file__).resolve().parents[1] / ".github/workflows/maintenance.yml").read_text(encoding="utf-8")
    assert "corpus/state/directory-cursor.json" in text
    assert "corpus/state/directory-published.json" in text


class _FakeTransport:
    def __init__(self, routes: dict) -> None:
        self.routes, self.calls = routes, []

    def __call__(self, url, headers, timeout, max_bytes):
        self.calls.append({"url": url})
        hit = self.routes.get(url, collect.Response(404, b"{}"))
        return hit(url) if callable(hit) else hit


# --------------------------------------------------------------------------- directory lead intake


def test_page_only_lead_reaches_intake_and_generated_map_with_origin(tmp_path):
    root = tmp_path / "c"
    tree = [tree_entry("agents/urlfallback.md", PAGE_URLFALLBACK.encode())]
    t = _FakeTransport(build_routes(SHA1, tree, {"agents/urlfallback.md": PAGE_URLFALLBACK.encode()}, backing=[], published=[]))
    collect.catalog(root, 10, transport=t, budget=collect.Budget())
    directory.capture(root, 25, transport=t)
    result = directory.ingest_new_leads(root, 50)
    assert result["candidates"] == 1 and result["picked"] == 1 and result["deferred"] == 0
    assert result["new_repos"] == ["orgu/urlfallback"]
    repos = core.load_repos(root)
    assert "orgu/urlfallback" in repos
    assert repos["orgu/urlfallback"]["origins"] == [directory.INGEST_ORIGIN]
    assert repos["orgu/urlfallback"]["projects"] == [directory.INGEST_PROJECT]
    from map_agents import maps
    maps.build(root)
    text = (root / "map/repos/orgu/urlfallback.md").read_text(encoding="utf-8")
    assert directory.INGEST_ORIGIN in text


def test_unchanged_second_pass_is_idempotent(tmp_path):
    root = tmp_path / "c"
    tree = [tree_entry("agents/urlfallback.md", PAGE_URLFALLBACK.encode())]
    t = _FakeTransport(build_routes(SHA1, tree, {"agents/urlfallback.md": PAGE_URLFALLBACK.encode()}, backing=[], published=[]))
    collect.catalog(root, 10, transport=t, budget=collect.Budget())
    directory.capture(root, 25, transport=t)
    first = directory.ingest_new_leads(root, 50)
    before = core.load_repos(root)
    second = directory.ingest_new_leads(root, 50)
    assert first["changed"] is True
    assert second["candidates"] == 0 and second["picked"] == 0 and second["changed"] is False
    assert core.load_repos(root) == before


def test_leads_beyond_limit_are_deferred_and_resume_fairly(tmp_path):
    root = tmp_path / "c"
    pages = {f"agents/lead{i}.md": f"---\nname: Lead{i}\nslug: lead{i}\ncategory: agent\nsource_code_url: https://github.com/org{i}/lead{i}\n---\nbody\n".encode() for i in range(3)}
    tree = [tree_entry(p, b) for p, b in pages.items()]
    t = _FakeTransport(build_routes(SHA1, tree, pages, backing=[], published=[]))
    collect.catalog(root, 10, transport=t, budget=collect.Budget())
    directory.capture(root, 25, transport=t)
    first = directory.ingest_new_leads(root, 2)
    assert first["candidates"] == 3 and first["picked"] == 2 and first["deferred"] == 1
    second = directory.ingest_new_leads(root, 2)
    assert second["picked"] == 1 and second["deferred"] == 0
    assert set(first["new_repos"]) | set(second["new_repos"]) == {"org0/lead0", "org1/lead1", "org2/lead2"}


def test_no_repo_and_verified_tracked_alias_never_become_bogus_candidates(tmp_path):
    from map_agents import intake
    root = tmp_path / "c"
    tree = [tree_entry("agents/pagesonly.md", b"---\nname: NoRepo\nslug: pagesonly\ncategory: agent\n---\nbody\n"),
            tree_entry("agents/aliased.md", b"---\nname: Aliased\nslug: aliased\ncategory: agent\nsource_code_url: https://github.com/old-org/aliased\n---\nbody\n")]
    pages = {"agents/pagesonly.md": b"---\nname: NoRepo\nslug: pagesonly\ncategory: agent\n---\nbody\n",
             "agents/aliased.md": b"---\nname: Aliased\nslug: aliased\ncategory: agent\nsource_code_url: https://github.com/old-org/aliased\n---\nbody\n"}
    t = _FakeTransport(build_routes(SHA1, tree, pages, backing=[], published=[]))
    collect.catalog(root, 10, transport=t, budget=collect.Budget())
    intake.ingest(root, "https://github.com/new-org/aliased", "test", "navy-yard")  # canonical already tracked
    directory.capture(root, 25, transport=t)
    write_aliases(root, [alias_row("old-org/aliased", "new-org/aliased", 42)])
    result = directory.ingest_new_leads(root, 50)
    assert result["candidates"] == 0 and result["picked"] == 0
    assert "old-org/aliased" not in core.load_repos(root)


def test_directory_budget_is_a_fresh_object_per_hosted_call_not_import_time(tmp_path):
    assert isinstance(hosted.DIRECTORY_BUDGET, dict), "must be plain config, not a live collect.Budget instantiated at import"
    b1 = collect.Budget(**hosted.DIRECTORY_BUDGET)
    b2 = collect.Budget(**hosted.DIRECTORY_BUDGET)
    assert b1 is not b2 and b1.bytes_used == 0 and b2.bytes_used == 0
    root = tmp_path / "c"
    r1 = hosted.run(root, tmp_path / "s1.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    r2 = hosted.run(root, tmp_path / "s2.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert r1["publishable"] and r2["publishable"]  # a stale/expired shared budget would have failed the second call


def test_unchanged_partitioned_corpus_audits_with_empty_repo_list_and_reports_scope(tmp_path, monkeypatch):
    root = tmp_path / "c"
    core.init(root)
    core.atomic_write_bytes(root / wiki.LAYOUT_FILE, core.dump_json({"schema_version": wiki.LAYOUT_SCHEMA, "layout": "partitioned"}))
    seen = {}

    def fake_audit(root_, level, repos=None):
        seen["repos"] = repos
        return {"ok": True, "level": level}
    monkeypatch.setattr(hosted.wiki, "audit", fake_audit)
    result = hosted.run(root, tmp_path / "summary.json", limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert seen["repos"] == []
    assert result["audit_scope"] == "scoped" and result["audit_scoped_repos"] == 0
    assert result["publishable"] is True
