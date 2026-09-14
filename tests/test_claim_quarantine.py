"""Behavioral tests for --quarantine-invalid-claims (lunaroute.py) and its populate.py passthrough.

Offline: a fake transport returns canned HTTP responses; no network or model call is made.

populate.py imports map_agents.source_review, which this isolated worktree does not carry (it is not
one of this task's owned files). The populate-forwarding tests below therefore importorskip and are
verified for real against an isolated copy of the integrated canonical tree with only lunaroute.py and
populate.py overlaid from this worktree -- see .coordination/claim-quarantine-result.md for that run's
actual output. The lunaroute.py tests run for real in this worktree; they do not need source_review.
"""
from __future__ import annotations

import io
import json

import pytest

from map_agents import lunaroute, wiki
from map_agents.workers import ENVELOPE_SCHEMA

OP = "op_" + "d" * 32
COMMIT = "b" * 40
SNAPSHOT = "c" * 16
SLICE_DOC = "slc_" + "a" * 64
SLICE_CODE = "slc_" + "e" * 64
SLICE_CONTRIB = "slc_" + "f" * 64


def _packet(**overrides) -> dict:
    packet = {
        "schema_version": wiki.PACKET_SCHEMA, "operation_id": OP, "repo": "example/repo",
        "commit": COMMIT, "snapshot_id": SNAPSHOT, "base_digest": "sha256:aaaa",
        "slices": [
            {"slice_id": SLICE_DOC, "source_id": "src1", "heading": "Overview",
             "locator": {"path": "README.md", "line_start": 1, "line_end": 5},
             "text": "This project implements an orchestration loop for worker repositories.", "truncated": False},
            {"slice_id": SLICE_CODE, "source_id": "src2", "heading": "Worker loop",
             "locator": {"path": "app/worker.py", "line_start": 10, "line_end": 40},
             "text": "def run():\n    while True:\n        dispatch_one_job()", "truncated": False},
            {"slice_id": SLICE_CONTRIB, "source_id": "src3", "heading": "Sandbox",
             "locator": {"path": "AGENTS.md", "line_start": 5, "line_end": 6},
             "text": "You operate in a sandbox where network access is disabled for the shell tool.", "truncated": False},
        ],
    }
    packet.update(overrides)
    return packet


def _envelope(packet: dict) -> bytes:
    return json.dumps({
        "schema_version": ENVELOPE_SCHEMA, "task": "dossier-proposal", "packet": packet,
        "coverage": {"notice": "Evidence is a bounded selection of one commit."},
        "output_contract": {"format": "exactly one JSON object on stdout, nothing else",
                            "schema": wiki.PROPOSAL_JSON_SCHEMA, "manual_models": []},
    }).encode("utf-8")


def _chat_response(content: object, usage: dict | None = None) -> bytes:
    body = content if isinstance(content, str) else json.dumps(content)
    return json.dumps({"choices": [{"message": {"content": body}}], "usage": usage or {"prompt_tokens": 10}}).encode()


def _run(monkeypatch, envelope_bytes: bytes, transport=None, argv=None, api_key="test-key"):
    if api_key is not None:
        monkeypatch.setenv("LUNAROUTE_API_KEY", api_key)
    else:
        monkeypatch.delenv("LUNAROUTE_API_KEY", raising=False)
    if transport is not None:
        monkeypatch.setattr(lunaroute, "_transport", transport)
    return lunaroute.main(argv or [], stdin=io.BytesIO(envelope_bytes))


VALID_CLAIM = {"facet": "workflows", "kind": "observation", "basis": "code-inspected",
               "text": "The worker module defines a run function that dispatches jobs in a loop.", "slices": [2]}
BAD_SLICE_CLAIM = {"facet": "workflows", "kind": "observation", "basis": "documented",
                   "text": "This claim cites a slice index outside the evidence shown to the model.", "slices": [99]}


# --------------------------------------------------------------------------- mixed valid/invalid


def test_quarantine_keeps_the_valid_claim_and_drops_the_invalid_one(monkeypatch, capsys):
    packet = _packet()
    reduced = {"summary": "Original model summary mentioning both claims and more context besides.",
               "claims": [VALID_CLAIM, BAD_SLICE_CLAIM]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 0, out.err
    proposal = json.loads(out.out)
    assert len(proposal["claims"]) == 1
    assert proposal["claims"][0]["text"] == VALID_CLAIM["text"]
    assert proposal["claims"][0]["slice_ids"] == [SLICE_CODE]
    wiki.validate_proposal(proposal, packet)  # the retained claim alone still satisfies the real kernel check
    receipt = json.loads(out.err.strip().splitlines()[-1])
    assert receipt["quarantine_invalid_claims"] is True
    prevalidation = receipt["calls"][0]["claim_prevalidation"]
    assert prevalidation["mode"] == "quarantine" and prevalidation["retained"] == 1
    assert prevalidation["rejected"] == [{"index": 1, "facet": "workflows", "reason": prevalidation["rejected"][0]["reason"]}]
    assert "slice index" in prevalidation["rejected"][0]["reason"]
    assert "text" not in prevalidation["rejected"][0]  # never echoes the untrusted claim body


def test_summary_is_rebuilt_from_retained_claims_when_anything_was_dropped(monkeypatch, capsys):
    packet = _packet()
    original_summary = "UNSUPPORTEDPHRASE that only belonged with the claim being dropped."
    reduced = {"summary": original_summary, "claims": [VALID_CLAIM, BAD_SLICE_CLAIM]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 0, out.err
    proposal = json.loads(out.out)
    assert "UNSUPPORTEDPHRASE" not in proposal["summary"]
    assert VALID_CLAIM["text"] in proposal["summary"]
    assert len(proposal["summary"]) <= wiki.BOUNDS["max_summary_chars"]


def test_summary_kept_when_nothing_was_dropped(monkeypatch, capsys):
    packet = _packet()
    reduced = {"summary": "Both claims are supported and nothing needs to be quarantined here.",
               "claims": [VALID_CLAIM]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    proposal = json.loads(out.out)
    assert proposal["summary"] == reduced["summary"]


# --------------------------------------------------------------------------- all-invalid still fails


def test_all_invalid_claims_still_fails_not_an_empty_success(monkeypatch, capsys):
    packet = _packet()
    reduced = {"summary": "Sparse evidence about this repository.", "claims": [BAD_SLICE_CLAIM]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 1 and out.out == ""
    assert "lunaroute adapter" in out.err
    receipt = json.loads(out.err.strip().splitlines()[0])  # the JSON receipt line precedes the human-readable error line
    assert receipt["status"] == "error"
    assert "claims" not in receipt  # the success-only claim count is never stamped on a failed receipt


# --------------------------------------------------------------------------- strict default unchanged


def test_strict_default_still_rejects_the_whole_response(monkeypatch, capsys):
    packet = _packet()
    reduced = {"summary": "Sparse evidence about this repository.", "claims": [VALID_CLAIM, BAD_SLICE_CLAIM]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)))
    out = capsys.readouterr()
    assert code == 1 and out.out == ""
    assert "slice index" in out.err


# --------------------------------------------------------------------------- contributor gate still applies


def test_contributor_only_runtime_claim_cannot_slip_through_quarantine(monkeypatch, capsys):
    packet = _packet()
    bad_contributor_claim = {"facet": "tools-permissions", "kind": "observation", "basis": "documented",
                             "text": "The product disables network access for its shell tool at runtime.", "slices": [3]}
    reduced = {"summary": "One valid and one mislabeled contributor-only claim.",
               "claims": [VALID_CLAIM, bad_contributor_claim]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 0, out.err
    proposal = json.loads(out.out)
    assert len(proposal["claims"]) == 1 and proposal["claims"][0]["facet"] == "workflows"
    assert not any(c["facet"] == "tools-permissions" for c in proposal["claims"])
    receipt = json.loads(out.err.strip().splitlines()[-1])
    rejected = receipt["calls"][0]["claim_prevalidation"]["rejected"]
    assert len(rejected) == 1 and "contributor-instruction" in rejected[0]["reason"]


# --------------------------------------------------------------------------- no guessing, foreign/duplicate slices


def test_foreign_slice_index_is_dropped_never_guessed(monkeypatch, capsys):
    packet = _packet()
    foreign_claim = {"facet": "workflows", "kind": "observation", "basis": "documented",
                     "text": "This claim references a slice index far outside anything shown.", "slices": [4321]}
    reduced = {"summary": "One valid claim and one foreign slice reference.", "claims": [VALID_CLAIM, foreign_claim]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    proposal = json.loads(capsys.readouterr().out)
    assert len(proposal["claims"]) == 1
    assert proposal["claims"][0]["slice_ids"] == [SLICE_CODE]  # never substituted with a guessed slice


def test_duplicate_claim_is_quarantined_not_silently_merged(monkeypatch, capsys):
    packet = _packet()
    reduced = {"summary": "A duplicate of the same claim appears twice.", "claims": [VALID_CLAIM, dict(VALID_CLAIM)]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    proposal = json.loads(out.out)
    assert len(proposal["claims"]) == 1
    receipt = json.loads(out.err.strip().splitlines()[-1])
    rejected = receipt["calls"][0]["claim_prevalidation"]["rejected"]
    assert len(rejected) == 1 and "duplicates an earlier retained claim" in rejected[0]["reason"]


def test_malformed_claim_shape_is_dropped_by_index(monkeypatch, capsys):
    packet = _packet()
    malformed = {"facet": "workflows", "kind": "observation", "basis": "documented", "text": "Missing the slices key entirely."}
    reduced = {"summary": "One valid claim and one malformed claim missing a required key.",
               "claims": [VALID_CLAIM, malformed]}
    code = _run(monkeypatch, _envelope(packet), transport=lambda req, timeout: (200, _chat_response(reduced)),
               argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    proposal = json.loads(out.out)
    assert len(proposal["claims"]) == 1
    receipt = json.loads(out.err.strip().splitlines()[-1])
    rejected = receipt["calls"][0]["claim_prevalidation"]["rejected"]
    assert rejected[0]["index"] == 1 and "keys must be exactly" in rejected[0]["reason"]


# --------------------------------------------------------------------------- interrupted calls never retry


def test_provider_timeout_never_retries_even_with_quarantine_enabled(monkeypatch, capsys):
    calls = []

    def fake_transport(req, timeout):
        calls.append(1)
        raise lunaroute.AdapterError("lunaroute request failed (TimeoutError)")

    code = _run(monkeypatch, _envelope(_packet()), transport=fake_transport, argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 1 and out.out == "" and len(calls) == 1


def test_truncated_response_never_retries_even_with_quarantine_enabled(monkeypatch, capsys):
    calls = []

    def fake_transport(req, timeout):
        calls.append(1)
        return 200, json.dumps({"choices": [{"message": {"content": "{}"}, "finish_reason": "length"}]}).encode()

    code = _run(monkeypatch, _envelope(_packet()), transport=fake_transport, argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 1 and out.out == "" and len(calls) == 1


def test_non_200_never_retries_even_with_quarantine_enabled(monkeypatch, capsys):
    calls = []

    def fake_transport(req, timeout):
        calls.append(1)
        return 500, b'{"error":"boom"}'

    code = _run(monkeypatch, _envelope(_packet()), transport=fake_transport, argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 1 and out.out == "" and len(calls) == 1


def test_malformed_top_level_shape_gets_the_existing_bounded_correction_not_a_new_retry(monkeypatch, capsys):
    """A whole-response parse/shape failure is not a per-claim issue: _quarantine_claims is never
    reached, and _parse_reduced's own gate is unchanged. It is still eligible for the pre-existing,
    already-bounded one-time completed-response correction (primary + one correction = 2 calls, not
    more) -- quarantine mode adds no additional retry on top of that existing allowance."""
    calls = []

    def fake_transport(req, timeout):
        calls.append(1)
        bad = {"summary": "ok", "claims": [], "unexpected_extra_key": True}
        return 200, _chat_response(bad)

    code = _run(monkeypatch, _envelope(_packet()), transport=fake_transport, argv=["--quarantine-invalid-claims"])
    out = capsys.readouterr()
    assert code == 1 and out.out == "" and len(calls) == 2
    assert "keys must be exactly" in out.err


# --------------------------------------------------------------------------- populate.py passthrough


def test_populate_cli_defaults_the_flag_off():
    populate = pytest.importorskip("map_agents.populate", reason="source_review.py not present in this isolated worktree")
    args = populate.build_parser().parse_args(["--root", "corpus", "--group", "g.json", "--receipts", "r"])
    assert args.quarantine_invalid_claims is False


def test_populate_forwards_only_the_trusted_flag_when_enabled(monkeypatch, tmp_path):
    """batch() really constructs the lunaroute subprocess argv, and --quarantine-invalid-claims
    appears in it iff the caller asked for it -- nothing else about the fixed argv changes."""
    populate = pytest.importorskip("map_agents.populate", reason="source_review.py not present in this isolated worktree")
    import sys as sys_mod
    from map_agents import core, wiki as wiki_mod, workers as workers_mod

    root = tmp_path / "corpus"
    core.init(root)
    if hasattr(wiki_mod, "enable_partitioned"):
        wiki_mod.enable_partitioned(root)
    repos = {"example/repo": {"status": "snapshotted", "latest_snapshot": {"snapshot_id": "x"},
                              "latest_snapshot_id": "x", "indexed_snapshot_id": None}}
    core.save_repos(root, repos)
    op = "op_" + "a" * 32
    fake_packet = {"operation_id": op, "repo": "example/repo", "schema_version": wiki_mod.PACKET_SCHEMA,
                   "commit": "b" * 40, "snapshot_id": "x", "base_digest": "sha256:aaa", "slices": []}
    monkeypatch.setattr(wiki_mod, "prepare", lambda root_, key: {"packet": f"packets/{op}.json"})
    monkeypatch.setattr(wiki_mod, "load_packet", lambda root_, path: fake_packet)
    monkeypatch.setattr(workers_mod, "envelope", lambda root_, packet: {"schema_version": workers_mod.ENVELOPE_SCHEMA, "task": "dossier-proposal"})
    seen: dict = {}

    def fake_launch(deadline, argv, payload, timeout, max_stdout, max_stderr):
        seen["argv"] = argv
        raise workers_mod.WorkerFailed("stop here deliberately; only the constructed argv matters to this test")

    monkeypatch.setattr(populate, "launch_before", fake_launch)

    populate.batch(root, ["example/repo"], tmp_path / "receipts-on", quarantine_invalid_claims=True)
    argv_on = seen["argv"]
    assert argv_on.count("--quarantine-invalid-claims") == 1
    assert argv_on[:3] == [sys_mod.executable, "-m", "map_agents.lunaroute"]

    seen.clear()
    populate.batch(root, ["example/repo"], tmp_path / "receipts-off", quarantine_invalid_claims=False)
    argv_off = seen["argv"]
    assert "--quarantine-invalid-claims" not in argv_off
    normalize = lambda argv: [a.replace("receipts-on", "R").replace("receipts-off", "R") for a in argv if a != "--quarantine-invalid-claims"]
    assert normalize(argv_off) == normalize(argv_on)
