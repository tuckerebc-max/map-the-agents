"""Read-only source inventory, text extraction, stable versioned slices."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

from .models import Metadata
from .storage import RCWError, config, content_id, digest, fail, fingerprint, source_root, stable_id, validate


class VisibleHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.blocked = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "iframe", "object", "template", "svg"}:
            self.blocked += 1
        if not self.blocked and tag in {"p", "div", "li", "h1", "h2", "h3", "br", "tr", "section"}:
            self.parts.append("\n\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "iframe", "object", "template", "svg"} and self.blocked:
            self.blocked -= 1
        if not self.blocked and tag in {"p", "div", "li", "h1", "h2", "h3", "tr", "section"}:
            self.parts.append("\n\n")

    def handle_data(self, data):
        if not self.blocked:
            self.parts.append(data)


def text_content(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = VisibleHTML()
        parser.feed(text)
        text = re.sub(r"\n\s*\n", "\n\n", "".join(parser.parts)).strip()
    return text.replace("\r\n", "\n").replace("\r", "\n")


def checked_source(base, relative, cfg):
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        fail("RCW_PATH_ESCAPE", str(relative))
    path = base / candidate
    if not path.resolve().is_relative_to(base.resolve()) or path.is_symlink():
        fail("RCW_PATH_ESCAPE", str(relative))
    if not path.is_file():
        fail("RCW_SOURCE_MISSING", str(relative))
    if path.stat().st_size > cfg["source_max_bytes"]:
        fail("RCW_SOURCE_TOO_LARGE", str(relative))
    return path


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        fail("RCW_METADATA_INVALID", str(error))


def metadata_for(path, cfg, supplied=None):
    if supplied is None:
        sidecar = path.with_name(path.name + ".source.json")
        if not sidecar.exists() or sidecar.is_symlink():
            fail("RCW_METADATA_REQUIRED", path.name + ".source.json")
        supplied = load_json(sidecar)
    return validate(Metadata, {"access": cfg["default_access"], **supplied})


def file_entry(root_id, base, relative, metadata, cfg):
    path = checked_source(base, relative, cfg)
    if path.suffix.lower() not in {".md", ".txt", ".html", ".htm"}:
        fail("RCW_UNSUPPORTED_INPUT", relative)
    # Decode now; invalid encodings are an inventory block, not a later crash.
    try:
        text_content(path)
    except UnicodeError:
        fail("RCW_ENCODING_INVALID", relative)
    return {
        "root_id": root_id,
        "path": relative,
        "digest": fingerprint(path),
        "metadata": metadata_for(path, cfg, metadata),
    }


def inventory(root):
    cfg = config(root)
    manifest_path = Path(root) / "state/manifest.json"
    manifest = load_json(manifest_path) if manifest_path.exists() else {}
    items: list[dict] = []
    for entry in cfg["source_roots"]:
        base = (Path(root) / entry["path"]).resolve()
        paths = sorted(p for p in base.rglob("*") if p.is_file() and ".git" not in p.relative_to(base).parts)
        manifests = [p for p in paths if p.name == "manifest.json"]
        # A declared package owns its directory, even when its manifest is invalid.
        loose = [
            p
            for p in paths
            if p.name != "manifest.json"
            and not p.name.endswith(".source.json")
            and not any(m.parent == p.parent or m.parent in p.parents for m in manifests)
        ]
        for path in [*manifests, *loose]:
            rel = path.relative_to(base).as_posix()
            key = entry["root_id"] + ":" + rel
            item = {"key": key, "path": rel, "status": "blocked", "files": [], "errors": []}
            try:
                checked_source(base, rel, cfg)
                if path.name == "manifest.json":
                    package = load_json(path)
                    if set(package) - {"complete", "files", "title", "bibliography", "unresolved_items"}:
                        fail("RCW_SCHEMA_INVALID", "Unknown manifest fields")
                    if package.get("complete") is not True or not package.get("files"):
                        fail("RCW_PACKAGE_INCOMPLETE", key)
                    for member in package["files"]:
                        if set(member) != {"path", "metadata"}:
                            fail("RCW_SCHEMA_INVALID", "Package members require path and metadata")
                        relative = Path(member["path"])
                        if relative.is_absolute() or ".." in relative.parts:
                            fail("RCW_PATH_ESCAPE", member["path"])
                        member_rel = (path.parent.relative_to(base) / relative).as_posix()
                        item["files"].append(
                            file_entry(entry["root_id"], base, member_rel, member["metadata"], cfg)
                        )
                    if len({f["path"] for f in item["files"]}) != len(item["files"]):
                        fail("RCW_DUPLICATE_MEMBER", key)
                    item["manifest_digest"] = fingerprint(path)
                else:
                    override = Path(root) / "metadata" / (content_id("meta", key) + ".json")
                    supplied = (
                        load_json(override) if override.exists() and not override.is_symlink() else None
                    )
                    item["files"] = [file_entry(entry["root_id"], base, rel, supplied, cfg)]
                item["files"].sort(key=lambda value: value["path"])
                item["digest"] = digest(
                    {"files": item["files"], "manifest_digest": item.get("manifest_digest")}
                )
                item["package_id"] = content_id("pkg", [cfg["corpus_id"], item["digest"]])
                prior = manifest.get(key)
                item["status"] = (
                    "unchanged"
                    if prior and prior["digest"] == item["digest"]
                    else ("changed" if prior else "new")
                )
                content_fingerprint = digest([f["digest"] for f in item["files"]])
                duplicate = next(
                    (other for other in items if other.get("content_fingerprint") == content_fingerprint),
                    None,
                )
                item["content_fingerprint"] = content_fingerprint
                if duplicate:
                    item["duplicate_of"] = duplicate["key"]
                # Probe original files only; all source text remains in source roots.
            except (RCWError, ValueError, KeyError, TypeError) as error:
                item["status"] = "blocked"
                item["errors"].append(str(error))
            items.append(item)
    return {
        "items": sorted(items, key=lambda value: value["key"]),
        "missing": sorted(set(manifest) - {item["key"] for item in items}),
    }


def tree_digest(root):
    cfg = config(root)
    entries = {}
    for entry in cfg["source_roots"]:
        base = (Path(root) / entry["path"]).resolve()
        for path in sorted(base.rglob("*")):
            if ".git" in path.relative_to(base).parts:
                continue
            rel = path.relative_to(base).as_posix()
            if path.is_symlink():
                entries[entry["root_id"] + ":" + rel] = "symlink"
            elif path.is_file():
                entries[entry["root_id"] + ":" + rel] = fingerprint(path)
    return digest(entries)


def slice_file(path):
    text = text_content(path)
    lines = text.splitlines()
    blocks = []
    start = None
    heading = ""
    for i, line in enumerate([*lines, ""]):
        if line.startswith("#"):
            if start is not None:
                blocks.append((start, i, heading))
                start = None
            heading = line.lstrip("#").strip()
            continue
        if line.strip() and start is None:
            start = i
        if not line.strip() and start is not None:
            blocks.append((start, i, heading))
            start = None
    return [
        {
            "locator": {
                "kind": "html_block" if path.suffix.lower() in {".html", ".htm"} else "lines",
                "line_start": start + 1,
                "line_end": end,
                "heading": heading,
                "ordinal": ordinal,
            },
            "text": "\n".join(lines[start:end]),
        }
        for ordinal, (start, end, heading) in enumerate(blocks)
    ]


def source_identity(cfg, entry):
    metadata = entry["metadata"]
    identifiers = metadata["identifiers"]
    identity = next(
        (
            (kind, identifiers[kind].strip().lower())
            for kind in ("doi", "official_id", "uri", "transcript_id")
            if identifiers.get(kind)
        ),
        None,
    )
    identity = identity or (
        metadata["url"] if metadata.get("url") else entry["root_id"] + ":" + entry["path"]
    )
    return stable_id("src", [cfg["corpus_id"], identity])


def packet_sources(root, item):
    cfg = config(root)
    sources, versions, slices = [], [], []
    for entry in item["files"]:
        sid = source_identity(cfg, entry)
        vid = content_id("ver", [sid, entry["digest"], digest(entry["metadata"])])
        sources.append(
            {"id": sid, "root_id": entry["root_id"], "path": entry["path"], "metadata": entry["metadata"]}
        )
        versions.append(
            {
                "id": vid,
                "source_id": sid,
                "package_id": item["package_id"],
                "digest": entry["digest"],
                "metadata_digest": digest(entry["metadata"]),
                "root_id": entry["root_id"],
                "path": entry["path"],
                "status": "current",
            }
        )
        path = checked_source(source_root(root, entry["root_id"]), entry["path"], cfg)
        for block in slice_file(path):
            slices.append(
                {
                    "id": content_id("slc", [vid, block["locator"], digest(block["text"].encode())]),
                    "source_id": sid,
                    "source_version_id": vid,
                    **block,
                    "text_digest": digest(block["text"].encode()),
                    "access": entry["metadata"]["access"],
                    "quotation_allowed": not entry["metadata"]["consent"]
                    or entry["metadata"]["consent"]["quote"],
                    "publication_allowed": not entry["metadata"]["consent"]
                    or entry["metadata"]["consent"]["publish"],
                }
            )
    if len({s["id"] for s in sources}) != len(sources):
        fail(
            "RCW_IDENTITY_CONFLICT",
            "A package contains multiple members with the same logical source identity",
        )
    return sources, versions, slices


def resolve_slice(root, slice_row, tables):
    version = tables["source_versions"][slice_row["source_version_id"]]
    path = checked_source(source_root(root, version["root_id"]), version["path"], config(root))
    if fingerprint(path) != version["digest"]:
        fail("RCW_SOURCE_VERSION_UNAVAILABLE", version["id"])
    blocks = slice_file(path)
    number = slice_row["locator"]["ordinal"]
    if (
        number >= len(blocks)
        or blocks[number]["locator"] != slice_row["locator"]
        or digest(blocks[number]["text"].encode()) != slice_row["text_digest"]
    ):
        fail("RCW_LOCATOR_MISMATCH", slice_row["id"])
    return blocks[number]["text"]
