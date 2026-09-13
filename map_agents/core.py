"""Corpus layout, stable JSON IO, atomic writes and the one-writer lock."""

from __future__ import annotations

import json
import os
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

REPOS_FILE = "catalog/repos.json"
OBSERVATIONS_FILE = "catalog/observations.jsonl"
LOCK_FILE = "state/writer.lock"
LAYOUT = ("catalog", "sources", "wiki", "map", "state", "packets", "proposals", "inbox/private", "inbox/public")
SEED_FILES = {REPOS_FILE: b"{}\n", OBSERVATIONS_FILE: b""}


class WorkbenchError(Exception):
    """Base error; `code` maps to a stable CLI exit status."""

    code = 1


class LockHeld(WorkbenchError):
    code = 5


class CorruptState(WorkbenchError):
    code = 6


def dump_json(obj: object) -> bytes:
    """Canonical JSON bytes: sorted keys, two-space indent, trailing newline."""
    return (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write via a same-directory temp file and os.replace, so readers never see partial content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with open(tmp, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def write_if_changed(path: Path, data: bytes) -> bool:
    """Atomic write that leaves identical bytes untouched. Returns True when written."""
    if path.exists() and path.read_bytes() == data:
        return False
    atomic_write_bytes(path, data)
    return True


def init(root: Path) -> dict:
    """Public init: takes the one-writer lock, then creates layout and seeds. Never overwrites."""
    with writer_lock(root):
        return init_locked(root)


def init_locked(root: Path) -> dict:
    """Layout/seed creation for callers that already hold writer_lock(root). Idempotent."""
    root = Path(root)
    created: list[str] = []
    for rel in LAYOUT:
        target = root / rel
        if not target.exists():
            target.mkdir(parents=True)
            created.append(rel)
    for rel, seed in SEED_FILES.items():
        target = root / rel
        if not target.exists():
            atomic_write_bytes(target, seed)
            created.append(rel)
    return {"root": str(root), "created": created, "existing": not created}


def load_repos(root: Path) -> dict[str, dict]:
    path = Path(root) / REPOS_FILE
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_bytes().decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise CorruptState(f"{path} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise CorruptState(f"{path} must contain a JSON object keyed by owner/repo")
    return data


def save_repos(root: Path, records: dict[str, dict]) -> bool:
    """Persist repos.json atomically with canonical bytes. Returns True when bytes changed."""
    for key in records:
        if key != key.lower() or key.count("/") != 1:
            raise WorkbenchError(f"repo key must be lowercase owner/repo: {key!r}")
    return write_if_changed(Path(root) / REPOS_FILE, dump_json(records))


def load_observations(root: Path) -> list[dict]:
    path = Path(root) / OBSERVATIONS_FILE
    if not path.exists():
        return []
    rows: list[dict] = []
    for n, line in enumerate(path.read_bytes().decode("utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError as exc:
            raise CorruptState(f"{path}:{n} is not valid JSON") from exc
        rows.append(row)
    return rows


def save_observations(root: Path, rows: list[dict]) -> bool:
    """Persist deduplicated, sorted origin/project associations as JSONL."""
    unique = {json.dumps(r, sort_keys=True, ensure_ascii=False) for r in rows}
    data = "".join(line + "\n" for line in sorted(unique)).encode("utf-8")
    return write_if_changed(Path(root) / OBSERVATIONS_FILE, data)


@contextmanager
def writer_lock(root: Path) -> Iterator[Path]:
    """Exclusive one-writer lock via O_EXCL creation of state/writer.lock."""
    path = Path(root) / LOCK_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    except FileExistsError as exc:
        raise LockHeld(f"another writer holds {path}") from exc
    try:
        os.write(fd, f"pid={os.getpid()}\n".encode())
        os.close(fd)
        yield path
    finally:
        path.unlink(missing_ok=True)
