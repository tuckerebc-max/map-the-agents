import json
import os
from pathlib import Path

import pytest
from conftest import canonical_bytes, ingest, proposal, source
from hypothesis import given
from hypothesis import strategies as st


def test_interview_claim_cannot_store_forbidden_verbatim_text(api, corpus):
    root, sources = corpus
    path = source(
        sources,
        text="# Interview\n\nOur class used the tool but we cannot tell whether it helped.\n",
        source_type="interview",
        access="confidential",
        identifiers={},
        consent={"state": "granted", "quote": False, "paraphrase": True, "identify": False, "publish": False},
    )
    packet = api.ingest_prepare(root, path.name)
    with pytest.raises(Exception, match="RCW_CONSENT_QUOTE"):
        api.ingest_apply(
            root,
            packet["operation_id"],
            proposal(packet, "Our class used the tool but we cannot tell whether it helped."),
        )


def test_source_access_downgrade_is_not_automatically_accepted(api, corpus):
    root, sources = corpus
    path = source(sources, access="restricted")
    ingest(api, root, path)
    source(sources, access="public")
    packet = api.ingest_prepare(root, path.name)
    with pytest.raises(Exception, match="RCW_ACCESS_DOWNGRADE"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))


def test_noop_still_detects_damaged_canonical_pages(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    page = next((root / "pages/sources").glob("*.md"))
    page.write_text(page.read_text().replace("rcw:end", "rcw:invalid"))
    packet = api.ingest_prepare(root, path.name)
    with pytest.raises(Exception, match="RCW_AUDIT_FAILED"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))


def test_cli_returns_json_error_without_python_traceback(api, corpus):
    import subprocess
    import sys

    root, _ = corpus
    script = Path(__file__).resolve().parents[1] / "scripts/rcw.py"
    result = subprocess.run(
        [sys.executable, str(script), "ingest", "prepare", str(root), "missing"],
        text=True,
        capture_output=True,
    )
    assert result.returncode == 3
    assert "Traceback" not in result.stderr
    assert json.loads(result.stderr)["error"] == "RCW_PACKAGE_AMBIGUOUS"


def test_invalid_access_and_limits_are_clear_errors(api, corpus):
    root, _ = corpus
    with pytest.raises(Exception, match="RCW_ACCESS_POLICY"):
        api.ask_prepare(root, "question", access="everyone")
    with pytest.raises(Exception, match="RCW_LIMIT_INVALID"):
        api.analyze_prepare(root, limit=-5)


def test_quote_length_policy_applies_to_stored_claims(api, corpus):
    root, sources = corpus
    sentence = " ".join("distinctword" + str(i) for i in range(25))
    path = source(sources, text="# Finding\n\n" + sentence + "\n")
    packet = api.ingest_prepare(root, path.name)
    with pytest.raises(Exception, match="RCW_QUOTE_LIMIT"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet, sentence))


def test_apply_failure_restores_all_original_bytes(api, corpus, monkeypatch):
    from rcw_core import storage

    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    before = canonical_bytes(root)
    original = storage.replace_file
    count = 0

    def interrupted(target, text):
        nonlocal count
        count += 1
        if count == 3:
            raise OSError("simulated disk failure")
        return original(target, text)

    monkeypatch.setattr(storage, "replace_file", interrupted)
    with pytest.raises(OSError, match="disk failure"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))
    assert canonical_bytes(root) == before


def test_live_lease_prevents_write(api, corpus):
    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    lock = root / "state/leases/corpus.lock"
    lock.write_text(json.dumps({"pid": os.getpid()}))
    with pytest.raises(Exception, match="RCW_LEASE_ACTIVE"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))


def test_recovery_restores_interrupted_transaction(api, corpus):
    from rcw_core.storage import digest

    root, _ = corpus
    path = root / "data/claims.jsonl"
    path.write_bytes(b"partial write\n")
    operation = root / "state/operations/op_interrupted"
    operation.mkdir()
    (operation / "journal.json").write_text(
        json.dumps(
            {
                "operation_id": "op_interrupted",
                "state": "prepared",
                "entries": [
                    {"path": "data/claims.jsonl", "before": "", "after_digest": digest(b"partial write\n")}
                ],
            }
        )
    )
    assert api.recover(root)["recovered"] == ["op_interrupted"]
    assert path.read_bytes() == b""


def test_source_change_during_apply_rolls_back(api, corpus, monkeypatch):
    from rcw_core import storage

    root, sources = corpus
    path = source(sources)
    packet = api.ingest_prepare(root, path.name)
    before = canonical_bytes(root)
    original = storage.replace_file
    mutated = False

    def mutate_after_write(target, text):
        nonlocal mutated
        original(target, text)
        if not mutated:
            mutated = True
            path.write_text("Concurrent external source change")

    monkeypatch.setattr(storage, "replace_file", mutate_after_write)
    with pytest.raises(Exception, match="RCW_SOURCE_MUTATED"):
        api.ingest_apply(root, packet["operation_id"], proposal(packet))
    assert canonical_bytes(root) == before


def test_audit_detects_unregistered_material_assertion(api, corpus):
    root, sources = corpus
    path = source(sources)
    ingest(api, root, path)
    page = next((root / "pages/sources").glob("*.md"))
    page.write_text(
        page.read_text().replace("<!-- rcw:end", "An uncited medical miracle was proven.\n<!-- rcw:end")
    )
    assert not api.audit(root)["ok"]


def test_entity_and_gap_pages_are_generated(api, corpus):
    root, sources = corpus
    path = source(sources, source_type="synthesis_report")
    packet = api.ingest_prepare(root, path.name)
    proposed = proposal(packet)
    proposed["entities"] = [
        {"key": "reading", "name": "Reading", "entity_type": "concept", "claim_keys": ["result"]}
    ]
    api.ingest_apply(root, packet["operation_id"], proposed)
    assert list((root / "pages/entities").glob("*.md"))
    assert list((root / "pages/gaps").glob("*.md"))


@given(st.lists(st.sampled_from(["public", "internal", "confidential", "restricted"]), min_size=1))
def test_access_join_never_downgrades_any_input(values):
    from rcw_core.storage import ACCESS, maximum_access

    result = maximum_access(values)
    assert all(ACCESS[result] >= ACCESS[v] for v in values)


@given(st.dictionaries(st.text(min_size=1, max_size=20), st.integers()))
def test_canonical_serialization_is_independent_of_dictionary_order(value):
    from rcw_core.storage import canonical

    assert canonical(value) == canonical(dict(reversed(list(value.items()))))


def test_metadata_can_be_registered_without_touching_source_root(api, corpus):
    root, sources = corpus
    (sources / "paper.md").write_text("# Result\n\nA reported result.\n")
    before = {p.name: p.read_bytes() for p in sources.iterdir()}
    api.register_metadata(
        root,
        "primary:paper.md",
        {"title": "Paper", "creator": "Office", "source_type": "report", "access": "public"},
    )
    assert api.inventory(root)["items"][0]["status"] == "new"
    assert {p.name: p.read_bytes() for p in sources.iterdir()} == before


def test_quartz_builder_rejects_a_moving_pin(tmp_path):
    import importlib

    builder = importlib.import_module("quartz_build")
    with pytest.raises(Exception, match="full 40-character"):
        builder.build_quartz(tmp_path, tmp_path, tmp_path, "main")


def test_exported_schemas_validate_against_actual_models():
    import importlib

    exporter = importlib.import_module("export_schemas")
    assert exporter.export_schemas(check=True)["ok"]


def test_demo_builds_both_views_and_passes_audit(tmp_path):
    import importlib

    demo = importlib.import_module("demo")
    result = demo.run_demo(tmp_path / "demo")
    assert result["audit"]["ok"]
    assert result["repeat_ingest_changed"] is False
    assert (tmp_path / "demo/public/index.html").exists()
    public_text = "\n".join(p.read_text() for p in (tmp_path / "demo/public").rglob("*.html"))
    assert "Restricted participant" not in public_text
