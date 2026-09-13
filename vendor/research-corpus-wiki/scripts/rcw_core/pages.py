"""Owned page blocks; keep handwritten material byte-for-byte outside a block."""

import re

from ruamel.yaml import YAML

from .storage import fail, safe_path, yaml_text

FOLDERS = {
    "source": "sources",
    "concept": "concepts",
    "entity": "entities",
    "finding": "findings",
    "debate": "debates",
    "theme": "themes",
    "gap": "gaps",
    "answer": "answers",
}
MARKER = re.compile(r"<!-- rcw:(begin|end) owner=([a-z]+:[a-z0-9_-]+) block=([a-z0-9_-]+) -->")


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:70] or "page"


def page_path(kind, title, identity):
    return f"pages/{FOLDERS[kind]}/{slug(title)}-{identity[-12:]}.md"


def frontmatter(text):
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail("RCW_FRONTMATTER_INVALID", "A page requires YAML frontmatter")
    end = text.index("\n---\n", 4) + 5
    return YAML(typ="safe").load(text[4 : end - 5]), text[end:]


def blocks(text):
    stack = None
    found = {}
    matches = list(MARKER.finditer(text))
    if len(re.findall(r"<!--\s*rcw:", text)) != len(matches):
        fail("RCW_MARKER_CONFLICT", "Malformed ownership marker")
    for match in matches:
        action, owner, block = match.groups()
        key = owner, block
        if action == "begin":
            if stack is not None or key in found:
                fail("RCW_MARKER_CONFLICT", "Nested or duplicate ownership marker")
            stack = (key, match.start())
        else:
            if stack is None or stack[0] != key:
                fail("RCW_MARKER_CONFLICT", "Unmatched ownership marker")
            found[key] = (stack[1], match.end())
            stack = None
    if stack:
        fail("RCW_MARKER_CONFLICT", "Missing end marker")
    return found


def assertion_markdown(assertion):
    text = assertion["text"].replace("<!--", "&lt;!--")
    ids = assertion["claim_ids"] + assertion.get("opposing_claim_ids", [])
    return "- " + text + " " + " ".join("[@claim:" + identity + "]" for identity in ids)


def page_text(root, row, owner):
    metadata = {
        "schema_version": "1.0",
        "page_id": row["id"],
        "page_type": row["page_type"],
        "title": row["title"],
        "aliases": row["aliases"],
        "access": row["access"],
        "maturity": row["maturity"],
        "review_state": row["review_state"],
        "claim_ids": row["claim_ids"],
        "source_ids": row["source_ids"],
        "updated_at": row["updated_at"],
    }
    generated = "\n".join(assertion_markdown(a) for a in row["assertions"])
    block = f"<!-- rcw:begin owner={owner} block=evidence -->\n{generated}\n<!-- rcw:end owner={owner} block=evidence -->"
    path = safe_path(root, row["path"])
    if path.exists():
        old_meta, body = frontmatter(path.read_text(encoding="utf-8"))
        if old_meta["page_id"] != row["id"]:
            fail("RCW_PAGE_ID_CONFLICT", row["path"])
        regions = blocks(body)
        key = (owner, "evidence")
        if key not in regions:
            fail("RCW_MARKER_CONFLICT", "The expected generated block is missing")
        start, end = regions[key]
        body = body[:start] + block + body[end:]
    else:
        body = "\n# " + row["title"] + "\n\n" + block + "\n\n## Researcher notes\n\n"
    return "---\n" + yaml_text(metadata) + "---\n" + body
