"""Small public Python API mirrored by the rcw command line."""

import os
from pathlib import Path

from .audit import audit
from .ingest import ingest_apply, ingest_prepare
from .knowledge import analyze_apply, analyze_prepare, ask_complete, ask_prepare, reindex
from .models import TABLES, CorpusConfig, Metadata
from .output import export_citations, render
from .sources import inventory
from .storage import (
    content_id,
    digest,
    fail,
    lease,
    load_tables,
    recover,
    safe_path,
    validate,
    write_json,
    yaml_text,
)


def init_corpus(root, sources, profile="mixed", access="internal", title="Research corpus"):
    root, sources = Path(root).resolve(), Path(sources).resolve()
    if not sources.is_dir():
        fail("RCW_SOURCE_MISSING", "Source directory must already exist")
    if root == sources or root in sources.parents or sources in root.parents:
        fail("RCW_PATH_OVERLAP", "Source and wiki directories must be disjoint")
    if root.exists() and any(root.iterdir()):
        fail("RCW_OUTPUT_NOT_EMPTY", "Initialize in an empty wiki directory")
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    cfg = validate(
        CorpusConfig,
        {
            "schema_version": "1.0",
            "corpus_id": root.name,
            "title": title,
            "profile": profile,
            "default_access": access,
            "source_roots": [
                {
                    "root_id": "primary",
                    "path": Path(os.path.relpath(sources, root)).as_posix(),
                    "read_only": True,
                }
            ],
        },
    )
    (root / "wiki.yaml").write_text(yaml_text(cfg))
    (root / "rcw.lock").write_text(
        'skill_version = "0.1.0"\nschema_version = "1.0"\npython_version = "3.12"\nconfig_digest = "'
        + digest(cfg)
        + '"\n'
    )
    for name in TABLES:
        path = root / "data" / (name + ".jsonl")
        path.parent.mkdir(exist_ok=True, mode=0o700)
        path.write_text("")
    for name in ("sources", "concepts", "entities", "findings", "debates", "themes", "gaps", "answers"):
        (root / "pages" / name).mkdir(parents=True, exist_ok=True, mode=0o700)
    for name in ("operations", "leases"):
        (root / "state" / name).mkdir(parents=True, exist_ok=True, mode=0o700)
    write_json(root / "state/manifest.json", {})
    (root / ".gitignore").write_text("build/\nstate/operations/\nstate/leases/\n*.rcw-tmp\n")
    return {"root": str(root), "initialized": True, "profile": profile, "access": access}


def status(root):
    tables = load_tables(root)
    report = inventory(root)
    return {
        "counts": {key: len(value) for key, value in tables.items()},
        "inventory": {
            state: sum(item["status"] == state for item in report["items"])
            for state in ("new", "changed", "unchanged", "blocked")
        },
        "missing_sources": report["missing"],
        "unverified_claims": sum(c["review_state"] == "unverified" for c in tables["claims"].values()),
        "open_gaps": sum(g["status"] == "open" for g in tables["gaps"].values()),
        "lease_active": safe_path(root, "state/leases/corpus.lock").exists(),
    }


def sync_plan(root):
    report = inventory(root)
    return {
        "pending": [item for item in report["items"] if item["status"] in {"new", "changed"}],
        "blocked": [item for item in report["items"] if item["status"] == "blocked"],
        "unchanged": sum(item["status"] == "unchanged" for item in report["items"]),
        "missing": report["missing"],
        "next_action": "Prepare and apply each pending package sequentially; checkpoint after each apply, then analyze changed claims.",
    }


def review_packet(root):
    tables = load_tables(root)
    return {
        "skill_version": "0.1.0",
        "counts": {key: len(value) for key, value in tables.items()},
        "audit": audit(root, "pr"),
        "operations": list(tables["operations"].values()),
        "gaps": list(tables["gaps"].values()),
        "unverified_claims": [
            c["id"] for c in tables["claims"].values() if c["review_state"] in {"unverified", "disputed"}
        ],
        "access_counts": {
            access: sum(c["access"] == access for c in tables["claims"].values())
            for access in ("public", "internal", "confidential", "restricted")
        },
    }


__all__ = [
    "init_corpus",
    "inventory",
    "ingest_prepare",
    "ingest_apply",
    "analyze_prepare",
    "analyze_apply",
    "ask_prepare",
    "ask_complete",
    "audit",
    "status",
    "sync_plan",
    "render",
    "export_citations",
    "review_packet",
    "recover",
    "reindex",
]


def register_metadata(root, key, metadata):
    from .storage import source_root

    if ":" not in key:
        fail("RCW_METADATA_INVALID", "Use the inventory key root_id:relative_path")
    root_id, relative = key.split(":", 1)
    path = safe_path(source_root(root, root_id), relative)
    if not path.is_file():
        fail("RCW_SOURCE_MISSING", key)
    value = validate(Metadata, metadata)
    target = safe_path(root, "metadata/" + content_id("meta", key) + ".json")
    with lease(root, "metadata"):
        write_json(target, value)
    return {"key": key, "metadata_path": str(target)}
