"""Hosted receivers: GitHub repository_dispatch event files and inbox/ lead files.

Both paths turn bounded data into plain text for intake.ingest. Event text is read
from a JSON file (GITHUB_EVENT_PATH), never from shell interpolation, and nothing in
it ever becomes a command. Only normalized public repository links and caller tags
persist; processed inbox files are recorded by digest so re-runs are no-ops.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from . import core, intake

EVENT_TYPE = "research-completed"
MAX_EVENT_BYTES = 200_000  # GitHub caps client_payload at 65,535 chars; the file also carries repo metadata
MAX_URLS = 200
MAX_URL_CHARS = 2_048
MAX_TEXT_CHARS = 65_535
INBOX_LANES = ("public", "private")
MAX_INBOX_FILES = 50
MAX_INBOX_FILE_BYTES = 200_000
INBOX_SUFFIXES = (".md", ".txt", ".json")
INBOX_STATE = "state/inbox.json"


class EventRejected(core.WorkbenchError):
    code = 8


def _bounded_file(path: Path, max_bytes: int, label: str) -> str:
    with open(path, "rb") as fh:
        return intake.read_bounded(fh, max_bytes, label)


def normalize_event(event: object) -> dict:
    """Validate a research-completed payload and return {origin, project, text} or raise EventRejected.

    Supported client_payload keys: project (required tag), origin (tag, default "research-completed"),
    urls (list of <= MAX_URLS strings) and/or text (<= MAX_TEXT_CHARS). Other keys are ignored data.
    """
    if not isinstance(event, dict):
        raise EventRejected("event must be a JSON object")
    action = event.get("action")
    if action != EVENT_TYPE:
        raise EventRejected(f"unsupported event_type {action!r}; expected {EVENT_TYPE!r}")
    payload = event.get("client_payload")
    if not isinstance(payload, dict):
        raise EventRejected("client_payload must be a JSON object")
    project = payload.get("project")
    origin = payload.get("origin", EVENT_TYPE)
    if not isinstance(project, str) or not isinstance(origin, str):
        raise EventRejected("project and origin must be strings")
    urls = payload.get("urls", [])
    text = payload.get("text", "")
    if not isinstance(urls, list) or not all(isinstance(u, str) for u in urls):
        raise EventRejected("urls must be a list of strings")
    if len(urls) > MAX_URLS:
        raise EventRejected(f"urls has {len(urls)} entries; limit is {MAX_URLS}")
    if any(len(u) > MAX_URL_CHARS for u in urls):
        raise EventRejected(f"a url exceeds {MAX_URL_CHARS} characters")
    if not isinstance(text, str) or len(text) > MAX_TEXT_CHARS:
        raise EventRejected(f"text must be a string of at most {MAX_TEXT_CHARS} characters")
    if not urls and not text:
        raise EventRejected("payload carries neither urls nor text")
    return {"origin": origin, "project": project, "text": "\n".join([*urls, text])}


def receive_event(root: Path, event_path: Path, max_bytes: int = MAX_EVENT_BYTES) -> dict:
    """Ingest one GitHub event JSON file through the ordinary intake parser."""
    try:
        event = json.loads(_bounded_file(Path(event_path), max_bytes, "event file"))
    except json.JSONDecodeError as exc:
        raise EventRejected(f"event file is not valid JSON: {exc.msg}") from exc
    lead = normalize_event(event)
    result = intake.ingest(Path(root), lead["text"], lead["origin"], lead["project"])
    return {"event_type": EVENT_TYPE, "origin": lead["origin"], "project": lead["project"], **result}


def _load_inbox_state(root: Path) -> dict:
    path = root / INBOX_STATE
    if not path.exists():
        return {"processed": {}}
    state = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(state, dict) or not isinstance(state.get("processed"), dict):
        raise core.CorruptState(f"{INBOX_STATE} is malformed")
    return state


def receive_inbox(root: Path, lane: str = "public", max_files: int = MAX_INBOX_FILES,
                  max_file_bytes: int = MAX_INBOX_FILE_BYTES) -> dict:
    """Ingest inbox/<lane>/<project>/<origin>.{md,txt,json} files; tags come from the path, never the body.

    Files are visited in sorted order, at most max_files per call; unchanged files (same sha256) are
    skipped. Private-lane files stay out of Git (.gitignore) and only their normalized links persist.
    """
    root = Path(root)
    if lane not in INBOX_LANES:
        raise EventRejected(f"lane must be one of {INBOX_LANES}")
    base = root / "inbox" / lane
    files = sorted(p for p in base.rglob("*") if p.is_file() and p.suffix in INBOX_SUFFIXES
                   and p.parent != base and not p.is_symlink()) if base.is_dir() else []
    state = _load_inbox_state(root)
    out = {"root": str(root), "lane": lane, "processed": [], "skipped": [], "failed": [],
           "deferred": max(0, len(files) - max_files)}
    for path in files[:max_files]:
        rel = path.relative_to(base).as_posix()
        project, origin = path.relative_to(base).parts[0], path.stem
        try:
            data = path.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            if state["processed"].get(rel) == digest:
                out["skipped"].append(rel)
                continue
            if len(data) > max_file_bytes:
                raise intake.InputTooLarge(f"{rel} is {len(data)} bytes; limit is {max_file_bytes}")
            result = intake.ingest(root, data.decode("utf-8"), origin, project, max_bytes=max_file_bytes)
        except (core.WorkbenchError, UnicodeDecodeError) as exc:
            out["failed"].append({"file": rel, "error": type(exc).__name__, "message": str(exc)[:300]})
            continue
        state["processed"][rel] = digest
        out["processed"].append({"file": rel, "origin": origin, "project": project, "accepted": result["accepted"],
                                 "rejected": len(result["rejected"]), "new_repos": result["new_repos"]})
    if out["processed"]:
        core.atomic_write_bytes(root / INBOX_STATE, core.dump_json(state))
    return out
