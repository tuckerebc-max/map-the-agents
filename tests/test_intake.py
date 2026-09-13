"""Behavioral tests for foundation (core) and intake. Offline, model-free, portable."""

from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

import pytest

from map_agents import core, intake

ORIGIN = "whatsapp:design-chat"
PROJECT = "navy-yard"

SAMPLE = """
Look at https://github.com/Owner-One/Agent-Repo/blob/main/README.md#usage and
[the tree](https://github.com/owner-one/agent-repo/tree/dev/src?tab=readme).
Issue: https://github.com/second/tool.git/issues/12, and https://github.com/third/multi-plexer.
Not a repo: https://github.com/settings/profile and https://github.com/onlyowner
Elsewhere: https://example.com/owner/repo https://gitlab.com/a/b
"""


def repos_bytes(root: Path) -> bytes:
    return (root / core.REPOS_FILE).read_bytes()


def obs_bytes(root: Path) -> bytes:
    return (root / core.OBSERVATIONS_FILE).read_bytes()


def test_init_is_non_destructive_and_idempotent(tmp_path: Path) -> None:
    first = core.init(tmp_path)
    assert set(first["created"]) >= {"catalog", "wiki", "sources", core.REPOS_FILE}
    core.save_repos(tmp_path, {"a/b": {"url": "https://github.com/a/b"}})
    before = repos_bytes(tmp_path)
    second = core.init(tmp_path)
    assert second["created"] == [] and second["existing"] is True
    assert repos_bytes(tmp_path) == before
    assert core.load_repos(tmp_path) == {"a/b": {"url": "https://github.com/a/b"}}


def test_save_repos_rejects_non_canonical_keys(tmp_path: Path) -> None:
    with pytest.raises(core.WorkbenchError):
        core.save_repos(tmp_path, {"Owner/Repo": {}})


def test_ingest_canonicalizes_and_records_provenance(tmp_path: Path) -> None:
    result = intake.ingest(tmp_path, SAMPLE, ORIGIN, PROJECT)
    assert result["accepted"] == ["owner-one/agent-repo", "second/tool", "third/multi-plexer"]
    assert result["new_repos"] == result["accepted"]
    assert result["new_associations"] == 3 and result["changed"] is True and result["empty"] is False
    reasons = {r["reason"] for r in result["rejected"]}
    assert reasons == {"reserved-route", "not-a-repository"}
    assert result["ignored_hosts"] == 2
    repos = core.load_repos(tmp_path)
    rec = repos["owner-one/agent-repo"]
    assert rec["url"] == "https://github.com/Owner-One/Agent-Repo"
    assert rec["origins"] == [ORIGIN] and rec["projects"] == [PROJECT]
    assert rec["status"] == "discovered" and rec["freshness"] == "pending"
    assert repos["second/tool"]["url"] == "https://github.com/second/tool"
    rows = core.load_observations(tmp_path)
    assert {"repo": "second/tool", "origin": ORIGIN, "project": PROJECT} in rows
    # Source text never persists: no fragment of the prose is in any catalog file.
    for path in (tmp_path / "catalog").iterdir():
        assert b"Look at" not in path.read_bytes() and b"Elsewhere" not in path.read_bytes()


def test_json_url_arrays_and_all_top_n_links_retained(tmp_path: Path) -> None:
    urls = [f"https://github.com/org{i}/repo{i}" for i in range(150)]
    payload = json.dumps({"leads": urls, "nested": [{"url": urls[0] + "/blob/main/x.md"}]})
    result = intake.ingest(tmp_path, payload, ORIGIN, PROJECT)
    assert result["accepted"] == [f"org{i}/repo{i}" for i in range(150)]
    assert len(core.load_repos(tmp_path)) == 150


def test_repeat_intake_is_canonical_no_op_and_associations_accumulate(tmp_path: Path) -> None:
    intake.ingest(tmp_path, SAMPLE, ORIGIN, PROJECT)
    r_before, o_before = repos_bytes(tmp_path), obs_bytes(tmp_path)
    repeat = intake.ingest(tmp_path, SAMPLE, ORIGIN, PROJECT)
    assert repeat["changed"] is False and repeat["new_repos"] == [] and repeat["new_associations"] == 0
    assert repos_bytes(tmp_path) == r_before and obs_bytes(tmp_path) == o_before
    again = intake.ingest(tmp_path, "https://github.com/Second/Tool", "notes:eric", "tech-triangle")
    assert again["new_repos"] == [] and again["new_associations"] == 1
    rec = core.load_repos(tmp_path)["second/tool"]
    assert rec["url"] == "https://github.com/second/tool"
    assert rec["origins"] == [ORIGIN, "notes:eric"] and rec["projects"] == [PROJECT, "tech-triangle"]
    assert len(core.load_observations(tmp_path)) == 4


@pytest.mark.parametrize(
    "link,reason",
    [
        ("https://user:pw@github.com/a/b", "credentialed"),
        ("https://github.com/a/b?token=abc", "private-access-parameter"),
        ("https://github.com/a/b?access_token=ghp_x", "private-access-parameter"),
        ("http://github.com/a/b", "insecure-scheme"),
        ("https://github.com:8443/a/b", "unsafe-port"),
        ("https://github.com/a/../b", "unsafe-path"),
        ("https://github.com/a/%2e%2e/b", "unsafe-path"),
        ("https://github.com/orgs/acme", "reserved-route"),
        ("https://github.com/-bad/repo", "invalid-owner"),
        ("https://github.com/a/b%3f", "unsafe-path"),
        ("https://github.localhost/a/b", "private-host"),
        ("https://127.0.0.1/a/b", "private-host"),
        ("https://10.0.0.5/a/b", "private-host"),
        ("https://ghe.internal/a/b", "private-host"),
    ],
)
def test_unsafe_links_are_rejected_and_not_written(tmp_path: Path, link: str, reason: str) -> None:
    result = intake.ingest(tmp_path, f"lead: {link}", ORIGIN, PROJECT)
    assert result["accepted"] == [] and result["empty"] is True
    assert [r["reason"] for r in result["rejected"]] == [reason]
    assert set(result["rejected"][0]) == {"position", "host", "reason"}
    assert not (tmp_path / "catalog").exists()


def test_input_limit_fails_before_any_write(tmp_path: Path) -> None:
    text = "https://github.com/a/b " * 100
    with pytest.raises(intake.InputTooLarge):
        intake.ingest(tmp_path, text, ORIGIN, PROJECT, max_bytes=100)
    assert not (tmp_path / "catalog").exists()
    with pytest.raises(intake.BadTag):
        intake.ingest(tmp_path, "https://github.com/a/b", "", PROJECT)
    assert not (tmp_path / "catalog").exists()


def test_interrupted_multi_file_write_keeps_prior_provenance(tmp_path: Path, monkeypatch) -> None:
    intake.ingest(tmp_path, "https://github.com/a/b", ORIGIN, PROJECT)
    r_before, o_before = repos_bytes(tmp_path), obs_bytes(tmp_path)
    real_replace = os.replace
    calls: list[str] = []

    def failing_replace(src, dst):
        calls.append(Path(dst).name)
        if Path(dst).name == "observations.jsonl":
            raise OSError("simulated interruption")
        return real_replace(src, dst)

    monkeypatch.setattr(os, "replace", failing_replace)
    with pytest.raises(OSError):
        intake.ingest(tmp_path, "https://github.com/c/d", "notes:eric", PROJECT)
    monkeypatch.setattr(os, "replace", real_replace)
    assert calls == ["repos.json", "observations.jsonl"]
    assert obs_bytes(tmp_path) == o_before
    repos = core.load_repos(tmp_path)
    assert repos["a/b"]["origins"] == [ORIGIN] and "c/d" in repos
    assert not list((tmp_path / "catalog").glob(".*.tmp"))
    assert not (tmp_path / core.LOCK_FILE).exists()
    healed = intake.ingest(tmp_path, "https://github.com/c/d", "notes:eric", PROJECT)
    assert healed["new_associations"] == 1 and healed["new_repos"] == []
    assert repos_bytes(tmp_path) != r_before and len(core.load_observations(tmp_path)) == 2


def run_cli(root: Path, *args: str, stdin: str = "") -> subprocess.CompletedProcess:
    proc = subprocess.run(
        [sys.executable, "-m", "map_agents", "--root", str(root), *args],
        input=stdin.encode("utf-8"), capture_output=True, cwd=Path(__file__).resolve().parents[1],
    )
    proc.stdout = proc.stdout.decode("utf-8")
    return proc


def test_public_init_holds_writer_lock_so_intake_cannot_interleave(tmp_path: Path, monkeypatch) -> None:
    real_write = core.atomic_write_bytes
    interleaved: list[Exception] = []

    def racing_write(path: Path, data: bytes) -> None:
        # Initializer is paused at the repos.json seed write; a second writer tries intake now.
        if path.name == "repos.json" and not interleaved:
            try:
                intake.ingest(tmp_path, "https://github.com/example/retained", ORIGIN, PROJECT)
            except core.LockHeld as exc:
                interleaved.append(exc)
        real_write(path, data)

    monkeypatch.setattr(core, "atomic_write_bytes", racing_write)
    core.init(tmp_path)
    assert len(interleaved) == 1 and core.load_repos(tmp_path) == {}
    monkeypatch.setattr(core, "atomic_write_bytes", real_write)
    with core.writer_lock(tmp_path):
        with pytest.raises(core.LockHeld):
            core.init(tmp_path)
    assert intake.ingest(tmp_path, "https://github.com/example/retained", ORIGIN, PROJECT)["new_repos"] == [
        "example/retained"
    ]


def test_threaded_init_and_intake_never_lose_a_retained_record(tmp_path: Path) -> None:
    for round_no in range(10):
        root = tmp_path / f"r{round_no}"
        barrier = threading.Barrier(2)
        outcomes: dict[str, object] = {}

        def run(name: str, fn) -> None:
            barrier.wait()
            try:
                outcomes[name] = fn()
            except core.LockHeld as exc:
                outcomes[name] = exc

        a = threading.Thread(target=run, args=("init", lambda: core.init(root)))
        b = threading.Thread(
            target=run,
            args=("intake", lambda: intake.ingest(root, "https://github.com/example/retained", ORIGIN, PROJECT)),
        )
        a.start(), b.start(), a.join(), b.join()
        if not isinstance(outcomes["intake"], core.LockHeld):
            assert "example/retained" in core.load_repos(root), round_no
        assert not (root / core.LOCK_FILE).exists()


def test_rejection_receipts_never_serialize_secret_shaped_input(tmp_path: Path) -> None:
    fakes = ["ghp_DEMONSTRATION_ONLY", "SECRETPW", "hiddenuser"]
    text = (
        "https://github.com/example/ghp_DEMONSTRATION_ONLY "
        "https://hiddenuser:SECRETPW@github.com/a/b "
        "https://hiddenuser:SECRETPW@github.com:notaport/ghp_DEMONSTRATION_ONLY "
        "https://github.com/a/b?token=ghp_DEMONSTRATION_ONLY"
    )
    result = intake.ingest(tmp_path, text, ORIGIN, PROJECT)
    serialized = json.dumps(result)
    assert result["empty"] is True and len(result["rejected"]) == 4
    assert [r["reason"] for r in result["rejected"]] == [
        "private-access-parameter", "credentialed", "private-access-parameter", "private-access-parameter",
    ]
    assert all(fake not in serialized for fake in fakes)
    assert all(set(r) == {"position", "host", "reason"} for r in result["rejected"])
    plain_malformed = intake.ingest(tmp_path, "https://hiddenuser:SECRETPW@github.com:notaport/x/y", ORIGIN, PROJECT)
    assert plain_malformed["rejected"][0]["reason"] == "malformed"  # urlsplit port parse error path
    assert all(fake not in json.dumps(plain_malformed) for fake in fakes)
    assert not (tmp_path / "catalog").exists()


class CountingStream(io.BytesIO):
    def __init__(self, data: bytes) -> None:
        super().__init__(data)
        self.requests: list[int] = []

    def read(self, size: int = -1) -> bytes:
        self.requests.append(size)
        return super().read(size)


@pytest.mark.parametrize('limit', [-2, -1, 0])
def test_invalid_byte_limits_are_rejected_before_read(limit: int) -> None:
    stream = CountingStream(b'large input' * 1000)
    with pytest.raises(intake.InputTooLarge, match='positive'):
        intake.read_bounded(stream, limit)
    assert stream.requests == []


def test_rejected_secret_hostname_is_not_echoed(tmp_path: Path) -> None:
    result = intake.ingest(tmp_path, 'https://ghp_DEMONSTRATION_ONLY.invalid/a/b', ORIGIN, PROJECT)
    assert result['rejected'][0]['reason'] == 'private-access-parameter'
    assert 'demonstration_only' not in json.dumps(result).lower()


def test_read_bounded_requests_limit_plus_one_and_rejects_bad_utf8() -> None:
    stream = CountingStream(b"https://github.com/a/b " * 1000)
    with pytest.raises(intake.InputTooLarge):
        intake.read_bounded(stream, 64, "stdin")
    assert stream.requests == [65]
    assert intake.read_bounded(io.BytesIO(b"https://github.com/a/b"), 64) == "https://github.com/a/b"
    with pytest.raises(intake.BadEncoding):
        intake.read_bounded(io.BytesIO(b"https://github.com/a/b\xff\xfe"), 64)


def test_cli_bounded_stdin_and_file_reads_leave_no_state(tmp_path: Path) -> None:
    root = tmp_path / "corpus"
    proc = run_cli(root, "intake", "--origin", ORIGIN, "--project", PROJECT, "--max-bytes", "40",
                   stdin="https://github.com/a/b " * 20)
    assert proc.returncode == 3 and json.loads(proc.stdout)["error"] == "InputTooLarge"
    bad = tmp_path / "bad.txt"
    bad.write_bytes(b"https://github.com/a/b\xff\xfe")
    proc = run_cli(root, "intake", "--origin", ORIGIN, "--project", PROJECT, "--file", str(bad))
    assert proc.returncode == 7 and json.loads(proc.stdout)["error"] == "BadEncoding"
    assert not root.exists()


def test_one_writer_lock_blocks_second_writer(tmp_path: Path) -> None:
    with core.writer_lock(tmp_path):
        with pytest.raises(core.LockHeld):
            intake.ingest(tmp_path, "https://github.com/a/b", ORIGIN, PROJECT)
        assert not (tmp_path / "catalog").exists()
    result = intake.ingest(tmp_path, "https://github.com/a/b", ORIGIN, PROJECT)
    assert result["new_repos"] == ["a/b"]
    assert not (tmp_path / core.LOCK_FILE).exists()


def test_cli_init_intake_status_round_trip(tmp_path: Path) -> None:
    root = tmp_path / "corpus"
    proc = run_cli(root, "init")
    assert proc.returncode == 0 and json.loads(proc.stdout)["existing"] is False
    proc = run_cli(root, "intake", "--origin", ORIGIN, "--project", PROJECT, stdin=SAMPLE)
    assert proc.returncode == 0, proc.stdout
    assert json.loads(proc.stdout)["accepted"] == ["owner-one/agent-repo", "second/tool", "third/multi-plexer"]
    proc = run_cli(root, "intake", "--origin", ORIGIN, "--project", PROJECT, "--text", "no links here")
    assert proc.returncode == 4 and json.loads(proc.stdout)["empty"] is True
    big = tmp_path / "big.txt"
    big.write_text("x" * 50, encoding="utf-8")
    proc = run_cli(root, "intake", "--origin", ORIGIN, "--project", PROJECT, "--file", str(big), "--max-bytes", "10")
    assert proc.returncode == 3 and json.loads(proc.stdout)["error"] == "InputTooLarge"
    proc = run_cli(root, "status")
    status = json.loads(proc.stdout)
    assert proc.returncode == 0 and status["repos"] == 3 and status["associations"] == 3
    assert status["by_status"] == {"discovered": 3} and status["lock_held"] is False
