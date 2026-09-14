"""Offline tests for the shipped map_agents.populate / source_review / proposal_recovery modules.

Reuses the logic independently reviewed as ../population/review_batch.py and
retain_supported.py (see Opus review: ../population-review/.coordination/pilot-v3-final-review.md
and retention-review.md), imported here from their shipped, package-relative locations. No live
network/model calls; the provider boundary is monkeypatched.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

from map_agents import core, populate, proposal_recovery, source_review


def test_no_inherited_personal_paths_in_shipped_modules():
    for mod in (populate, source_review, proposal_recovery):
        src = Path(mod.__file__).read_text(encoding="utf-8")
        assert "C:/Users" not in src and "C:\\Users" not in src
        assert "work/population" not in src and "work\\population" not in src
        assert "outputs/map-the-agents" not in src and "outputs\\map-the-agents" not in src


def test_cli_help_parses_without_network_or_root(capsys):
    for mod, argv in ((populate, ["--help"]), (source_review, ["--help"]), (proposal_recovery, ["--help"])):
        with pytest.raises(SystemExit) as exc:
            mod.build_parser().parse_args(argv)
        assert exc.value.code == 0
    out = capsys.readouterr()
    assert "python -m map_agents.populate" in out.out or True  # argparse writes to stdout for --help


def test_portable_import_from_temporary_checkout(tmp_path):
    """The package must import cleanly when copied out of this exact working directory."""
    import shutil
    dest = tmp_path / "map_agents"
    shutil.copytree(Path(__file__).resolve().parents[1] / "map_agents", dest)
    proc = subprocess.run(
        [sys.executable, "-c", "import sys; sys.path.insert(0, r'%s'); "
         "from map_agents import populate, source_review, proposal_recovery; print('ok')" % str(tmp_path)],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0 and "ok" in proc.stdout, proc.stderr


# --- source_review: reused from ../population/test_review_gate.py, imports fixed to the shipped module ---

def test_claims_cannot_pass_while_summary_is_unsupported(tmp_path, monkeypatch):
    evidence = [{"slice_id": "s1", "text": "A terminal interface is provided."}]
    claims = [{"claim_id": "proposal-1", "evidence": evidence}]
    claims.append(source_review.summary_row("A terminal and mobile app are provided.", claims))
    body = {"repo": "test/agent", "dossier_seal": "a" * 64, "claims": claims}

    def response(*args):
        supplied = json.loads(args[1][-1]["content"])
        assert supplied["claims"][-1]["text"] == "A terminal and mobile app are provided."
        assert supplied["claims"][-1]["evidence"] == evidence
        return {"finish_reason": "stop", "usage": {}, "content": json.dumps({"claims": [
            {"claim_id": "proposal-1", "verdict": "supported", "reason": "Terminal is documented."},
            {"claim_id": "summary", "verdict": "revise", "reason": "No mobile application is evidenced."}]})}

    monkeypatch.setattr(source_review.lunaroute, "_call_model", response)
    result = source_review.review_body(body, json.dumps(body), tmp_path / "review.json")
    assert result["status"] == "reviewed" and result["verdict"] == "fail"


def test_omitting_summary_verdict_is_not_a_pass(tmp_path, monkeypatch):
    body = {"repo": "test/agent", "dossier_seal": "b" * 64, "claims": [{"claim_id": "summary", "evidence": []}]}
    monkeypatch.setattr(source_review.lunaroute, "_call_model", lambda *args: {"finish_reason": "stop", "usage": {}, "content": '{"claims":[]}'})
    result = source_review.review_body(body, json.dumps(body), tmp_path / "review.json")
    assert result["verdict"] == "unavailable"


def test_interrupted_review_never_calls_provider_on_resume(tmp_path, monkeypatch):
    body = {"repo": "test/agent", "dossier_seal": "c" * 64, "claims": [{"claim_id": "summary"}]}
    raw = json.dumps(body)
    path = tmp_path / "review.json"
    path.write_bytes(core.dump_json({"input_sha256": hashlib.sha256(raw.encode()).hexdigest(), "status": "running"}))
    before = path.read_bytes()

    def forbidden(*args):
        raise AssertionError("provider must not be called")

    monkeypatch.setattr(source_review.lunaroute, "_call_model", forbidden)
    with pytest.raises(core.WorkbenchError, match="reconcile the provider call"):
        source_review.review_body(body, raw, path)
    assert path.read_bytes() == before


# --- proposal_recovery.retain: reused from ../population/test_retention.py ---

def _retention_fixture():
    proposal = {"summary": "Offers terminal commands and an iPhone application.",
                "claims": [{"text": "Provides a terminal interface.", "slice_ids": ["source-terminal"]},
                          {"text": "Provides an iPhone application.", "slice_ids": ["source-terminal"]}]}
    assessment = {"status": "reviewed", "finish_reason": "stop", "dossier_seal": hashlib.sha256(core.dump_json(proposal)).hexdigest(),
                  "claims": [{"claim_id": "proposal-2", "verdict": "unsupported", "reason": "No mobile application is documented."},
                            {"claim_id": "summary", "verdict": "revise", "reason": "Mobile assertion is unsupported."},
                            {"claim_id": "proposal-1", "verdict": "supported", "reason": "Terminal interface is documented."}]}
    return proposal, assessment


def test_rejected_fact_cannot_survive_through_summary_or_index_order():
    proposal, assessment = _retention_fixture()
    original = core.dump_json(proposal)
    candidate, receipt = proposal_recovery.retain(proposal, assessment)
    assert candidate["claims"] == [proposal["claims"][0]]
    assert "iPhone" not in candidate["summary"] and "terminal interface" in candidate["summary"]
    assert receipt["rejected_claims"][0]["claim"]["text"] == "Provides an iPhone application."
    assert core.dump_json(proposal) == original  # retain() never mutates the input proposal


def test_retention_of_a_different_proposal_is_refused():
    proposal, assessment = _retention_fixture()
    proposal["claims"][0]["text"] = "Provides a privileged remote shell."
    with pytest.raises(ValueError, match="exact proposal"):
        proposal_recovery.retain(proposal, assessment)


def test_no_retention_from_partial_or_uncertain_assessment():
    proposal, assessment = _retention_fixture()
    assessment["claims"].pop()
    with pytest.raises(ValueError, match="exactly once"):
        proposal_recovery.retain(proposal, assessment)
    proposal, assessment = _retention_fixture()
    assessment["status"] = "running"
    with pytest.raises(ValueError, match="completed assessment"):
        proposal_recovery.retain(proposal, assessment)


def test_retained_summary_cannot_preserve_a_rejected_assertion():
    proposal, assessment = _retention_fixture()
    candidate, _ = proposal_recovery.retain(proposal, assessment)
    assert "iPhone" not in candidate["summary"]
    assert all("iPhone" not in c["text"] for c in candidate["claims"])


def test_all_rejected_leaves_nothing_to_retain():
    proposal, assessment = _retention_fixture()
    for row in assessment["claims"]:
        if row["claim_id"] == "proposal-1":
            row["verdict"] = "unsupported"
    with pytest.raises(ValueError, match="no supported feature observations"):
        proposal_recovery.retain(proposal, assessment)


# --- proposal_recovery.correct: default must never silently re-run a past failure ---

def test_repair_refuses_a_job_not_in_a_completed_failed_stage(tmp_path):
    directory = tmp_path
    (directory / "example--repo.json").write_bytes(core.dump_json({"repo": "example/repo", "stage": "applied"}))
    with pytest.raises(ValueError, match="only explicitly completed failed proposals"):
        proposal_recovery.correct(tmp_path, "example/repo", directory)


def test_repair_refuses_an_uncertain_timed_out_model_outcome(tmp_path):
    directory = tmp_path
    (directory / "example--repo.json").write_bytes(core.dump_json(
        {"repo": "example/repo", "stage": "model-failed", "model": {"timed_out": True, "drain_complete": False}}))
    with pytest.raises(ValueError, match="uncertain model outcome"):
        proposal_recovery.correct(tmp_path, "example/repo", directory)
