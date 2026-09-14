"""Opt-in partitioned per-repository pinned-kernel wiki layout, and the deterministic long-identifier
storage-prefix fix that keeps stored source/dossier paths well under Windows' path-length ceiling.

Offline, model-free, real kernel. Reuses the FakeTransport/repo_routes fixtures from test_collect.py.
"""

from __future__ import annotations

import json
import shutil
import time
from pathlib import Path

import pytest

from map_agents import collect, core, wiki
from test_collect import FakeTransport, repo_routes

README = b"# Agent\n\nA tiny synthetic agent used for partitioned wiki layout tests.\n"
FILES = {"README.md": README}


def sha_for(n: int) -> str:
    return f"{n:040x}"


def snap(root: Path, key: str, sha: str, files: dict[str, bytes] = FILES) -> dict:
    return collect.snapshot(root, key, 5, 50_000, transport=FakeTransport(repo_routes(key, sha, files)))


def good_proposal(packet: dict) -> dict:
    readme = next(s for s in packet["slices"] if s["locator"]["path"] == "README.md")
    return {
        "schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
        "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
        "summary": "Synthetic agent used to exercise the partitioned kernel layout.",
        "claims": [{"facet": "components", "text": "A tiny synthetic agent is documented for this partition test.",
                    "slice_ids": [readme["slice_id"]], "kind": "observation", "basis": "documented"}],
    }


def write(path: Path, obj: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(core.dump_json(obj))
    return path


# ---------------------------------------------------------------- layout config


def test_default_layout_is_shared(tmp_path: Path) -> None:
    core.init(tmp_path)
    assert wiki.load_layout(tmp_path) == {"schema_version": wiki.LAYOUT_SCHEMA, "layout": "shared"}


def test_enable_partitioned_is_versioned_and_idempotent(tmp_path: Path) -> None:
    res = wiki.enable_partitioned(tmp_path)
    assert res == {"root": str(tmp_path), "layout": "partitioned", "changed": True}
    cfg = json.loads((tmp_path / wiki.LAYOUT_FILE).read_bytes())
    assert cfg == {"schema_version": wiki.LAYOUT_SCHEMA, "layout": "partitioned"}
    again = wiki.enable_partitioned(tmp_path)
    assert again == {"root": str(tmp_path), "layout": "partitioned", "changed": False}


def test_unsafe_or_unversioned_config_is_rejected(tmp_path: Path) -> None:
    core.init(tmp_path)
    (tmp_path / wiki.LAYOUT_FILE).write_bytes(b"not json")
    with pytest.raises(wiki.WikiError, match="not valid UTF-8 JSON"):
        wiki.load_layout(tmp_path)
    (tmp_path / wiki.LAYOUT_FILE).write_bytes(core.dump_json({"schema_version": "map-agents.wiki-layout/2", "layout": "shared"}))
    with pytest.raises(wiki.WikiError, match="invalid or unversioned"):
        wiki.load_layout(tmp_path)
    (tmp_path / wiki.LAYOUT_FILE).write_bytes(core.dump_json({"schema_version": wiki.LAYOUT_SCHEMA, "layout": "custom"}))
    with pytest.raises(wiki.WikiError, match="invalid or unversioned"):
        wiki.load_layout(tmp_path)


def test_enable_partitioned_refuses_while_another_writer_holds_the_lock(tmp_path: Path) -> None:
    core.init(tmp_path)
    lock = tmp_path / core.LOCK_FILE
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_bytes(b"pid=999999\n")
    with pytest.raises(core.LockHeld):
        wiki.enable_partitioned(tmp_path)
    lock.unlink()


def test_enable_partitioned_refuses_when_shared_wiki_already_initialized(tmp_path: Path) -> None:
    snap(tmp_path, "org-a/alpha", sha_for(1))
    wiki.prepare(tmp_path, "org-a/alpha")  # initializes the shared kernel; no claims applied yet
    with pytest.raises(wiki.WikiError, match="shared wiki kernel is already initialized"):
        wiki.enable_partitioned(tmp_path)


def test_enable_partitioned_refuses_when_indexed_dossier_exists(tmp_path: Path) -> None:
    snap(tmp_path, "org-a/alpha", sha_for(1))
    prepared = wiki.prepare(tmp_path, "org-a/alpha")
    packet = json.loads((tmp_path / prepared["packet"]).read_bytes())
    wiki.apply(tmp_path, tmp_path / prepared["packet"], write(tmp_path / "proposals" / "p.json", good_proposal(packet)))
    # An applied dossier always leaves the shared kernel initialized too; either refusal reason is a correct migration guard.
    with pytest.raises(wiki.WikiError, match="already initialized|already has indexed dossier evidence"):
        wiki.enable_partitioned(tmp_path)
    # Directly exercise the indexed-dossier guard on its own, with the shared kernel absent.
    bare = tmp_path / "bare"
    core.init(bare)
    core.save_repos(bare, {"org-a/alpha": core.load_repos(tmp_path)["org-a/alpha"]})
    with pytest.raises(wiki.WikiError, match="already has indexed dossier evidence"):
        wiki.enable_partitioned(bare)


def test_config_downgrade_after_partitioned_evidence_exists_is_rejected(tmp_path: Path) -> None:
    snap(tmp_path, "org-a/alpha", sha_for(1))
    wiki.enable_partitioned(tmp_path)
    prepared = wiki.prepare(tmp_path, "org-a/alpha")
    packet = json.loads((tmp_path / prepared["packet"]).read_bytes())
    wiki.apply(tmp_path, tmp_path / prepared["packet"], write(tmp_path / "proposals" / "p.json", good_proposal(packet)))
    (tmp_path / wiki.LAYOUT_FILE).write_bytes(core.dump_json({"schema_version": wiki.LAYOUT_SCHEMA, "layout": "shared"}))
    with pytest.raises(wiki.WikiError, match="downgraded to shared"):
        wiki.load_layout(tmp_path)
    (tmp_path / wiki.LAYOUT_FILE).unlink()  # deleting the config is the same unsupported downgrade
    with pytest.raises(wiki.WikiError, match="downgraded to shared"):
        wiki.prepare(tmp_path, "org-a/alpha")


# ---------------------------------------------------------------- two independent partitions coexist


@pytest.fixture
def two_partition_corpus(tmp_path: Path) -> Path:
    snap(tmp_path, "org-a/alpha", sha_for(1))
    snap(tmp_path, "org-b/beta", sha_for(2))
    wiki.enable_partitioned(tmp_path)
    return tmp_path


def test_two_partitions_prepare_apply_coexist_without_foreign_ids(two_partition_corpus: Path) -> None:
    root = two_partition_corpus
    key_a, key_b = "org-a/alpha", "org-b/beta"
    prep_a, prep_b = wiki.prepare(root, key_a), wiki.prepare(root, key_b)
    kernel_a, kernel_b = wiki._kernel_root(root, key_a), wiki._kernel_root(root, key_b)
    assert kernel_a != kernel_b and kernel_a.parent == kernel_b.parent == root / wiki.WIKI_DIR / wiki.SHARD_DIR
    items_a = wiki.rcw(kernel_a, "inventory", str(kernel_a))["items"]
    items_b = wiki.rcw(kernel_b, "inventory", str(kernel_b))["items"]
    assert len(items_a) == 1 and len(items_b) == 1, "each partition's kernel only ever inventories its own repository"
    packet_a = json.loads((root / prep_a["packet"]).read_bytes())
    packet_b = json.loads((root / prep_b["packet"]).read_bytes())
    applied_a = wiki.apply(root, root / prep_a["packet"], write(root / "proposals" / "a.json", good_proposal(packet_a)))
    applied_b = wiki.apply(root, root / prep_b["packet"], write(root / "proposals" / "b.json", good_proposal(packet_b)))
    assert applied_a["changed"] is True and applied_b["changed"] is True
    dossier_a, dossier_b = wiki.load_dossier(root, key_a), wiki.load_dossier(root, key_b)
    assert dossier_a["repo"] == key_a and dossier_b["repo"] == key_b
    claims_a = {c["id"] for c in wiki._rows(kernel_a, "claims")}
    claims_b = {c["id"] for c in wiki._rows(kernel_b, "claims")}
    assert claims_a and claims_b and claims_a.isdisjoint(claims_b), "no foreign claim IDs cross a partition boundary"
    ops_a = {o["id"] for o in wiki._rows(kernel_a, "operations")}
    ops_b = {o["id"] for o in wiki._rows(kernel_b, "operations")}
    assert ops_a.isdisjoint(ops_b) and applied_a["operation_id"] not in ops_b and applied_b["operation_id"] not in ops_a
    report = wiki.audit(root)
    assert report["ok"] is True and report["layout"] == "partitioned"
    assert set(report["repos"]) == {key_a, key_b} and all(r["claims"] == 1 and r["problems"] == [] for r in report["repos"].values())
    assert len(report["partitions"]) == 2 and all(p["ok"] and p["initialized"] for p in report["partitions"].values())


def test_wrong_partition_packet_is_rejected_by_its_seal(two_partition_corpus: Path) -> None:
    root = two_partition_corpus
    prep_b = wiki.prepare(root, "org-b/beta")
    packet_b = json.loads((root / prep_b["packet"]).read_bytes())
    forged = {**packet_b, "repo": "org-a/alpha"}  # claims to be alpha's packet but is beta's sealed bytes, edited
    forged_path = write(root / "proposals" / "forged-packet.json", forged)
    with pytest.raises(wiki.StalePacket, match="differ from their seal"):
        wiki.apply(root, forged_path, write(root / "proposals" / "forged-proposal.json", good_proposal(forged)))


def test_tampered_source_bytes_rejected_before_the_kernel_in_partitioned_mode(two_partition_corpus: Path) -> None:
    root = two_partition_corpus
    rec = core.load_repos(root)["org-a/alpha"]
    snapshot = json.loads((root / rec["latest_snapshot"]["snapshot"]).read_bytes())
    readme = root / rec["latest_snapshot"]["dir"] / next(f["stored"] for f in snapshot["files"] if f["path"] == "README.md")
    original = readme.read_bytes()
    readme.write_bytes(b"# Tampered\nBytes changed after the snapshot was recorded.\n")
    with pytest.raises(wiki.SourceIntegrityError):
        wiki.prepare(root, "org-a/alpha")
    readme.write_bytes(original)
    assert wiki.prepare(root, "org-a/alpha")["operation_id"].startswith("op_"), "restored evidence prepares normally"
    # A change to org-a/alpha's source must not affect org-b/beta's independent partition.
    assert wiki.prepare(root, "org-b/beta")["operation_id"].startswith("op_")


def test_unrelated_repository_changes_do_not_stale_a_different_partitions_packets(two_partition_corpus: Path) -> None:
    root = two_partition_corpus
    prep_a = wiki.prepare(root, "org-a/alpha")
    prep_b = wiki.prepare(root, "org-b/beta")
    packet_b = json.loads((root / prep_b["packet"]).read_bytes())
    wiki.apply(root, root / prep_b["packet"], write(root / "proposals" / "b-first.json", good_proposal(packet_b)))
    # Applying beta's packet moved only beta's kernel base digest; alpha's independently-prepared packet still applies.
    packet_a = json.loads((root / prep_a["packet"]).read_bytes())
    applied_a = wiki.apply(root, root / prep_a["packet"], write(root / "proposals" / "a-after-b.json", good_proposal(packet_a)))
    assert applied_a["changed"] is True


# ---------------------------------------------------------------- CLI opt-in


def test_cli_wiki_layout_shows_and_enables(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    from map_agents import __main__ as cli

    assert cli.main(["--root", str(tmp_path), "wiki-layout"]) == 0
    assert json.loads(capsys.readouterr().out)["layout"] == "shared"
    assert cli.main(["--root", str(tmp_path), "wiki-layout", "--enable-partitioned"]) == 0
    enabled = json.loads(capsys.readouterr().out)
    assert enabled["layout"] == "partitioned" and enabled["changed"] is True
    assert cli.main(["--root", str(tmp_path), "wiki-layout"]) == 0
    assert json.loads(capsys.readouterr().out)["layout"] == "partitioned"


# ---------------------------------------------------------------- 500-repository source-scale isolation


def test_partition_ignores_unrelated_sources_at_source_scale(tmp_path: Path) -> None:
    """Regression for the measured 93.672s full-corpus inventory scan: a partition must only ever
    walk its own repository's sources, proven by count, by a deliberately malformed unrelated package,
    and by elapsed time."""
    root, n = tmp_path, 500
    for i in range(n):
        snap(root, f"owner{i}/repo{i}", sha_for(i))
    target = "owner0/repo0"
    other_rec = core.load_repos(root)[f"owner{n - 1}/repo{n - 1}"]
    other_manifest = root / other_rec["latest_snapshot"]["package"]
    other_manifest.write_bytes(b"{not valid json, deliberately malformed}")
    wiki.enable_partitioned(root)
    started = time.monotonic()
    prepared = wiki.prepare(root, target)
    prepare_elapsed = time.monotonic() - started
    kernel = wiki._kernel_root(root, target)
    items = wiki.rcw(kernel, "inventory", str(kernel))["items"]
    assert len(items) == 1, "the target partition's kernel inventories only its own repository, not all 500"
    assert prepare_elapsed < 10.0, f"partitioned prepare took {prepare_elapsed:.3f}s across {n} unrelated repositories"
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "scale.json", good_proposal(packet)))
    assert applied["changed"] is True
    started_audit = time.monotonic()
    report = wiki.audit(root)
    audit_elapsed = time.monotonic() - started_audit
    assert report["repos"][target]["problems"] == [] and audit_elapsed < 10.0, f"audit took {audit_elapsed:.3f}s"


# ---------------------------------------------------------------- long identifiers (WinError 206 fix)

LONG_OWNER = "aws-samples"
LONG_REPO = "setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit"
LONG_KEY = f"{LONG_OWNER}/{LONG_REPO}"
assert len(LONG_OWNER) + len(LONG_REPO) > collect.STORAGE_SEGMENT_LIMIT, "fixture must exercise the long-identifier branch"


def test_storage_segments_shortens_long_identifiers_but_keeps_short_ones_unchanged(tmp_path: Path) -> None:
    assert collect.storage_segments(tmp_path, "org-a/alpha") == ("org-a", "alpha"), "existing captured snapshots keep their layout"
    owner_seg, repo_seg = collect.storage_segments(tmp_path, LONG_KEY)
    assert len(owner_seg) == len(repo_seg) == 8 and (owner_seg, repo_seg) != (LONG_OWNER, LONG_REPO)
    assert collect.storage_segments(tmp_path, LONG_KEY) == (owner_seg, repo_seg), "deterministic across repeated calls/hosts"
    other_long = "owner-with-a-very-long-name-here/another-quite-long-repository-name"
    assert collect.storage_segments(tmp_path, other_long) != (owner_seg, repo_seg), "distinct long identifiers get distinct segments"


def test_long_identifier_snapshot_and_partitioned_apply_avoid_long_path_segments(tmp_path: Path) -> None:
    root = tmp_path
    res = snap(root, LONG_KEY, sha_for(999))
    assert res["files_stored"] == 1
    rec = core.load_repos(root)[LONG_KEY]
    stored_path = root / rec["latest_snapshot"]["package"]
    assert stored_path.is_file()
    assert LONG_OWNER not in stored_path.parts and LONG_REPO not in stored_path.parts, "long identity is not a path segment"
    rel_len = len(str(stored_path.relative_to(root)))
    assert rel_len < 130, f"relative storage path is {rel_len} chars: {stored_path.relative_to(root)}"
    snapshot_record = json.loads((root / rec["latest_snapshot"]["snapshot"]).read_bytes())
    assert snapshot_record["repo"] == LONG_KEY and snapshot_record["url"].endswith(LONG_REPO), "full identity stays in metadata/URLs"
    wiki.enable_partitioned(root)
    prepared = wiki.prepare(root, LONG_KEY)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    assert packet["repo"] == LONG_KEY
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "long.json", good_proposal(packet)))
    assert applied["changed"] is True
    dossier = wiki.load_dossier(root, LONG_KEY)
    assert dossier["repo"] == LONG_KEY
    dossier_path = root / core.load_repos(root)[LONG_KEY]["dossier"]
    assert LONG_OWNER not in dossier_path.parts and LONG_REPO not in dossier_path.parts
    dossier_rel_len = len(str(dossier_path.relative_to(root)))
    assert dossier_rel_len < 130, f"relative dossier path is {dossier_rel_len} chars: {dossier_path.relative_to(root)}"


def test_long_identifier_storage_paths_fit_a_windows_budget_at_the_real_task_root() -> None:
    """Uses this checkout's own path (the provided Windows task path), not pytest's temp directory,
    since the temp directory's own length is outside this fix's control."""
    task_root = Path(__file__).resolve().parents[1]
    owner_seg, repo_seg = collect.storage_segments(task_root / "corpus", LONG_KEY)  # no legacy dir there: hashed
    stored_name = collect.storage_name("README.md")
    candidate = task_root / "corpus" / collect.SOURCE_DIR / owner_seg / repo_seg / sha_for(999) / ("0" * 16) / stored_name
    assert len(str(candidate)) < 250, f"{len(str(candidate))} chars: {candidate}"


# ---------------------------------------------------------------- legacy long-name snapshots (pre-fix captures)

LEGACY_KEYS = [
    "ai-maker-space/interactive-dev-environment-for-ai-engineers",
    "alexdevassy/ai-powered-vulnerability-impact-analyzer",
    "anaconda-labs/building-intelligent-apps-with-anaconda",
    "anishsingh20/useful-generativeai-tools-repo",
    "aws-samples/sample-multi-agent-orchestration-chat-on-agentcore",
    "spark-engine-opensource-projects/fullstack-nextjs-app-generator",
    "strategic-automation/dspy-compounding-engineering",
]


@pytest.mark.parametrize("key", LEGACY_KEYS)
def test_all_seven_canonical_legacy_long_names_qualify_for_prefix_preservation(key: str) -> None:
    owner, name = key.split("/")
    assert len(owner) + len(name) > collect.STORAGE_SEGMENT_LIMIT, key


def test_legacy_long_name_snapshot_prefix_is_preserved_across_partition_enable_and_refresh(
    tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch
) -> None:
    # A short, explicit basename (unlike the default tmp_path, which embeds the whole test name) keeps this
    # legacy real long-name path realistic instead of artificially exceeding Windows' ceiling from test-harness depth alone.
    root, key = tmp_path_factory.mktemp("legacy"), LEGACY_KEYS[0]
    owner, name = key.split("/")
    legacy_dir = root / collect.SOURCE_DIR / owner / name

    # Simulate a snapshot captured before this fix existed, when every identifier used its real directories.
    monkeypatch.setattr(collect, "storage_segments", lambda _root, k: tuple(k.split("/", 1)))
    first = snap(root, key, sha_for(1))
    monkeypatch.undo()

    assert legacy_dir.is_dir() and list(legacy_dir.glob(f"*/*/{collect.RCW_MANIFEST}")), "fixture must be a genuine prior capture"
    # With the real resolver restored, a long identifier with an established real prefix keeps it.
    assert collect.storage_segments(root, key) == (owner, name)

    wiki.enable_partitioned(root)
    prepared = wiki.prepare(root, key)
    layout = wiki.load_layout(root)
    assert wiki._kernel_sources_root(root, key, layout) == legacy_dir, "partition source root is the repository's real directory"
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "legacy.json", good_proposal(packet)))
    assert applied["changed"] is True
    dossier_path = root / core.load_repos(root)[key]["dossier"]
    assert dossier_path.is_relative_to(root / wiki.DOSSIER_DIR / owner / name), "dossier keeps the real legacy prefix too"

    # A subsequent refresh (new commit) must land in the SAME legacy directory tree, not a new hash directory.
    second = snap(root, key, sha_for(2))
    assert (root / second["dir"]).is_relative_to(legacy_dir)
    kernel = wiki._kernel_root(root, key)
    items = wiki.rcw(kernel, "inventory", str(kernel))["items"]
    assert len(items) == 2, "old and new snapshots share one kernel source root"
    assert first["dir"] != second["dir"]


def test_empty_leftover_long_name_directory_is_not_treated_as_an_established_prefix(tmp_path: Path) -> None:
    # The fixture deliberately models a long legacy path. Keep its pytest-owned
    # root short enough that creating the fixture itself works on Windows.
    root, key = tmp_path.parent / "legacy-leftover", LEGACY_KEYS[0]
    owner, name = key.split("/")
    # A directory tree with no completed package manifest (as a WinError 206 interruption would leave behind).
    stray = root / collect.SOURCE_DIR / owner / name / sha_for(1) / ("0" * 16)
    stray.mkdir(parents=True)
    (stray / "not-a-manifest.txt").write_bytes(b"partial write")
    owner_seg, name_seg = collect.storage_segments(root, key)
    assert (owner_seg, name_seg) != (owner, name), "an incomplete leftover directory must not be treated as established"


# ---------------------------------------------------------------- verified source coverage propagation


def test_prepare_emits_coverage_from_the_verified_snapshot(tmp_path: Path) -> None:
    root, key = tmp_path, "org-a/alpha"
    snap(root, key, sha_for(1))
    rec = core.load_repos(root)[key]
    snapshot = json.loads((root / rec["latest_snapshot"]["snapshot"]).read_bytes())
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    cov = packet["coverage"]
    assert set(cov) == wiki.COVERAGE_KEYS
    assert cov["files"] == [{"path": f["path"], "lines": f["lines"], "size": f["size"]} for f in snapshot["files"]]
    assert cov["selection"] == snapshot["selection"] and cov["repository"] == snapshot["repository"]
    assert cov["omitted"] == snapshot["omitted"] and cov["omitted_count"] == snapshot["omitted_count"]
    assert cov["explicit_paths"] == snapshot["explicit_paths"] and cov["omitted_slices"] == packet["omitted_slices"]


def test_coverage_propagates_from_packet_to_dossier_and_survives_replay(tmp_path: Path) -> None:
    root, key = tmp_path, "org-a/alpha"
    snap(root, key, sha_for(1))
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "p.json", good_proposal(packet)))
    dossier = json.loads((root / applied["dossier"]).read_bytes())
    assert dossier["coverage"] == packet["coverage"]
    loaded = wiki.load_dossier(root, key)  # cross-checked against the verified snapshot and the kernel's own sources
    assert loaded["coverage"] == packet["coverage"]
    assert wiki.audit(root)["ok"] is True


def test_load_dossier_rejects_resealed_coverage_that_disagrees_with_the_verified_snapshot(tmp_path: Path) -> None:
    root, key = tmp_path, "org-a/alpha"
    snap(root, key, sha_for(1))
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "p.json", good_proposal(packet)))
    dossier_path = root / applied["dossier"]
    pristine = dossier_path.read_bytes()

    for false_count in (1, -1, True, "0"):
        changed = json.loads(pristine)
        changed["coverage"]["omitted_slices"] = false_count
        dossier_path.write_bytes(core.dump_json(wiki.seal(changed)))
        with pytest.raises(wiki.DossierInvalid, match="coverage"):
            wiki.load_dossier(root, key)

    forged = json.loads(pristine)
    forged["coverage"]["omitted_count"] = forged["coverage"]["omitted_count"] + 1
    dossier_path.write_bytes(core.dump_json(wiki.seal(forged)))
    with pytest.raises(wiki.DossierInvalid, match="coverage differs from the verified"):
        wiki.load_dossier(root, key)
    report = wiki.audit(root)
    assert report["ok"] is False and "coverage differs" in report["repos"][key]["problems"][0]

    forged2 = json.loads(pristine)
    forged2["coverage"]["files"] = forged2["coverage"]["files"] + [{"path": "phantom.md", "lines": 1, "size": 1}]
    dossier_path.write_bytes(core.dump_json(wiki.seal(forged2)))
    with pytest.raises(wiki.DossierInvalid):
        wiki.load_dossier(root, key)

    dossier_path.write_bytes(pristine)
    assert wiki.audit(root)["ok"] is True


def test_load_dossier_accepts_an_old_dossier_written_without_a_coverage_field(tmp_path: Path) -> None:
    """Backward compatibility: a dossier from before this field existed loads without pretending it is
    complete evidence; the absence of `coverage` is honest, not a synthesized 'complete' claim."""
    root, key = tmp_path, "org-a/alpha"
    snap(root, key, sha_for(1))
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "p.json", good_proposal(packet)))
    dossier_path = root / applied["dossier"]
    legacy = json.loads(dossier_path.read_bytes())
    del legacy["coverage"]  # simulates a dossier written by code that predates this field entirely
    dossier_path.write_bytes(core.dump_json(wiki.seal(legacy)))
    loaded = wiki.load_dossier(root, key)
    assert "coverage" not in loaded
    assert wiki.audit(root)["ok"] is True


def test_coverage_check_uses_the_dossiers_own_stale_snapshot_not_the_latest_one(tmp_path: Path) -> None:
    root, key = tmp_path, "org-a/alpha"
    snap(root, key, sha_for(1))
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    applied = wiki.apply(root, root / prepared["packet"], write(root / "proposals" / "p.json", good_proposal(packet)))
    old_coverage = json.loads((root / applied["dossier"]).read_bytes())["coverage"]
    # A new snapshot (different file set) makes the record stale; the dossier's own bound (older) snapshot
    # is what its coverage must still agree with, not the newly active one.
    snap(root, key, sha_for(2), files={**FILES, "docs/design.md": b"# Design\n\nMore detail.\n"})
    assert core.load_repos(root)[key]["freshness"] == "stale"
    loaded = wiki.load_dossier(root, key)
    assert loaded["coverage"] == old_coverage
    assert wiki.audit(root)["ok"] is True


# ---------------------------------------------------------------- portable-copy (ZIP) regression


def _tracked_ignore(dirpath: str, names: list[str]) -> set[str]:
    """Mirrors this project's .gitignore for a corpus root: ephemeral packets/proposals/state stay behind."""
    parent = Path(dirpath).name
    skip = set()
    for n in names:
        if n in ("packets", "proposals") and (Path(dirpath) / n).is_dir():
            skip.add(n)
        if parent == "state" and n in ("operations", "workers", "packets", "leases", "writer.lock"):
            skip.add(n)
    return skip


def copy_tracked(src: Path, dst: Path) -> Path:
    shutil.copytree(src, dst, ignore=_tracked_ignore)
    return dst


def test_portable_copy_of_tracked_files_keeps_shared_layout_working(tmp_path_factory: pytest.TempPathFactory) -> None:
    src, key = tmp_path_factory.mktemp("orig"), "org-a/alpha"
    snap(src, key, sha_for(1))
    prepared = wiki.prepare(src, key)
    packet = json.loads((src / prepared["packet"]).read_bytes())
    wiki.apply(src, src / prepared["packet"], write(src / "proposals" / "p.json", good_proposal(packet)))
    original_dossier = wiki.load_dossier(src, key)

    copied_root = tmp_path_factory.mktemp("copy") / "relocated" / "corpus"  # a genuinely different absolute path/depth
    copy_tracked(src, copied_root)
    assert not (copied_root / "state" / "operations").exists() and not (copied_root / "packets").exists()
    cfg = (copied_root / "wiki" / "wiki.yaml").read_text(encoding="utf-8")
    assert "../sources" in cfg and str(src) not in cfg, "the relative sources config travels unedited, tied to no absolute path"

    assert wiki.audit(copied_root)["ok"] is True
    assert wiki.load_dossier(copied_root, key) == original_dossier

    # A brand-new prepare/apply cycle (a fresh operation, not a retry of one from before the copy) works.
    snap(copied_root, key, sha_for(2))
    refreshed = wiki.prepare(copied_root, key)
    refreshed_packet = json.loads((copied_root / refreshed["packet"]).read_bytes())
    applied2 = wiki.apply(copied_root, copied_root / refreshed["packet"],
                          write(copied_root / "proposals" / "p2.json", good_proposal(refreshed_packet)))
    assert applied2["changed"] is True


def test_portable_copy_of_tracked_files_keeps_partitioned_layout_working(tmp_path_factory: pytest.TempPathFactory) -> None:
    src, key_a, key_b = tmp_path_factory.mktemp("porig"), "org-a/alpha", "org-b/beta"
    snap(src, key_a, sha_for(1))
    snap(src, key_b, sha_for(2))
    wiki.enable_partitioned(src)
    prep_a, prep_b = wiki.prepare(src, key_a), wiki.prepare(src, key_b)
    wiki.apply(src, src / prep_a["packet"], write(src / "proposals" / "a.json",
               good_proposal(json.loads((src / prep_a["packet"]).read_bytes()))))
    wiki.apply(src, src / prep_b["packet"], write(src / "proposals" / "b.json",
               good_proposal(json.loads((src / prep_b["packet"]).read_bytes()))))

    copied_root = tmp_path_factory.mktemp("pcopy") / "relocated" / "corpus"
    copy_tracked(src, copied_root)
    for key in (key_a, key_b):
        kernel = wiki._kernel_root(copied_root, key)
        cfg = (kernel / "wiki.yaml").read_text(encoding="utf-8")
        assert str(src) not in cfg, "each partition's relative sources config is also tied to no absolute path"

    report = wiki.audit(copied_root)
    assert report["ok"] is True and report["layout"] == "partitioned"
    assert wiki.load_dossier(copied_root, key_a)["repo"] == key_a
    assert wiki.load_dossier(copied_root, key_b)["repo"] == key_b
    assert wiki.prepare(copied_root, key_a)["operation_id"].startswith("op_"), "a fresh prepare resolves the relocated partition"


def test_portable_copy_disclosed_limitation_in_flight_apply_state_does_not_travel(
    tmp_path_factory: pytest.TempPathFactory, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Discloses a real, narrow non-portability: recovering an apply that is mid-flight (kernel already
    committed, local receipt/dossier not yet written) depends on this project's own gitignored local
    recovery state (state/packets/<op>.receipt.json, and the ephemeral packets/proposals files). A ZIP or
    directory copy that only carries tracked files must not be made mid-apply; finish or discard in-flight
    work first. Fully completed operations (the common case) are unaffected, as the prior two tests show."""
    src, key = tmp_path_factory.mktemp("iorig"), "org-a/alpha"
    snap(src, key, sha_for(1))
    prepared = wiki.prepare(src, key)
    packet_path = src / prepared["packet"]
    packet = json.loads(packet_path.read_bytes())
    proposal_path = write(src / "proposals" / "p.json", good_proposal(packet))
    real_finish = wiki._finish

    def crash(*args, **kwargs):
        raise RuntimeError("simulated interruption after the kernel committed, before local receipt/dossier writes")

    monkeypatch.setattr(wiki, "_finish", crash)
    with pytest.raises(RuntimeError):
        wiki.apply(src, packet_path, proposal_path)
    monkeypatch.setattr(wiki, "_finish", real_finish)

    copied_root = tmp_path_factory.mktemp("icopy") / "relocated" / "corpus"
    copy_tracked(src, copied_root)
    assert not (copied_root / "state" / "packets").exists(), "the local seal/receipt directory is gitignored, by design"
    carried_packet = write(copied_root / "packets" / f"{prepared['operation_id']}.json", packet)  # manually carried by hand
    carried_proposal = write(copied_root / "proposals" / "p.json", good_proposal(packet))
    with pytest.raises(wiki.StalePacket, match="no seal in this corpus"):
        wiki.apply(copied_root, carried_packet, carried_proposal)

    # Recovery in place (no relocation) is unaffected: the kernel already committed, and the local seal survives.
    retry = wiki.apply(src, packet_path, proposal_path)
    assert retry["reconciled"] is True and retry["changed"] is True
