"""Evidence wiki adapter: bounded packets and strict dossier proposals over the real rcw kernel.

Canonical wiki records are written only by `rcw ingest apply` from the pinned vendor kernel, invoked as
a trusted argv with shell=False. This module never edits wiki/data or pages. A dossier is an auxiliary,
validated record that stores the claim IDs the kernel actually created plus the exact original locators.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from . import collect, core, intake

RCW_SCRIPT = Path(__file__).resolve().parents[1] / "vendor" / "research-corpus-wiki" / "scripts" / "rcw.py"
WIKI_DIR, SOURCES_DIR, PACKET_DIR, PROPOSAL_DIR = "wiki", "sources", "packets", "proposals"
SEAL_DIR, DOSSIER_DIR = "state/packets", "wiki/dossiers"  # dossiers sit outside rcw's canonical digest
OP_RE = re.compile(r"^op_[0-9a-f]{32}$")
CODE_SUFFIXES = collect.SOURCE_SUFFIXES - collect.DOC_SUFFIXES - collect.RCW_SUFFIXES  # .py .ts .toml .yaml ...
PACKET_SCHEMA, DOSSIER_SCHEMA = "map-agents.packet/1", "map-agents.dossier/1"
FACETS = ("specifications", "components", "design-choices", "workflows", "skills-patterns", "interfaces",
          "memory-state", "orchestration", "tools-permissions", "evaluation", "dependencies", "limitations", "relevance")
KINDS, BASES = ("observation", "inference"), ("documented", "code-inspected")
EVIDENCE_TYPE = {"documented": "organizational_statement", "code-inspected": "contextual_fact"}
CONFIDENCE = {"observation": 0.8, "inference": 0.5}
STALE_CODES = {"RCW_BASE_DIVERGED", "RCW_SOURCE_MUTATED", "RCW_OPERATION_MISSING", "RCW_PACKET_INVALID"}
BOUNDS = {"max_claims": 40, "min_claim_chars": 12, "max_claim_chars": 400, "max_summary_chars": 800,
          "max_slices_per_claim": 8, "max_proposal_bytes": 200_000, "max_packet_slices": 400,
          "max_slice_chars": 1500, "max_packet_bytes": 2_000_000}
CLAIM_KEYS = {"facet", "text", "slice_ids", "kind", "basis"}
DOSSIER_KEYS = {"schema_version", "operation_id", "repo", "commit", "snapshot_id", "base_digest", "summary", "claims"}
KERNEL_TIMEOUT = 300.0
MAX_DOSSIER_BYTES = 2_000_000
SCOPE_KEYS = ("population", "jurisdiction", "timeframe", "setting", "method", "instrument_status", "qualifiers")
PROPOSAL_JSON_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema", "title": "map-agents dossier proposal",
    "type": "object", "additionalProperties": False, "required": sorted(DOSSIER_KEYS),
    "properties": {
        "schema_version": {"const": DOSSIER_SCHEMA},
        "operation_id": {"type": "string", "pattern": OP_RE.pattern}, "repo": {"type": "string"},
        "commit": {"type": "string", "pattern": "^[0-9a-f]{40}$"}, "snapshot_id": {"type": "string", "pattern": "^[0-9a-f]{16}$"},
        "base_digest": {"type": "string"},
        "summary": {"type": "string", "minLength": 1, "maxLength": BOUNDS["max_summary_chars"]},
        "claims": {"type": "array", "maxItems": BOUNDS["max_claims"], "items": {
            "type": "object", "additionalProperties": False, "required": sorted(CLAIM_KEYS),
            "properties": {
                "facet": {"enum": list(FACETS)}, "kind": {"enum": list(KINDS)}, "basis": {"enum": list(BASES)},
                "text": {"type": "string", "minLength": BOUNDS["min_claim_chars"], "maxLength": BOUNDS["max_claim_chars"]},
                "slice_ids": {"type": "array", "minItems": 1, "maxItems": BOUNDS["max_slices_per_claim"], "uniqueItems": True,
                              "items": {"type": "string", "pattern": "^slc_[0-9a-f]{64}$"}},
            }}},
    },
}


class WikiError(core.WorkbenchError):
    code = 10


class ProposalRejected(WikiError):
    code = 11


class StalePacket(WikiError):
    code = 12


class SourceIntegrityError(WikiError):
    """Stored snapshot bytes or metadata no longer match the collector's recorded provenance."""

    code = 14


class DossierInvalid(WikiError):
    """Auxiliary dossier fails its seal or its correspondence with record and kernel tables."""

    code = 15


class KernelError(WikiError):
    """The kernel refused an operation; `rcw_code` is its stable error code."""

    code = 13

    def __init__(self, rcw_code: str, message: str) -> None:
        super().__init__(f"{rcw_code}: {message}")
        self.rcw_code = rcw_code


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_bounded(path: Path, max_bytes: int, label: str, error: type[WikiError] = ProposalRejected) -> bytes:
    """Read at most max_bytes+1 bytes; never trust a stat() size for the bound."""
    if not path.is_file():
        raise WikiError(f"{label} not found: {path.name}")
    with open(path, "rb") as fh:
        data = fh.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise error(f"{label} exceeds {max_bytes} bytes")
    return data


def _parse_object(data: bytes, label: str, error: type[WikiError] = ProposalRejected) -> dict:
    try:
        obj = json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        raise error(f"{label} is not valid UTF-8 JSON") from exc
    if not isinstance(obj, dict):
        raise error(f"{label} must be a JSON object")
    return obj


def _read_json(path: Path, max_bytes: int, label: str) -> dict:
    return _parse_object(_read_bounded(path, max_bytes, label), label)


def _kernel_digest(value: object) -> str:
    """The kernel's own digest format (compact sorted JSON) so stored proposal digests can be re-verified."""
    return "sha256:" + _sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def verify_snapshot(root: Path, key: str, active: dict) -> tuple[dict, dict]:
    """Check the active snapshot against the collector's provenance BEFORE the kernel sees it.

    Every stored member must be a direct, non-symlink child of the snapshot directory whose bytes match the
    recorded size, SHA-256 and Git blob hash, and the rcw manifest must carry the same identifiers.
    """
    root = Path(root)
    for rel in (active.get("dir"), active.get("snapshot"), active.get("package")):
        if not isinstance(rel, str) or "\\" in rel or ".." in Path(rel).parts or Path(rel).is_absolute() or not rel.startswith(f"{SOURCES_DIR}/"):
            raise SourceIntegrityError(f"snapshot pointer escapes sources/: {rel}")
    snap_dir, snap_file, package = root / active["dir"], root / active["snapshot"], root / active["package"]
    try:
        collect._safe_storage(root, snap_dir)
    except core.WorkbenchError as exc:
        raise SourceIntegrityError(str(exc)) from exc
    if not snap_dir.is_dir() or not snap_file.is_file() or not package.is_file():
        raise SourceIntegrityError(f"active snapshot package missing on disk: {active['package']}")
    if snap_file.parent != snap_dir or package.parent != snap_dir:
        raise SourceIntegrityError("snapshot record and manifest must sit in the snapshot directory")
    snapshot = _parse_object(_read_bounded(snap_file, MAX_DOSSIER_BYTES, "snapshot record", SourceIntegrityError),
                             "snapshot record", SourceIntegrityError)
    manifest = _parse_object(_read_bounded(package, MAX_DOSSIER_BYTES, "package manifest", SourceIntegrityError),
                             "package manifest", SourceIntegrityError)
    if (snapshot.get("snapshot_id"), snapshot.get("commit"), snapshot.get("repo"), snapshot.get("dir"), snapshot.get("package")) != (
            active["snapshot_id"], active["commit"], key, active["dir"], active["package"]):
        raise SourceIntegrityError("snapshot record does not match the catalog record's active snapshot")
    files = snapshot.get("files")
    if not isinstance(files, list) or not files:
        raise SourceIntegrityError("snapshot record lists no files")
    members = {m.get("path"): m.get("metadata") for m in manifest.get("files", []) if isinstance(m, dict)}
    if manifest.get("complete") is not True or len(members) != len(files):
        raise SourceIntegrityError("package manifest is incomplete or lists a different member set")
    for f in files:
        target = snap_dir / str(f.get("stored"))
        if not collect._contained(snap_dir, target) or not target.is_file():
            raise SourceIntegrityError(f"stored member escapes or is missing: {f.get('stored')}")
        data = _read_bounded(target, int(f["size"]), f"stored {f['path']}", SourceIntegrityError)
        if len(data) != int(f["size"]) or _sha256(data) != f["sha256"] or collect.git_blob_sha(data) != f["git_sha"]:
            raise SourceIntegrityError(f"stored bytes differ from recorded SHA-256/Git blob hash: {f['path']}")
        meta = members.get(f["stored"])
        ids = meta.get("identifiers") if isinstance(meta, dict) else None
        if ids != {"repository": key, "commit": active["commit"], "path": f["path"], "git_sha": f["git_sha"],
                   "snapshot_id": active["snapshot_id"]} or meta.get("url") != f["url"]:
            raise SourceIntegrityError(f"package metadata disagrees with the snapshot record: {f['path']}")
    return snapshot, manifest


def rcw(wiki: Path, *args: str, timeout: float = KERNEL_TIMEOUT) -> dict:
    """Run one real kernel command. Arguments are trusted literals; source text never reaches argv."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    argv = [sys.executable, str(RCW_SCRIPT), *args]
    proc = subprocess.run(argv, capture_output=True, shell=False, timeout=timeout, env=env)
    out = proc.stdout.decode("utf-8", "replace")
    try:
        payload = json.loads(out) if out.strip() else None
    except ValueError:
        payload = None
    if proc.returncode == 0 and isinstance(payload, dict):
        return payload
    if isinstance(payload, dict) and "ok" in payload:  # audit returns its report with exit 3
        return payload
    err = proc.stderr.decode("utf-8", "replace").strip().splitlines()
    try:
        detail = json.loads(err[-1]) if err else {}
    except ValueError:
        detail = {}
    code = detail.get("error") if isinstance(detail, dict) else None
    message = detail.get("message") if isinstance(detail, dict) else None
    raise KernelError(str(code or f"RCW_EXIT_{proc.returncode}"), str(message or (err[-1][:300] if err else "no output")))


def _wiki_root(root: Path) -> Path:
    return Path(root) / WIKI_DIR


def _ensure_wiki(root: Path) -> bool:
    """Initialize the rcw corpus once, with sources/ and wiki/ as disjoint sibling roots."""
    wiki = _wiki_root(root)
    if (wiki / "wiki.yaml").exists():
        return False
    (root / SOURCES_DIR).mkdir(parents=True, exist_ok=True)
    rcw(wiki, "init", str(wiki), "--sources", str(root / SOURCES_DIR), "--profile", "mixed",
        "--access", "internal", "--title", "Map the Agents evidence corpus")
    return True


def _record(root: Path, repo: str) -> tuple[str, dict[str, dict], dict]:
    key, _canonical, reason = intake.normalize(f"https://github.com/{repo}")
    if not key:
        raise WikiError(f"repository rejected: {reason or 'not-github'}")
    repos = core.load_repos(root)
    record = repos.get(key)
    if record is None or not isinstance(record.get("latest_snapshot"), dict):
        raise WikiError(f"no snapshot recorded for {key}; run snapshot first")
    return key, repos, record


def _locator(source: dict, line_start: int | None = None, line_end: int | None = None) -> dict:
    loc = {"repository": source["repository"], "commit": source["commit"], "path": source["path"],
           "git_sha": source["git_sha"], "url": source["url"]}
    if line_start is not None:
        loc.update({"line_start": line_start, "line_end": line_end, "url": f"{source['url']}#L{line_start}-L{line_end}"})
    return loc


def prepare(root: Path, repo: str) -> dict:
    """Prepare a real rcw ingest operation for the repository's active snapshot and emit a bounded packet."""
    root = Path(root)
    with core.writer_lock(root):
        core.init_locked(root)
        key, _repos, record = _record(root, repo)
        active = record["latest_snapshot"]
        snapshot, _manifest = verify_snapshot(root, key, active)  # bytes and metadata checked before any kernel call
        initialized = _ensure_wiki(root)
        wiki = _wiki_root(root)
        rel = Path(active["package"]).relative_to(SOURCES_DIR).as_posix()
        item = next((i for i in rcw(wiki, "inventory", str(wiki))["items"] if i["path"] == rel), None)
        if item is None:
            raise WikiError(f"kernel inventory does not list the active package: {rel}")
        if item["status"] == "blocked":
            raise WikiError(f"kernel blocks the package: {'; '.join(item['errors'])[:300]}")
        packet = rcw(wiki, "ingest", "prepare", str(wiki), item["key"])
        by_stored = {f["stored"]: f for f in snapshot["files"]}
        sources: dict[str, dict] = {}
        for src in packet["sources"]:
            info = by_stored.get(Path(src["path"]).name)
            if info is None:
                raise WikiError(f"kernel source not in snapshot record: {src['path']}")
            sources[src["id"]] = {"source_id": src["id"], "stored": info["stored"], "repository": key, "commit": active["commit"],
                                  "path": info["path"], "git_sha": info["git_sha"], "sha256": info["sha256"],
                                  "url": info["url"], "lines": info["lines"]}
        slices, omitted = [], 0
        for s in packet["slices"]:
            if len(slices) >= BOUNDS["max_packet_slices"]:
                omitted += 1
                continue
            loc, text = s["locator"], s["text"]
            slices.append({"slice_id": s["id"], "source_id": s["source_id"], "heading": loc["heading"],
                           "locator": _locator(sources[s["source_id"]], loc["line_start"], loc["line_end"]),
                           "text": text[:BOUNDS["max_slice_chars"]], "truncated": len(text) > BOUNDS["max_slice_chars"]})
        out = {
            "schema_version": PACKET_SCHEMA, "kind": "dossier-packet", "operation_id": packet["operation_id"],
            "repo": key, "commit": active["commit"], "snapshot_id": active["snapshot_id"], "package": active["package"],
            "inventory_key": item["key"], "package_id": item["package_id"], "package_status": item["status"],
            "base_digest": packet["base_digest"], "source_tree_digest": packet["source_tree_digest"],
            "created_at": packet["created_at"], "already_indexed": record.get("indexed_snapshot_id") == active["snapshot_id"],
            "rcw_packet": f"{WIKI_DIR}/state/operations/{packet['operation_id']}/packet.json",
            "sources": sorted(sources.values(), key=lambda v: v["path"]), "slices": slices, "omitted_slices": omitted,
            "facets": list(FACETS), "kinds": list(KINDS), "bases": list(BASES), "bounds": dict(BOUNDS),
            "proposal_schema": PROPOSAL_JSON_SCHEMA,
            "proposal_contract": {
                "schema_version": DOSSIER_SCHEMA,
                "required": sorted(DOSSIER_KEYS),
                "bindings": "operation_id, repo, commit, snapshot_id and base_digest must equal this packet's values",
                "summary": f"plain text, 1..{BOUNDS['max_summary_chars']} chars",
                "claims": f"0..{BOUNDS['max_claims']} objects with exactly {sorted(CLAIM_KEYS)}; facet in facets, kind in kinds, "
                          f"basis in bases, slice_ids 1..{BOUNDS['max_slices_per_claim']} IDs from this packet, "
                          f"text {BOUNDS['min_claim_chars']}..{BOUNDS['max_claim_chars']} chars paraphrased (no 21-word verbatim runs)",
                "basis": "code-inspected requires at least one cited slice from a code/config file (by original path); "
                         "documentation slices alone are 'documented'. This checks evidence linkage, not truth.",
                "gaps": "every facet without a claim is recorded as an explicit unknown; do not infer to fill it",
            },
            "untrusted_source_notice": packet["untrusted_source_notice"],
        }
        data = core.dump_json(out)
        if len(data) > BOUNDS["max_packet_bytes"]:
            raise WikiError(f"packet exceeds {BOUNDS['max_packet_bytes']} bytes; reduce the snapshot selection")
        packet_path = root / PACKET_DIR / f"{packet['operation_id']}.json"
        core.atomic_write_bytes(packet_path, data)
        core.write_if_changed(root / SEAL_DIR / f"{packet['operation_id']}.json", core.dump_json(
            {"packet_sha256": _sha256(data), "repo": key, "snapshot_id": active["snapshot_id"]}))
    return {"root": str(root), "repo": key, "operation_id": packet["operation_id"], "packet": packet_path.relative_to(root).as_posix(),
            "commit": active["commit"], "snapshot_id": active["snapshot_id"], "package_status": item["status"],
            "already_indexed": out["already_indexed"], "sources": len(sources), "slices": len(slices),
            "omitted_slices": omitted, "wiki_initialized": initialized}


def load_packet(root: Path, packet_path: Path) -> dict:
    root, packet_path = Path(root), Path(packet_path)
    data = _read_bounded(packet_path, BOUNDS["max_packet_bytes"], "packet", WikiError)
    packet = _parse_object(data, "packet", WikiError)
    if packet.get("schema_version") != PACKET_SCHEMA:
        raise WikiError("packet schema mismatch")
    if not isinstance(packet.get("operation_id"), str) or not OP_RE.match(packet["operation_id"]):
        raise WikiError("packet operation_id is not a kernel operation ID")
    seal_path = root / SEAL_DIR / f"{packet['operation_id']}.json"
    if not seal_path.is_file():
        raise StalePacket(f"packet has no seal in this corpus: {packet.get('operation_id')}")
    if json.loads(seal_path.read_bytes()).get("packet_sha256") != _sha256(data):
        raise StalePacket("packet bytes differ from their seal")
    return packet


def validate_proposal(proposal: dict, packet: dict) -> list[dict]:
    """Strict dossier proposal check against its packet. Returns normalized claims."""
    keys = set(proposal)
    if keys != DOSSIER_KEYS:
        raise ProposalRejected(f"proposal keys must be exactly {sorted(DOSSIER_KEYS)}; got {sorted(keys)}")
    if proposal["schema_version"] != DOSSIER_SCHEMA:
        raise ProposalRejected(f"unsupported schema_version: {proposal['schema_version']!r}")
    for field in ("operation_id", "repo", "commit", "snapshot_id", "base_digest"):
        if proposal[field] != packet[field]:
            raise ProposalRejected(f"{field} does not match the packet")
    summary = proposal["summary"]
    if not isinstance(summary, str) or not summary.strip() or len(summary) > BOUNDS["max_summary_chars"]:
        raise ProposalRejected(f"summary must be 1..{BOUNDS['max_summary_chars']} chars")
    claims = proposal["claims"]
    if not isinstance(claims, list) or len(claims) > BOUNDS["max_claims"]:
        raise ProposalRejected(f"claims must be a list of at most {BOUNDS['max_claims']}")
    known = {s["slice_id"]: s for s in packet["slices"]}
    seen: set[tuple] = set()
    out = []
    for n, claim in enumerate(claims):
        if not isinstance(claim, dict) or set(claim) != CLAIM_KEYS:
            raise ProposalRejected(f"claim {n} keys must be exactly {sorted(CLAIM_KEYS)}")
        if claim["facet"] not in FACETS:
            raise ProposalRejected(f"claim {n} unsupported facet {claim['facet']!r}")
        if claim["kind"] not in KINDS or claim["basis"] not in BASES:
            raise ProposalRejected(f"claim {n} unsupported kind/basis {claim['kind']!r}/{claim['basis']!r}")
        text = claim["text"].strip() if isinstance(claim["text"], str) else ""
        if not BOUNDS["min_claim_chars"] <= len(text) <= BOUNDS["max_claim_chars"]:
            raise ProposalRejected(f"claim {n} text must be {BOUNDS['min_claim_chars']}..{BOUNDS['max_claim_chars']} chars")
        ids = claim["slice_ids"]
        if (not isinstance(ids, list) or not ids or len(ids) > BOUNDS["max_slices_per_claim"]
                or any(not isinstance(i, str) for i in ids) or len(set(ids)) != len(ids)):
            raise ProposalRejected(f"claim {n} needs 1..{BOUNDS['max_slices_per_claim']} distinct slice_ids")
        foreign = [i for i in ids if i not in known]
        if foreign:
            raise ProposalRejected(f"claim {n} cites slice IDs outside this packet: {foreign[0][:80]}")
        if claim["basis"] == "code-inspected" and not any(
                Path(known[i]["locator"]["path"]).suffix.lower() in CODE_SUFFIXES for i in ids):
            raise ProposalRejected(f"claim {n} is code-inspected but cites no code/config slice (documentation only)")
        identity = (text, tuple(sorted(ids)))
        if identity in seen:
            raise ProposalRejected(f"claim {n} duplicates an earlier claim")
        seen.add(identity)
        out.append({"facet": claim["facet"], "text": text, "slice_ids": sorted(ids), "kind": claim["kind"], "basis": claim["basis"]})
    return out


def translate(claims: list[dict], packet: dict) -> dict:
    """Dossier claims -> allowed rcw ingest proposal (claims + one repository entity, no relationships)."""
    drafts = [{
        "key": f"c{n:03d}-{c['facet']}", "text": c["text"], "slice_ids": c["slice_ids"],
        "evidence_type": EVIDENCE_TYPE[c["basis"]], "polarity": "affirmed", "extraction_confidence": CONFIDENCE[c["kind"]],
        "scope": {**{k: None for k in SCOPE_KEYS}, "method": c["basis"], "qualifiers": f"kind={c['kind']}; facet={c['facet']}",
                  "setting": f"{packet['repo']}@{packet['commit'][:12]} snapshot {packet['snapshot_id']}"},
    } for n, c in enumerate(claims)]
    # Shape mirrors the kernel's validated dump (defaults filled) so its stored proposal_digest can be re-verified.
    entities = [{"key": "repository", "name": packet["repo"], "entity_type": "program", "aliases": [],
                 "external_ids": {"github": packet["repo"]}, "claim_keys": [d["key"] for d in drafts]}] if drafts else []
    return {"schema_version": "1.0", "operation_id": packet["operation_id"], "claims": drafts, "entities": entities, "relationships": []}


def _rows(wiki: Path, table: str) -> list[dict]:
    path = wiki / "data" / f"{table}.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] if path.exists() else []


def _identity(draft: dict) -> tuple:
    scope = {k: draft["scope"].get(k) for k in SCOPE_KEYS}
    return (draft["text"], tuple(sorted(draft["slice_ids"])), json.dumps(scope, sort_keys=True), draft["evidence_type"], draft["polarity"])


def _reconcile_claims(wiki: Path, drafts: list[dict]) -> list[dict]:
    """Current kernel rows matching each translated claim's full identity (the kernel's own content-ID inputs)."""
    index: dict[tuple, list[dict]] = {}
    for row in _rows(wiki, "claims"):
        index.setdefault(_identity(row), []).append(row)
    out = []
    for d in drafts:
        found = [r for r in index.get(_identity(d), []) if r["review_state"] != "superseded"]
        if len(found) != 1:
            raise WikiError(f"kernel claim reconciliation failed for {d['text'][:40]!r} ({len(found)} current matches)")
        out.append(found[0])
    return out


def seal(dossier: dict) -> dict:
    body = {k: v for k, v in dossier.items() if k != "seal"}
    return {**body, "seal": _sha256(core.dump_json(body))}


def _finish(root: Path, packet: dict, proposal: dict, claims: list[dict], rows: list[dict], result: dict, repos: dict, record: dict) -> dict:
    """Auxiliary writes after a confirmed kernel commit: sealed dossier, then catalog record."""
    wiki, key = _wiki_root(root), packet["repo"]
    entity = next((r["id"] for r in _rows(wiki, "entities") if r.get("external_ids", {}).get("github") == key), None)
    slices = {s["slice_id"]: s for s in packet["slices"]}
    owner, name = key.split("/")
    dossier_path = root / DOSSIER_DIR / owner / name / packet["commit"] / f"{packet['snapshot_id']}.json"
    prior = _parse_object(_read_bounded(dossier_path, MAX_DOSSIER_BYTES, "dossier", DossierInvalid), "dossier", DossierInvalid) if dossier_path.is_file() else {}
    current_ids = {r["id"] for r in rows}
    superseded = sorted((set(prior.get("superseded_claim_ids", [])) | {c["claim_id"] for c in prior.get("claims", [])}) - current_ids)
    present = {c["facet"] for c in claims}
    dossier = seal({
        "schema_version": DOSSIER_SCHEMA, "repo": key, "commit": packet["commit"], "snapshot_id": packet["snapshot_id"],
        "package": packet["package"], "package_id": packet["package_id"],
        "applied_operation_id": packet["operation_id"] if result["changed"] else prior.get("applied_operation_id", packet["operation_id"]),
        "entity_id": entity, "summary": proposal["summary"].strip(),
        "claims": [{"claim_id": r["id"], "review_state": r["review_state"], **c, "evidence_type": EVIDENCE_TYPE[c["basis"]],
                    "locators": [slices[s]["locator"] for s in c["slice_ids"]]} for r, c in zip(rows, claims)],
        "superseded_claim_ids": superseded,
        "facets": {f: sum(1 for c in claims if c["facet"] == f) for f in FACETS},
        "gaps": [{"facet": f, "status": "unknown", "reason": "no source-linked claim submitted for this facet"}
                 for f in FACETS if f not in present],
        "sources": packet["sources"],
    })
    dossier_changed = core.write_if_changed(dossier_path, core.dump_json(dossier))
    record.pop("last_error", None)
    record.update({"indexed_snapshot_id": packet["snapshot_id"], "indexed_commit": packet["commit"], "status": "distilled",
                   "freshness": "current", "dossier": dossier_path.relative_to(root).as_posix(),
                   "indexed_operation_id": dossier["applied_operation_id"], "claims": len(rows)})
    changed = core.save_repos(root, repos)
    return {"dossier": record["dossier"], "dossier_changed": dossier_changed, "record_changed": changed, "entity_id": entity,
            "gaps": [g["facet"] for g in dossier["gaps"]], "superseded_claim_ids": superseded}


def apply(root: Path, packet_path: Path, proposal_path: Path) -> dict:
    """Validate a dossier proposal, apply it through the real kernel, then store the dossier and record state."""
    root = Path(root)
    packet = load_packet(root, packet_path)
    proposal = _read_json(Path(proposal_path), BOUNDS["max_proposal_bytes"], "proposal")
    claims = validate_proposal(proposal, packet)
    wiki, op = _wiki_root(root), packet["operation_id"]
    translated = translate(claims, packet)
    proposal_sha = _sha256(core.dump_json({"summary": proposal["summary"].strip(), "claims": claims}))
    kernel_sha = _kernel_digest({k: v for k, v in translated.items() if k != "operation_id"})
    with core.writer_lock(root):
        key, repos, record = _record(root, packet["repo"])
        if record["latest_snapshot"]["snapshot_id"] != packet["snapshot_id"]:
            raise StalePacket(f"packet snapshot {packet['snapshot_id']} superseded by {record['latest_snapshot']['snapshot_id']}")
        receipt_path = root / SEAL_DIR / f"{op}.receipt.json"
        applied = next((o for o in _rows(wiki, "operations") if o["id"] == op), None)
        if applied is not None:
            # The kernel already committed this operation (retry after interruption). Only the identical proposal may finish.
            verify_snapshot(root, key, record["latest_snapshot"])
            receipt = _parse_object(_read_bounded(receipt_path, 4096, "receipt", StalePacket), "receipt", StalePacket) if receipt_path.is_file() else {}
            if applied["state"] != "applied" or applied["proposal_digest"] != kernel_sha or receipt.get("proposal_sha256") != proposal_sha:
                raise ProposalRejected(f"operation {op} was already applied with a different proposal")
            result, reconciled = {"changed": True, "paths": applied["output_paths"]}, True
        else:
            core.write_if_changed(receipt_path, core.dump_json({"operation_id": op, "repo": key, "snapshot_id": packet["snapshot_id"],
                                                                "proposal_sha256": proposal_sha, "kernel_proposal_digest": kernel_sha}))
            rcw_proposal = root / PROPOSAL_DIR / f"{op}.rcw.json"
            core.atomic_write_bytes(rcw_proposal, core.dump_json(translated))
            try:
                result, reconciled = rcw(wiki, "ingest", "apply", str(wiki), op, str(rcw_proposal)), False
            except KernelError as exc:
                receipt_path.unlink(missing_ok=True)
                if exc.rcw_code in STALE_CODES:
                    raise StalePacket(str(exc)) from exc
                raise
        rows = _reconcile_claims(wiki, translated["claims"])
        aux = _finish(root, packet, proposal, claims, rows, result, repos, record)
    return {"root": str(root), "repo": key, "operation_id": op, "changed": result["changed"], "reconciled": reconciled,
            "kernel_paths": len(result["paths"]), "claims": len(rows), "claim_ids": [r["id"] for r in rows],
            "status": record["status"], "freshness": record["freshness"], **aux}


def _check(cond: bool, why: str) -> None:
    if not cond:
        raise DossierInvalid(why)


def load_dossier(root: Path, repo: str, tables: dict | None = None) -> dict:
    """Public validated loader for maps: seal, record correspondence, kernel claim/slice/source fields, exact locators.

    Raises DossierInvalid; never trusts the auxiliary JSON alone. Passing `tables` avoids re-reading kernel JSONL.
    Validation covers evidence linkage and integrity, not the truth of any claim.
    """
    root, wiki = Path(root), _wiki_root(Path(root))
    key, _repos, record = _record(root, repo)
    rel = record.get("dossier")
    _check(isinstance(rel, str) and rel.startswith(f"{DOSSIER_DIR}/") and ".." not in Path(rel).parts, "record has no dossier path")
    _check((wiki / "wiki.yaml").is_file(), "record claims distilled evidence but the wiki is not initialized")
    dossier = _parse_object(_read_bounded(root / rel, MAX_DOSSIER_BYTES, "dossier", DossierInvalid), "dossier", DossierInvalid)
    _check(dossier.get("schema_version") == DOSSIER_SCHEMA and seal(dossier)["seal"] == dossier.get("seal"), "dossier seal mismatch")
    _check((dossier["repo"], dossier["commit"], dossier["snapshot_id"], dossier["applied_operation_id"], len(dossier["claims"])) == (
        key, record.get("indexed_commit"), record.get("indexed_snapshot_id"), record.get("indexed_operation_id"), record.get("claims")),
        "dossier bindings differ from the catalog record")
    _check(record["latest_snapshot"]["snapshot_id"] == dossier["snapshot_id"] or record.get("freshness") in {"stale", "refresh-failed"},
           "record freshness does not reflect a superseded snapshot")
    summary = dossier.get("summary")
    _check(isinstance(summary, str) and 0 < len(summary) <= BOUNDS["max_summary_chars"], "summary out of bounds")
    t = tables or {name: {r["id"]: r for r in _rows(wiki, name)} for name in ("claims", "slices", "sources", "operations")}
    op = t["operations"].get(dossier["applied_operation_id"])
    _check(op is not None and op["state"] == "applied", "applied operation is not in the kernel operations table")
    facets = {f: 0 for f in FACETS}
    for c in dossier["claims"]:
        _check(set(c) == {"claim_id", "review_state", "facet", "text", "slice_ids", "kind", "basis", "evidence_type", "locators"},
               "claim shape")
        row = t["claims"].get(c["claim_id"])
        _check(row is not None, f"claim not in kernel: {c['claim_id'][:20]}")
        _check(row["text"] == c["text"] and sorted(row["slice_ids"]) == sorted(c["slice_ids"]) == c["slice_ids"]
               and row["evidence_type"] == c["evidence_type"] == EVIDENCE_TYPE.get(c["basis"])
               and row["scope"].get("qualifiers") == f"kind={c['kind']}; facet={c['facet']}" and row["scope"].get("method") == c["basis"]
               and row["review_state"] == c["review_state"] != "superseded" and c["facet"] in FACETS,
               f"claim fields differ from the kernel record: {c['claim_id'][:20]}")
        _check(len(c["locators"]) == len(c["slice_ids"]), "locator count")
        for sid, loc in zip(c["slice_ids"], c["locators"]):
            s_ = t["slices"].get(sid)
            src = t["sources"].get(s_["source_id"]) if s_ else None
            _check(s_ is not None and src is not None, f"slice/source not in kernel: {sid[:20]}")
            ids = src["metadata"]["identifiers"]
            _check(loc == {"repository": ids["repository"], "commit": ids["commit"], "path": ids["path"], "git_sha": ids["git_sha"],
                           "line_start": s_["locator"]["line_start"], "line_end": s_["locator"]["line_end"],
                           "url": f"{src['metadata']['url']}#L{s_['locator']['line_start']}-L{s_['locator']['line_end']}"}
                   and ids["repository"] == key and ids["commit"] == dossier["commit"] and ids["snapshot_id"] == dossier["snapshot_id"],
                   f"locator differs from kernel slice/source: {sid[:20]}")
        facets[c["facet"]] += 1
    _check(dossier["facets"] == facets and [g["facet"] for g in dossier["gaps"]] == [f for f in FACETS if not facets[f]]
           and all(g["status"] == "unknown" for g in dossier["gaps"]), "facet counts or gaps do not match the claims")
    pkg_dir = Path(dossier["package"]).parent.as_posix()
    verify_snapshot(root, key, {"snapshot_id": dossier["snapshot_id"], "commit": dossier["commit"], "package": dossier["package"],
                                "dir": pkg_dir, "snapshot": f"{pkg_dir}/{collect.SNAPSHOT_FILE}"})
    return dossier


def audit(root: Path, level: str = "working") -> dict:
    """Real kernel audit plus full dossier/record/kernel correspondence for every distilled record. Never writes."""
    root, wiki = Path(root), _wiki_root(Path(root))
    if level not in ("working", "pr"):
        raise WikiError("level must be working or pr")
    initialized = (wiki / "wiki.yaml").is_file()
    report = rcw(wiki, "audit", str(wiki), "--level", level) if initialized else {"ok": True, "errors": [], "warnings": []}
    tables = {n: {r["id"]: r for r in _rows(wiki, n)} for n in ("claims", "slices", "sources", "operations")} if initialized else None
    repos, problems, freshness = {}, 0, {}
    for key, record in core.load_repos(root).items():
        freshness[record.get("freshness", "pending")] = freshness.get(record.get("freshness", "pending"), 0) + 1
        if not record.get("indexed_snapshot_id") and record.get("status") != "distilled":
            continue
        entry = {"freshness": record.get("freshness"), "indexed_snapshot_id": record.get("indexed_snapshot_id"), "problems": []}
        try:
            dossier = load_dossier(root, key, tables)
            entry.update({"claims": len(dossier["claims"]), "gaps": len(dossier["gaps"]), "operation_id": dossier["applied_operation_id"]})
        except core.WorkbenchError as exc:
            entry["problems"].append(f"{type(exc).__name__}: {str(exc)[:200]}")
        problems += len(entry["problems"])
        repos[key] = entry
    return {"ok": bool(report["ok"]) and problems == 0, "level": level, "wiki_initialized": initialized,
            "rcw": {"ok": report["ok"], "errors": report.get("errors", [])[:20], "warnings": len(report.get("warnings", []))} if initialized else None,
            "repos": repos, "freshness": dict(sorted(freshness.items())), "problems": problems}
