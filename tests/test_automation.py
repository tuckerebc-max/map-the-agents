"""Behavioral tests for the hosted receivers: event normalization, input limits, failure handling. Offline."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import __main__ as cli
from map_agents import automation, core, intake

SAMPLE = Path(__file__).resolve().parents[1] / "samples" / "research-completed.json"


def event(payload: dict | None, action: str = automation.EVENT_TYPE) -> dict:
    return {"action": action, "client_payload": payload, "repository": {"full_name": "x/y"}, "sender": {"login": "z"}}


def test_sample_payload_ingests_and_repeat_is_a_noop(tmp_path: Path) -> None:
    first = automation.receive_event(tmp_path, SAMPLE)
    assert first["project"] == "navy-yard" and first["origin"] == "research-completed"
    assert first["accepted"] == ["org-a/alpha", "org-b/bravo"] and first["new_repos"] == first["accepted"]
    assert first["changed"] is True
    before = (tmp_path / core.REPOS_FILE).read_bytes()
    again = automation.receive_event(tmp_path, SAMPLE)
    assert again["changed"] is False and (tmp_path / core.REPOS_FILE).read_bytes() == before


def test_event_text_is_data_only_and_top_n_candidates_are_all_kept(tmp_path: Path) -> None:
    payload = {"project": "tech-triangle", "origin": "wa-2026-09-13",
               "urls": ["https://github.com/Org-A/Alpha", "https://github.com/orgc/charlie; rm -rf /"],
               "text": "$(echo hi) `id` also https://github.com/orgd/delta and https://evil.example/x",
               "argv": ["never", "run"], "shell": "curl | sh"}
    path = tmp_path / "e.json"
    path.write_text(json.dumps(event(payload)), encoding="utf-8")
    res = automation.receive_event(tmp_path, path)
    assert res["accepted"] == ["org-a/alpha", "orgc/charlie", "orgd/delta"]
    record = core.load_repos(tmp_path)["orgc/charlie"]
    assert record["origins"] == ["wa-2026-09-13"] and record["projects"] == ["tech-triangle"]
    stored = json.dumps(core.load_repos(tmp_path)) + (tmp_path / core.OBSERVATIONS_FILE).read_text(encoding="utf-8")
    assert "rm -rf" not in stored and "curl" not in stored and "echo hi" not in stored


@pytest.mark.parametrize("bad,why", [
    ("not-an-object", "JSON object"),
    (event({"project": "p", "urls": ["https://github.com/a/b"]}, action="other-event"), "unsupported event_type"),
    (event(None), "client_payload"),
    (event({"urls": ["https://github.com/a/b"]}), "project and origin"),
    (event({"project": 7, "urls": ["https://github.com/a/b"]}), "project and origin"),
    (event({"project": "p", "urls": "https://github.com/a/b"}), "list of strings"),
    (event({"project": "p", "urls": [f"https://github.com/a/b{i}" for i in range(automation.MAX_URLS + 1)]}), "limit is"),
    (event({"project": "p", "urls": ["https://github.com/a/" + "b" * automation.MAX_URL_CHARS]}), "exceeds"),
    (event({"project": "p", "text": "x" * (automation.MAX_TEXT_CHARS + 1)}), "at most"),
    (event({"project": "p"}), "neither urls nor text"),
])
def test_malformed_or_oversized_events_are_rejected_before_any_write(tmp_path: Path, bad: object, why: str) -> None:
    with pytest.raises(automation.EventRejected, match=why):
        automation.normalize_event(bad)
    assert not (tmp_path / core.REPOS_FILE).exists()


def test_event_file_limits_and_bad_tags_fail_loudly_via_cli(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    big = tmp_path / "big.json"
    big.write_bytes(b"{" + b" " * automation.MAX_EVENT_BYTES + b"}")
    assert cli.main(["--root", str(tmp_path), "receive", "--event-path", str(big)]) == intake.InputTooLarge.code
    assert json.loads(capsys.readouterr().out)["error"] == "InputTooLarge"
    broken = tmp_path / "broken.json"
    broken.write_text("{not json", encoding="utf-8")
    assert cli.main(["--root", str(tmp_path), "receive", "--event-path", str(broken)]) == automation.EventRejected.code
    tagged = tmp_path / "tag.json"
    tagged.write_text(json.dumps(event({"project": "bad/tag\n", "urls": ["https://github.com/a/b"]})), encoding="utf-8")
    assert cli.main(["--root", str(tmp_path), "receive", "--event-path", str(tagged)]) == intake.BadTag.code
    empty = tmp_path / "empty.json"
    empty.write_text(json.dumps(event({"project": "p", "text": "no links here"})), encoding="utf-8")
    assert cli.main(["--root", str(tmp_path), "receive", "--event-path", str(empty)]) == cli.EXIT_EMPTY
    assert not (tmp_path / core.REPOS_FILE).exists()


def test_inbox_lanes_take_tags_from_paths_skip_processed_files_and_receipt_failures(tmp_path: Path) -> None:
    pub = tmp_path / "inbox" / "public"
    (pub / "navy-yard").mkdir(parents=True)
    (pub / "navy-yard" / "wa-2026-09-13.md").write_text("see https://github.com/Org-A/Alpha\n", encoding="utf-8")
    (pub / "navy-yard" / "notes.json").write_text(json.dumps({"links": ["https://github.com/orgb/bravo"]}), encoding="utf-8")
    (pub / "navy-yard" / "huge.txt").write_bytes(b"https://github.com/orgz/zulu " * 50)
    (pub / "navy-yard" / "binary.md").write_bytes(b"\xff\xfe https://github.com/orgy/yankee")
    (pub / "stray.md").write_text("https://github.com/orgx/xray\n", encoding="utf-8")  # no project directory: ignored
    (pub / "navy-yard" / "ignored.yaml").write_text("https://github.com/orgw/whiskey\n", encoding="utf-8")
    res = automation.receive_inbox(tmp_path, "public", max_file_bytes=200)
    assert [p["file"] for p in res["processed"]] == ["navy-yard/notes.json", "navy-yard/wa-2026-09-13.md"]
    assert res["processed"][1]["origin"] == "wa-2026-09-13" and res["processed"][1]["project"] == "navy-yard"
    assert sorted(f["file"] for f in res["failed"]) == ["navy-yard/binary.md", "navy-yard/huge.txt"]
    assert {f["error"] for f in res["failed"]} == {"InputTooLarge", "UnicodeDecodeError"}
    repos = core.load_repos(tmp_path)
    assert set(repos) == {"org-a/alpha", "orgb/bravo"}
    again = automation.receive_inbox(tmp_path, "public", max_file_bytes=200)
    assert again["processed"] == [] and sorted(again["skipped"]) == ["navy-yard/notes.json", "navy-yard/wa-2026-09-13.md"]
    priv = tmp_path / "inbox" / "private" / "tech-triangle"
    priv.mkdir(parents=True)
    priv.joinpath("chat-export.txt").write_text("Alice said: try https://github.com/orgc/charlie tonight\n", encoding="utf-8")
    res = automation.receive_inbox(tmp_path, "private", max_files=1)
    assert res["processed"][0]["accepted"] == ["orgc/charlie"] and res["deferred"] == 0
    persisted = (tmp_path / core.REPOS_FILE).read_text(encoding="utf-8") + (tmp_path / core.OBSERVATIONS_FILE).read_text(encoding="utf-8")
    assert "Alice" not in persisted and "tonight" not in persisted
    limited = automation.receive_inbox(tmp_path, "public", max_files=1, max_file_bytes=200)
    assert limited["deferred"] == 3 and limited["processed"] == []


def test_inbox_cursor_is_fair_across_calls_and_lanes_do_not_collide(tmp_path: Path) -> None:
    pub = tmp_path / "inbox" / "public" / "proj"
    pub.mkdir(parents=True)
    (pub / "a.md").write_text("https://github.com/org/aaa\n", encoding="utf-8")
    (pub / "b.md").write_text("https://github.com/org/bbb\n", encoding="utf-8")
    (pub / "c.md").write_text("https://github.com/org/ccc\n", encoding="utf-8")
    seen: list[str] = []
    for _ in range(6):
        res = automation.receive_inbox(tmp_path, "public", max_files=1)
        seen += [p["file"] for p in res["processed"]] + res["skipped"]
    # every visited slot is spent on a file, unchanged repeats included, so 3 files over 6 calls of 1
    # each visit every file at least twice instead of starving b.md/c.md behind a.md forever.
    assert set(seen) == {"proj/a.md", "proj/b.md", "proj/c.md"}
    assert seen[:3] == ["proj/a.md", "proj/b.md", "proj/c.md"]  # first cycle in sorted order
    assert seen[3:6] == ["proj/a.md", "proj/b.md", "proj/c.md"]  # wraps and repeats (all now unchanged)

    priv = tmp_path / "inbox" / "private" / "proj"
    priv.mkdir(parents=True)
    (priv / "a.md").write_text("https://github.com/org/private-aaa\n", encoding="utf-8")  # same rel path, different bytes
    pub_state_before = automation._load_inbox_state(tmp_path)["cursor"]["public"]
    res = automation.receive_inbox(tmp_path, "private", max_files=1)
    assert res["processed"][0]["accepted"] == ["org/private-aaa"]
    state = automation._load_inbox_state(tmp_path)
    assert state["cursor"]["public"] == pub_state_before  # the private-lane call never touched public's cursor
    # both lanes keep an entry under the identical relative path "proj/a.md" with different digests: the
    # lane-scoped processed map means neither lane's record shadows or is skipped because of the other's.
    assert state["processed"]["private"]["proj/a.md"] != state["processed"]["public"]["proj/a.md"]
    again = automation.receive_inbox(tmp_path, "private", max_files=1)
    assert again["skipped"] == ["proj/a.md"]  # private's own record, unaffected by public sharing the same rel


def test_bounded_read_never_allocates_the_whole_oversized_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    pub = tmp_path / "inbox" / "public" / "proj"
    pub.mkdir(parents=True)
    (pub / "big.md").write_bytes(b"x" * 10_000)
    monkeypatch.setattr(Path, "read_bytes", lambda self: (_ for _ in ()).throw(AssertionError("whole-file read used")))
    res = automation.receive_inbox(tmp_path, "public", max_file_bytes=100)
    assert res["failed"] == [{"file": "proj/big.md", "error": "InputTooLarge"}]


@pytest.mark.parametrize("kwargs", [{"max_files": 0}, {"max_files": -1}, {"max_file_bytes": 0}, {"max_file_bytes": -5}])
def test_invalid_inbox_limits_are_rejected_before_any_mutation(tmp_path: Path, kwargs: dict) -> None:
    pub = tmp_path / "inbox" / "public" / "proj"
    pub.mkdir(parents=True)
    (pub / "a.md").write_text("https://github.com/org/aaa\n", encoding="utf-8")
    with pytest.raises(automation.InvalidLimits):
        automation.receive_inbox(tmp_path, "public", **kwargs)
    assert not (tmp_path / core.REPOS_FILE).exists()
    assert not (tmp_path / automation.INBOX_STATE).exists()


def test_symlinked_project_directory_is_not_read(tmp_path: Path) -> None:
    pub = tmp_path / "inbox" / "public"
    real = tmp_path / "outside-project"
    real.mkdir()
    (real / "a.md").write_text("https://github.com/org/outside\n", encoding="utf-8")
    pub.mkdir(parents=True)
    link = pub / "linked"
    try:
        link.symlink_to(real, target_is_directory=True)
    except OSError:
        pytest.skip("creating a directory symlink requires elevated privilege on this host")
    res = automation.receive_inbox(tmp_path, "public")
    assert res["processed"] == [] and res["failed"] == [] and res["skipped"] == []
    assert not core.load_repos(tmp_path)


def test_held_orchestrator_lease_blocks_inbox_receiver(tmp_path: Path) -> None:
    pub = tmp_path / "inbox" / "public" / "proj"
    pub.mkdir(parents=True)
    (pub / "a.md").write_text("https://github.com/org/aaa\n", encoding="utf-8")
    from map_agents import workers

    with workers.Lease(tmp_path, "maintain"):
        with pytest.raises(workers.LeaseHeld):
            automation.receive_inbox(tmp_path, "public")
    assert not (tmp_path / core.REPOS_FILE).exists()
