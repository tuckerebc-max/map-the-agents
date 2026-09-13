import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
from conftest import canonical_bytes, ingest, proposal, rows, source


def test_init_creates_portable_config_and_empty_valid_corpus(api, corpus):
    root, sources = corpus
    assert (root / "wiki.yaml").exists()
    assert str(sources) not in (root / "wiki.yaml").read_text()
    assert api.audit(root)["ok"]


def test_inventory_does_not_write_and_hashes_all_bytes(api, corpus):
    root, sources = corpus
    path = source(sources)
    before = canonical_bytes(root)
    item = api.inventory(root)["items"][0]
    assert item["status"] == "new"
    assert item["files"][0]["digest"] == "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
    assert canonical_bytes(root) == before


def test_ingest_preserves_sources_and_traces_claim_to_slice(api, corpus):
    root, sources = corpus
    path = source(sources)
    original = path.read_bytes()
    _, result = ingest(api, root, path)
    assert result["changed"] is True
    assert path.read_bytes() == original
    claim = rows(root, "claims")[0]
    slice_row = rows(root, "slices")[-1]
    assert claim["slice_ids"] == [slice_row["id"]]
    assert slice_row["locator"]["line_start"] == 3
    assert api.audit(root)["ok"]


def test_noop_ingest_creates_no_canonical_diff(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    before = canonical_bytes(root)
    _, result = ingest(api, root, path)
    assert result["changed"] is False
    assert canonical_bytes(root) == before


def test_revision_preserves_history_and_unrelated_human_prose(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    page = next((root / "pages" / "sources").glob("*.md"))
    with page.open("a") as stream:
        stream.write("\nHuman note: verify this with the research team.\n")
    path.write_text("# Findings\n\nReading scores rose by 8 points in the study sample.\n")
    packet = api.ingest_prepare(root, path.name)
    api.ingest_apply(
        root, packet["operation_id"], proposal(packet, "Reading scores rose by 8 points in the study sample.")
    )
    assert len(rows(root, "source_versions")) == 2
    assert any(r["review_state"] == "superseded" for r in rows(root, "claims"))
    assert "Human note: verify" in page.read_text()


def test_unknown_evidence_is_rejected_without_writes(api, corpus):
    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    bad = proposal(packet)
    bad["claims"][0]["slice_ids"] = ["slc_" + "a" * 64]
    before = canonical_bytes(root)
    with pytest.raises(Exception, match="RCW_PROPOSAL_OUT_OF_SCOPE"):
        api.ingest_apply(root, packet["operation_id"], bad)
    assert canonical_bytes(root) == before


def test_unknown_proposal_field_is_rejected(api, corpus):
    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    bad = proposal(packet)
    bad["approve_all"] = True
    with pytest.raises(Exception, match="RCW_SCHEMA_INVALID"):
        api.ingest_apply(root, packet["operation_id"], bad)


def test_source_changed_after_prepare_fails_closed(api, corpus):
    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    path.write_text("Changed during extraction")
    with pytest.raises(Exception, match="RCW_SOURCE_MUTATED"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))


def test_stale_base_is_rejected(api, corpus):
    root, sources = corpus
    path = source(sources)
    first = api.ingest_prepare(root, path.name)
    second = api.ingest_prepare(root, path.name)
    api.ingest_apply(root, first["operation_id"], proposal(first))
    with pytest.raises(Exception, match="RCW_BASE_DIVERGED"):
        api.ingest_apply(root, second["operation_id"], proposal(second))


def test_symlink_escape_is_blocked(api, corpus, tmp_path, symlink):
    root, sources = corpus
    outside = tmp_path / "outside.md"
    outside.write_text("private outside data")
    symlink(sources / "escape.md", outside)
    assert api.inventory(root)["items"][0]["status"] == "blocked"


def test_interview_without_consent_is_blocked(api, corpus):
    root, sources = corpus
    source(sources, source_type="interview", access="confidential", identifiers={})
    assert api.inventory(root)["items"][0]["status"] == "blocked"


def test_research_container_does_not_become_original_authority(api, corpus):
    root, sources = corpus
    path = source(
        sources,
        source_type="synthesis_report",
        original_sources=[
            {"title": "Missing evaluation", "identifier": "evaluation-2025", "locator": "p. 8"}
        ],
    )
    ingest(api, root, path)
    claim = rows(root, "claims")[0]
    assert claim["review_state"] == "unverified"
    assert claim["lineage_status"] == "original_missing"
    assert rows(root, "gaps")


def test_completed_manifest_ingests_all_members_once(api, corpus):
    root, sources = corpus
    folder = sources / "package"
    folder.mkdir()
    (folder / "report.md").write_text("# Report\n\nSome evidence.\n")
    (folder / "manifest.json").write_text(
        json.dumps(
            {
                "complete": True,
                "files": [
                    {
                        "path": "report.md",
                        "metadata": {
                            "title": "Report",
                            "creator": "Office",
                            "date": "2026-01-01",
                            "source_type": "report",
                            "access": "public",
                            "identifiers": {},
                        },
                    }
                ],
            }
        )
    )
    items = api.inventory(root)["items"]
    assert len(items) == 1
    packet = api.ingest_prepare(root, items[0]["key"])
    api.ingest_apply(root, packet["operation_id"], proposal(packet, "Some evidence."))
    assert len(rows(root, "sources")) == 1


def test_html_excludes_scripts_and_keeps_locator(api, corpus):
    root, sources = corpus
    path = source(
        sources,
        name="report.html",
        text='<h1 id="finding">Finding</h1><script>send_all_secrets()</script><p>Safe visible finding.</p>',
        source_type="report",
    )
    packet = api.ingest_prepare(root, path.name)
    assert "send_all_secrets" not in json.dumps(packet)
    assert any("Safe visible finding." in s["text"] for s in packet["slices"])


def test_public_render_omits_restricted_content_and_metadata(api, corpus, tmp_path):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    secret = source(
        sources,
        name="interview.md",
        text="# Interview\n\nSecret person has confidential concerns.\n",
        title="Secret person interview",
        source_type="interview",
        access="restricted",
        identifiers={},
        consent={"state": "granted", "quote": False, "paraphrase": True, "identify": False, "publish": False},
    )
    packet = api.ingest_prepare(root, secret.name)
    api.ingest_apply(root, packet["operation_id"], proposal(packet, "The participant described concerns."))
    output = tmp_path / "site"
    api.render(root, output, adapter="html", access="public")
    text = "\n".join(p.read_text() for p in output.rglob("*") if p.is_file())
    assert "12 points" in text
    assert "Secret person" not in text
    assert "interview.md" not in text
    assert "confidential concerns" not in text


def test_renderer_is_deterministic_and_escapes_html(api, corpus, tmp_path):
    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    api.ingest_apply(root, packet["operation_id"], proposal(packet, "<script>alert(1)</script> Scores rose."))
    out1, out2 = tmp_path / "one", tmp_path / "two"
    api.render(root, out1, adapter="html", access="public")
    api.render(root, out2, adapter="html", access="public")
    assert canonical_bytes(out1) == canonical_bytes(out2)
    assert "<script>alert(1)</script>" not in (out1 / "index.html").read_text()


def test_quartz_export_emits_content_and_evidence_cards(api, corpus, tmp_path):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    output = tmp_path / "quartz"
    api.render(root, output, adapter="quartz", access="public")
    assert (output / "content" / "index.md").exists()
    assert list((output / "content" / "evidence").glob("*.md"))


def test_ask_requires_opened_source_evidence(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    packet = api.ask_prepare(root, "reading scores", access="public")
    assert packet["claims"] and packet["slices"]
    answer = {
        "schema_version": "1.0",
        "operation_id": packet["operation_id"],
        "status": "answered",
        "assertions": [{"text": "Scores rose in this sample.", "claim_ids": [packet["claims"][0]["id"]]}],
        "limitations": ["One study sample."],
    }
    result = api.ask_complete(root, packet["operation_id"], answer)
    assert "evidence/" in result["markdown"]


def test_answer_without_evidence_must_refuse(api, corpus):
    root, _ = corpus
    packet = api.ask_prepare(root, "Does this work?", access="public")
    bad = {
        "schema_version": "1.0",
        "operation_id": packet["operation_id"],
        "status": "answered",
        "assertions": [{"text": "Yes.", "claim_ids": []}],
        "limitations": [],
    }
    with pytest.raises(Exception, match="RCW_EVIDENCE_REQUIRED"):
        api.ask_complete(root, packet["operation_id"], bad)
    good = {
        **bad,
        "status": "insufficient_evidence",
        "assertions": [],
        "limitations": ["No source evidence is available."],
    }
    assert "insufficient_evidence" in api.ask_complete(root, packet["operation_id"], good)["status"]


def test_analysis_accepts_cited_assertions_and_preserves_disagreement(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    packet = api.analyze_prepare(root)
    cid = packet["claims"][0]["id"]
    proposed = {
        "schema_version": "1.0",
        "operation_id": packet["operation_id"],
        "pages": [
            {
                "key": "reading",
                "title": "Reading evidence",
                "page_type": "finding",
                "assertions": [
                    {"text": "A study reports improvement within its sample.", "claim_ids": [cid]}
                ],
            }
        ],
        "relationships": [],
        "gaps": [
            {"question": "Does the finding generalize?", "reason": "Only one sample.", "claim_ids": [cid]}
        ],
    }
    api.analyze_apply(root, packet["operation_id"], proposed)
    assert list((root / "pages" / "findings").glob("*.md"))
    assert rows(root, "gaps")
    assert api.audit(root)["ok"]


def test_audit_detects_changed_claim_access(api, corpus):
    root, sources = corpus
    path = source(sources, access="restricted")
    ingest(api, root, path)
    data = rows(root, "claims")
    data[0]["access"] = "public"
    (root / "data" / "claims.jsonl").write_text("\n".join(json.dumps(row) for row in data) + "\n")
    report = api.audit(root)
    assert not report["ok"]
    assert any("ACCESS" in e["code"] for e in report["errors"])


def test_audit_detects_marker_damage(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    page = next((root / "pages" / "sources").glob("*.md"))
    page.write_text(page.read_text().replace("rcw:end", "rcw:broken"))
    assert not api.audit(root)["ok"]


def test_citation_exports_keep_legal_types_without_doi_invention(api, corpus):
    root, sources = corpus
    path = source(
        sources,
        source_type="legislation",
        identifiers={},
        jurisdiction="Vermont",
        legal_status="enacted",
        status_date="2026-01-01",
        provision="Section 2",
    )
    ingest(api, root, path)
    csl = api.export_citations(root, "csl-json", "public")
    assert csl[0]["type"] == "legislation"
    assert "DOI" not in csl[0]
    assert "Vermont" in api.export_citations(root, "bibtex", "public")


def test_sync_and_review_packet_are_real_outputs(api, corpus):
    root, sources = corpus
    path = source(sources)
    assert len(api.sync_plan(root)["pending"]) == 1
    ingest(api, root, path)
    assert not api.sync_plan(root)["pending"]
    review = api.review_packet(root)
    assert review["counts"]["claims"] == 1
    assert review["audit"]["ok"]


def test_cli_runs_from_outside_skill_directory(tmp_path):
    script = Path(__file__).resolve().parents[1] / "scripts" / "rcw.py"
    result = subprocess.run(
        [sys.executable, str(script), "--help"], cwd=tmp_path, text=True, capture_output=True
    )
    assert result.returncode == 0, result.stderr
    assert "ingest" in result.stdout
