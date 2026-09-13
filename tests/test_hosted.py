"""Executable hosted pipeline boundary checks with real local state and no live network."""
import json
from pathlib import Path
import subprocess
import sys

import pytest

from map_agents import __main__ as cli, automation, collect, core, intake, wiki, workers
from scripts import run_maintenance as hosted


def test_partial_refresh_keeps_valid_progress_and_reports_failure(tmp_path):
    root = tmp_path / "c"
    intake.ingest(root, "https://github.com/example/missing", "test", "navy-yard")
    summary_path = tmp_path / "summary.json"
    res = hosted.run(root, summary_path, limits=workers.Limits(catalog_entries=0, max_repos=1),
                     transport=lambda *a, **kw: collect.Response(404, b"{}"))
    assert res["publishable"] and res["status"] == "partial"
    assert res["refresh"]["failures"] == 1
    state = json.loads((root / workers.QUEUE_FILE).read_text())
    assert state["cursor"] == "example/missing" and state["repos"]["example/missing"]["failures"] == 1
    assert hosted.report(summary_path) == 5
    assert (root / "map/index.md").is_file()


def test_bad_event_and_failed_audit_cannot_publish(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"action": "private-sentinel"}))
    summary = tmp_path / "summary.json"
    result = hosted.run(tmp_path / "bad", summary, event_path=event)
    assert result["publishable"] is False and result["stage"] == "receive"
    assert "private-sentinel" not in summary.read_text()
    monkeypatch.setattr(wiki, "audit", lambda *a: {"ok": False})
    result = hosted.run(tmp_path / "c", summary, limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert not result["publishable"] and result["stage"] == "audit"


def test_all_dispatch_links_and_inbox_tags_reach_validated_map(tmp_path):
    root = tmp_path / "c"
    inbox = root / "inbox/public/tech-triangle/search.txt"
    inbox.parent.mkdir(parents=True)
    inbox.write_text("https://github.com/example/c")
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"action": "research-completed", "client_payload": {
        "project": "navy-yard", "urls": ["https://github.com/example/a", "https://github.com/example/b"]}}))
    result = hosted.run(root, tmp_path / "summary.json", event_path=event,
                        limits=workers.Limits(catalog_entries=0, max_repos=0))
    assert result["status"] == "validated" and result["received_repos"] == 2
    repos = core.load_repos(root)
    assert set(repos) == {"example/a", "example/b", "example/c"}
    assert repos["example/c"]["projects"] == ["tech-triangle"]


def test_demo_refuses_to_remove_existing_data(tmp_path):
    sentinel = tmp_path / "keep.txt"
    sentinel.write_text("keep me")
    demo = Path(__file__).resolve().parents[1] / "scripts/demo_synthetic.py"
    proc = subprocess.run([sys.executable, str(demo), "--root", str(tmp_path)], capture_output=True)
    assert proc.returncode != 0 and sentinel.read_text() == "keep me"
    assert b"existing content is never removed" in proc.stderr


def test_manual_worker_cli_exposes_actual_envelope_cap():
    args = cli.build_parser().parse_args(["worker", "--max-envelope-bytes", "12345"])
    assert cli._limits(args).max_envelope_bytes == 12345


@pytest.mark.parametrize("limit", [True, 1.2, float("inf")])
def test_inbox_rejects_non_integer_limits_before_mutation(tmp_path, limit):
    with pytest.raises(automation.InvalidLimits):
        automation.receive_inbox(tmp_path, max_files=limit)
    assert not list(tmp_path.iterdir())


def test_ancestor_inbox_link_is_rejected_before_read(tmp_path):
    root, outside = tmp_path / "c", tmp_path / "outside"
    root.mkdir()
    (outside / "public/p").mkdir(parents=True)
    (outside / "public/p/chat.txt").write_text("https://github.com/example/private")
    try:
        (root / "inbox").symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("directory symlink creation unavailable on this host")
    with pytest.raises(collect.InvalidPath):
        automation.receive_inbox(root)
    assert not (root / core.REPOS_FILE).exists()
