"""Behavioral tests for maintain/run_worker: bounds, fairness, resumability, receipts, fake processes. Offline."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import pytest

from map_agents import __main__ as cli
from map_agents import collect, core, wiki, workers
from test_collect import SHA1, SHA2, FakeTransport, catalog_routes, repo_routes, repos_bytes
from test_wiki import FILES, good_proposal

PY = sys.executable
TESTS = Path(__file__).resolve().parent
REPOS = ("org-a/alpha", "orgb/bravo", "orgc/charlie", "orge/echo", "orgg/golf")
FAST = dict(net_seconds=30.0, max_seconds=60.0, worker_seconds=20.0)

VALID = f"""import json, sys
sys.path.insert(0, {str(TESTS)!r})
from test_wiki import good_proposal
env = json.load(sys.stdin)
assert env["coverage"]["explicit_paths"] == ["src/agent.py"], env["coverage"]
print(json.dumps(good_proposal(env["packet"])))
"""
NOISY = "import sys\nsys.stderr.write('n' * 300_000); sys.stderr.flush()\n" + VALID
SCRIPTS = {
    "valid": VALID, "noisy": NOISY,
    "invalid": "import sys\nsys.stdin.read()\nprint('not json at all')\n",
    "array": "import sys\nsys.stdin.read()\nprint('[1, 2]')\n",
    "oversized": "import sys\nsys.stdin.read()\nprint('{' + 'x' * 30_000)\n",
    "timeout": "import sys, time\nsys.stdin.read()\ntime.sleep(30)\n",
    "exit": "import sys\nsys.stdin.read()\nsys.exit(3)\n",
    "rejected": VALID.replace("print(json.dumps(", "p = ").replace("good_proposal(env[\"packet\"])))", "good_proposal(env['packet'])\n"
                                                                                                  "p['claims'][0]['slice_ids'] = ['slc_' + '0' * 64]\nprint(json.dumps(p))"),
    "flood": "import sys, time\nsys.stdout.write('y' * 2_000_000); sys.stdout.flush(); time.sleep(30)\n",
    "forbidden": "import sys\nsys.exit(99)\n",
}


@pytest.fixture(scope="module")
def scripts(tmp_path_factory: pytest.TempPathFactory) -> dict[str, list[str]]:
    base = tmp_path_factory.mktemp("fw")
    out = {}
    for name, body in SCRIPTS.items():
        (base / f"{name}.py").write_text(body, encoding="utf-8")
        out[name] = [PY, str(base / f"{name}.py")]
    return out


def routes(sha: str = SHA1, files: dict | None = None, **over) -> dict:
    r = catalog_routes(sha)
    for key in REPOS:
        r.update(repo_routes(key, sha, over.get(key, files or {"README.md": f"# {key}\n".encode()})))
    return r


def queue(root: Path) -> dict:
    return json.loads((root / workers.QUEUE_FILE).read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def corpus(tmp_path_factory: pytest.TempPathFactory) -> Path:
    root = tmp_path_factory.mktemp("c")
    res = collect.snapshot(root, "Org-A/Alpha", 20, 50_000, paths=["src/agent.py"], transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    assert res["files_stored"] == 4
    return root


@pytest.fixture
def clone(corpus: Path, tmp_path: Path) -> Path:
    shutil.copytree(corpus, tmp_path / "c")
    return tmp_path / "c"


# ---------------------------------------------------------------- maintain

def test_maintain_is_bounded_fair_resumable_and_names_needs_distillation(tmp_path: Path) -> None:
    limits = workers.Limits(max_repos=2, **FAST)
    t = FakeTransport(routes())
    first = workers.maintain(tmp_path, limits, transport=t)
    assert first["catalog"]["processed"] == 9 and first["status"] == "needs-distillation"
    assert [s["repo"] for s in first["snapshots"]] == ["org-a/alpha", "orgb/bravo"] and first["stopped"] is None
    assert first["needs_distillation"] == ["org-a/alpha", "orgb/bravo"] and first["timing"]["stages"].keys() == {"catalog", "snapshots"}
    second = workers.maintain(tmp_path, limits, transport=t)
    third = workers.maintain(tmp_path, limits, transport=t)
    assert [s["repo"] for s in second["snapshots"]] == ["orgc/charlie", "orge/echo"], "cursor resumes past the first batch"
    assert [s["repo"] for s in third["snapshots"]] == ["orgg/golf", "org-a/alpha"], "queue wraps around fairly"
    assert third["snapshots"][1]["reused"] is True and second["catalog"]["processed"] == 0
    assert queue(tmp_path)["cursor"] == "org-a/alpha" and len(queue(tmp_path)["runs"]) == 3
    assert queue(tmp_path)["repos"]["orgb/bravo"] == {**queue(tmp_path)["repos"]["orgb/bravo"], "failures": 0, "last_outcome": "snapshotted"}
    # Quiescent world: everything reused, the catalog record is byte-identical, still explicitly needs distillation.
    before = repos_bytes(tmp_path)
    again = workers.maintain(tmp_path, workers.Limits(max_repos=10, **FAST), transport=t)
    assert all(s["reused"] for s in again["snapshots"]) and repos_bytes(tmp_path) == before
    assert again["needs_distillation"] == sorted(REPOS) and again["budget"]["requests"] < 40
    assert not (tmp_path / core.LOCK_FILE).exists() and not (tmp_path / workers.LEASE_FILE).exists()


def test_failing_first_repository_does_not_block_others_and_is_parked_then_retried(tmp_path: Path) -> None:
    broken = routes()
    broken[f"https://{collect.API_HOST}/repos/org-a/alpha"] = collect.Response(404, b"{}")
    limits = workers.Limits(max_repos=2, max_failures=2, **FAST)
    first = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))
    assert [f["repo"] for f in first["failures"]] == ["org-a/alpha"] and first["failures"][0]["error"] == "FetchFailed"
    assert first["attempted"] == ["org-a/alpha", "orgb/bravo"], "max_repos bounds attempts, failures included"
    assert [s["repo"] for s in first["snapshots"]] == ["orgb/bravo"], "a failing head does not stall the batch"
    assert core.load_repos(tmp_path)["org-a/alpha"]["status"] == "blocked" and queue(tmp_path)["cursor"] == "orgb/bravo"
    second = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))
    assert [s["repo"] for s in second["snapshots"]] == ["orgc/charlie", "orge/echo"], "the next run starts after the cursor"
    third = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))  # wraps: golf, alpha(fail again)
    assert third["attempted"] == ["orgg/golf", "org-a/alpha"] and queue(tmp_path)["repos"]["org-a/alpha"]["failures"] == 2
    fourth = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))
    fifth = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))
    assert fourth["attempted"] == ["orgb/bravo", "orgc/charlie"] and fifth["attempted"] == ["orge/echo", "orgg/golf"]
    sixth = workers.maintain(tmp_path, limits, transport=FakeTransport(broken))
    assert sixth["parked"] == ["org-a/alpha"] and sixth["attempted"] == ["orgb/bravo", "orgc/charlie"]
    assert sixth["failures"] == [], "a parked repository is not retried forever"
    fixed = workers.maintain(tmp_path, workers.Limits(max_repos=3, max_failures=2, **FAST), transport=FakeTransport(routes()), retry_parked=True)
    assert [s["repo"] for s in fixed["snapshots"]] == ["orge/echo", "orgg/golf", "org-a/alpha"]
    assert queue(tmp_path)["repos"]["org-a/alpha"]["failures"] == 0 and core.load_repos(tmp_path)["org-a/alpha"]["status"] == "snapshotted"
    receipts = json.dumps(queue(tmp_path))
    assert "Authorization" not in receipts and "ghp_" not in receipts


def test_maintain_preserves_explicit_selection_and_reports_removed_path(corpus: Path, tmp_path: Path) -> None:
    root = tmp_path / "c"
    shutil.copytree(corpus, root)
    limits = workers.Limits(max_files=2, max_bytes=100, catalog_entries=0, **FAST)  # smaller than the prior capture
    kept = workers.maintain(root, limits, transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    snap = kept["snapshots"][0]
    assert snap["reused"] is False and snap["explicit_paths"] == ["src/agent.py"] and snap["files_stored"] == 2
    meta = json.loads((root / core.load_repos(root)["org-a/alpha"]["latest_snapshot"]["snapshot"]).read_text(encoding="utf-8"))
    assert [f["path"] for f in meta["files"]] == ["src/agent.py", "empty.md"] and meta["budgets"]["max_bytes"] == 100, "current ceilings honored"
    assert {o["path"]: o["reason"] for o in meta["omitted"]}["README.md"] == "byte-budget", "documentation omission stays explicit"
    gone = {k: v for k, v in FILES.items() if k != "src/agent.py"}
    removed = workers.maintain(root, limits, transport=FakeTransport(repo_routes("org-a/alpha", SHA2, gone)))
    assert removed["snapshots"] == [] and removed["failures"][0]["error"] == "InvalidPath"
    assert "src/agent.py" in removed["failures"][0]["message"], "an upstream-removed explicit path is a reported gap"
    record = core.load_repos(root)["org-a/alpha"]
    assert record["latest_snapshot"]["commit"] == SHA1 and record["freshness"] == "refresh-failed"


def test_shrinking_budget_or_growing_code_keeps_prior_snapshot_and_reports_the_gap(corpus: Path, tmp_path: Path) -> None:
    root = tmp_path / "c"
    shutil.copytree(corpus, root)
    before = core.load_repos(root)["org-a/alpha"]["latest_snapshot"]
    shrunk = workers.maintain(root, workers.Limits(max_files=2, max_bytes=40, catalog_entries=0, **FAST),
                              transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    assert shrunk["snapshots"] == [] and shrunk["failures"][0]["error"] == "BudgetGap" and "src/agent.py" in shrunk["failures"][0]["message"]
    grown = {**FILES, "src/agent.py": FILES["src/agent.py"] + b"# " + b"x" * 400 + b"\n"}
    bigger = workers.maintain(root, workers.Limits(max_files=4, max_bytes=300, catalog_entries=0, **FAST),
                              transport=FakeTransport(repo_routes("org-a/alpha", SHA2, grown)))
    assert bigger["snapshots"] == [] and bigger["failures"][0]["error"] == "BudgetGap" and "byte-budget" in bigger["failures"][0]["message"]
    record = core.load_repos(root)["org-a/alpha"]
    assert record["latest_snapshot"] == before and record["freshness"] == "refresh-failed", "old pointer retained, not a docs-only capture"
    assert not (root / collect.SOURCE_DIR / "org-a" / "alpha" / SHA2).exists()
    assert record["last_error"]["code"] == "BudgetGap"


def test_limits_reject_bool_as_int_and_allow_zero_only_for_stop_controls() -> None:
    for bad in ({"max_files": True}, {"net_seconds": 0}, {"max_bytes": 0}, {"build": 1}, {"max_files": 2.0}, {"worker_seconds": "3"}):
        with pytest.raises(workers.InvalidLimits):
            workers.Limits(**bad)
    ok = workers.Limits(max_seconds=0, max_repos=0, catalog_entries=0, max_stderr_bytes=0)
    assert ok.max_seconds == 0 and workers.Limits(net_seconds=5).net_seconds == 5


def test_worker_deadline_defers_apply_and_build_but_keeps_the_saved_proposal(clone: Path, scripts: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    limits = workers.Limits(**FAST)
    real_stage = workers._Clock.stage

    def slow_model(self, name, fn, *args, **kwargs):
        if name == "model":
            self.started -= limits.max_seconds + 1  # the model stage consumed the whole run budget
        return real_stage(self, name, fn, *args, **kwargs)

    monkeypatch.setattr(workers._Clock, "stage", slow_model)
    res = workers.run_worker(clone, scripts["valid"], limits)
    monkeypatch.undo()
    assert res["outcome"] == "deferred" and res["deferred_before"] == "apply" and res["pending"]["stage"] == "pending-apply"
    job = json.loads((clone / workers.JOB_DIR / "org-a__alpha.json").read_text(encoding="utf-8"))
    assert (clone / job["proposal"]).exists() and not wiki._rows(clone / "wiki", "operations")
    assert core.load_repos(clone)["org-a/alpha"]["status"] == "snapshotted"
    zero = workers.run_worker(clone, scripts["forbidden"], workers.Limits(max_seconds=0), repo="org-a/alpha")
    assert zero["outcome"] == "deferred" and zero["deferred_before"] == "recover", "no recovery apply starts past the deadline"
    done = workers.run_worker(clone, scripts["forbidden"], limits, repo="org-a/alpha")
    assert done["outcome"] == "recovered" and done["apply"]["claims"] == 4 and done["build"]["known"] == 1
    assert core.load_repos(clone)["org-a/alpha"]["status"] == "distilled"


def test_maintain_aggregate_network_budget_stops_the_run_with_receipts(tmp_path: Path) -> None:
    res = workers.maintain(tmp_path, workers.Limits(net_bytes=600, **FAST), transport=FakeTransport(routes()))
    assert res["stopped"] == "network-budget" and {f["error"] for f in res["failures"]} == {"BudgetExceeded"}
    assert res["budget"]["max_bytes"] == 600 and "byte-budget" in res["failures"][0]["message"] and res["snapshots"] == []
    assert res["status"] == "degraded" and res["needs_distillation"] == [], "a budget failure is explicit even when no leads landed"


def test_lease_refuses_live_owner_reclaims_dead_owner_and_surfaces_stale_writer_lock(tmp_path: Path) -> None:
    lease = tmp_path / workers.LEASE_FILE
    lease.parent.mkdir(parents=True)
    limits = workers.Limits(catalog_entries=0, **FAST)
    lease.write_bytes(core.dump_json({"pid": os.getpid(), "kind": "worker", "started": "x", "host": workers._host()}))
    with pytest.raises(workers.LeaseHeld, match=f"pid {os.getpid()}"):
        workers.maintain(tmp_path, limits)
    lease.write_bytes(core.dump_json({"pid": _dead_pid(), "kind": "worker", "started": "x", "host": workers._host()}))
    res = workers.maintain(tmp_path, limits)
    assert res["lease_reclaimed"] is True and not lease.exists()
    lease.write_bytes(core.dump_json({"pid": 4, "kind": "maintain", "started": "x", "host": "elsewhere"}))
    with pytest.raises(workers.LeaseHeld):
        workers.maintain(tmp_path, limits)
    lease.unlink()
    (tmp_path / core.LOCK_FILE).write_bytes(b"pid=0\n")
    with pytest.raises(core.LockHeld):
        workers.maintain(tmp_path, limits)
    assert (tmp_path / core.LOCK_FILE).exists() and not lease.exists(), "a foreign writer lock is never deleted"


def _dead_pid() -> int:
    with subprocess.Popen([PY, "-c", "pass"]) as proc:
        proc.wait()
    return proc.pid


# ---------------------------------------------------------------- real fake processes

def test_run_process_bounds_time_and_output_and_never_deadlocks(scripts: dict) -> None:
    payload = b'{"packet": null, "pad": "' + b"p" * 300_000 + b'"}'
    noisy = workers.run_process([PY, "-c", "import sys\nsys.stderr.write('n' * 300000); sys.stderr.flush()\nd = sys.stdin.read()\nprint(len(d))"],
                                payload, 20.0, 10_000, 8_192)
    assert noisy["returncode"] == 0 and noisy["stdout"].strip() == str(len(payload)).encode()
    assert noisy["stderr_over"] is True and noisy["stderr_bytes"] == 8_192, "stderr drained and bounded even before stdin is read"
    t0 = time.monotonic()
    flood = workers.run_process(scripts["flood"], b"{}", 20.0, 50_000, 1_000)
    assert flood["stdout_over"] is True and len(flood["stdout"]) == 50_000 and time.monotonic() - t0 < 15
    t0 = time.monotonic()
    slow = workers.run_process(scripts["timeout"], b"{}", 1.0, 1_000, 1_000)
    assert slow["timed_out"] is True and time.monotonic() - t0 < 10


def test_worker_argv_is_validated_and_never_derived_from_data() -> None:
    for bad in (None, [], ["ok", ""], "python fake.py", [1]):
        with pytest.raises(workers.WorkerFailed):
            workers.check_argv(bad)
    assert workers.check_argv(["x", "--flag"]) == ["x", "--flag"]


# ---------------------------------------------------------------- model worker over the real kernel

def test_worker_valid_proposal_applies_builds_and_repeat_is_noop(clone: Path, scripts: dict) -> None:
    limits = workers.Limits(**FAST)
    res = workers.run_worker(clone, scripts["valid"], limits)
    assert res["outcome"] == "applied" and res["apply"]["claims"] == 4 and res["apply"]["changed"] is True
    assert res["build"]["known"] == 1 and res["model"]["returncode"] == 0 and "stdout" not in res["model"]
    assert set(res["timing"]["stages"]) == {"prepare", "model", "apply", "build"} and res["model"]["drain_complete"] is True
    assert res["timing"]["stage_timeouts"]["kernel_call_seconds"] == wiki.KERNEL_TIMEOUT and "cooperative" in res["timing"]["deadline"]
    assert (clone / res["proposal"]).exists() and (clone / res["envelope"]).exists() and not (clone / workers.JOB_DIR / "org-a__alpha.json").exists()
    envelope = json.loads((clone / res["envelope"]).read_text(encoding="utf-8"))
    assert envelope["coverage"]["selection"]["stored"] == 4 and envelope["coverage"]["repository"]["tree_truncated"] is False
    assert envelope["output_contract"]["schema"] == wiki.PROPOSAL_JSON_SCHEMA
    rec = core.load_repos(clone)["org-a/alpha"]
    assert rec["status"] == "distilled" and rec["freshness"] == "current"
    receipt = json.dumps(queue(clone))
    assert scripts["valid"][1] not in receipt and res["command_digest"] in receipt, "receipts carry a digest, not argv"
    again = workers.run_worker(clone, scripts["forbidden"], limits)
    assert again["outcome"] == "no-op", "already-distilled versions are skipped without a model call"
    explicit = workers.run_worker(clone, scripts["forbidden"], limits, repo="org-a/alpha")
    assert explicit["outcome"] == "skipped" and explicit["reason"] == "already-distilled"
    assert [o["id"] for o in wiki._rows(clone / "wiki", "operations")] == [res["apply"]["operation_id"]]


@pytest.mark.parametrize("name, outcome", [("invalid", "model-invalid-json"), ("array", "model-invalid-json"),
                                           ("oversized", "model-oversized-output"), ("timeout", "model-timeout"),
                                           ("exit", "model-exit-3"), ("rejected", "model-rejected")])
def test_worker_failures_never_complete_work_and_leave_receipts(clone: Path, scripts: dict, name: str, outcome: str) -> None:
    limits = workers.Limits(net_seconds=30.0, max_seconds=60.0, worker_seconds=2.0, max_proposal_bytes=20_000)
    with pytest.raises(workers.WorkerFailed):
        workers.run_worker(clone, scripts[name], limits)
    job = json.loads((clone / workers.JOB_DIR / "org-a__alpha.json").read_text(encoding="utf-8"))
    assert job["stage"] == "failed" and job["model"]["stdout_bytes"] <= 20_001 and "stderr" not in json.dumps(job).replace("stderr_", "")
    run = queue(clone)["runs"][-1]
    assert run["outcome"] == outcome and run["failure"]["error"] == "WorkerFailed" and run["timing"]["stages"]["model"] < 10
    rec = core.load_repos(clone)["org-a/alpha"]
    assert rec["status"] == "snapshotted" and rec.get("indexed_snapshot_id") is None and not wiki._rows(clone / "wiki", "claims")
    assert queue(clone)["repos"]["org-a/alpha"]["failures"] == 1


def test_worker_recovers_uncertain_apply_from_stored_proposal_without_second_model_call(clone: Path, scripts: dict, monkeypatch: pytest.MonkeyPatch) -> None:
    limits = workers.Limits(build=False, **FAST)

    def interrupted(*_a, **_k):
        raise wiki.WikiError("simulated interruption after the kernel commit")

    monkeypatch.setattr(wiki, "_finish", interrupted)
    with pytest.raises(wiki.WikiError):
        workers.run_worker(clone, scripts["valid"], limits)
    monkeypatch.undo()
    job = json.loads((clone / workers.JOB_DIR / "org-a__alpha.json").read_text(encoding="utf-8"))
    assert job["stage"] == "applying" and (clone / job["proposal"]).exists()
    ops = wiki._rows(clone / "wiki", "operations")
    assert len(ops) == 1 and ops[0]["state"] == "applied" and core.load_repos(clone)["org-a/alpha"]["status"] == "snapshotted"
    res = workers.run_worker(clone, scripts["forbidden"], limits, repo="org-a/alpha")
    assert res["outcome"] == "recovered" and res["apply"]["reconciled"] is True and res["apply"]["claims"] == 4
    assert core.load_repos(clone)["org-a/alpha"]["status"] == "distilled" and len(wiki._rows(clone / "wiki", "operations")) == 1
    assert not (clone / workers.JOB_DIR / "org-a__alpha.json").exists()


def test_cli_manual_envelope_then_apply_and_time_budget_stop(clone: Path, capsys: pytest.CaptureFixture) -> None:
    assert cli.main(["--root", str(clone), "worker", "--repo", "org-a/alpha", "--max-seconds", "60"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["outcome"] == "manual" and out["command_digest"] is None and "gemini" in out["next"]
    envelope = json.loads((clone / out["envelope"]).read_text(encoding="utf-8"))
    assert envelope["coverage"]["explicit_paths"] == ["src/agent.py"] and [f["path"] for f in envelope["coverage"]["files"]][0] == "README.md"
    proposal = clone / "proposals" / "manual.json"
    proposal.write_bytes(core.dump_json(good_proposal(envelope["packet"])))
    assert cli.main(["--root", str(clone), "apply", str(clone / out["packet"]), str(proposal)]) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "distilled"
    assert cli.main(["--root", str(clone), "maintain", "--catalog-entries", "0", "--max-seconds", "0"]) == 0
    stopped = json.loads(capsys.readouterr().out)
    assert stopped["stopped"] == "time-budget" and stopped["snapshots"] == [] and stopped["needs_distillation"] == []
    assert cli.main(["--root", str(clone), "worker", "--repo", "nobody/none", "--", PY, "-c", "pass"]) == workers.WorkerFailed.code
