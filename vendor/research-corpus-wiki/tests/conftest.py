import importlib
import json
import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))


@pytest.fixture
def api():
    try:
        return importlib.import_module("rcw_core.api")
    except ImportError:
        pytest.fail("The executable corpus kernel is not implemented")


@pytest.fixture
def corpus(api, tmp_path):
    sources = tmp_path / "sources"
    sources.mkdir()
    root = tmp_path / "wiki"
    api.init_corpus(root, sources, profile="mixed", access="internal")
    return root, sources


@pytest.fixture
def symlink():
    def create(link, target, *, target_is_directory=False):
        try:
            link.symlink_to(target, target_is_directory=target_is_directory)
        except OSError as error:
            if (
                sys.platform == "win32"
                and getattr(error, "winerror", None) == 1314
                and os.environ.get("RCW_REQUIRE_SYMLINKS") != "1"
            ):
                pytest.skip("Windows symlink creation requires an unavailable privilege (WinError 1314)")
            raise

    return create


def source(
    sources,
    name="study.md",
    text="# Findings\n\nReading scores rose by 12 points in the study sample.\n",
    **meta,
):
    path = sources / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    metadata = {
        "title": "Reading study",
        "creator": "Research team",
        "date": "2025-06-01",
        "source_type": "scholarly_article",
        "access": "public",
        "identifiers": {"doi": "10.1000/example"},
        **meta,
    }
    path.with_name(path.name + ".source.json").write_text(json.dumps(metadata), encoding="utf-8")
    return path


def proposal(packet, text="Reading scores rose by 12 points in the study sample."):
    return {
        "schema_version": "1.0",
        "operation_id": packet["operation_id"],
        "claims": [
            {
                "key": "result",
                "text": text,
                "slice_ids": [packet["slices"][-1]["id"]],
                "evidence_type": "empirical_result",
                "scope": {"population": "study sample"},
            }
        ],
        "entities": [],
        "relationships": [],
    }


def canonical_bytes(root):
    return {
        str(p.relative_to(root)): p.read_bytes()
        for p in root.rglob("*")
        if p.is_file() and p.relative_to(root).parts[0] not in {"state", "build", ".git"}
    }


def rows(root, name):
    return [json.loads(line) for line in (root / "data" / (name + ".jsonl")).read_text().splitlines() if line]


def ingest(api, root, path):
    packet = api.ingest_prepare(root, path.name)
    result = api.ingest_apply(root, packet["operation_id"], proposal(packet))
    return packet, result
