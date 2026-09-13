"""Source-first retrieval, bounded synthesis, and validated answers."""

import re
import sqlite3

from . import pages
from .ingest import commit_changes, make_gap, make_page, relationships
from .models import AnalysisProposal, AnswerProposal
from .operations import check_operation, load_packet, prepare
from .sources import resolve_slice
from .storage import ACCESS, fail, lease, load_tables, safe_path, validate


def reindex(root):
    tables = load_tables(root)
    path = safe_path(root, "build/index.sqlite")
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with sqlite3.connect(path) as conn:
        conn.execute("DROP TABLE IF EXISTS claims_fts")
        conn.execute("CREATE VIRTUAL TABLE claims_fts USING fts5(id UNINDEXED, text, title)")
        for row in sorted(tables["claims"].values(), key=lambda value: value["id"]):
            if row["review_state"] == "superseded":
                continue
            title = " ".join(tables["sources"][sid]["metadata"]["title"] for sid in row["source_ids"])
            conn.execute("INSERT INTO claims_fts VALUES (?, ?, ?)", (row["id"], row["text"], title))
    path.chmod(0o600)
    return {
        "path": str(path),
        "claims": sum(c["review_state"] != "superseded" for c in tables["claims"].values()),
    }


def evidence_packet(root, selected, tables, access):
    claims, slices, warnings = [], {}, []
    for row in selected:
        if ACCESS[row["access"]] > ACCESS[access] or row["review_state"] == "superseded":
            continue
        claim_slices = []
        try:
            for sid in row["slice_ids"]:
                s = tables["slices"][sid]
                if ACCESS[s["access"]] > ACCESS[access]:
                    fail("RCW_ACCESS_LEAK", sid)
                text = resolve_slice(root, s, tables)
                claim_slices.append({**s, "text": text})
        except Exception as error:
            warnings.append({"claim_id": row["id"], "reason": str(error)})
            continue
        claims.append(row)
        for s in claim_slices:
            slices[s["id"]] = s
    source_ids = {sid for row in claims for sid in row["source_ids"]}
    return {
        "claims": claims,
        "slices": list(slices.values()),
        "sources": [tables["sources"][key] for key in sorted(source_ids)],
        "warnings": warnings,
        "access": access,
    }


def ask_prepare(root, question, access="internal", limit=40):
    if access not in ACCESS:
        fail("RCW_ACCESS_POLICY", access)
    if not 1 <= limit <= 500:
        fail("RCW_LIMIT_INVALID", "Limit must be between 1 and 500")
    tables = load_tables(root)
    path = reindex(root)["path"]
    tokens = re.findall(r"\w+", question, flags=re.UNICODE)[:30]
    query = " OR ".join('"' + t.replace('"', '""') + '"' for t in tokens)
    ids = []
    if query:
        with sqlite3.connect(path) as conn:
            ids = [
                r[0]
                for r in conn.execute(
                    "SELECT id FROM claims_fts WHERE claims_fts MATCH ? ORDER BY rank LIMIT ?", (query, limit)
                )
            ]
    payload = evidence_packet(root, [tables["claims"][key] for key in ids], tables, access)
    payload["question"] = question
    payload["retrieval"] = {
        "method": "SQLite FTS5 lexical search",
        "limit": limit,
        "complete_corpus_scan": False,
    }
    payload["relationships"] = [
        r
        for r in tables["relationships"].values()
        if ACCESS[r["access"]] <= ACCESS[access]
        and set(r["claim_ids"]).issubset({c["id"] for c in payload["claims"]})
    ]
    return prepare(root, "ask", payload)


def analyze_prepare(root, scope="changed", access="restricted", limit=200):
    if access not in ACCESS:
        fail("RCW_ACCESS_POLICY", access)
    if not 1 <= limit <= 500:
        fail("RCW_LIMIT_INVALID", "Limit must be between 1 and 500")
    if scope not in {"changed", "full"}:
        fail("RCW_SCOPE_INVALID", scope)
    tables = load_tables(root)
    selected = sorted(
        (
            c
            for c in tables["claims"].values()
            if c["review_state"] != "superseded" and ACCESS[c["access"]] <= ACCESS[access]
        ),
        key=lambda value: value["id"],
    )
    if scope == "changed":
        covered = {
            key
            for p in tables["pages"].values()
            if p["page_type"] in {"finding", "concept", "debate", "theme"}
            for key in p["claim_ids"]
        }
        selected = [c for c in selected if c["id"] not in covered]
    payload = evidence_packet(root, selected[:limit], tables, access)
    payload["scope"] = scope
    payload["remaining_claims"] = max(0, len(selected) - limit)
    payload["pages"] = [p for p in tables["pages"].values() if ACCESS[p["access"]] <= ACCESS[access]]
    payload["entities"] = [e for e in tables["entities"].values() if ACCESS[e["access"]] <= ACCESS[access]]
    payload["relationships"] = [
        r for r in tables["relationships"].values() if ACCESS[r["access"]] <= ACCESS[access]
    ]
    return prepare(root, "analyze", payload)


def check_reproduction(text, source_slice, quote_max_words=20):
    words = re.findall(r"\w+", source_slice["text"].casefold())
    response = " ".join(re.findall(r"\w+", text.casefold()))
    width = 6 if not source_slice["quotation_allowed"] else quote_max_words + 1
    if width and any(
        " ".join(words[i : i + width]) in response for i in range(max(0, len(words) - width + 1))
    ):
        fail(
            "RCW_CONSENT_QUOTE" if not source_slice["quotation_allowed"] else "RCW_QUOTE_LIMIT",
            "Paraphrase the evidence within its reproduction permission",
        )


def validate_assertions(assertions, packet):
    allowed = {c["id"]: c for c in packet["claims"]}
    slices = {s["id"]: s for s in packet["slices"]}
    for assertion in assertions:
        if not assertion["claim_ids"]:
            fail("RCW_EVIDENCE_REQUIRED", "Every material assertion requires a claim from the packet")
        for cid in assertion["claim_ids"] + assertion.get("opposing_claim_ids", []):
            if cid not in allowed:
                fail("RCW_PROPOSAL_OUT_OF_SCOPE", cid)
            for sid in allowed[cid]["slice_ids"]:
                s = slices[sid]
                check_reproduction(assertion["text"], s)


def analyze_apply(root, operation, proposal):
    proposed = validate(AnalysisProposal, proposal)
    with lease(root, operation):
        packet = load_packet(root, operation, "analyze")
        check_operation(packet, proposed)
        tables = load_tables(root)
        allowed = {c["id"] for c in packet["claims"]}
        changes = {}
        if len({p["key"] for p in proposed["pages"]}) != len(proposed["pages"]):
            fail("RCW_DUPLICATE_KEY", "Page keys must be unique")
        for p in proposed["pages"]:
            validate_assertions(p["assertions"], packet)
            ids = {cid for a in p["assertions"] for cid in a["claim_ids"] + a["opposing_claim_ids"]}
            source_ids = {sid for cid in ids for sid in tables["claims"][cid]["source_ids"]}
            row = make_page(
                root, tables, operation, p["page_type"], p["title"], p["key"], p["assertions"], source_ids
            )
            changes[row["path"]] = pages.page_text(root, row, "analysis:" + row["id"])
        for gap in proposed["gaps"]:
            if not set(gap["claim_ids"]).issubset(allowed):
                fail("RCW_PROPOSAL_OUT_OF_SCOPE", "Gap cites a claim outside the packet")
            make_gap(
                tables, operation, gap["question"], gap["reason"], gap["claim_ids"], gap["suggested_source"]
            )
        endpoints = allowed | {e["id"] for e in packet["entities"]} | {s["id"] for s in packet["sources"]}
        relationships(tables, proposed["relationships"], operation, endpoints)
        return commit_changes(root, tables, packet, proposed, changes)


def ask_complete(root, operation, proposal, file_answer=False):
    proposed = validate(AnswerProposal, proposal)
    packet = load_packet(root, operation, "ask")
    check_operation(packet, proposed)
    validate_assertions(proposed["assertions"], packet)
    if proposed["status"] != "insufficient_evidence" and not proposed["assertions"]:
        fail("RCW_EVIDENCE_REQUIRED", "A substantive answer requires cited assertions")
    if proposed["status"] == "insufficient_evidence" and (
        proposed["assertions"] or not proposed["limitations"]
    ):
        fail("RCW_EVIDENCE_REQUIRED", "A refusal has no material assertions and states the evidence gap")
    cited = {cid for a in proposed["assertions"] for cid in a["claim_ids"]}
    uncertain = {
        c["id"] for c in packet["claims"] if c["review_state"] in {"unverified", "disputed", "superseded"}
    }
    if cited & uncertain and (proposed["status"] == "answered" or not proposed["limitations"]):
        fail("RCW_UNVERIFIED_ANSWER", "Missing or disputed original evidence requires a qualified answer")
    lines = ["# " + packet["question"], "", "**Evidence status:** " + proposed["status"], ""]
    for assertion in proposed["assertions"]:
        lines.append(
            assertion["text"]
            + " "
            + " ".join(
                f"[{cid}](evidence/{cid}.html)"
                for cid in assertion["claim_ids"] + assertion["opposing_claim_ids"]
            )
        )
    if proposed["limitations"]:
        lines.extend(["", "## Limitations", *("- " + text for text in proposed["limitations"])])
    result = {"status": proposed["status"], "markdown": "\n\n".join(lines) + "\n", "filed": False}
    if file_answer:
        with lease(root, operation):
            packet = load_packet(root, operation, "ask")
            tables = load_tables(root)
            if proposed["status"] == "insufficient_evidence":
                make_gap(tables, operation, packet["question"], "; ".join(proposed["limitations"]), [])
                changes = {}
            else:
                source_ids = {sid for cid in cited for sid in tables["claims"][cid]["source_ids"]}
                row = make_page(
                    root,
                    tables,
                    operation,
                    "answer",
                    packet["question"],
                    packet["question"].strip().casefold(),
                    proposed["assertions"],
                    source_ids,
                    packet["access"],
                )
                changes = {row["path"]: pages.page_text(root, row, "analysis:" + row["id"])}
            committed = commit_changes(root, tables, packet, proposed, changes)
            result["filed"] = committed["changed"]
    return result
