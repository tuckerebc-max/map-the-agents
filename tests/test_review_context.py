"""Heading-context regression tests for source_review: the author saw each slice's heading;
the review packet must keep it. Offline, model-free (the provider boundary is monkeypatched).

Run against the actual current canonical map_agents/vendor/tests (see
.coordination/review-heading-context-final.md for the isolated validation setup and paths).
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from map_agents import collect, core, source_review, wiki
from test_collect import SHA1, FakeTransport, repo_routes

# The claim's subject ("SDKMAN or WinGet") lives ONLY in the heading; the body text alone never
# names either tool, so a reviewer who never sees the heading cannot support this claim's subject.
README = (
    b"Intro sentence sitting before any heading at all.\n\n"
    b"## Do I need SDKMAN or WinGet?\n\nOnly for automatic JDK installation and switching.\n\n"
    b"## Install\n\npip install demo-agent\n"
)
FILES = {"README.md": README}
FAQ_HEADING = "Do I need SDKMAN or WinGet?"
FAQ_BODY = "Only for automatic JDK installation and switching."
FAQ_CLAIM_TEXT = "SDKMAN or WinGet are needed only for automatic JDK installation and switching."


def _claim(facet: str, text: str, ids: list[str]) -> dict:
    return {"facet": facet, "text": text, "slice_ids": ids, "kind": "observation", "basis": "documented"}


def slice_by_heading(packet: dict, heading: str) -> dict:
    return next(s for s in packet["slices"] if s["heading"] == heading)


def _write(path: Path, obj: dict) -> Path:
    path.write_bytes(core.dump_json(obj))
    return path


def _apply_faq_dossier(root: Path) -> dict:
    """Real wiki.prepare -> wiki.apply, citing the FAQ-heading slice, exactly as authoring would."""
    collect.snapshot(root, "Org-A/Demo", 20, 50_000, transport=FakeTransport(repo_routes("org-a/demo", SHA1, FILES)))
    prepared = wiki.prepare(root, "org-a/demo")
    packet = json.loads((root / prepared["packet"]).read_bytes())
    faq = slice_by_heading(packet, FAQ_HEADING)
    intro = slice_by_heading(packet, "")
    proposal = {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": "Demo agent FAQ scopes SDKMAN/WinGet to JDK installation; intro precedes any heading.",
        "claims": [
            _claim("dependencies", FAQ_CLAIM_TEXT, [faq["slice_id"]]),
            _claim("specifications", "An introductory sentence precedes the first document heading.", [intro["slice_id"]]),
        ],
    }
    proposal_path = _write(root / "proposals" / "demo.json", proposal)
    wiki.apply(root, root / prepared["packet"], proposal_path)
    return packet


def _fake_critic_needs_subject_in_evidence(model, messages, timeout, max_tokens):
    """A real (if trivial) critic: it can only find the SDKMAN/WinGet subject if the evidence it
    was actually given -- heading included -- names it. Proves a genuine behavioral effect, not a
    dict-equality check on what source_review happens to send.
    """
    body = json.loads(messages[-1]["content"])
    rows = []
    for claim in body["claims"]:
        if claim.get("facet") != "dependencies":  # only the SDKMAN/WinGet claim is under test here
            rows.append({"claim_id": claim["claim_id"], "verdict": "supported", "reason": "Not the claim under test."})
            continue
        haystack = " ".join(e.get("heading", "") + " " + e.get("text", "") for e in claim["evidence"])
        if "SDKMAN" in haystack or "WinGet" in haystack:
            rows.append({"claim_id": claim["claim_id"], "verdict": "supported",
                        "reason": "Evidence names SDKMAN/WinGet and scopes it to JDK installation."})
        else:
            rows.append({"claim_id": claim["claim_id"], "verdict": "revise",
                        "reason": "Evidence text never names SDKMAN or WinGet; claim subject is unsupported."})
    return {"finish_reason": "stop", "usage": {}, "content": json.dumps({"claims": rows})}


# --------------------------------------------------------------- dossier review (pinned-kernel path)

@pytest.mark.parametrize("layout", ["shared", "partitioned"])
def test_dossier_review_recovers_persisted_heading_without_ephemeral_packets(layout, tmp_path):
    root = tmp_path / "corpus"
    root.mkdir()
    if layout == "partitioned":
        core.init(root)
        wiki.enable_partitioned(root)
    _apply_faq_dossier(root)
    # A ZIP release omits the ignored, ephemeral authoring artifacts entirely.
    shutil.rmtree(root / "packets")
    assert not (root / "packets").exists()
    assert wiki.load_layout(root)["layout"] == layout

    body, raw = source_review.packet_for(root, "org-a/demo")

    faq_claim = next(c for c in body["claims"] if c["facet"] == "dependencies")
    assert faq_claim["evidence"][0]["heading"] == FAQ_HEADING
    assert faq_claim["evidence"][0]["text"] == FAQ_BODY
    intro_claim = next(c for c in body["claims"] if c["facet"] == "specifications")
    assert intro_claim["evidence"][0]["heading"] == ""  # no heading preceded this slice; never invented
    assert json.loads(raw) == body


def test_packet_for_evidence_scope_is_cited_slices_not_packet_total(tmp_path):
    root = tmp_path / "corpus"
    root.mkdir()
    _apply_faq_dossier(root)
    body, _ = source_review.packet_for(root, "org-a/demo")
    assert "evidence_scope" in body
    assert "2 distinct source slice" in body["evidence_scope"]
    assert "authoring packet" in body["evidence_scope"] and "adapter" in body["evidence_scope"]
    assert "packet slice count" not in body["evidence_scope"].lower()


def test_recovered_heading_makes_the_critic_support_the_faq_claim(tmp_path, monkeypatch):
    """The behavioral proof: with the heading actually preserved, a critic that requires the
    claim's subject to appear somewhere in its evidence finds it (in the heading) and passes.
    """
    root = tmp_path / "corpus"
    root.mkdir()
    _apply_faq_dossier(root)
    shutil.rmtree(root / "packets")
    monkeypatch.setattr(source_review.lunaroute, "_call_model", _fake_critic_needs_subject_in_evidence)
    result = source_review.review_one(root, "org-a/demo", tmp_path)
    faq_row = next(r for r in result["claims"] if r["reason"].startswith("Evidence names"))
    assert result["status"] == "reviewed"
    assert faq_row["verdict"] == "supported"
    assert result["verdict"] == "pass"


def test_a_heading_stripped_review_packet_makes_the_same_critic_revise_the_same_claim(tmp_path, monkeypatch):
    """The 'before' side of the same behavioral proof: strip only the heading field (simulating the
    pre-fix evidence shape) and show the identical critic now rejects the identical claim, because
    its subject truly lived only in the dropped heading, not the body text.
    """
    root = tmp_path / "corpus"
    root.mkdir()
    _apply_faq_dossier(root)
    body, _ = source_review.packet_for(root, "org-a/demo")
    for claim in body["claims"]:
        for item in claim["evidence"]:
            item["heading"] = ""  # simulate the pre-fix code path, which never populated this field
    stripped_raw = json.dumps(body, ensure_ascii=False)
    monkeypatch.setattr(source_review.lunaroute, "_call_model", _fake_critic_needs_subject_in_evidence)
    result = source_review.review_body(body, stripped_raw, tmp_path / "stripped-review.json")
    faq_row = next(r for r in result["claims"] if r["claim_id"] == next(
        c["claim_id"] for c in body["claims"] if c["facet"] == "dependencies"))
    assert faq_row["verdict"] == "revise"
    assert result["verdict"] == "fail"


# --------------------------------------------------------------- proposal review (sealed packet path)

def test_review_proposal_forwards_the_exact_packet_heading_to_the_reviewer(tmp_path, monkeypatch):
    packet = {
        "operation_id": "op_" + "a" * 32, "repo": "org/demo", "commit": "c" * 40, "snapshot_id": "s" * 16,
        "base_digest": "sha256:deadbeef", "omitted_slices": 0,
        "slices": [{"slice_id": "slc_" + "f" * 64, "heading": FAQ_HEADING, "text": FAQ_BODY,
                    "locator": {"path": "README.md", "line_start": 10, "line_end": 10}, "truncated": False}],
    }
    proposal = {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": "Demo summary about install-manager scope.",
        "claims": [_claim("dependencies", FAQ_CLAIM_TEXT, ["slc_" + "f" * 64])],
    }
    seen = {}

    def capture_then_critic(model, messages, timeout, max_tokens):
        seen["body"] = json.loads(messages[-1]["content"])
        return _fake_critic_needs_subject_in_evidence(model, messages, timeout, max_tokens)

    monkeypatch.setattr(source_review.lunaroute, "_call_model", capture_then_critic)
    result = source_review.review_proposal(packet, proposal, tmp_path / "review.json")
    assert result["status"] == "reviewed" and result["verdict"] == "pass"
    sent_evidence = seen["body"]["claims"][0]["evidence"]
    assert sent_evidence == [{
        "slice_id": "slc_" + "f" * 64, "path": "README.md", "start": 10, "end": 10, "heading": FAQ_HEADING,
        "text": FAQ_BODY, "truncated": False}]


# --------------------------------------------------------------- source-file coverage denominators

def _coverage_packet() -> dict:
    return {
        "operation_id": "op_" + "b" * 32, "repo": "org/covered", "commit": "d" * 40, "snapshot_id": "t" * 16,
        "base_digest": "sha256:c0ffee", "omitted_slices": 0,
        "coverage": {
            "files": [{"path": "README.md", "lines": 50, "size": 2000}], "explicit_paths": [],
            "selection": {"candidates": 154, "complete": False, "omitted": 151, "stored": 3},
            "repository": {"complete": True, "tree_blobs": 900, "tree_truncated": False},
            "omitted_count": 151, "omitted_slices": 0,
            # A real, complete detailed list (real packets can hold hundreds of rows): two named,
            # reasoned omissions an approved summary might cite by name, plus filler rows, to prove
            # the full list -- not a truncated or synthesized one -- reaches the critic.
            "omitted": [{"path": "README_en.md", "reason": "omitted by file budget"},
                       {"path": "requirements.txt", "reason": "omitted by file budget"}]
                      + [{"path": f"candidate-{i}.md", "reason": "not selected"} for i in range(198)],
        },
        "slices": [{"slice_id": "slc_" + "e" * 64, "heading": "Files", "text": "This snapshot includes README.md only.",
                    "locator": {"path": "README.md", "line_start": 1, "line_end": 1}, "truncated": False}],
    }


def _coverage_proposal(packet: dict, summary: str) -> dict:
    return {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": summary,
        "claims": [_claim("specifications", "The snapshot documents README.md as the covered source file.",
                          [packet["slices"][0]["slice_id"]])],
    }


def _fake_critic_checks_named_omission(model, messages, timeout, max_tokens):
    """Only supports a summary naming a specific omitted file and its actual reason if that exact
    fact is verifiable in the supplied source coverage -- proving a genuine behavioral dependency
    on the full omitted list, not a dict-equality check.
    """
    body = json.loads(messages[-1]["content"])
    rows = []
    for claim in body["claims"]:
        if claim["claim_id"] != "summary":
            rows.append({"claim_id": claim["claim_id"], "verdict": "supported", "reason": "Not the claim under test."})
            continue
        omitted = claim.get("coverage_metadata", {}).get("source_coverage", {}).get("omitted", [])
        named = {(o.get("path"), o.get("reason")) for o in omitted if isinstance(o, dict)}
        required = {("README_en.md", "omitted by file budget"), ("requirements.txt", "omitted by file budget")}
        if required <= named:
            rows.append({"claim_id": "summary", "verdict": "supported",
                        "reason": "Coverage's omitted list confirms README_en.md and requirements.txt were omitted by file budget."})
        else:
            rows.append({"claim_id": "summary", "verdict": "revise",
                        "reason": "No verifiable omitted-file record supports naming README_en.md/requirements.txt or their reason."})
    return {"finish_reason": "stop", "usage": {}, "content": json.dumps({"claims": rows})}


COVERAGE_SUMMARY = "Evidence covers README.md only; README_en.md and requirements.txt were omitted by file budget."


def test_full_source_coverage_lets_the_critic_verify_a_named_omitted_file_and_reason(tmp_path, monkeypatch):
    packet = _coverage_packet()
    proposal = _coverage_proposal(packet, COVERAGE_SUMMARY)
    seen = {}

    def capture_then_critic(model, messages, timeout, max_tokens):
        seen["body"] = json.loads(messages[-1]["content"])
        return _fake_critic_checks_named_omission(model, messages, timeout, max_tokens)

    monkeypatch.setattr(source_review.lunaroute, "_call_model", capture_then_critic)
    result = source_review.review_proposal(packet, proposal, tmp_path / "review.json")

    summary_sent = next(c for c in seen["body"]["claims"] if c["claim_id"] == "summary")
    source_cov = summary_sent["coverage_metadata"]["source_coverage"]
    assert source_cov == packet["coverage"]  # the complete, genuine map -- not synthesized, not truncated
    assert len(source_cov["omitted"]) == 200
    assert {"path": "README_en.md", "reason": "omitted by file budget"} in source_cov["omitted"]
    assert {"path": "requirements.txt", "reason": "omitted by file budget"} in source_cov["omitted"]
    assert result["status"] == "reviewed" and result["verdict"] == "pass"


def test_removing_the_omitted_list_makes_the_same_critic_revise_the_same_summary(tmp_path, monkeypatch):
    """The 'before' side: strip only the detailed omitted list (simulating the earlier, too-narrow
    whitelist) and show the identical critic can no longer verify the identical named-omission claim.
    """
    packet = _coverage_packet()
    proposal = _coverage_proposal(packet, COVERAGE_SUMMARY)
    captured = {}

    def capture_then_critic(model, messages, timeout, max_tokens):
        captured["body"] = json.loads(messages[-1]["content"])
        return _fake_critic_checks_named_omission(model, messages, timeout, max_tokens)

    monkeypatch.setattr(source_review.lunaroute, "_call_model", capture_then_critic)
    source_review.review_proposal(packet, proposal, tmp_path / "first-review.json")
    body = captured["body"]
    for claim in body["claims"]:
        if claim["claim_id"] == "summary":
            del claim["coverage_metadata"]["source_coverage"]["omitted"]  # simulate the too-narrow whitelist
    stripped_raw = json.dumps(body, ensure_ascii=False)
    result = source_review.review_body(body, stripped_raw, tmp_path / "stripped-review.json")
    summary_row = next(r for r in result["claims"] if r["claim_id"] == "summary")
    assert summary_row["verdict"] == "revise"
    assert result["verdict"] == "fail"


def test_packet_without_coverage_field_yields_an_empty_source_coverage_map(tmp_path, monkeypatch):
    packet = _coverage_packet()
    del packet["coverage"]
    proposal = _coverage_proposal(packet, "Evidence covers README.md only; no source-file coverage metadata is available.")
    captured = {}

    def capture_then_pass(model, messages, timeout, max_tokens):
        captured["body"] = json.loads(messages[-1]["content"])
        rows = [{"claim_id": c["claim_id"], "verdict": "supported", "reason": "ok"} for c in captured["body"]["claims"]]
        return {"finish_reason": "stop", "usage": {}, "content": json.dumps({"claims": rows})}

    monkeypatch.setattr(source_review.lunaroute, "_call_model", capture_then_pass)
    result = source_review.review_proposal(packet, proposal, tmp_path / "review.json")
    summary_sent = next(c for c in captured["body"]["claims"] if c["claim_id"] == "summary")
    assert summary_sent["coverage_metadata"]["source_coverage"] == {}
    assert result["status"] == "reviewed" and result["verdict"] == "pass"


# ------------------------------------------------------ _slice_headings unit behavior

def test_slice_headings_never_invents_a_heading_for_a_row_that_has_none(tmp_path, monkeypatch):
    monkeypatch.setattr(source_review.wiki, "_kernel_root", lambda root, key: root / "wiki")
    monkeypatch.setattr(source_review.wiki, "_rows", lambda kernel, table: [
        {"id": "slc_present", "locator": {"heading": "Install"}},
        {"id": "slc_blank", "locator": {"heading": ""}},
        {"id": "slc_missing_key", "locator": {}},
    ])
    result = source_review._slice_headings(tmp_path, "org/any", {"slc_present", "slc_blank", "slc_missing_key"})
    assert result == {"slc_present": "Install", "slc_blank": "", "slc_missing_key": ""}


def test_slice_headings_refuses_a_cited_id_absent_from_the_kernel(tmp_path, monkeypatch):
    monkeypatch.setattr(source_review.wiki, "_kernel_root", lambda root, key: root / "wiki")
    monkeypatch.setattr(source_review.wiki, "_rows", lambda kernel, table: [])
    with pytest.raises(ValueError, match="not found in the pinned kernel"):
        source_review._slice_headings(tmp_path, "org/any", {"slc_ghost"})


# --------------------------------------------------------------- existing strict gates still apply

def test_saved_review_sha_binding_still_rejects_a_changed_input(tmp_path):
    body = {"repo": "test/agent", "dossier_seal": "a" * 64, "evidence_scope": "x", "claims": [{"claim_id": "summary", "evidence": []}]}
    raw = json.dumps(body)
    path = tmp_path / "review.json"
    path.write_bytes(core.dump_json({"input_sha256": "0" * 64, "status": "reviewed", "verdict": "pass"}))
    with pytest.raises(ValueError, match="different dossier/evidence input"):
        source_review.review_body(body, raw, path)


def test_interrupted_review_still_holds_without_reissuing_the_call(tmp_path, monkeypatch):
    import hashlib
    body = {"repo": "test/agent", "dossier_seal": "c" * 64, "evidence_scope": "x", "claims": [{"claim_id": "summary"}]}
    raw = json.dumps(body)
    path = tmp_path / "review.json"
    path.write_bytes(core.dump_json({"input_sha256": hashlib.sha256(raw.encode()).hexdigest(), "status": "running"}))
    before = path.read_bytes()

    def forbidden(*args, **kwargs):
        raise AssertionError("provider must not be called for a held, unfinished review")

    monkeypatch.setattr(source_review.lunaroute, "_call_model", forbidden)
    with pytest.raises(core.WorkbenchError, match="reconcile the provider call"):
        source_review.review_body(body, raw, path)
    assert path.read_bytes() == before
