"""Disposable, access-filtered wiki views and interoperable citation exports."""

import html
import json
from pathlib import Path

from .audit import audit
from .pages import FOLDERS
from .storage import ACCESS, canonical, config, digest, fail, load_tables, safe_path


def permitted_claims(tables, access):
    if access not in ACCESS:
        fail("RCW_ACCESS_POLICY", access)
    result = {}
    for cid, claim in tables["claims"].items():
        if ACCESS[claim["access"]] > ACCESS[access] or claim["review_state"] == "superseded":
            continue
        slices = [tables["slices"][key] for key in claim["slice_ids"]]
        if any(ACCESS[s["access"]] > ACCESS[access] for s in slices):
            continue
        if access == "public" and any(not s["publication_allowed"] for s in slices):
            continue
        result[cid] = claim
    return result


CSS = """body{margin:0;background:#f5f4ef;color:#172d32;font:17px/1.6 system-ui,sans-serif}header,main,footer{max-width:1100px;margin:auto;padding:28px}header{border-bottom:1px solid #bcc9c5}h1{font-size:2.7rem;letter-spacing:-.04em;line-height:1.1}a{color:#006762}input,select{padding:12px;border:1px solid #9eaead;border-radius:6px;font:inherit;margin:4px}input{width:min(60vw,560px)}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}.card{background:white;border:1px solid #d5dfd9;border-radius:10px;padding:20px}.tag{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:#4f635e}.status{font-weight:600}blockquote{border-left:3px solid #1c847b;padding-left:16px}footer{font-size:13px}button{font:inherit;padding:8px} [hidden]{display:none!important}"""


def document(title, body, home="index.html"):
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'
        + html.escape(title)
        + "</title><style>"
        + CSS
        + '</style></head><body><header><a href="'
        + home
        + '">Research corpus</a></header><main>'
        + body
        + "</main><footer>Generated from versioned research records. Mechanical validation does not establish that a claim is true.</footer></body></html>\n"
    )


def metadata_display(source):
    metadata = source["metadata"]
    if metadata["consent"] and not metadata["consent"]["identify"]:
        return "Interview source", "Participant"
    return metadata["title"], metadata["creator"]


def evidence_html(claim, tables):
    parts = [
        "<h1>Evidence record</h1><p>" + html.escape(claim["text"]) + "</p>",
        '<p class="status">'
        + html.escape(claim["review_state"])
        + " · "
        + html.escape(claim["evidence_type"])
        + "</p>",
    ]
    for sid in claim["slice_ids"]:
        s = tables["slices"][sid]
        source = tables["sources"][s["source_id"]]
        title, creator = metadata_display(source)
        locator = s["locator"]
        parts.append(
            '<section class="card"><h2>'
            + html.escape(title)
            + "</h2><p>"
            + html.escape(creator)
            + "</p><p>"
            + html.escape(locator["heading"])
            + f" · {html.escape(locator['kind'])} {locator['line_start']}–{locator['line_end']}</p>"
        )
        if s["excerpt"]:
            parts.append("<blockquote>" + html.escape(s["excerpt"]) + "</blockquote>")
        else:
            parts.append(
                "<p>Open the protected source at the locator above. Verbatim reproduction is not permitted.</p>"
            )
        if source["metadata"]["url"]:
            parts.append(
                '<p><a rel="noopener noreferrer" href="'
                + html.escape(source["metadata"]["url"], quote=True)
                + '">Open original source</a></p>'
            )
        parts.append(
            '<p class="tag">Source '
            + html.escape(source["id"])
            + "<br>Slice "
            + html.escape(sid)
            + "</p></section>"
        )
    return document("Evidence record", "\n".join(parts), "../index.html")


def markdown_safe(text):
    # Escape active HTML and Markdown link/image injection in generated prose.
    return html.escape(text).replace("[", "\\[").replace("]", "\\]").replace("!", "\\!")


def render(root, output, adapter="html", access="internal"):
    report = audit(root, "pr")
    if not report["ok"]:
        fail("RCW_AUDIT_FAILED", json.dumps(report["errors"]))
    if adapter not in {"html", "quartz"}:
        fail("RCW_RENDERER_INVALID", adapter)
    root, output = Path(root).resolve(), Path(output).resolve()
    cfg = config(root)
    if output == root or output in root.parents:
        fail("RCW_PATH_OVERLAP", "Build cannot replace the corpus or its parent")
    for folder in ("data", "pages", "state"):
        protected = root / folder
        if output == protected or output.is_relative_to(protected):
            fail("RCW_PATH_OVERLAP", str(output))
    for item in cfg["source_roots"]:
        protected = (root / item["path"]).resolve()
        if output == protected or output.is_relative_to(protected) or protected.is_relative_to(output):
            fail("RCW_PATH_OVERLAP", "Build overlaps source tree")
    tables = load_tables(root)
    claims = permitted_claims(tables, access)
    eligible = [
        p
        for p in tables["pages"].values()
        if ACCESS[p["access"]] <= ACCESS[access] and set(p["claim_ids"]).issubset(claims) and p["claim_ids"]
    ]
    eligible.sort(key=lambda row: (row["page_type"], row["title"], row["id"]))
    files = {}
    if adapter == "html":
        cards = []
        for p in eligible:
            title = p["title"]
            if any(
                tables["sources"][sid]["metadata"]["consent"]
                and not tables["sources"][sid]["metadata"]["consent"]["identify"]
                for sid in p["source_ids"]
            ):
                title = "Interview evidence"
            cards.append(
                '<article class="card" data-type="'
                + p["page_type"]
                + '"><div class="tag">'
                + p["page_type"]
                + " · "
                + p["review_state"]
                + '</div><h2><a href="pages/'
                + p["id"]
                + '.html">'
                + html.escape(title)
                + "</a></h2><p>"
                + html.escape(p["assertions"][0]["text"])
                + "</p></article>"
            )
            body = (
                "<h1>" + html.escape(title) + '</h1><p class="tag">' + html.escape(p["review_state"]) + "</p>"
            )
            for a in p["assertions"]:
                body += (
                    "<p>"
                    + html.escape(a["text"])
                    + "</p><p>"
                    + " ".join(
                        '<a href="../evidence/' + cid + '.html">Evidence ' + str(i + 1) + "</a>"
                        for i, cid in enumerate(a["claim_ids"] + a["opposing_claim_ids"])
                    )
                    + "</p>"
                )
            files["pages/" + p["id"] + ".html"] = document(title, body, "../index.html")
        controls = (
            '<h1>Explore the research</h1><p>Follow a finding to its evidence, compare sources, and identify what remains unresolved.</p><label>Search <input id="search" type="search" placeholder="Find a concept, source, or claim"></label><label>Page type <select id="type"><option value="">All types</option>'
            + "".join("<option>" + kind + "</option>" for kind in sorted({p["page_type"] for p in eligible}))
            + '</select></label><p id="count"></p><div class="grid">'
            + "".join(cards)
            + "</div>"
        )
        script = """<script>const cards=[...document.querySelectorAll('.card')],q=document.getElementById('search'),t=document.getElementById('type');function filter(){let n=0;for(const c of cards){c.hidden=!(c.textContent.toLowerCase().includes(q.value.toLowerCase())&&(!t.value||c.dataset.type===t.value));if(!c.hidden)n++}document.getElementById('count').textContent=n+' pages'}q.addEventListener('input',filter);t.addEventListener('change',filter);filter();</script>"""
        files["index.html"] = document("Research corpus", controls + script)
        for cid, claim in sorted(claims.items()):
            files["evidence/" + cid + ".html"] = evidence_html(claim, tables)
    else:
        index = [
            "---",
            "title: Research corpus",
            "---",
            "",
            "# Research corpus",
            "",
            "Open a page, then follow its claim links to the evidence.",
            "",
        ]
        for p in eligible:
            path = f"content/{FOLDERS[p['page_type']]}/{p['id']}.md"
            title = p["title"]
            if any(
                tables["sources"][sid]["metadata"]["consent"]
                and not tables["sources"][sid]["metadata"]["consent"]["identify"]
                for sid in p["source_ids"]
            ):
                title = "Interview evidence"
            text = [
                "---",
                "title: " + json.dumps(title),
                "tags: [" + p["page_type"] + ", " + p["review_state"] + "]",
                "---",
                "",
                "# " + markdown_safe(title),
                "",
            ]
            for a in p["assertions"]:
                text.append(
                    markdown_safe(a["text"])
                    + " "
                    + " ".join(
                        f"[[evidence/{cid}|Evidence]]" for cid in a["claim_ids"] + a["opposing_claim_ids"]
                    )
                )
            files[path] = "\n\n".join(text) + "\n"
            index.append(f"- [[{FOLDERS[p['page_type']]}/{p['id']}|{markdown_safe(title)}]]")
        files["content/index.md"] = "\n".join(index) + "\n"
        for cid, claim in sorted(claims.items()):
            parts = [
                "---",
                "title: Evidence record",
                "---",
                "",
                "# Evidence record",
                "",
                markdown_safe(claim["text"]),
                "",
                "**Review:** " + claim["review_state"],
            ]
            for sid in claim["slice_ids"]:
                s = tables["slices"][sid]
                source = tables["sources"][s["source_id"]]
                title, creator = metadata_display(source)
                parts.extend(
                    [
                        "",
                        "## " + markdown_safe(title),
                        markdown_safe(creator),
                        "Locator: " + markdown_safe(canonical(s["locator"])),
                    ]
                )
                if s["excerpt"]:
                    parts.append("> " + markdown_safe(s["excerpt"]))
                if source["metadata"]["url"]:
                    # Encode parens so a source URL cannot terminate the Markdown destination.
                    url = (
                        source["metadata"]["url"].replace("(", "%28").replace(")", "%29").replace(" ", "%20")
                    )
                    parts.append("[Original source](<" + html.escape(url, quote=True) + ">)")
            files["content/evidence/" + cid + ".md"] = "\n".join(parts) + "\n"
    # Export only allowed relationships; counts and identifiers follow the same access filter.
    relations = [
        r
        for r in tables["relationships"].values()
        if ACCESS[r["access"]] <= ACCESS[access]
        and r["subject"] in claims
        and r["object"] in claims
        and set(r["claim_ids"]).issubset(claims)
    ]
    files["graph.json"] = (
        canonical(
            {
                "nodes": [
                    {"id": c["id"], "label": c["text"]}
                    for c in sorted(claims.values(), key=lambda value: value["id"])
                ],
                "edges": relations,
            }
        )
        + "\n"
    )
    manifest = {
        "producer": "research-corpus-wiki",
        "version": "0.1.0",
        "adapter": adapter,
        "access": access,
        "files": {name: digest(text.encode()) for name, text in sorted(files.items())},
    }
    if output.exists() and any(output.iterdir()):
        old_manifest = output / "build-manifest.json"
        if not old_manifest.exists():
            fail("RCW_OUTPUT_NOT_EMPTY", "Use an empty output directory")
        old = json.loads(old_manifest.read_text())
        if old.get("producer") != "research-corpus-wiki":
            fail("RCW_OUTPUT_NOT_OWNED", str(output))
        for name, expected in old["files"].items():
            path = safe_path(output, name)
            if path.exists() and digest(path.read_bytes()) != expected:
                fail("RCW_OUTPUT_EDITED", name)
        for name in set(old["files"]) - set(files):
            safe_path(output, name).unlink(missing_ok=True)
    output.mkdir(parents=True, exist_ok=True, mode=0o700)
    for name, text in files.items():
        path = safe_path(output, name)
        path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        path.write_text(text, encoding="utf-8")
    (output / "build-manifest.json").write_text(canonical(manifest) + "\n")
    return {
        "adapter": adapter,
        "access": access,
        "output": str(output),
        "pages": len(eligible),
        "claims": len(claims),
        "manifest": manifest,
    }


def export_citations(root, format="csl-json", access="internal"):
    tables = load_tables(root)
    claims = permitted_claims(tables, access)
    sources = {sid for c in claims.values() for sid in c["source_ids"]}
    items = [
        r["csl"]
        for r in sorted(tables["citations"].values(), key=lambda value: value["id"])
        if r["source_id"] in sources and ACCESS[r["access"]] <= ACCESS[access]
    ]
    if format == "csl-json":
        return items
    if format != "bibtex":
        fail("RCW_EXPORT_INVALID", format)

    def escape(value):
        return (
            str(value)
            .replace("\\", "\\textbackslash{}")
            .replace("{", "\\{")
            .replace("}", "\\}")
            .replace("%", "\\%")
            .replace("&", "\\&")
            .replace("#", "\\#")
            .replace("_", "\\_")
        )

    rendered = []
    for item in items:
        kind = (
            "article" if item["type"] == "article-journal" else ("book" if item["type"] == "book" else "misc")
        )
        fields = {
            "title": item["title"],
            "author": " and ".join(a["literal"] for a in item["author"]),
            "note": "; ".join(str(item[k]) for k in ("type", "jurisdiction", "note") if k in item),
        }
        for csl_key, bib_key in (("DOI", "doi"), ("URL", "url")):
            if csl_key in item:
                fields[bib_key] = item[csl_key]
        if "issued" in item:
            fields["year"] = item["issued"]["literal"][:4]
        rendered.append(
            "@"
            + kind
            + "{"
            + item["id"]
            + ",\n"
            + ",\n".join("  " + key + " = {" + escape(value) + "}" for key, value in fields.items())
            + "\n}"
        )
    return "\n\n".join(rendered) + ("\n" if rendered else "")
