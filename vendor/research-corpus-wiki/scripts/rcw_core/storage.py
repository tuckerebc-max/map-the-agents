"""Canonical serialization, path boundaries, and journaled filesystem writes."""

import hashlib
import io
import json
import os
import socket
import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import NoReturn

from pydantic import ValidationError
from ruamel.yaml import YAML

from .models import TABLES, CorpusConfig, dump


class RCWError(RuntimeError):
    def __init__(self, code, message):
        self.code = code
        super().__init__(f"{code}: {message}")


def fail(code, message) -> NoReturn:
    raise RCWError(code, message)


def validate(model, value):
    try:
        return dump(model.model_validate(value))
    except ValidationError as error:
        fail("RCW_SCHEMA_INVALID", str(error))


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def digest(value):
    data = value if isinstance(value, bytes) else canonical(value).encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def fingerprint(path):
    hasher = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return "sha256:" + hasher.hexdigest()


def content_id(prefix, value):
    return prefix + "_" + digest(value).split(":")[1]


def stable_id(prefix, value):
    return prefix + "_" + uuid.uuid5(uuid.NAMESPACE_URL, canonical(value)).hex


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def envelope(prefix, identity, access, operation, review="mechanically_checked"):
    stamp = now()
    return {
        "schema_version": "1.0",
        "id": identity,
        "access": access,
        "review_state": review,
        "created_at": stamp,
        "updated_at": stamp,
        "created_by_operation": operation,
        "updated_by_operation": operation,
    }


def yaml_text(value):
    buffer = io.StringIO()
    yaml = YAML(typ="safe")
    yaml.default_flow_style = False
    yaml.dump(value, buffer)
    return buffer.getvalue()


def config(root):
    root = Path(root).resolve()
    try:
        data = YAML(typ="safe").load((root / "wiki.yaml").read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        fail("RCW_CONFIG_INVALID", str(error))
    value = validate(CorpusConfig, data)
    for item in value["source_roots"]:
        path = (root / item["path"]).resolve()
        if root == path or path in root.parents or root in path.parents:
            fail("RCW_PATH_OVERLAP", "Source and wiki trees must be disjoint")
        if not path.is_dir():
            fail("RCW_SOURCE_MISSING", item["root_id"])
    return value


def safe_path(root, relative):
    base = Path(root).resolve()
    # Corpus paths use portable slash syntax; validate before native normalization.
    candidate = PurePosixPath(relative)
    if (
        candidate.is_absolute()
        or ".." in candidate.parts
        or "\\" in str(relative)
        or PureWindowsPath(candidate.as_posix()).drive
    ):
        fail("RCW_PATH_ESCAPE", str(relative))
    result = base / candidate
    if not result.resolve().is_relative_to(base):
        fail("RCW_PATH_ESCAPE", str(relative))
    for part in [result, *result.parents]:
        if part == base:
            break
        if part.is_symlink():
            fail("RCW_PATH_ESCAPE", "Symlinks are not valid corpus write targets")
    return result


def source_root(root, root_id):
    cfg = config(root)
    for item in cfg["source_roots"]:
        if item["root_id"] == root_id:
            return (Path(root) / item["path"]).resolve()
    fail("RCW_SOURCE_MISSING", root_id)


def load_tables(root):
    result = {}
    for table, model in TABLES.items():
        path = safe_path(root, "data/" + table + ".jsonl")
        if not path.exists():
            fail("RCW_RECORDS_MISSING", table)
        records = {}
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                row = validate(model, json.loads(line))
                if row["id"] in records:
                    fail("RCW_DUPLICATE_ID", row["id"])
                records[row["id"]] = row
        except json.JSONDecodeError as error:
            fail("RCW_SCHEMA_INVALID", str(error))
        result[table] = records
    return result


def serialized_tables(tables):
    return {
        "data/" + table + ".jsonl": "".join(
            canonical(validate(TABLES[table], row)) + "\n" for _, row in sorted(records.items())
        )
        for table, records in tables.items()
    }


def semantic(row):
    return {
        key: value
        for key, value in row.items()
        if key not in {"created_at", "updated_at", "created_by_operation", "updated_by_operation"}
    }


def upsert(records, row):
    old = records.get(row["id"])
    if old and semantic(old) == semantic(row):
        return old
    if old:
        row["created_at"] = old["created_at"]
        row["created_by_operation"] = old["created_by_operation"]
    records[row["id"]] = row
    return row


def corpus_digest(root):
    root = Path(root)
    entries = {}
    for name in ("wiki.yaml", "rcw.lock"):
        path = safe_path(root, name)
        if path.exists():
            entries[name] = fingerprint(path)
    for folder in ("data", "pages", "metadata", "reports"):
        for path in sorted((root / folder).rglob("*")):
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                entries[relative] = fingerprint(safe_path(root, relative))
    return digest(entries)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    path.write_text(canonical(value) + "\n", encoding="utf-8")
    path.chmod(0o600)


@contextmanager
def lease(root, operation):
    lock = safe_path(root, "state/leases/corpus.lock")
    lock.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    try:
        descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        fail("RCW_LEASE_ACTIVE", "Inspect or recover the current operation before applying another")
    with os.fdopen(descriptor, "w") as stream:
        stream.write(
            canonical(
                {
                    "operation_id": operation,
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                    "expires_at": time.time() + 1800,
                }
            )
        )
    try:
        yield
    finally:
        if lock.exists():
            lock.unlink()


def replace_file(path, text):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temp = path.with_name(path.name + ".rcw-tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(text)
        stream.flush()
        os.fsync(stream.fileno())
    temp.chmod(0o600)
    os.replace(temp, path)


def transaction(root, operation, changes, final_check=None):
    changed = {
        rel: text
        for rel, text in changes.items()
        if not safe_path(root, rel).exists() or safe_path(root, rel).read_text(encoding="utf-8") != text
    }
    if not changed:
        return []
    journal_path = safe_path(root, f"state/operations/{operation}/journal.json")
    journal = {"state": "prepared", "operation_id": operation, "entries": []}
    for rel, text in changed.items():
        target = safe_path(root, rel)
        journal["entries"].append(
            {
                "path": rel,
                "before": target.read_text(encoding="utf-8") if target.exists() else None,
                "after_digest": digest(text.encode()),
            }
        )
    write_json(journal_path, journal)
    try:
        for rel, text in changed.items():
            replace_file(safe_path(root, rel), text)
        if final_check:
            final_check()
        journal["state"] = "applied"
        write_json(journal_path, journal)
    except BaseException:
        rollback(root, journal)
        journal["state"] = "rolled_back"
        write_json(journal_path, journal)
        raise
    return sorted(changed)


def rollback(root, journal):
    for entry in journal["entries"]:
        target = safe_path(root, entry["path"])
        if entry["before"] is None:
            target.unlink(missing_ok=True)
        else:
            replace_file(target, entry["before"])


def recover(root):
    lock = safe_path(root, "state/leases/corpus.lock")
    if lock.exists():
        holder = json.loads(lock.read_text())
        if holder["host"] != socket.gethostname():
            fail("RCW_LEASE_ACTIVE", "Recovery requires the same host or an administrator review")
        try:
            os.kill(holder["pid"], 0)
        except ProcessLookupError:
            pass
        else:
            fail("RCW_LEASE_ACTIVE", "The owning process still exists")
        lock.unlink()
    recovered = []
    with lease(root, "recovery"):
        for path in sorted((Path(root) / "state/operations").glob("*/journal.json")):
            journal = json.loads(path.read_text())
            if journal["state"] != "prepared":
                continue
            # Refuse to overwrite a third party edit made after the failed run.
            for entry in journal["entries"]:
                target = safe_path(root, entry["path"])
                current = digest(target.read_bytes()) if target.exists() else None
                prior = digest(entry["before"].encode()) if entry["before"] is not None else None
                if current not in {prior, entry["after_digest"]}:
                    fail("RCW_RECOVERY_CONFLICT", entry["path"])
            rollback(root, journal)
            journal["state"] = "rolled_back"
            write_json(path, journal)
            recovered.append(journal["operation_id"])
    return {"recovered": recovered}


ACCESS = {"public": 0, "internal": 1, "confidential": 2, "restricted": 3}


def maximum_access(values):
    return max(values, key=lambda value: ACCESS[value], default="public")
