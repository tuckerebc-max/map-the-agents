"""Validated ingestion: model judgments arrive as proposals, never direct writes."""

import json

from . import pages
from .models import IngestProposal
from .operations import check_operation, load_packet, operation_record, prepare, proposal_digest
from .sources import inventory, packet_sources, tree_digest
from .storage import (
    ACCESS,
    canonical,
    config,
    content_id,
    envelope,
    fail,
    lease,
    load_tables,
    maximum_access,
    safe_path,
    serialized_tables,
    stable_id,
    transaction,
    upsert,
    validate,
    write_json,
)


def ingest_prepare(root, selector):
    report = inventory(root)
    matches = [
        item for item in report["items"] if selector in {item["key"], item["path"], item.get("package_id")}
    ]
    if len(matches) != 1:
        fail("RCW_PACKAGE_AMBIGUOUS", "Select one inventory key or package ID")
    item = matches[0]
    if item["status"] == "blocked":
        fail("RCW_PACKAGE_BLOCKED", "; ".join(item["errors"]))
    sources, versions, slices = packet_sources(root, item)
    return prepare(
        root,
        "ingest",
        {
            "package": item,
            "sources": sources,
            "versions": versions,
            "slices": slices,
            "existing_entities": list(load_tables(root)["entities"].values()),
            "proposal_contract": "schemas/v1/ingest-proposal.schema.json",
        },
    )


def citation(metadata, sid):
    types = {
        "scholarly_article": "article-journal",
        "legislation": "legislation",
        "regulation": "regulation",
        "book": "book",
        "dataset": "dataset",
        "webpage": "webpage",
        "interview": "interview",
        "session": "speech",
    }
    row = {
        "id": sid,
        "type": types.get(metadata["source_type"], "report"),
        "title": metadata["title"],
        "author": [{"literal": metadata["creator"]}],
    }
    if metadata["date"]:
        row["issued"] = {"literal": metadata["date"]}
    if metadata["identifiers"].get("doi") and metadata["source_type"] not in {"legislation", "regulation"}:
        row["DOI"] = metadata["identifiers"]["doi"]
    if metadata["url"]:
        row["URL"] = metadata["url"]
    if metadata["jurisdiction"]:
        row["jurisdiction"] = metadata["jurisdiction"]
    notes = [
        metadata.get(key)
        for key in ("legal_status", "status_date", "provision", "venue")
        if metadata.get(key)
    ]
    if notes:
        row["note"] = "; ".join(notes)
    return row


def make_gap(tables, operation, question, reason, claim_ids, suggested="Original primary evidence"):
    identity = content_id("gap", [question.strip().casefold(), sorted(claim_ids)])
    access = (
        maximum_access([tables["claims"][key]["access"] for key in claim_ids]) if claim_ids else "internal"
    )
    row = {
        **envelope("gap", identity, access, operation, "unverified"),
        "record_type": "gap",
        "question": question,
        "reason": reason,
        "claim_ids": sorted(claim_ids),
        "suggested_source": suggested,
        "status": "open",
    }
    return upsert(tables["gaps"], row)


def make_page(
    root, tables, operation, kind, title, identity_key, assertions, source_ids, access_floor="public"
):
    identity = stable_id("pg", [config(root)["corpus_id"], kind, identity_key])
    claim_ids = sorted({key for a in assertions for key in a["claim_ids"] + a.get("opposing_claim_ids", [])})
    claims = [tables["claims"][key] for key in claim_ids]
    prior = tables["pages"].get(identity)
    row = {
        **envelope("pg", identity, maximum_access([access_floor] + [c["access"] for c in claims]), operation),
        "record_type": "page",
        "page_type": kind,
        "path": prior["path"] if prior else pages.page_path(kind, title, identity),
        "title": title,
        "aliases": prior["aliases"] if prior else [],
        "claim_ids": claim_ids,
        "source_ids": sorted(set(source_ids)),
        "assertions": assertions,
        "maturity": "draft",
    }
    if any(c["review_state"] in {"unverified", "superseded", "disputed"} for c in claims):
        row["review_state"] = "unverified"
    return upsert(tables["pages"], row)


def relationships(tables, drafts, operation, allowed, aliases=None):
    aliases = aliases or {}
    for draft in drafts:
        subject = aliases.get(draft["subject"], draft["subject"])
        obj = aliases.get(draft["object"], draft["object"])
        claims = [aliases.get(value, value) for value in draft["claim_ids"]]
        if (
            subject not in allowed
            or obj not in allowed
            or any(c not in tables["claims"] or c not in allowed for c in claims)
        ):
            fail("RCW_PROPOSAL_OUT_OF_SCOPE", "Unknown relationship endpoint or supporting claim")
        identity = content_id("rel", [subject, draft["predicate"], obj, sorted(claims)])
        endpoint_access = [
            row["access"]
            for records in tables.values()
            for identity, row in records.items()
            if identity in {subject, obj}
        ]
        access = maximum_access(endpoint_access + [tables["claims"][key]["access"] for key in claims])
        row = {
            **envelope("rel", identity, access, operation, "extracted"),
            "record_type": "relationship",
            "subject": subject,
            "predicate": draft["predicate"],
            "object": obj,
            "claim_ids": sorted(claims),
            "rationale": draft["rationale"],
        }
        upsert(tables["relationships"], row)


def commit_changes(root, tables, packet, proposed, page_changes, extra=None):
    from .audit import audit_tables

    for gap in list(tables["gaps"].values()):
        if gap["status"] != "open":
            continue
        assertions = (
            [
                {
                    "text": "Open question: " + gap["question"] + " " + gap["reason"],
                    "claim_ids": gap["claim_ids"],
                    "opposing_claim_ids": [],
                }
            ]
            if gap["claim_ids"]
            else []
        )
        row = make_page(
            root,
            tables,
            packet["operation_id"],
            "gap",
            gap["question"],
            gap["id"],
            assertions,
            [],
            gap["access"],
        )
        page_changes[row["path"]] = pages.page_text(root, row, "gap:" + gap["id"])
    report = audit_tables(root, tables, page_changes)
    if not report["ok"]:
        fail("RCW_AUDIT_FAILED", json.dumps(report["errors"]))
    changes = {**serialized_tables(tables), **page_changes, **(extra or {})}
    changed = [
        rel
        for rel, value in changes.items()
        if not safe_path(root, rel).exists() or safe_path(root, rel).read_text(encoding="utf-8") != value
    ]
    if not changed:
        return {"changed": False, "operation_id": packet["operation_id"], "paths": []}
    op = operation_record(packet, proposed, changed)
    tables["operations"][op["id"]] = op
    changes.update(serialized_tables(tables))
    changes[f"reports/proposals/{packet['operation_id']}.json"] = canonical(proposed) + "\n"

    def check_sources():
        if tree_digest(root) != packet["source_tree_digest"]:
            fail("RCW_SOURCE_MUTATED", "Source tree changed during apply; the corpus change is rolled back")

    check_sources()
    paths = transaction(root, packet["operation_id"], changes, final_check=check_sources)
    write_json(safe_path(root, f"state/operations/{packet['operation_id']}/accepted-proposal.json"), proposed)
    return {"changed": True, "operation_id": packet["operation_id"], "paths": paths}


def ingest_apply(root, operation, proposal):
    proposed = validate(IngestProposal, proposal)
    with lease(root, operation):
        packet = load_packet(root, operation, "ingest")
        check_operation(packet, proposed)
        tables = load_tables(root)
        from .audit import audit

        existing_audit = audit(root)
        if not existing_audit["ok"]:
            # A revised on-disk source may make the previous current version unavailable.
            blocking = [e for e in existing_audit["errors"] if e["code"] != "RCW_SOURCE_VERSION_UNAVAILABLE"]
            if blocking:
                fail("RCW_AUDIT_FAILED", canonical(blocking))
        cfg = config(root)
        p = packet["package"]
        known = tables["packages"].get(p["package_id"])
        if known and known["proposal_digest"] == proposal_digest(proposed) and known["status"] == "active":
            return {"changed": False, "operation_id": operation, "paths": []}
        slice_map = {row["id"]: row for row in packet["slices"]}
        source_map = {row["id"]: row for row in packet["sources"]}
        claim_keys = {}
        draft_keys = [d["key"] for d in proposed["claims"] + proposed["entities"]]
        if len(set(draft_keys)) != len(draft_keys):
            fail("RCW_DUPLICATE_KEY", "Claim and entity keys must be unique within a proposal")
        for c in proposed["claims"]:
            if any(key not in slice_map for key in c["slice_ids"]):
                fail("RCW_PROPOSAL_OUT_OF_SCOPE", "Claim refers to evidence outside this packet")
            from .knowledge import check_reproduction

            for sid in c["slice_ids"]:
                check_reproduction(c["text"], slice_map[sid], cfg["quote_max_words"])
        for s in packet["sources"]:
            previous = tables["sources"].get(s["id"])
            if previous and ACCESS[previous["access"]] > ACCESS[s["metadata"]["access"]]:
                fail(
                    "RCW_ACCESS_DOWNGRADE",
                    "Prepare a separately reviewed redaction product; reingest cannot lower source access",
                )
        current_ids = {s["id"] for s in packet["sources"]}
        version_ids = {v["id"] for v in packet["versions"]}
        for v in tables["source_versions"].values():
            if v["source_id"] in current_ids and v["id"] not in version_ids:
                v["status"] = "superseded"
                v["review_state"] = "superseded"
        for c in tables["claims"].values():
            if set(c["source_ids"]) & current_ids:
                c["review_state"] = "superseded"
        for old in tables["packages"].values():
            if old["key"] == p["key"] and old["id"] != p["package_id"]:
                old["status"] = "superseded"
                old["review_state"] = "superseded"
        for s in packet["sources"]:
            row = {
                **envelope("src", s["id"], s["metadata"]["access"], operation),
                "record_type": "source",
                **s,
            }
            upsert(tables["sources"], row)
            csl = citation(s["metadata"], s["id"])
            cid = stable_id("cit", s["id"])
            upsert(
                tables["citations"],
                {
                    **envelope("cit", cid, s["metadata"]["access"], operation),
                    "record_type": "citation",
                    "source_id": s["id"],
                    "csl": csl,
                },
            )
        for v in packet["versions"]:
            access = source_map[v["source_id"]]["metadata"]["access"]
            upsert(
                tables["source_versions"],
                {**envelope("ver", v["id"], access, operation), "record_type": "source_version", **v},
            )
        for s in packet["slices"]:
            excerpt = (
                " ".join(s["text"].split()[: cfg["quote_max_words"]]) if s["quotation_allowed"] else None
            )
            fields = {key: value for key, value in s.items() if key != "text"}
            upsert(
                tables["slices"],
                {
                    **envelope("slc", s["id"], s["access"], operation),
                    "record_type": "slice",
                    **fields,
                    "excerpt": excerpt,
                },
            )
        for c in proposed["claims"]:
            supporting = [slice_map[key] for key in c["slice_ids"]]
            source_ids = sorted({s["source_id"] for s in supporting})
            original_missing = any(
                source_map[sid]["metadata"]["source_type"] == "synthesis_report" for sid in source_ids
            )
            # A report may quote an authority, but only original source slices can establish its claims.
            identity = content_id(
                "clm",
                [sorted(c["slice_ids"]), c["text"].strip(), c["scope"], c["evidence_type"], c["polarity"]],
            )
            row = {
                **envelope(
                    "clm",
                    identity,
                    maximum_access([s["access"] for s in supporting]),
                    operation,
                    "unverified" if original_missing else "mechanically_checked",
                ),
                "record_type": "claim",
                **{key: value for key, value in c.items() if key != "key"},
                "source_ids": source_ids,
                "lineage_status": "original_missing" if original_missing else "original_available",
            }
            upsert(tables["claims"], row)
            claim_keys[c["key"]] = identity
            if original_missing:
                make_gap(
                    tables,
                    operation,
                    "Obtain the original evidence for: " + c["text"],
                    "The available evidence is a synthesis report; the attributed original has not been verified.",
                    [identity],
                )
        for e in proposed["entities"]:
            if any(key not in claim_keys for key in e["claim_keys"]):
                fail("RCW_PROPOSAL_OUT_OF_SCOPE", "Unknown entity evidence key")
            ids = sorted(claim_keys[key] for key in e["claim_keys"])
            evidence_sources = sorted({sid for cid in ids for sid in tables["claims"][cid]["source_ids"]})
            entity_id = stable_id(
                "ent",
                [
                    cfg["corpus_id"],
                    e["entity_type"],
                    e["external_ids"] or [evidence_sources, e["key"], e["name"].strip().casefold()],
                ],
            )
            previous_entity = tables["entities"].get(entity_id)
            if previous_entity:
                ids = sorted(set(ids) | set(previous_entity["claim_ids"]))
            row = {
                **envelope(
                    "ent",
                    entity_id,
                    maximum_access([tables["claims"][key]["access"] for key in ids]),
                    operation,
                    "extracted",
                ),
                "record_type": "entity",
                **{key: value for key, value in e.items() if key not in {"key", "claim_keys"}},
                "claim_ids": ids,
                "identity_state": "proposed",
            }
            if previous_entity:
                row["access"] = maximum_access([row["access"], previous_entity["access"]])
                row["aliases"] = sorted(
                    set(row["aliases"])
                    | set(previous_entity["aliases"])
                    | ({previous_entity["name"]} - {row["name"]})
                )
                row["identity_state"] = previous_entity["identity_state"]
            upsert(tables["entities"], row)
            claim_keys[e["key"]] = entity_id
        allowed = set(claim_keys.values()) | set(current_ids)
        relationships(tables, proposed["relationships"], operation, allowed, claim_keys)
        page_changes = {}
        for s in packet["sources"]:
            claims = [
                c
                for c in tables["claims"].values()
                if s["id"] in c["source_ids"] and c["review_state"] != "superseded"
            ]
            assertions = [
                {"text": c["text"], "claim_ids": [c["id"]], "opposing_claim_ids": []}
                for c in sorted(claims, key=lambda value: value["id"])
            ]
            row = make_page(
                root,
                tables,
                operation,
                "source",
                s["metadata"]["title"],
                s["id"],
                assertions,
                [s["id"]],
                s["metadata"]["access"],
            )
            page_changes[row["path"]] = pages.page_text(root, row, "source:" + s["id"])
        for e in tables["entities"].values():
            if e["updated_by_operation"] != operation:
                continue
            assertions = [
                {
                    "text": e["name"] + " is mentioned in this evidence.",
                    "claim_ids": e["claim_ids"],
                    "opposing_claim_ids": [],
                }
            ]
            row = make_page(root, tables, operation, "entity", e["name"], e["id"], assertions, [])
            page_changes[row["path"]] = pages.page_text(root, row, "entity:" + e["id"])
        for row in list(tables["pages"].values()):
            if row["page_type"] in {"finding", "concept", "debate", "theme", "answer"} and any(
                tables["claims"][cid]["review_state"] == "superseded" for cid in row["claim_ids"]
            ):
                row["review_state"] = "unverified"
                page_changes[row["path"]] = pages.page_text(root, row, "analysis:" + row["id"])
        package = {
            **envelope(
                "pkg",
                p["package_id"],
                maximum_access([s["metadata"]["access"] for s in packet["sources"]]),
                operation,
            ),
            "record_type": "package",
            "key": p["key"],
            "digest": p["digest"],
            "status": "active",
            "duplicate_of": p.get("duplicate_of"),
            "proposal_digest": proposal_digest(proposed),
            "files": p["files"],
        }
        upsert(tables["packages"], package)
        manifest_path = safe_path(root, "state/manifest.json")
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        manifest[p["key"]] = {"digest": p["digest"], "package_id": p["package_id"]}
        return commit_changes(
            root, tables, packet, proposed, page_changes, {"state/manifest.json": canonical(manifest) + "\n"}
        )
