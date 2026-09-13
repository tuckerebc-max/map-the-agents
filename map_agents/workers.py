"""Resumable maintenance and the optional bounded model worker.

maintain() refreshes catalog leads and repository snapshots under aggregate budgets with a fair, persistent
queue; it never calls a model and reports repositories that still need distillation. run_worker() prepares
one real kernel packet, hands a JSON envelope to an explicitly configured trusted argv (shell=False, finite
time, bounded stdout/stderr), validates the single JSON proposal it returns, and applies it through the
kernel. Source text is evidence data only: no command, argument or path is ever derived from it.

Timing is a COOPERATIVE whole-run deadline: no stage starts once `max_seconds` has elapsed, network and
model waits are clamped to the remaining time, and a stage already running finishes under its own finite
timeout (kernel calls: wiki.KERNEL_TIMEOUT each). There is no hard whole-run kill; a deployment ceiling
belongs to the job runner around this process.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import threading
import time
from dataclasses import asdict, dataclass, fields
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

from . import collect, core, maps, wiki

QUEUE_FILE, LEASE_FILE, JOB_DIR = "state/maintenance.json", "state/leases/orchestrator.json", "state/workers"
QUEUE_SCHEMA, ENVELOPE_SCHEMA, JOB_SCHEMA = "map-agents.maintenance/1", "map-agents.worker-envelope/1", "map-agents.worker-job/1"
MAX_RUNS_KEPT, MAX_MESSAGE, DRAIN_JOIN_SECONDS = 20, 300, 10.0
MANUAL_MODELS = ("gemini", "codex-5.3", "glm-flash")  # served by the same envelope/prepare/apply path; no SDK here
ZERO_OK = {"max_repos", "catalog_entries", "max_stderr_bytes", "max_seconds"}  # zero = stop/skip control
KERNEL_CALLS = {"prepare": 3, "apply": 1}  # init-if-needed + inventory + prepare; apply


class LeaseHeld(core.WorkbenchError):
    code = 16


class WorkerFailed(core.WorkbenchError):
    """The configured worker produced no usable proposal; nothing was applied."""

    code = 17


class InvalidLimits(core.WorkbenchError):
    code = 18


@dataclass
class Limits:
    """Every bound one maintenance or worker run may consume. Validated finite on construction."""

    max_repos: int = 5  # repositories ATTEMPTED per maintain run (successes and failures); 0 skips snapshots
    max_files: int = 12  # per-snapshot selected files (current ceiling; prior explicit paths must fit)
    max_bytes: int = 400_000  # per-snapshot selected bytes
    catalog_entries: int = 50  # pending feed entries per run; 0 skips the catalog stage
    net_bytes: int = 12_000_000  # aggregate network bytes for the whole run
    net_seconds: float = 120.0  # aggregate network time, clamped to the remaining run time
    net_requests: int = 120
    max_seconds: float = 600.0  # cooperative whole-run deadline; 0 stops before any stage
    max_failures: int = 3  # consecutive failures before a repository is parked
    worker_seconds: float = 180.0  # model subprocess wall clock, clamped to the remaining run time
    max_envelope_bytes: int = wiki.BOUNDS["max_packet_bytes"] + 200_000
    max_proposal_bytes: int = wiki.BOUNDS["max_proposal_bytes"]  # model stdout bound
    max_stderr_bytes: int = 65_536  # stderr retained for counting only
    build: bool = True  # rebuild map/ after a successful apply

    def __post_init__(self) -> None:
        for f in fields(self):
            value = getattr(self, f.name)
            if f.name == "build":
                if not isinstance(value, bool):
                    raise InvalidLimits("build must be a bool")
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise InvalidLimits(f"{f.name} must be a number, got {type(value).__name__}")
            if f.type == "int" and not isinstance(value, int):
                raise InvalidLimits(f"{f.name} must be an integer")
            if not math.isfinite(value) or value < 0 or (value == 0 and f.name not in ZERO_OK):
                raise InvalidLimits(f"{f.name} must be a finite {'non-negative' if f.name in ZERO_OK else 'positive'} number")

    def stage_timeouts(self) -> dict:
        """Finite per-stage bounds that apply even after the cooperative deadline passes mid-stage."""
        return {"kernel_call_seconds": wiki.KERNEL_TIMEOUT, "kernel_calls": dict(KERNEL_CALLS),
                "model_seconds": self.worker_seconds, "network_seconds": self.net_seconds,
                "build": "local file work, bounded by corpus size, not by time"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _host() -> str:
    return os.uname().nodename if hasattr(os, "uname") else os.environ.get("COMPUTERNAME", "")


def _pid_alive(pid: int) -> bool:
    if os.name == "nt":
        import ctypes

        k = ctypes.windll.kernel32  # type: ignore[attr-defined]
        handle = k.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION; never a kill
        if not handle:
            return k.GetLastError() == 5  # access denied: exists, owned by someone else
        try:
            code = ctypes.c_ulong()
            return bool(k.GetExitCodeProcess(handle, ctypes.byref(code))) and code.value == 259
        finally:
            k.CloseHandle(handle)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


class Lease:
    """Orchestration ownership for maintain/worker batches, separate from the non-reentrant core.writer_lock.

    A dead owner's lease on this host is reclaimed; a possibly live owner yields a precise recoverable error.
    """

    def __init__(self, root: Path, kind: str) -> None:
        self.path, self.kind, self.reclaimed = Path(root) / LEASE_FILE, kind, False

    def __enter__(self) -> "Lease":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        for attempt in (0, 1):
            try:
                fd = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
            except FileExistsError:
                held = collect._load_json(self.path) or {}
                who = f"lease {self.path.name} held by {held.get('kind')} pid {held.get('pid')} since {held.get('started')}"
                if attempt or held.get("host") != _host() or not isinstance(held.get("pid"), int) or _pid_alive(held["pid"]):
                    raise LeaseHeld(f"{who}; owner may be active. Stop it or remove the lease by hand.")
                self.path.unlink()
                self.reclaimed = True
                continue
            os.write(fd, core.dump_json({"pid": os.getpid(), "kind": self.kind, "started": _now(), "host": _host()}))
            os.close(fd)
            return self
        raise LeaseHeld(f"lease {self.path.name} could not be acquired")

    def __exit__(self, *_exc: object) -> None:
        self.path.unlink(missing_ok=True)


def _load_queue(root: Path) -> dict:
    queue = collect._load_json(Path(root) / QUEUE_FILE) or {}
    return {"schema_version": QUEUE_SCHEMA, "cursor": queue.get("cursor"), "worker_cursor": queue.get("worker_cursor"),
            "repos": queue.get("repos") if isinstance(queue.get("repos"), dict) else {}, "runs": list(queue.get("runs") or [])}


def _save_queue(root: Path, queue: dict, run: dict) -> None:
    queue["runs"] = (queue["runs"] + [run])[-MAX_RUNS_KEPT:]
    core.write_if_changed(Path(root) / QUEUE_FILE, core.dump_json(queue))


def _fair_order(keys: list[str], cursor: str | None) -> list[str]:
    keys = sorted(keys)
    return [k for k in keys if cursor is None or k > cursor] + [k for k in keys if cursor is not None and k <= cursor]


def _failure(exc: Exception) -> dict:
    """Receipt-safe failure: class, stable code and our own bounded message; foreign exceptions keep only their class."""
    message = str(exc) if isinstance(exc, core.WorkbenchError) else f"{type(exc).__name__} (detail withheld)"
    return {"error": type(exc).__name__, "code": getattr(exc, "code", 1), "message": message[:MAX_MESSAGE]}


def _note(queue: dict, key: str, outcome: str, failure: dict | None) -> None:
    entry = queue["repos"].setdefault(key, {"failures": 0})
    entry.update({"last_outcome": outcome, "last_at": _now()})
    entry["failures"] = entry["failures"] + 1 if failure else 0
    if failure:
        entry["last_error"] = failure
    else:
        entry.pop("last_error", None)


def _needs_distillation(record: dict) -> bool:
    snap = record.get("latest_snapshot")
    return isinstance(snap, dict) and record.get("indexed_snapshot_id") != snap.get("snapshot_id")


def _snapshot_meta(root: Path, record: dict) -> dict:
    snap = record.get("latest_snapshot")
    return (collect._load_json(Path(root) / snap["snapshot"]) or {}) if isinstance(snap, dict) else {}


class _Clock:
    """Cooperative deadline: stages ask `remaining()` before starting and measure themselves."""

    def __init__(self, limits: Limits) -> None:
        self.limits, self.started, self.stages = limits, time.monotonic(), {}

    def remaining(self) -> float:
        return self.limits.max_seconds - (time.monotonic() - self.started)

    def expired(self) -> bool:
        return self.remaining() <= 0

    def stage(self, name: str, fn, *args, **kwargs):
        t0 = time.monotonic()
        try:
            return fn(*args, **kwargs)
        finally:
            self.stages[name] = round(self.stages.get(name, 0.0) + time.monotonic() - t0, 3)

    def summary(self) -> dict:
        return {"elapsed": round(time.monotonic() - self.started, 3), "max_seconds": self.limits.max_seconds,
                "deadline": "cooperative: no stage starts after max_seconds; a running stage finishes under its own timeout",
                "stages": dict(self.stages), "stage_timeouts": self.limits.stage_timeouts()}


def maintain(root: Path, limits: Limits | None = None, transport=None, retry_parked: bool = False) -> dict:
    """Bounded, resumable refresh without a model: catalog leads, fair snapshot queue, explicit needs-distillation."""
    root, limits = Path(root), limits or Limits()
    clock = _Clock(limits)
    budget = collect.Budget(max_bytes=limits.net_bytes, max_seconds=min(limits.net_seconds, max(clock.remaining(), 0.0)),
                            max_requests=limits.net_requests)
    run: dict = {"kind": "maintain", "started": _now(), "catalog": None, "attempted": [], "snapshots": [], "failures": [],
                 "stopped": None, "parked": []}
    with Lease(root, "maintain") as lease:
        with core.writer_lock(root):
            core.init_locked(root)
        queue = _load_queue(root)
        if clock.expired():
            run["stopped"] = "time-budget"
        elif limits.catalog_entries > 0:
            try:
                res = clock.stage("catalog", collect.catalog, root, limits.catalog_entries, transport=transport, budget=budget)
                run["catalog"] = {k: res[k] for k in ("commit", "processed", "backlog", "version_changed", "changed", "slugs")}
            except core.WorkbenchError as exc:
                run["failures"].append({"stage": "catalog", **_failure(exc)})
                if isinstance(exc, collect.BudgetExceeded):
                    run["stopped"] = "network-budget"  # the aggregate allowance is shared with the snapshot stage
        repos = core.load_repos(root)
        for key in _fair_order(list(repos), queue["cursor"]):
            if len(run["attempted"]) >= limits.max_repos or run["stopped"]:
                break
            if clock.expired():
                run["stopped"] = "time-budget"
                break
            if queue["repos"].get(key, {}).get("failures", 0) >= limits.max_failures and not retry_parked:
                run["parked"].append(key)
                continue
            explicit = [p for p in _snapshot_meta(root, repos[key]).get("explicit_paths", []) if isinstance(p, str)]
            queue["cursor"] = key  # persisted whatever happens next, so a failure never starves the next run
            core.atomic_write_bytes(root / QUEUE_FILE, core.dump_json(queue))
            run["attempted"].append(key)
            try:
                res = clock.stage("snapshots", collect.snapshot, root, key, limits.max_files, limits.max_bytes, paths=explicit,
                                  transport=transport, budget=budget, strict_explicit=True)
            except collect.BudgetExceeded as exc:
                run["failures"].append({"stage": "snapshot", "repo": key, **_failure(exc)})
                _note(queue, key, "budget-exceeded", None)  # the run's budget, not the repository's fault
                run["stopped"] = "network-budget"
                break
            except (core.WorkbenchError, OSError) as exc:
                failure = _failure(exc)
                run["failures"].append({"stage": "snapshot", "repo": key, **failure})
                _note(queue, key, "snapshot-failed", failure)
                continue
            run["snapshots"].append({"repo": key, "commit": res["commit"], "snapshot_id": res["snapshot_id"], "reused": res["reused"],
                                     "freshness": res["freshness"], "files_stored": res["files_stored"],
                                     "omitted_count": res["omitted_count"], "explicit_paths": explicit})
            _note(queue, key, "reused" if res["reused"] else "snapshotted", None)
        repos = core.load_repos(root)
        needs = sorted(k for k, r in repos.items() if _needs_distillation(r))
        run.update({"finished": _now(), "needs_distillation": needs, "timing": clock.summary(), "lease_reclaimed": lease.reclaimed})
        _save_queue(root, queue, run)
    return {"root": str(root), "status": "degraded" if run["failures"] else "stopped" if run["stopped"] else "needs-distillation" if needs else "quiescent", **run, "budget": budget.summary(),
            "queue": {"cursor": queue["cursor"], "repos_known": len(repos)}, "limits": asdict(limits)}


# --------------------------------------------------------------------------- model worker

def check_argv(command_argv: object) -> list[str]:
    """The worker command is trusted operator configuration: a non-empty list of strings, nothing else."""
    if not isinstance(command_argv, list) or not command_argv or any(not isinstance(a, str) or not a for a in command_argv):
        raise WorkerFailed("command_argv must be a non-empty list of non-empty strings")
    return list(command_argv)


def _command_digest(argv: list[str]) -> str:
    return sha256(core.dump_json(argv)).hexdigest()[:16]  # receipts identify the configuration without persisting it


def envelope(root: Path, packet: dict) -> dict:
    """What a small worker receives: the sealed packet plus honest coverage of the bounded evidence."""
    root = Path(root)
    meta = _snapshot_meta(root, core.load_repos(root).get(packet["repo"], {}))
    return {
        "schema_version": ENVELOPE_SCHEMA, "task": "dossier-proposal", "packet": packet,
        "coverage": {"files": [{"path": f["path"], "lines": f["lines"], "size": f["size"]} for f in meta.get("files", [])],
                     "explicit_paths": meta.get("explicit_paths", []), "selection": meta.get("selection"),
                     "repository": meta.get("repository"), "omitted": meta.get("omitted", []),
                     "omitted_count": meta.get("omitted_count"), "omitted_slices": packet.get("omitted_slices", 0),
                     "notice": "Evidence is a bounded selection of one commit. Facets without support stay unknown."},
        "output_contract": {"format": "exactly one JSON object on stdout, nothing else", "schema": packet["proposal_schema"],
                            "manual_models": list(MANUAL_MODELS)},
    }


def _drain(stream, limit: int, out: dict, key: str, on_overflow) -> None:
    buf, over, fd = bytearray(), False, stream.fileno()
    while True:
        chunk = os.read(fd, 65536)
        if not chunk:
            break
        if not over:
            buf += chunk
            if len(buf) > limit:
                over = True
                del buf[limit:]
                on_overflow()
    out[key], out[key + "_over"] = bytes(buf), over


def run_process(argv: list[str], payload: bytes, timeout: float, max_stdout: int, max_stderr: int) -> dict:
    """Trusted argv, shell=False, stdin fed and both pipes drained on threads (no deadlock, no unbounded buffering).

    Bounds: `timeout` for the direct child (killed on expiry), stdout overflow kills the child, stderr overflow
    is discarded. Pipe drain waits at most DRAIN_JOIN_SECONDS in total after exit; a grandchild that keeps a
    pipe open leaves `drain_complete` false and is not killed (no unrelated process is ever signalled).
    OSError from launch propagates to the caller.
    """
    proc = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    out: dict = {}

    def feed() -> None:
        try:
            proc.stdin.write(payload)
            proc.stdin.close()
        except (BrokenPipeError, OSError):
            pass

    threads = [threading.Thread(target=feed, daemon=True),
               threading.Thread(target=_drain, args=(proc.stdout, max_stdout, out, "stdout", proc.kill), daemon=True),
               threading.Thread(target=_drain, args=(proc.stderr, max_stderr, out, "stderr", lambda: None), daemon=True)]
    for t in threads:
        t.start()
    started, timed_out = time.monotonic(), False
    try:
        proc.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        proc.kill()
        proc.wait()
    join_deadline = time.monotonic() + DRAIN_JOIN_SECONDS
    for t in threads:
        t.join(timeout=max(0.0, join_deadline - time.monotonic()))
    return {"returncode": proc.returncode, "timed_out": timed_out, "seconds": round(time.monotonic() - started, 3),
            "timeout": timeout, "drain_complete": not any(t.is_alive() for t in threads),
            "stdout": out.get("stdout", b""), "stdout_over": out.get("stdout_over", False),
            "stderr_bytes": len(out.get("stderr", b"")), "stderr_over": out.get("stderr_over", False)}


def _job_path(root: Path, key: str) -> Path:
    return Path(root) / JOB_DIR / (key.replace("/", "__") + ".json")


def _pick_repo(repos: dict, queue: dict, limits: Limits, retry_parked: bool) -> str | None:
    for key in _fair_order([k for k, r in repos.items() if _needs_distillation(r)], queue["worker_cursor"]):
        if queue["repos"].get(key, {}).get("failures", 0) < limits.max_failures or retry_parked:
            return key
    return None


def run_worker(root: Path, command_argv: list[str] | None, limits: Limits | None = None, repo: str | None = None,
               retry_parked: bool = False) -> dict:
    """Distill one repository: recover -> prepare -> envelope -> trusted worker process -> validate -> apply -> build.

    command_argv=None stops after the envelope (manual path for Gemini, Codex 5.3, GLM Flash or a person).
    Outcomes: applied | recovered | skipped | no-op | manual | deferred (time; saved state preserved) or raises
    WorkerFailed (model-* / failed) or a wiki error; every raise leaves a receipt and never marks work complete.
    """
    root, limits = Path(root), limits or Limits()
    argv = check_argv(command_argv) if command_argv is not None else None
    clock = _Clock(limits)
    run: dict = {"kind": "worker", "started": _now(), "repo": None, "stage": "select", "outcome": None, "failure": None,
                 "command_digest": _command_digest(argv) if argv else None}
    with Lease(root, "worker") as lease:
        with core.writer_lock(root):
            core.init_locked(root)
        queue, repos = _load_queue(root), core.load_repos(root)
        key = repo.lower() if repo else _pick_repo(repos, queue, limits, retry_parked)
        if key is None:
            run.update({"outcome": "no-op", "finished": _now(), "timing": clock.summary()})
            _save_queue(root, queue, run)
            return {"root": str(root), **run, "reason": "no repository needs distillation"}
        if key not in repos:
            raise WorkerFailed(f"unknown repository: {key}")
        run["repo"], queue["worker_cursor"] = key, key
        job_path = _job_path(root, key)
        try:
            result = _finish_job(root, key, repos[key], collect._load_json(job_path) or {}, job_path, argv, limits, clock, run)
            _note(queue, key, run["outcome"], None)
        except (core.WorkbenchError, OSError, subprocess.TimeoutExpired) as exc:
            failure = _failure(exc)
            run.update({"outcome": run["outcome"] or "failed", "failure": failure})
            _note(queue, key, run["outcome"], failure)
            run.update({"finished": _now(), "timing": clock.summary(), "lease_reclaimed": lease.reclaimed})
            _save_queue(root, queue, run)
            if isinstance(exc, core.WorkbenchError):
                raise
            raise WorkerFailed(f"worker stage {run['stage']} failed: {type(exc).__name__}") from None
        run.update({"finished": _now(), "timing": clock.summary(), "lease_reclaimed": lease.reclaimed})
        _save_queue(root, queue, run)
    return {"root": str(root), **run, **result, "limits": asdict(limits)}


def _deferred(run: dict, before: str, job: dict | None, extra: dict | None = None) -> dict:
    run.update({"outcome": "deferred", "deferred_before": before})
    return {"recovered": False, "pending": {k: job[k] for k in ("stage", "packet", "proposal", "operation_id") if job and k in job},
            **(extra or {})}


def _recover(root: Path, job: dict, clock: _Clock) -> dict | None:
    """A saved job with a stored proposal is replayed through wiki.apply first; the model is never re-run for it."""
    if job.get("stage") not in ("applying", "pending-apply"):
        return None
    try:
        return clock.stage("apply", wiki.apply, root, root / job["packet"], root / job["proposal"])
    except wiki.StalePacket:
        return None  # nothing of that job reached the kernel and the world moved on: prepare afresh


def _fail(job_path: Path, job: dict, run: dict, outcome: str, message: str) -> WorkerFailed:
    run["outcome"] = outcome
    core.atomic_write_bytes(job_path, core.dump_json({**job, "stage": "failed"}))
    return WorkerFailed(message)


def _finish_job(root: Path, key: str, record: dict, job: dict, job_path: Path, argv: list[str] | None, limits: Limits,
                clock: _Clock, run: dict) -> dict:
    if job.get("stage") in ("applying", "pending-apply") and clock.expired():
        return _deferred(run, "recover", job)
    recovered = _recover(root, job, clock)
    if recovered is not None:
        job_path.unlink(missing_ok=True)
        run.update({"stage": "applied", "outcome": "recovered"})
        return {"apply": recovered, "recovered": True, "build": _build(root, limits, clock)}
    if not _needs_distillation(record):
        run.update({"stage": "select", "outcome": "skipped"})
        return {"reason": "already-distilled", "snapshot_id": record["latest_snapshot"]["snapshot_id"], "recovered": False}
    if clock.expired():
        return _deferred(run, "prepare", None)
    run["stage"] = "prepare"
    prepared = clock.stage("prepare", wiki.prepare, root, key)
    packet = wiki.load_packet(root, root / prepared["packet"])
    env = core.dump_json(envelope(root, packet))
    if len(env) > limits.max_envelope_bytes:
        run["outcome"] = "envelope-oversized"
        raise WorkerFailed(f"envelope exceeds {limits.max_envelope_bytes} bytes; narrow the snapshot selection")
    env_path = root / wiki.PACKET_DIR / f"{packet['operation_id']}.envelope.json"
    core.atomic_write_bytes(env_path, env)
    job = {"schema_version": JOB_SCHEMA, "repo": key, "operation_id": packet["operation_id"], "packet": prepared["packet"],
           "envelope": env_path.relative_to(root).as_posix(), "snapshot_id": packet["snapshot_id"], "stage": "prepared",
           "command_digest": run["command_digest"], "started": run["started"]}
    core.atomic_write_bytes(job_path, core.dump_json(job))
    if argv is None:
        run.update({"stage": "prepared", "outcome": "manual"})
        return {"packet": prepared["packet"], "envelope": job["envelope"], "recovered": False,
                "next": f"feed the envelope to one of {list(MANUAL_MODELS)} by hand, then run apply PACKET PROPOSAL"}
    if clock.expired():
        return _deferred(run, "model", job, {"packet": prepared["packet"], "envelope": job["envelope"]})
    run["stage"] = "model"
    try:
        proc = clock.stage("model", run_process, argv, env, min(limits.worker_seconds, clock.remaining()),
                           limits.max_proposal_bytes, limits.max_stderr_bytes)
    except (OSError, ValueError) as exc:  # launch failure: missing executable, permissions, bad handle
        raise _fail(job_path, {**job, "launch_error": type(exc).__name__}, run, "failed",
                    f"worker could not be launched ({type(exc).__name__})") from None
    receipt = {k: proc[k] for k in ("returncode", "timed_out", "timeout", "seconds", "drain_complete", "stdout_over",
                                    "stderr_bytes", "stderr_over")}
    receipt["stdout_bytes"] = len(proc["stdout"])
    job["model"] = receipt  # no stdout/stderr text is ever persisted
    if proc["timed_out"] or proc["stdout_over"] or proc["returncode"] != 0:
        why = "timeout" if proc["timed_out"] else "oversized-output" if proc["stdout_over"] else f"exit-{proc['returncode']}"
        raise _fail(job_path, job, run, f"model-{why}", f"worker {why} after {proc['seconds']}s (stdout {len(proc['stdout'])} bytes)")
    try:
        proposal = json.loads(proc["stdout"].decode("utf-8"))
        if not isinstance(proposal, dict):
            raise ValueError("not an object")
    except (ValueError, UnicodeDecodeError) as exc:
        raise _fail(job_path, job, run, "model-invalid-json", f"worker stdout is not one JSON object ({type(exc).__name__})") from exc
    try:
        wiki.validate_proposal(proposal, packet)
    except wiki.ProposalRejected as exc:
        raise _fail(job_path, job, run, "model-rejected", "proposal rejected; check the packet's output schema") from None
    proposal_path = root / wiki.PROPOSAL_DIR / f"{packet['operation_id']}.json"
    core.atomic_write_bytes(proposal_path, core.dump_json(proposal))  # exact bounded proposal kept for recovery
    job.update({"proposal": proposal_path.relative_to(root).as_posix(), "stage": "pending-apply"})
    core.atomic_write_bytes(job_path, core.dump_json(job))
    if clock.expired():
        return _deferred(run, "apply", job, {"packet": prepared["packet"], "proposal": job["proposal"], "model": receipt})
    job["stage"] = "applying"
    core.atomic_write_bytes(job_path, core.dump_json(job))
    run["stage"] = "apply"
    try:
        applied = clock.stage("apply", wiki.apply, root, root / prepared["packet"], proposal_path)
    except wiki.StalePacket:
        job_path.unlink(missing_ok=True)  # the kernel refused before committing; a retry must prepare afresh
        run["outcome"] = "stale"
        raise
    job_path.unlink(missing_ok=True)
    run.update({"stage": "applied", "outcome": "applied"})
    return {"packet": prepared["packet"], "envelope": job["envelope"], "proposal": job["proposal"], "model": receipt,
            "apply": applied, "recovered": False, "build": _build(root, limits, clock)}


def _build(root: Path, limits: Limits, clock: _Clock) -> dict | None:
    if not limits.build:
        return None
    if clock.expired():
        return {"deferred": True, "next": "run `build` by hand or let the next successful worker apply rebuild"}
    res = clock.stage("build", maps.build, root)
    return {k: res[k] for k in ("known", "written", "unchanged") if k in res} or {"ok": True}
