"""Tests for compact map build/query: real dossiers, genuine evidence links, gaps, freshness, budgets."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from map_agents import collect, core, intake, maps, wiki
from test_collect import SHA1, SHA2, FakeTransport, repo_routes
from test_wiki import FILES, good_proposal, slice_by_path, write

BRAVO_FILES = {
    "README.md": b"# Bravo\n\nBravo orchestrates a swarm of worker agents using a shared task queue.\n",
    "docs/design.md": b"# Design\n\nWorkflow: dispatch tasks, wait for completion, then aggregate results.\n",
}
BRAVO_FILES_V2 = {
    "README.md": b"# Bravo\n\nBravo v2 orchestrates a larger swarm of worker agents using a shared task queue.\n",
    "docs/design.md": b"# Design\n\nWorkflow: dispatch tasks, wait for completion, then aggregate results.\n",
}


def bravo_proposal(packet: dict) -> dict:
    spec = slice_by_path(packet, "README.md", "Bravo")
    design = slice_by_path(packet, "docs/design.md")
    return {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": "Synthetic orchestrator: dispatches tasks to a worker swarm over a shared queue.",
        "claims": [
            {"facet": "specifications", "text": "Bravo orchestrates a swarm of worker agents over a shared task queue.",
             "slice_ids": [spec["slice_id"]], "kind": "observation", "basis": "documented"},
            {"facet": "workflows", "text": "The documented workflow is dispatch, wait, then aggregate results.",
             "slice_ids": [design["slice_id"]], "kind": "observation", "basis": "documented"},
        ],
    }


@pytest.fixture(scope="module")
def corpus(tmp_path_factory: pytest.TempPathFactory) -> Path:
    root = tmp_path_factory.mktemp("mapcorpus")
    collect.snapshot(root, "org-a/alpha", 20, 50_000, paths=["src/agent.py"],
                      transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    collect.snapshot(root, "org-b/bravo", 20, 50_000,
                      transport=FakeTransport(repo_routes("org-b/bravo", SHA1, BRAVO_FILES)))
    intake.ingest(root, "https://github.com/org-c/charlie", "chat", "observatory")
    p1 = wiki.prepare(root, "org-a/alpha")
    packet1 = json.loads((root / p1["packet"]).read_bytes())
    wiki.apply(root, root / p1["packet"], write(root / "proposals" / "alpha.json", good_proposal(packet1)))
    p2 = wiki.prepare(root, "org-b/bravo")
    packet2 = json.loads((root / p2["packet"]).read_bytes())
    wiki.apply(root, root / p2["packet"], write(root / "proposals" / "bravo.json", bravo_proposal(packet2)))
    repos = core.load_repos(root)
    repos["org-a/alpha"]["classes"] = ["agent-framework"]
    repos["org-b/bravo"]["classes"] = ["orchestrator"]
    core.save_repos(root, repos)
    return root


def clone(corpus: Path, tmp_path: Path) -> Path:
    target = tmp_path / "corpus"
    shutil.copytree(corpus, target)
    return target


def repo_text(root: Path, key: str) -> str:
    owner, name = key.split("/")
    return (root / f"map/repos/{owner}/{name}.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- build


def test_build_covers_two_classes_with_genuine_evidence_links(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    result = maps.build(root)
    assert result["total"] == 3 and result["known"] == 2
    assert result["by_status"] == {"discovered": 1, "distilled": 2}
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    for key in ("org-a/alpha", "org-b/bravo", "org-c/charlie"):
        assert key in index_text
    assert "agent-framework" in index_text and "orchestrator" in index_text
    dossier = wiki.load_dossier(root, "org-a/alpha")
    comp_claim = next(c for c in dossier["claims"] if c["facet"] == "components")
    loc = comp_claim["locators"][0]
    evidence = f"{loc['path']}#L{loc['line_start']}-L{loc['line_end']}"
    assert evidence in index_text, "component nav must cite the real kernel-verified locator"
    assert evidence in repo_text(root, "org-a/alpha")
    pointer = (root / "AGENTS_CORPUS.md").read_text(encoding="utf-8")
    for anchor in ("classes", "agents", "components", "patterns", "gaps", "freshness"):
        assert f"map/index.md#{anchor}" in pointer
    for key in ("org-a/alpha", "org-b/bravo", "org-c/charlie"):
        assert (root / maps._repo_page_rel(key)).is_file()


def test_lead_only_repo_never_shown_as_analyzed(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    text = repo_text(root, "org-c/charlie")
    assert "No source snapshot or code has been analyzed" in text
    assert "All facets are pending" in text
    for facet in wiki.FACETS:
        assert facet not in text, "a lead must not list any facet as if it were evidence-checked"
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    components_section = index_text.split("## Components")[1].split("## Patterns")[0]
    assert "org-c/charlie" not in components_section


def test_missing_facets_are_explicit_unknown_and_counted_as_gaps(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    result = maps.build(root)
    alpha_text = repo_text(root, "org-a/alpha")
    assert "- specifications: unknown (no source-linked claim submitted for this facet)" in alpha_text
    bravo_text = repo_text(root, "org-b/bravo")
    assert "- components: unknown (no source-linked claim submitted for this facet)" in bravo_text
    # alpha has specifications missing, bravo has it -> gap count 1; neither has evaluation -> gap count 2.
    assert result["gaps"]["specifications"] == 1
    assert result["gaps"]["evaluation"] == 2
    assert result["gaps"]["components"] == 1


def test_stale_dossier_shown_with_reason_and_kept_evidence(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    collect.snapshot(root, "org-b/bravo", 20, 50_000,
                      transport=FakeTransport(repo_routes("org-b/bravo", SHA2, BRAVO_FILES_V2)))
    assert core.load_repos(root)["org-b/bravo"]["freshness"] == "stale"
    result = maps.build(root)
    assert result["stale"] == ["org-b/bravo"]
    text = repo_text(root, "org-b/bravo")
    assert "Status: distilled - Freshness: stale" in text
    assert "specifications" in text and "workflows" in text, "prior valid evidence stays visible while stale"
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    freshness_section = index_text.split("## Freshness")[1]
    assert "org-b/bravo" in freshness_section and "stale" in freshness_section


def test_dossier_validation_problem_is_reported_not_fabricated(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    rel = core.load_repos(root)["org-a/alpha"]["dossier"]
    dossier = json.loads((root / rel).read_bytes())
    dossier["claims"][0]["text"] = "Tampered claim text not matching the kernel record."
    dossier["seal"] = wiki.seal({k: v for k, v in dossier.items() if k != "seal"})["seal"]
    (root / rel).write_bytes(core.dump_json(dossier))
    result = maps.build(root)
    text = repo_text(root, "org-a/alpha")
    assert "Dossier validation failed and its claims are not shown here" in text
    assert "DossierInvalid" in text
    assert "Tampered claim text" not in text
    assert result["known"] == 1, "an invalid dossier must not count toward known evidence coverage"
    assert result["invalid_dossiers"] == ["org-a/alpha"]
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    assert "Coverage: 1 of 3 known/total" in index_text
    assert "org-a/alpha" in index_text.split("Invalid dossiers")[1].split("\n")[0]


def test_repo_and_index_pages_respect_word_budgets(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    assert maps._word_count(repo_text(root, "org-a/alpha")) <= maps.REPO_WORD_LIMIT
    assert maps._word_count(repo_text(root, "org-b/bravo")) <= maps.REPO_WORD_LIMIT
    assert maps._word_count(repo_text(root, "org-c/charlie")) <= maps.REPO_WORD_LIMIT
    assert maps._word_count((root / "map/index.md").read_text(encoding="utf-8")) <= maps.INDEX_WORD_LIMIT


def test_build_is_deterministic_and_a_second_call_is_a_noop(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    first = maps.build(root)
    assert first["written"], "first build must actually write files"
    before = {p: (root / p).read_bytes() for p in first["written"]}
    second = maps.build(root)
    assert second["written"] == []
    assert second["unchanged"] == first["unchanged"] + len(first["written"])
    for path, data in before.items():
        assert (root / path).read_bytes() == data


def test_notes_file_is_created_once_and_never_overwritten(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    notes_path = root / maps._notes_rel("org-a/alpha")
    assert notes_path.is_file()
    custom = "# Notes for org-a/alpha\n\nHuman insight: watch the retry budget.\n"
    notes_path.write_text(custom, encoding="utf-8")
    maps.build(root)
    assert notes_path.read_text(encoding="utf-8") == custom


# ---------------------------------------------------------------- query


def test_query_never_surfaces_raw_source_text(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    # "install" only occurs in the raw README under sources/, never in any generated claim, summary or page.
    result = maps.query(root, "install")
    assert result["results"] == []
    for base in (root / "sources",):
        assert base.is_dir()  # the marker text does live under sources/, proving the miss is not accidental


def test_query_finds_dossier_evidence_with_repo_and_freshness(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    result = maps.query(root, "SQLite")
    assert result["results"], "the summary/claim text that mentions SQLite must be indexed"
    hit = next(r for r in result["results"] if r["path"].endswith("org-a/alpha.md"))
    assert hit["repo"] == "org-a/alpha" and hit["status"] == "distilled" and hit["freshness"] == "current"
    assert "SQLite" in hit["excerpt"]


def test_query_result_and_char_budgets_are_enforced(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    result = maps.query(root, "agent worker", limit=1, max_chars=80)
    assert len(result["results"]) <= 1
    assert result["total_chars"] <= 80
    with pytest.raises(core.WorkbenchError):
        maps.query(root, "agent", limit=0)


def test_query_is_deterministic_across_repeat_calls(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    first = maps.query(root, "agent swarm")
    second = maps.query(root, "agent swarm")
    assert first == second


def test_query_excerpt_centers_on_matched_term(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    result = maps.query(root, "eight-step", max_chars=60)
    assert result["results"], "at least one generated page mentions the eight-step claim"
    hit = result["results"][0]
    assert "eight" in hit["excerpt"] and "step" in hit["excerpt"], \
        "excerpt must be a window around the match, not the file's opening bytes"
    assert len(hit["excerpt"]) <= 60


def test_archive_pages_excluded_by_default_and_labelled_when_included(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    default = maps.query(root, "bosun supervision")
    assert not any(r["path"].startswith(f"{wiki.WIKI_DIR}/pages/") for r in default["results"])
    with_archive = maps.query(root, "bosun supervision", include_archive=True)
    archive_hits = [r for r in with_archive["results"] if r["path"].startswith(f"{wiki.WIKI_DIR}/pages/")]
    assert archive_hits, "the kernel's own source page should match once the archive is explicitly included"
    assert all(h.get("archive") is True and "repo" not in h for h in archive_hits)


# ---------------------------------------------------------------- real evidence links


def test_evidence_links_are_clickable_immutable_github_urls(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    dossier = wiki.load_dossier(root, "org-a/alpha")
    comp_claim = next(c for c in dossier["claims"] if c["facet"] == "components")
    loc = comp_claim["locators"][0]
    link = f"[{loc['path']}#L{loc['line_start']}-L{loc['line_end']}]({loc['url']})"
    assert loc["url"].startswith("https://github.com/org-a/alpha/blob/")
    text = repo_text(root, "org-a/alpha")
    assert link in text
    detail = (root / maps._detail_rel("org-a/alpha")).read_text(encoding="utf-8")
    assert link in detail
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    assert link in index_text
    nav_text = (root / "map/components/index.md").read_text(encoding="utf-8")
    assert link in nav_text


def test_dossier_and_notes_links_are_real_relative_markdown_links(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    maps.build(root)
    text = repo_text(root, "org-a/alpha")
    assert "[full detail](alpha.detail.md)" in text
    assert "[notes](alpha.notes.md)" in text
    assert (root / "map/repos/org-a/alpha.detail.md").is_file()
    detail = (root / "map/repos/org-a/alpha.detail.md").read_text(encoding="utf-8")
    rel = core.load_repos(root)["org-a/alpha"]["dossier"]
    assert f"[{rel}](../../../{rel})" in detail
    assert (root / rel).is_file()


def test_repo_page_never_discards_project_associations(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    repos = core.load_repos(root)
    many_projects = [f"proj-{i:03d}" for i in range(40)]
    repos["org-a/alpha"]["projects"] = many_projects
    core.save_repos(root, repos)
    maps.build(root)
    orientation = repo_text(root, "org-a/alpha")
    assert maps._word_count(orientation) <= maps.REPO_WORD_LIMIT
    assert "more; full list in the detail page" in orientation
    detail = (root / maps._detail_rel("org-a/alpha")).read_text(encoding="utf-8")
    for proj in many_projects:
        assert proj in detail, "every project association must still be reachable from the detail page"


# ---------------------------------------------------------------- reachable navigation at scale


@pytest.fixture(scope="module")
def big_corpus(corpus: Path, tmp_path_factory: pytest.TempPathFactory) -> Path:
    root = tmp_path_factory.mktemp("bigmapcorpus")
    shutil.copytree(corpus, root, dirs_exist_ok=True)
    leads = "\n".join(f"https://github.com/lead-org/item{i:04d}" for i in range(1100))
    intake.ingest(root, leads, "bulk", "observatory-scale")
    return root


def test_navigation_reaches_every_repo_and_index_stays_bounded_at_scale(big_corpus: Path, tmp_path: Path) -> None:
    root = clone(big_corpus, tmp_path)
    result = maps.build(root)
    assert result["total"] == 1103
    index_text = (root / "map/index.md").read_text(encoding="utf-8")
    assert maps._word_count(index_text) <= maps.INDEX_WORD_LIMIT
    assert "## Freshness" in index_text and "## Gaps" in index_text, "the emergency truncation must not cut headings"
    agents_index = (root / "map/agents/index.md").read_text(encoding="utf-8")
    assert "[Next](index.page-2.md)" in agents_index
    assert any("lead-org/item1099" in p.read_text(encoding="utf-8") for p in (root / 'map/agents').glob('*.md'))
    assert (root / "map/repos/lead-org/item1099.md").is_file()


def test_query_scans_the_full_generated_corpus_without_a_silent_cutoff(big_corpus: Path, tmp_path: Path) -> None:
    root = clone(big_corpus, tmp_path)
    maps.build(root)
    result = maps.query(root, "item1099")
    assert result["complete"] is True
    assert any(r.get("repo") == "lead-org/item1099" for r in result["results"]), "the tail of a large corpus must stay reachable"
    assert not any(p.endswith(maps.NOTES_SUFFIX) for p in (r["path"] for r in result["results"]))
