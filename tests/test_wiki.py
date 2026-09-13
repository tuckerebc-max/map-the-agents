"""Real-kernel tests for wiki prepare/apply/audit on a synthetic public snapshot. Offline, model-free."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from map_agents import __main__ as cli
from map_agents import collect, core, wiki
from test_collect import SHA1, FakeTransport, repo_routes, repos_bytes

README = (
    b"# Alpha\n\nAlpha is a coding agent that plans a task, runs shell tools inside a sandbox, and reports a\n"
    b"summary back to the operator once every tool call has finished and the final answer is ready.\n\n"
    b"## Install\n\npip install alpha-agent\n\n## Memory\n\nSession state is kept in a local SQLite file.\n"
)
FILES = {
    "README.md": README,
    "docs/design.md": b"# Design\n\nThe planner delegates to a worker loop with a bounded retry budget.\n",
    "src/agent.py": b"class Agent:\n    def run(self, task):\n        return self.loop(task, max_steps=8)\n",
    "empty.md": b"",
}


def _claim(facet: str, text: str, ids: list[str], kind: str = "observation", basis: str = "documented") -> dict:
    return {"facet": facet, "text": text, "slice_ids": ids, "kind": kind, "basis": basis}


def slice_by_path(packet: dict, path: str, heading: str | None = None) -> dict:
    return next(s for s in packet["slices"] if s["locator"]["path"] == path and (heading is None or s["heading"] == heading))


def good_proposal(packet: dict) -> dict:
    readme = slice_by_path(packet, "README.md", "Alpha")
    memory = slice_by_path(packet, "README.md", "Memory")
    code = slice_by_path(packet, "src/agent.py")
    design = slice_by_path(packet, "docs/design.md")
    return {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": "Synthetic coding agent: planner plus sandboxed tool loop; local SQLite session state.",
        "claims": [
            _claim("components", "A planner and a sandboxed tool runner are the documented components.", [readme["slice_id"]]),
            _claim("memory-state", "Session state persists in a local SQLite file per the README.", [memory["slice_id"]]),
            _claim("interfaces", "The Agent class exposes run(task) with an eight-step loop bound.", [code["slice_id"]],
                   basis="code-inspected"),
            _claim("relevance", "Bounded retry plus delegation resembles Navy Yard bosun supervision.",
                   [design["slice_id"], readme["slice_id"]], kind="inference"),
        ],
    }


def write(path: Path, obj: dict) -> Path:
    path.write_bytes(core.dump_json(obj))
    return path


def claims_table(root: Path) -> list[dict]:
    return wiki._rows(root / wiki.WIKI_DIR, "claims")


@pytest.fixture(scope="module")
def corpus(tmp_path_factory: pytest.TempPathFactory) -> Path:
    root = tmp_path_factory.mktemp("corpus")
    res = collect.snapshot(root, "Org-A/Alpha", 20, 50_000, paths=["src/agent.py"], transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    assert res["files_stored"] == 4
    return root


def clone(corpus: Path, tmp_path: Path) -> Path:
    target = tmp_path / "corpus"
    shutil.copytree(corpus, target)
    return target


# ---------------------------------------------------------------- prepare

def test_prepare_emits_bounded_packet_bound_to_real_kernel_ids(corpus: Path) -> None:
    res = wiki.prepare(corpus, "org-a/alpha")
    assert res["wiki_initialized"] is True and res["already_indexed"] is False and res["package_status"] == "new"
    cfg = (corpus / "wiki/wiki.yaml").read_text(encoding="utf-8")
    assert "../sources" in cfg, "source and wiki roots are disjoint siblings"
    packet = json.loads((corpus / res["packet"]).read_bytes())
    kernel = json.loads((corpus / packet["rcw_packet"]).read_bytes())
    assert packet["operation_id"] == kernel["operation_id"] == res["operation_id"] and res["operation_id"].startswith("op_")
    assert packet["base_digest"] == kernel["base_digest"] and packet["source_tree_digest"] == kernel["source_tree_digest"]
    assert {s["slice_id"] for s in packet["slices"]} == {s["id"] for s in kernel["slices"]}
    assert {s["source_id"] for s in packet["sources"]} == {s["id"] for s in kernel["sources"]}
    assert res["sources"] == 4 and res["slices"] == len(kernel["slices"]) >= 5 and res["omitted_slices"] == 0
    snap = json.loads((corpus / core.load_repos(corpus)["org-a/alpha"]["latest_snapshot"]["snapshot"]).read_bytes())
    by_path = {f["path"]: f for f in snap["files"]}
    memory = slice_by_path(packet, "README.md", "Memory")
    assert memory["locator"] == {"repository": "org-a/alpha", "commit": SHA1, "path": "README.md", "git_sha": by_path["README.md"]["git_sha"],
                                 "line_start": 12, "line_end": 12, "url": f"{by_path['README.md']['url']}#L12-L12"}
    assert memory["text"] == "Session state is kept in a local SQLite file." and memory["truncated"] is False
    assert slice_by_path(packet, "src/agent.py")["locator"]["path"] == "src/agent.py", "original path, not the stored .txt name"
    assert packet["facets"] == list(wiki.FACETS) and packet["proposal_contract"]["schema_version"] == wiki.DOSSIER_SCHEMA
    assert packet["snapshot_id"] == snap["snapshot_id"] and packet["commit"] == SHA1
    assert (corpus / wiki.SEAL_DIR / f"{res['operation_id']}.json").exists()
    assert not (corpus / "wiki/data/claims.jsonl").read_bytes(), "prepare writes no canonical claims"


def test_prepare_requires_a_snapshot(tmp_path: Path) -> None:
    core.init(tmp_path)
    with pytest.raises(wiki.WikiError, match="no snapshot"):
        wiki.prepare(tmp_path, "org-a/alpha")
    assert not (tmp_path / "wiki/wiki.yaml").exists()


# ---------------------------------------------------------------- apply / audit / replay

def test_apply_distills_then_replay_reconciles_and_old_packet_is_stale(corpus: Path) -> None:
    first = wiki.prepare(corpus, "org-a/alpha")
    second = wiki.prepare(corpus, "org-a/alpha")  # same base; becomes stale once `first` applies
    packet = json.loads((corpus / first["packet"]).read_bytes())
    proposal = write(corpus / "proposals" / "alpha.json", good_proposal(packet))
    res = wiki.apply(corpus, corpus / first["packet"], proposal)
    assert res["changed"] is True and res["claims"] == 4 and res["status"] == "distilled" and res["freshness"] == "current"
    table = {c["id"]: c for c in claims_table(corpus)}
    assert set(res["claim_ids"]) <= set(table) and len(table) == 4
    inferred = table[res["claim_ids"][3]]
    assert inferred["evidence_type"] == "organizational_statement" and inferred["extraction_confidence"] == 0.5
    assert inferred["scope"]["qualifiers"] == "kind=inference; facet=relevance" and len(inferred["slice_ids"]) == 2
    assert table[res["claim_ids"][2]]["evidence_type"] == "contextual_fact"
    assert res["entity_id"] and any(e["external_ids"] == {"github": "org-a/alpha"} for e in wiki._rows(corpus / "wiki", "entities"))
    ops = wiki._rows(corpus / "wiki", "operations")
    assert [o["id"] for o in ops] == [first["operation_id"]] and ops[0]["state"] == "applied"
    dossier = json.loads((corpus / res["dossier"]).read_bytes())
    assert res["dossier"] == f"wiki/dossiers/org-a/alpha/{SHA1}/{packet['snapshot_id']}.json"
    assert [c["claim_id"] for c in dossier["claims"]] == res["claim_ids"] and dossier["applied_operation_id"] == first["operation_id"]
    assert dossier["claims"][1]["locators"][0]["url"].endswith("/blob/" + SHA1 + "/README.md#L12-L12")
    assert dossier["claims"][2]["basis"] == "code-inspected" and dossier["claims"][2]["locators"][0]["path"] == "src/agent.py"
    assert {g["facet"] for g in dossier["gaps"]} == set(wiki.FACETS) - {"components", "memory-state", "interfaces", "relevance"}
    assert all(g["status"] == "unknown" for g in dossier["gaps"]) and dossier["facets"]["components"] == 1
    rec = core.load_repos(corpus)["org-a/alpha"]
    assert rec["indexed_snapshot_id"] == packet["snapshot_id"] and rec["indexed_commit"] == SHA1 and rec["claims"] == 4
    report = wiki.audit(corpus)
    assert report["ok"] is True and report["rcw"]["ok"] is True and report["repos"]["org-a/alpha"]["problems"] == []
    assert report["repos"]["org-a/alpha"]["claims"] == 4 and report["freshness"] == {"current": 1}
    # The sibling packet prepared before the apply is now stale: the kernel's base digest moved.
    stale_packet = json.loads((corpus / second["packet"]).read_bytes())
    stale_proposal = write(corpus / "proposals" / "stale.json", {**good_proposal(stale_packet)})
    with pytest.raises(wiki.StalePacket, match="RCW_BASE_DIVERGED"):
        wiki.apply(corpus, corpus / second["packet"], stale_proposal)
    assert len(claims_table(corpus)) == 4
    # Replay: fresh packet, same dossier content -> no canonical change, same claim IDs, identical dossier bytes.
    frozen = {"claims": (corpus / "wiki/data/claims.jsonl").read_bytes(), "dossier": (corpus / res["dossier"]).read_bytes(),
              "repos": repos_bytes(corpus)}
    third = wiki.prepare(corpus, "org-a/alpha")
    assert third["already_indexed"] is True and third["package_status"] == "unchanged"
    replay = good_proposal(json.loads((corpus / third["packet"]).read_bytes()))
    again = wiki.apply(corpus, corpus / third["packet"], write(corpus / "proposals" / "replay.json", replay))
    assert again["changed"] is False and again["claim_ids"] == res["claim_ids"] and again["dossier_changed"] is False
    assert again["record_changed"] is False and again["operation_id"] == third["operation_id"]
    assert (corpus / "wiki/data/claims.jsonl").read_bytes() == frozen["claims"]
    assert (corpus / res["dossier"]).read_bytes() == frozen["dossier"] and repos_bytes(corpus) == frozen["repos"]
    assert [o["id"] for o in wiki._rows(corpus / "wiki", "operations")] == [first["operation_id"]], "no duplicate canonical evidence"


REJECTIONS = [
    ("foreign-slice", lambda p: p["claims"][0].__setitem__("slice_ids", ["slc_" + "0" * 64]), "outside this packet"),
    ("bad-facet", lambda p: p["claims"][0].__setitem__("facet", "architecture"), "unsupported facet"),
    ("bad-kind", lambda p: p["claims"][0].__setitem__("kind", "guess"), "unsupported kind"),
    ("bad-basis", lambda p: p["claims"][0].__setitem__("basis", "catalog-blurb"), "unsupported kind"),
    ("extra-key", lambda p: p["claims"][0].__setitem__("confidence", 1), "keys must be exactly"),
    ("short-text", lambda p: p["claims"][0].__setitem__("text", "tiny"), "text must be"),
    ("long-text", lambda p: p["claims"][0].__setitem__("text", "x" * 401), "text must be"),
    ("no-slices", lambda p: p["claims"][0].__setitem__("slice_ids", []), "distinct slice_ids"),
    ("too-many-claims", lambda p: p.__setitem__("claims", [dict(p["claims"][0], text=f"claim number {i} about the same slice") for i in range(41)]), "at most 40"),
    ("changed-commit", lambda p: p.__setitem__("commit", "b" * 40), "commit does not match"),
    ("changed-base", lambda p: p.__setitem__("base_digest", "sha256:" + "0" * 64), "base_digest does not match"),
    ("changed-snapshot", lambda p: p.__setitem__("snapshot_id", "0" * 16), "snapshot_id does not match"),
    ("foreign-operation", lambda p: p.__setitem__("operation_id", "op_" + "f" * 32), "operation_id does not match"),
    ("bad-schema", lambda p: p.__setitem__("schema_version", "map-agents.dossier/2"), "unsupported schema_version"),
    ("long-summary", lambda p: p.__setitem__("summary", "s" * 801), "summary must be"),
    ("unknown-top-key", lambda p: p.__setitem__("gaps", []), "keys must be exactly"),
    ("docs-labelled-code", lambda p: p["claims"][0].__setitem__("basis", "code-inspected"), "cites no code/config slice"),
    ("object-slice-id", lambda p: p["claims"][0].__setitem__("slice_ids", [{"id": p["claims"][0]["slice_ids"][0]}]), "distinct slice_ids"),
]


@pytest.fixture(scope="module")
def rejection_packet(corpus: Path) -> dict:
    """One real packet shared by the pre-kernel rejection cases; none of them may touch the corpus."""
    return wiki.prepare(corpus, "org-a/alpha")


@pytest.mark.parametrize("name,mutate,match", REJECTIONS, ids=[r[0] for r in REJECTIONS])
def test_apply_rejects_unsupported_proposals_before_the_kernel(corpus: Path, tmp_path: Path, rejection_packet: dict, name: str, mutate, match: str) -> None:
    prepared = rejection_packet
    proposal = good_proposal(json.loads((corpus / prepared["packet"]).read_bytes()))
    mutate(proposal)
    before = {"claims": (corpus / "wiki/data/claims.jsonl").read_bytes(), "repos": repos_bytes(corpus)}
    with pytest.raises(wiki.ProposalRejected, match=match):
        wiki.apply(corpus, corpus / prepared["packet"], write(tmp_path / "bad.json", proposal))
    assert (corpus / "wiki/data/claims.jsonl").read_bytes() == before["claims"] and repos_bytes(corpus) == before["repos"]
    assert not (corpus / "proposals" / f"{prepared['operation_id']}.rcw.json").exists(), "nothing reached the kernel"


def test_oversized_and_tampered_inputs_are_rejected(corpus: Path, tmp_path: Path) -> None:
    prepared = wiki.prepare(corpus, "org-a/alpha")
    big = tmp_path / "big.json"
    big.write_bytes(b"{" + b" " * wiki.BOUNDS["max_proposal_bytes"] + b"}")
    with pytest.raises(wiki.ProposalRejected, match="exceeds"):
        wiki.apply(corpus, corpus / prepared["packet"], big)
    packet_path = corpus / prepared["packet"]
    packet = json.loads(packet_path.read_bytes())
    packet["slices"].append({**packet["slices"][0], "slice_id": "slc_" + "1" * 64})
    edited = write(tmp_path / "edited-packet.json", packet)
    with pytest.raises(wiki.StalePacket, match="differ from their seal"):
        wiki.apply(corpus, edited, write(tmp_path / "p.json", good_proposal(packet)))
    foreign = write(tmp_path / "foreign.json", {**packet, "operation_id": "op_" + "e" * 32})
    with pytest.raises(wiki.StalePacket, match="no seal"):
        wiki.apply(corpus, foreign, write(tmp_path / "p2.json", good_proposal(packet)))


def test_kernel_rejects_verbatim_quote_and_leaves_record_untouched(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    prepared = wiki.prepare(root, "org-a/alpha")
    packet = json.loads((root / prepared["packet"]).read_bytes())
    proposal = good_proposal(packet)
    proposal["claims"][0]["text"] = slice_by_path(packet, "README.md", "Alpha")["text"]  # > 20 verbatim words
    before = {"claims": (root / "wiki/data/claims.jsonl").read_bytes(), "repos": repos_bytes(root)}
    with pytest.raises(wiki.KernelError, match="RCW_QUOTE_LIMIT") as info:
        wiki.apply(root, root / prepared["packet"], write(tmp_path / "quote.json", proposal))
    assert info.value.rcw_code == "RCW_QUOTE_LIMIT" and info.value.code == 13
    assert (root / "wiki/data/claims.jsonl").read_bytes() == before["claims"] and repos_bytes(root) == before["repos"]
    assert core.load_repos(root)["org-a/alpha"]["status"] == "distilled", "prior distillation survives a rejected refresh"


def test_changed_source_bytes_and_superseded_snapshot_are_stale(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    prepared = wiki.prepare(root, "org-a/alpha")
    packet = json.loads((root / prepared["packet"]).read_bytes())
    stored = root / packet["package"]
    original = stored.read_bytes()
    stored.write_bytes(original + b"\n")
    with pytest.raises(wiki.StalePacket, match="RCW_SOURCE_MUTATED"):
        wiki.apply(root, root / prepared["packet"], write(tmp_path / "a.json", good_proposal(packet)))
    stored.write_bytes(original)
    # Same commit, different inspected file set -> new snapshot ID; the old packet no longer binds the active package.
    res = collect.snapshot(root, "org-a/alpha", 20, 50_000, transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    assert res["snapshot_id"] != packet["snapshot_id"] and res["freshness"] == "stale"
    with pytest.raises(wiki.StalePacket, match="superseded"):
        wiki.apply(root, root / prepared["packet"], write(tmp_path / "b.json", good_proposal(packet)))
    assert core.load_repos(root)["org-a/alpha"]["indexed_snapshot_id"] == packet["snapshot_id"]
    assert wiki.audit(root)["freshness"] == {"stale": 1}


def test_cli_prepare_apply_audit_and_error_codes(corpus: Path, tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    root = clone(corpus, tmp_path)
    assert cli.main(["--root", str(root), "prepare", "org-a/alpha"]) == 0
    prepared = json.loads(capsys.readouterr().out)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    proposal = good_proposal(packet)
    proposal["claims"].append(_claim("dependencies", "Documented install path is the alpha-agent pip package.",
                                     [slice_by_path(packet, "README.md", "Install")["slice_id"]]))
    good = write(tmp_path / "cli.json", proposal)
    assert cli.main(["--root", str(root), "apply", str(root / prepared["packet"]), str(good)]) == 0
    applied = json.loads(capsys.readouterr().out)
    assert applied["changed"] is True and applied["claims"] == 5 and "dependencies" not in applied["gaps"]
    assert cli.main(["--root", str(root), "audit", "--level", "pr"]) == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True
    assert cli.main(["--root", str(root), "apply", str(root / prepared["packet"]), str(good)]) == 0, "identical retry reconciles"
    retry = json.loads(capsys.readouterr().out)
    assert retry["reconciled"] is True and retry["claim_ids"] == applied["claim_ids"]
    other = write(tmp_path / "other.json", {**proposal, "summary": "A different summary for the same operation."})
    assert cli.main(["--root", str(root), "apply", str(root / prepared["packet"]), str(other)]) == wiki.ProposalRejected.code
    assert "already applied with a different proposal" in json.loads(capsys.readouterr().out)["message"]
    proposal["claims"][0]["facet"] = "vibes"
    assert cli.main(["--root", str(root), "prepare", "org-a/alpha"]) == 0
    fresh = json.loads(capsys.readouterr().out)
    bad = write(tmp_path / "bad.json", {**good_proposal(json.loads((root / fresh["packet"]).read_bytes())), "claims": proposal["claims"]})
    assert cli.main(["--root", str(root), "apply", str(root / fresh["packet"]), str(bad)]) == wiki.ProposalRejected.code
    assert json.loads(capsys.readouterr().out)["error"] == "ProposalRejected"


# ---------------------------------------------------------------- correction round 1

def test_prepare_rejects_tampered_source_bytes_or_metadata_before_the_kernel(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    rec = core.load_repos(root)["org-a/alpha"]
    snap = json.loads((root / rec["latest_snapshot"]["snapshot"]).read_bytes())
    readme = root / rec["latest_snapshot"]["dir"] / next(f["stored"] for f in snap["files"] if f["path"] == "README.md")
    original, ops = readme.read_bytes(), sorted((root / "wiki/state/operations").iterdir())
    readme.write_bytes(b"# Alpha\nFabricated before preparation.\n")  # advertised git_sha/commit untouched
    with pytest.raises(wiki.SourceIntegrityError, match="differ from recorded SHA-256/Git blob hash: README.md"):
        wiki.prepare(root, "org-a/alpha")
    assert sorted((root / "wiki/state/operations").iterdir()) == ops, "no kernel operation was prepared"
    readme.write_bytes(original)
    manifest_path = root / rec["latest_snapshot"]["package"]
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"][0]["metadata"]["identifiers"]["git_sha"] = "0" * 40
    manifest_bytes = manifest_path.read_bytes()
    manifest_path.write_bytes(core.dump_json(manifest))
    with pytest.raises(wiki.SourceIntegrityError, match="package metadata disagrees"):
        wiki.prepare(root, "org-a/alpha")
    manifest_path.write_bytes(manifest_bytes)
    assert wiki.prepare(root, "org-a/alpha")["operation_id"].startswith("op_"), "restored evidence prepares normally"
    assert wiki.audit(root)["ok"] is True


def test_revised_classification_supersedes_reconciles_and_survives_interruption(corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    root = clone(corpus, tmp_path)
    prepared = wiki.prepare(root, "org-a/alpha")
    packet = json.loads((root / prepared["packet"]).read_bytes())
    current = wiki.apply(root, root / prepared["packet"], write(tmp_path / "p1.json", good_proposal(packet)))
    # Revise only claims[0].kind: observation -> inference. Same text and slices, different kernel identity.
    prepared = wiki.prepare(root, "org-a/alpha")
    revised = good_proposal(json.loads((root / prepared["packet"]).read_bytes()))
    revised["claims"][0]["kind"] = "inference"
    res = wiki.apply(root, root / prepared["packet"], write(tmp_path / "p2.json", revised))
    assert res["changed"] is True and res["claim_ids"][0] != current["claim_ids"][0] and res["claim_ids"][1:] == current["claim_ids"][1:]
    table = {c["id"]: c for c in claims_table(root)}
    assert table[current["claim_ids"][0]]["review_state"] == "superseded" and table[res["claim_ids"][0]]["review_state"] == "mechanically_checked"
    assert table[res["claim_ids"][0]]["scope"]["qualifiers"] == "kind=inference; facet=components"
    dossier = wiki.load_dossier(root, "org-a/alpha")
    assert dossier["claims"][0]["kind"] == "inference" and dossier["superseded_claim_ids"] == [current["claim_ids"][0]]
    assert wiki.audit(root)["ok"] is True
    prepared = wiki.prepare(root, "org-a/alpha")
    rebound = json.loads((root / prepared["packet"]).read_bytes())
    replay = wiki.apply(root, root / prepared["packet"], write(tmp_path / "p3.json", dict(
        revised, operation_id=rebound["operation_id"], base_digest=rebound["base_digest"])))
    assert replay["changed"] is False and replay["claim_ids"] == res["claim_ids"] and replay["dossier_changed"] is False
    # Interruption after the kernel commits but before the auxiliary writes; the retry must finish without a second commit.
    prepared = wiki.prepare(root, "org-a/alpha")
    revised2 = good_proposal(json.loads((root / prepared["packet"]).read_bytes()))
    revised2["claims"][1]["kind"] = "inference"
    proposal = write(tmp_path / "p4.json", revised2)
    real_finish = wiki._finish

    def crash(*args, **kwargs):
        raise RuntimeError("simulated interruption after kernel commit")

    monkeypatch.setattr(wiki, "_finish", crash)
    with pytest.raises(RuntimeError):
        wiki.apply(root, root / prepared["packet"], proposal)
    monkeypatch.setattr(wiki, "_finish", real_finish)
    ops = [o["id"] for o in wiki._rows(root / "wiki", "operations")]
    assert prepared["operation_id"] in ops and core.load_repos(root)["org-a/alpha"]["indexed_operation_id"] != prepared["operation_id"]
    with pytest.raises(wiki.DossierInvalid, match="claim fields differ from the kernel record"):
        wiki.load_dossier(root, "org-a/alpha")  # kernel superseded the old claim; the stale dossier no longer corresponds
    retry = wiki.apply(root, root / prepared["packet"], proposal)
    assert retry["reconciled"] is True and retry["changed"] is True and retry["operation_id"] == prepared["operation_id"]
    assert [o["id"] for o in wiki._rows(root / "wiki", "operations")] == ops, "no duplicate canonical evidence"
    assert core.load_repos(root)["org-a/alpha"]["indexed_operation_id"] == prepared["operation_id"]
    assert wiki.load_dossier(root, "org-a/alpha")["claims"][1]["kind"] == "inference" and wiki.audit(root)["ok"] is True
    different = write(tmp_path / "p5.json", {**revised2, "summary": "Not the proposal the kernel applied."})
    with pytest.raises(wiki.ProposalRejected, match="already applied with a different proposal"):
        wiki.apply(root, root / prepared["packet"], different)


def test_recovery_rejects_source_tampering_after_a_successful_apply(tmp_path: Path) -> None:
    collect.snapshot(tmp_path, "org-a/alpha", 20, 50_000, paths=["src/agent.py"],
                     transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    prepared = wiki.prepare(tmp_path, "org-a/alpha")
    packet_path = tmp_path / prepared["packet"]
    proposal = write(tmp_path / "proposals/recovery.json", good_proposal(json.loads(packet_path.read_bytes())))
    wiki.apply(tmp_path, packet_path, proposal)
    active = core.load_repos(tmp_path)["org-a/alpha"]["latest_snapshot"]
    snapshot = json.loads((tmp_path / active["snapshot"]).read_bytes())
    member = next(f for f in snapshot["files"] if f["path"] == "README.md")
    (tmp_path / active["dir"] / member["stored"]).write_bytes(b"Altered after successful apply.\n")
    with pytest.raises(wiki.SourceIntegrityError):
        wiki.apply(tmp_path, packet_path, proposal)


def test_valid_old_dossier_survives_failed_refresh_after_new_snapshot(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    old = core.load_repos(root)["org-a/alpha"]["indexed_snapshot_id"]
    collect.snapshot(root, "org-a/alpha", 20, 50_000, paths=["src/agent.py"],
                     transport=FakeTransport(repo_routes("org-a/alpha", "b" * 40, FILES)))
    with pytest.raises(collect.FetchFailed):
        collect.snapshot(root, "org-a/alpha", 20, 50_000, transport=FakeTransport({}))
    assert core.load_repos(root)["org-a/alpha"]["freshness"] == "refresh-failed"
    assert wiki.load_dossier(root, "org-a/alpha")["snapshot_id"] == old
    assert wiki.audit(root)["ok"] is True


def test_audit_detects_dossier_tampering_and_uninitialized_wiki(corpus: Path, tmp_path: Path) -> None:
    root = clone(corpus, tmp_path)
    rec = core.load_repos(root)["org-a/alpha"]
    assert rec["status"] == "distilled" and wiki.audit(root)["ok"] is True
    path = root / rec["dossier"]
    pristine = path.read_bytes()
    dossier = json.loads(pristine)
    dossier["claims"][0]["text"] = "Alpha ships a Kubernetes operator with autoscaling."  # invented, claim_id retained
    path.write_bytes(core.dump_json(dossier))
    report = wiki.audit(root)
    assert report["ok"] is False and "seal mismatch" in report["repos"]["org-a/alpha"]["problems"][0]
    path.write_bytes(core.dump_json(wiki.seal(dossier)))  # re-sealed forgery: caught by kernel-field verification
    report = wiki.audit(root)
    assert report["ok"] is False and "claim fields differ from the kernel record" in report["repos"]["org-a/alpha"]["problems"][0]
    with pytest.raises(wiki.DossierInvalid):
        wiki.load_dossier(root, "org-a/alpha")
    dossier = json.loads(pristine)
    dossier["claims"][1]["locators"][0]["line_start"] = 3
    path.write_bytes(core.dump_json(wiki.seal(dossier)))
    assert "locator differs from kernel" in wiki.audit(root)["repos"]["org-a/alpha"]["problems"][0]
    dossier = json.loads(pristine)
    dossier["summary"] = "Edited summary."
    path.write_bytes(core.dump_json(wiki.seal(dossier)))
    assert wiki.audit(root)["ok"] is True, "summary edits are only seal-protected: re-sealed summary edits pass (known limit)"
    path.write_bytes(pristine)
    assert wiki.audit(root)["ok"] is True
    # A record that claims distilled evidence without an initialized wiki is not healthy.
    bare = tmp_path / "bare"
    core.init(bare)
    core.save_repos(bare, {"org-a/alpha": {**rec}})
    report = wiki.audit(bare)
    assert report["ok"] is False and report["wiki_initialized"] is False
    assert "wiki is not initialized" in report["repos"]["org-a/alpha"]["problems"][0]
