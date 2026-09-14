"""Tests for the pilot-review follow-ups: rename/identity lineage, coverage depth, facet-major comparison.

Reuses the real snapshot/prepare/apply pipeline from test_wiki.py and test_maps.py fixtures.
Coverage comes from genuine collector responses and selection limits. Removing an optional legacy
field tests backward compatibility; malformed or forged coverage must be rejected even if resealed.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import collect, core, directory, maps, wiki
from test_collect import SHA1, SHA2, FakeTransport, repo_routes
from test_wiki import FILES, good_proposal, slice_by_path, write
from test_maps import BRAVO_FILES, bravo_proposal, clone, repo_text

ALIASES_REL = directory.ALIASES_FILE


def _distill(root: Path, repo: str, sha: str, files: dict[str, bytes], proposal_fn, paths=None, max_files=20, truncated=False) -> dict:
    collect.snapshot(root, repo, max_files, 50_000, paths=paths, transport=FakeTransport(repo_routes(repo, sha, files, truncated=truncated)))
    p = wiki.prepare(root, repo)
    packet = json.loads((root / p["packet"]).read_bytes())
    proposal = proposal_fn(packet)
    wiki.apply(root, root / p["packet"], write(root / "proposals" / f"{repo.replace('/', '-')}.json", proposal))
    return json.loads((root / core.load_repos(root)[repo]["dossier"]).read_bytes())


def _patch_dossier(root: Path, repo: str, patch: dict) -> None:
    rel = core.load_repos(root)[repo]["dossier"]
    dossier = json.loads((root / rel).read_bytes())
    dossier.update(patch)
    dossier["seal"] = wiki.seal({k: v for k, v in dossier.items() if k != "seal"})["seal"]
    (root / rel).write_bytes(core.dump_json(dossier))


def write_aliases(root: Path, resolutions: list[dict]) -> None:
    core.atomic_write_bytes(root / ALIASES_REL, core.dump_json({"schema_version": 1, "resolutions": resolutions}))


def alias_row(requested: str, resolved: str, gid: int, **over) -> dict:
    base = {"authority": f"https://api.github.com/repos/{requested}", "github_repository_id": gid,
            "html_url": f"https://github.com/{resolved}", "observed_at": "2026-09-13T23:39:00+00:00",
            "outcome": "resolved", "private": False, "requested_repo": requested, "resolved_repo": resolved}
    return {**base, **over}


@pytest.fixture()
def corpus(tmp_path: Path) -> Path:
    root = tmp_path / "corpus"
    _distill(root, "org-a/alpha", SHA1, FILES, good_proposal, paths=["src/agent.py"])
    collect.snapshot(root, "org-b/bravo", 20, 50_000, transport=FakeTransport(repo_routes("org-b/bravo", SHA1, BRAVO_FILES)))
    p2 = wiki.prepare(root, "org-b/bravo")
    packet2 = json.loads((root / p2["packet"]).read_bytes())
    wiki.apply(root, root / p2["packet"], write(root / "proposals" / "bravo.json", bravo_proposal(packet2)))
    from map_agents import intake
    intake.ingest(root, "https://github.com/org-c/charlie", "chat", "observatory")
    return root


# --------------------------------------------------------------------------- 1. identity lineage


def test_repo_page_shows_rename_when_canonical_not_tracked(corpus: Path) -> None:
    write_aliases(corpus, [alias_row("org-a/alpha", "org-a/alpha-renamed", 983715534)])
    maps.build(corpus)
    text = repo_text(corpus, "org-a/alpha")
    assert "Renamed: GitHub reports this repository is now `org-a/alpha-renamed`" in text
    assert "github id 983715534" in text and "not yet tracked under that identity" in text
    assert "[https://github.com/org-a/alpha-renamed](https://github.com/org-a/alpha-renamed)" in text


def test_two_leads_resolve_to_one_current_identity(corpus: Path) -> None:
    """M3-shaped fixture: two former identities both now point at the same canonical, tracked repo."""
    from map_agents import intake
    intake.ingest(corpus, "https://github.com/new-org/canonical", "chat", "observatory")
    write_aliases(corpus, [
        alias_row("old-org/one", "new-org/canonical", 555000111),
        alias_row("old-org-two/two", "new-org/canonical", 555000111),
    ])
    maps.build(corpus)
    text = repo_text(corpus, "new-org/canonical")
    assert "Formerly: old-org/one, old-org-two/two" in text
    assert "github id 555000111" in text


def test_repo_page_links_to_canonical_dossier_when_tracked(corpus: Path) -> None:
    from map_agents import intake
    intake.ingest(corpus, "https://github.com/org-a/alpha-renamed", "chat", "observatory")
    write_aliases(corpus, [alias_row("org-a/alpha", "org-a/alpha-renamed", 42)])
    maps.build(corpus)
    text = repo_text(corpus, "org-a/alpha")
    assert "[org-a/alpha-renamed](../org-a/alpha-renamed.md)" in text
    assert "canonical dossier" in text


def test_repo_record_own_id_and_aliases_are_accepted_without_external_file(corpus: Path) -> None:
    repos = core.load_repos(corpus)
    repos["org-a/alpha"]["github_repository_id"] = 999
    repos["org-a/alpha"]["aliases"] = ["old-collector-known/name"]
    core.save_repos(corpus, repos)
    maps.build(corpus)
    text = repo_text(corpus, "org-a/alpha")
    assert "Formerly: old-collector-known/name (github id 999)" in text


def test_directory_entry_links_renamed_lead_to_canonical_dossier(corpus: Path) -> None:
    write_aliases(corpus, [alias_row("org-b/bravo", "org-b/bravo-new", 1010)])
    view = directory.resolve(corpus)
    # Simulate a directory page whose only repo hint is the pre-rename identity.
    entry = directory._build_entry("x", None, None,
                                    {"frontmatter": {"source_code_url": "https://github.com/org-b/bravo"}, "body": "", "path": "agents/x.md", "error": None},
                                    {}, None, core.load_repos(corpus), directory.load_aliases(corpus))
    assert entry["repo_key"] == "org-b/bravo" and entry["repo_canonical_key"] == "org-b/bravo-new"
    assert entry["repo_canonical_tracked"] is False  # bravo-new not tracked yet
    rendered, _ = directory._render_entry(entry)
    assert "not yet tracked under the new identity" in rendered
    from map_agents import intake
    intake.ingest(corpus, "https://github.com/org-b/bravo-new", "chat", "observatory")
    entry2 = directory._build_entry("x", None, None,
                                     {"frontmatter": {"source_code_url": "https://github.com/org-b/bravo"}, "body": "", "path": "agents/x.md", "error": None},
                                     {}, None, core.load_repos(corpus), directory.load_aliases(corpus))
    assert entry2["repo_canonical_key"] == "org-b/bravo-new" and entry2["repo_canonical_tracked"] is True
    rendered2, _ = directory._render_entry(entry2)
    assert "[org-b/bravo-new](../../repos/org-b/bravo-new.md)" in rendered2
    assert "org-b/bravo" in rendered2, "the original lead stays visible alongside the canonical link"


def test_malformed_alias_data_never_crashes_or_invents_a_rename(corpus: Path) -> None:
    for bad in [b"not json", b'{"resolutions": "not-a-list"}',
                b'{"resolutions": [{"requested_repo": "a/b", "resolved_repo": "c/d", "outcome": "not_found", "github_repository_id": 1}]}',
                b'{"resolutions": [{"requested_repo": "a/b", "resolved_repo": "c/d", "outcome": "resolved", "github_repository_id": "not-a-number"}]}']:
        core.atomic_write_bytes(corpus / ALIASES_REL, bad)
        aliases = directory.load_aliases(corpus)
        assert aliases == {"by_former": {}, "by_canonical": {}}
        result = maps.build(corpus)  # must not raise
        assert result["repos"] == 3
        text = repo_text(corpus, "org-a/alpha")
        assert "Renamed:" not in text and "Formerly:" not in text


def test_aliases_participate_in_stale_view(corpus: Path) -> None:
    maps.build(corpus)
    fresh = maps.query(corpus, "alpha")
    assert fresh["stale_view"] is False
    write_aliases(corpus, [alias_row("org-a/alpha", "org-a/alpha-renamed", 1)])
    stale = maps.query(corpus, "alpha")
    assert stale["stale_view"] is True, "a new/changed alias file alone must invalidate the generated view"
    maps.build(corpus)
    assert maps.query(corpus, "alpha")["stale_view"] is False


# --------------------------------------------------------------------------- 2. coverage depth


def test_legacy_dossier_reports_coverage_unknown_not_complete(corpus: Path) -> None:
    for repo in ("org-a/alpha", "org-b/bravo"):
        path = corpus / core.load_repos(corpus)[repo]["dossier"]
        dossier = json.loads(path.read_bytes())
        dossier.pop("coverage")  # A real legacy dossier predates this optional field.
        dossier["seal"] = wiki.seal(dossier)["seal"]
        path.write_bytes(core.dump_json(dossier))
    result = maps.build(corpus)
    assert result["coverage"] == {"unknown": 2}
    text = repo_text(corpus, "org-a/alpha")
    assert "Source coverage (unknown): selection unknown (legacy dossier" in text
    assert "repository completeness unknown (legacy dossier)" in text
    assert "3 documented, 1 code-inspected" in text
    index_text = (corpus / "map/index.md").read_text(encoding="utf-8")
    assert "complete=0, partial=0, unknown=2" in index_text
    assert "a current commit is not complete source coverage" in index_text.lower()


def test_partial_and_complete_coverage_are_distinguished_from_freshness(tmp_path: Path) -> None:
    corpus = tmp_path / "corpus"
    files = {**FILES, **{f"docs/extra-{i:02}.md": b"# Additional documentation\n" for i in range(15)}}
    _distill(corpus, "org-a/alpha", SHA1, files, good_proposal, paths=["src/agent.py"], max_files=3)
    _distill(corpus, "org-b/bravo", SHA1, BRAVO_FILES, bravo_proposal)
    result = maps.build(corpus)
    assert result["coverage"] == {"complete": 1, "partial": 1}
    alpha_text = repo_text(corpus, "org-a/alpha")
    assert "Source coverage (partial): 3 of 19 candidate file(s) selected (selection incomplete); repository tree complete" in alpha_text
    bravo_text = repo_text(corpus, "org-b/bravo")
    assert "Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete" in bravo_text
    fresh_text = (corpus / "map/freshness/index.md").read_text(encoding="utf-8")
    assert "org-a/alpha) [coverage: partial]" in fresh_text or "[coverage: partial]" in fresh_text
    assert "[coverage: complete]" in fresh_text
    assert "matches the latest locally collected snapshot" in fresh_text
    assert "A lookup does not check upstream HEAD" in fresh_text
    index_text = (corpus / "map/index.md").read_text(encoding="utf-8")
    assert "complete=1, partial=1, unknown=0" in index_text


def test_repository_tree_truncated_is_shown_even_when_selection_complete(tmp_path: Path) -> None:
    corpus = tmp_path / "corpus"
    _distill(corpus, "org-a/alpha", SHA1, FILES, good_proposal, paths=["src/agent.py"], truncated=True)
    maps.build(corpus)
    text = repo_text(corpus, "org-a/alpha")
    assert "Source coverage (partial): 4 of 4 candidate file(s) selected; repository tree truncated (partial listing)" in text


def test_malformed_coverage_field_is_rejected_even_when_resealed(corpus: Path) -> None:
    _patch_dossier(corpus, "org-a/alpha", {"coverage": {"selection": "not-a-dict", "repository": None}})
    result = maps.build(corpus)
    assert result["coverage"] == {"complete": 1}
    assert result["invalid_dossiers"] == ["org-a/alpha"]
    with pytest.raises(wiki.DossierInvalid, match="coverage shape"):
        wiki.load_dossier(corpus, "org-a/alpha")


# --------------------------------------------------------------------------- 3. facet-major comparison


def test_features_index_lists_every_facet_with_counts(corpus: Path) -> None:
    maps.build(corpus)
    text = (corpus / "map/features/index.md").read_text(encoding="utf-8")
    for facet in wiki.FACETS:
        assert f"[{facet}]({facet}.md)" in text
    index_text = (corpus / "map/index.md").read_text(encoding="utf-8")
    assert "features/index.md" in index_text and "## Features" in index_text
    pointer = (corpus / "AGENTS_CORPUS.md").read_text(encoding="utf-8")
    assert "features/index.md" in pointer


def test_facet_page_distinguishes_unknown_from_product_absence(corpus: Path) -> None:
    """Positive counterexample: org-a/alpha's dossier (components, memory-state, interfaces, relevance)
    has no `specifications` claim, so that facet page must call it `unknown` (no source-linked claim
    submitted), never `documented absence` or any wording that reads as a verified statement that the
    product lacks the feature. Only an actual source-linked claim saying the product lacks a capability
    could ever support real absence."""
    maps.build(corpus)
    relevance = (corpus / "map/features/relevance.md").read_text(encoding="utf-8")
    assert "org-a/alpha" in relevance and "[inference/documented]" in relevance
    assert "bosun supervision" in relevance
    specifications = (corpus / "map/features/specifications.md").read_text(encoding="utf-8")
    assert "documented absence" not in specifications.lower()
    assert "unknown" in specifications.lower()
    assert "no source-linked claim submitted" in specifications
    assert "not evidence the product lacks the feature" in specifications
    assert "org-a/alpha" in specifications  # distilled, examined, no claim for this facet: unknown, not absent
    assert "org-c/charlie" not in specifications, "a never-distilled lead is a different kind of unknown and must not appear here"
    assert "org-c/charlie" not in relevance
    for facet_page in (relevance, specifications):
        assert "documented absence" not in facet_page.lower()


def test_never_distilled_lead_never_appears_on_any_facet_page(corpus: Path) -> None:
    maps.build(corpus)
    for facet in wiki.FACETS:
        text = (corpus / f"map/features/{facet}.md").read_text(encoding="utf-8")
        assert "org-c/charlie" not in text


def test_facet_page_evidence_matches_existing_component_index_label_format(corpus: Path) -> None:
    maps.build(corpus)
    components_nav = (corpus / "map/components/index.md").read_text(encoding="utf-8")
    components_facet = (corpus / "map/features/components.md").read_text(encoding="utf-8")
    line = next(l for l in components_nav.splitlines() if "org-a/alpha" in l)
    evidence = line.split("--", 1)[0].split("]", 1)[1].strip()
    assert evidence in components_facet


def test_query_finds_facet_pages(corpus: Path) -> None:
    maps.build(corpus)
    result = maps.query(corpus, "bosun supervision", max_chars=8000)
    assert any(r["path"] == "map/features/relevance.md" for r in result["results"])
