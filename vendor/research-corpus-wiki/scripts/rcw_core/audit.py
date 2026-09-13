"""Mechanical integrity checks; these never claim semantic entailment."""

import re
from pathlib import Path

from .pages import MARKER, assertion_markdown, blocks, frontmatter
from .sources import resolve_slice
from .storage import ACCESS, RCWError, config, load_tables, safe_path


def audit_tables(root, tables, page_overrides=None):
    errors: list[dict] = []
    warnings: list[dict] = []
    page_overrides = page_overrides or {}
    all_ids = set()

    def issue(code, identity, detail, warning=False):
        (warnings if warning else errors).append({"code": code, "id": identity, "detail": detail})

    for table, records in tables.items():
        for identity in records:
            if identity in all_ids:
                issue("RCW_DUPLICATE_ID", identity, table)
            all_ids.add(identity)

    def refs(row, target, ids):
        for identity in ids:
            if identity not in tables[target]:
                issue("RCW_REFERENCE_MISSING", row["id"], identity)
            elif ACCESS[row["access"]] < ACCESS[tables[target][identity]["access"]]:
                issue("RCW_ACCESS_LEAK", row["id"], identity)

    for row in tables["source_versions"].values():
        if row["source_id"] not in tables["sources"] or row["package_id"] not in tables["packages"]:
            issue("RCW_REFERENCE_MISSING", row["id"], "Source or package missing")
    for row in tables["slices"].values():
        refs(row, "source_versions", [row["source_version_id"]])
        if row["source_version_id"] not in tables["source_versions"]:
            continue
        version = tables["source_versions"][row["source_version_id"]]
        if row["source_id"] != version["source_id"]:
            issue("RCW_REFERENCE_MISMATCH", row["id"], "Slice and version identify different sources")
        if not row["quotation_allowed"] and row["excerpt"]:
            issue("RCW_CONSENT_QUOTE", row["id"], "Quotation is not permitted")
        try:
            text = resolve_slice(root, row, tables)
            if row["excerpt"] and row["excerpt"] not in " ".join(text.split()):
                issue("RCW_LOCATOR_MISMATCH", row["id"], "Excerpt is absent from source slice")
        except (RCWError, OSError, KeyError) as error:
            issue(
                getattr(error, "code", "RCW_SOURCE_MISSING"),
                row["id"],
                str(error),
                warning=version["status"] == "superseded",
            )
    for row in tables["claims"].values():
        refs(row, "slices", row["slice_ids"])
        if any(sid not in tables["sources"] for sid in row["source_ids"]):
            issue("RCW_REFERENCE_MISSING", row["id"], "Claim source is missing")
        if row["review_state"] in {"unverified", "disputed", "superseded"}:
            issue("RCW_CLAIM_REVIEW", row["id"], row["review_state"], warning=True)
        if row["lineage_status"] == "original_missing" and row["review_state"] not in {
            "unverified",
            "disputed",
            "superseded",
        }:
            issue("RCW_LINEAGE_INVALID", row["id"], "Missing original cannot be verified")
    for table in ("entities", "relationships", "pages", "gaps"):
        for row in tables[table].values():
            refs(row, "claims", row["claim_ids"])
    for row in tables["relationships"].values():
        for key in ("subject", "object"):
            if row[key] not in all_ids:
                issue("RCW_REFERENCE_MISSING", row["id"], row[key])
            else:
                for target, records in tables.items():
                    if row[key] in records:
                        refs(row, target, [row[key]])
    alias_map: dict[str, str] = {}
    for row in tables["pages"].values():
        for alias in [row["title"], *row["aliases"]]:
            key = alias.casefold()
            if key in alias_map and alias_map[key] != row["id"]:
                issue("RCW_ALIAS_COLLISION", row["id"], alias, warning=True)
            alias_map[key] = row["id"]
        try:
            path = safe_path(root, row["path"])
            text = page_overrides.get(row["path"])
            if text is None:
                text = path.read_text(encoding="utf-8")
            metadata, body = frontmatter(text)
            regions = blocks(body)
            for field, target in (
                ("page_id", "id"),
                ("claim_ids", "claim_ids"),
                ("source_ids", "source_ids"),
                ("access", "access"),
                ("review_state", "review_state"),
                ("page_type", "page_type"),
                ("title", "title"),
            ):
                if metadata.get(field) != row[target]:
                    issue("RCW_FRONTMATTER_DRIFT", row["id"], field)
            cited = set()
            for (owner, block), (start, end) in regions.items():
                if not owner.startswith("human:"):
                    cited.update(re.findall(r"\[@claim:([a-z0-9_]+)\]", body[start:end]))
                    actual = MARKER.sub("", body[start:end]).strip()
                    expected = "\n".join(assertion_markdown(a) for a in row["assertions"]).strip()
                    if actual != expected:
                        issue(
                            "RCW_PAGE_CONTENT_DRIFT",
                            row["id"],
                            "Generated content differs from the registered assertions",
                        )
            if cited != set(row["claim_ids"]):
                issue("RCW_PAGE_EVIDENCE_DRIFT", row["id"], "Generated citations differ from the ledger")
            for assertion in row["assertions"]:
                if not assertion["claim_ids"]:
                    issue("RCW_EVIDENCE_REQUIRED", row["id"], "Uncited material assertion")
                for identity in assertion["claim_ids"] + assertion["opposing_claim_ids"]:
                    if identity not in row["claim_ids"]:
                        issue("RCW_PAGE_EVIDENCE_DRIFT", row["id"], identity)
        except (RCWError, OSError, KeyError, ValueError) as error:
            issue(getattr(error, "code", "RCW_PAGE_INVALID"), row["id"], str(error))
    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": {name: len(records) for name, records in tables.items()},
        "semantic_entailment": "requires reviewer judgment",
    }


def audit(root, level="working"):
    try:
        config(root)
        tables = load_tables(root)
        result = audit_tables(root, tables)
        if level in {"pr", "release"}:
            secret = re.compile(
                r"gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}"
            )
            for folder in ("data", "pages"):
                for path in (Path(root) / folder).rglob("*"):
                    if path.is_file() and secret.search(path.read_text(encoding="utf-8")):
                        result["errors"].append(
                            {
                                "code": "RCW_SECRET_FOUND",
                                "id": path.relative_to(root).as_posix(),
                                "detail": "Credential pattern detected; value omitted",
                            }
                        )
            result["ok"] = not result["errors"]
        result["level"] = level
        return result
    except (RCWError, ValueError, OSError) as error:
        return {
            "ok": False,
            "errors": [{"code": getattr(error, "code", "RCW_AUDIT_FAILED"), "detail": str(error)}],
            "warnings": [],
            "counts": {},
            "level": level,
        }
