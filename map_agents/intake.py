"""Lead intake: extract public GitHub repository links and record origin/project tags.

Source text is parsed and discarded. Only normalized links and caller-supplied
tags reach catalog/repos.json and catalog/observations.jsonl.
"""

from __future__ import annotations

import ipaddress
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from . import core

MAX_INPUT_BYTES = 1_000_000
MAX_TAG_CHARS = 200
GITHUB_HOSTS = {"github.com", "www.github.com"}
RESERVED_OWNERS = set(
    "about account apps blog codespaces collections contact dashboard enterprise events explore "
    "features issues join login logout marketplace new notifications organizations orgs pricing "
    "pulls search security sessions settings site sponsors topics trending users "
    "stars readme team discussions customer-stories nonprofit git-guides".split()
)
PRIVATE_PARAMS = re.compile(r"(?i)(^|[?&#])(token|access_token|auth|key|api_key|password|secret|private_token)=")
SECRET_SHAPES = re.compile(r"(?i)(ghp_|gho_|ghu_|ghs_|github_pat_)")
OWNER_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")
REPO_RE = re.compile(r"^[A-Za-z0-9._-]{1,100}$")
URL_RE = re.compile(r"https?://[^\s<>\"'`\[\]()]+")
TRAILING = ".,;:!?'\""


class InputTooLarge(core.WorkbenchError):
    code = 3


class BadTag(core.WorkbenchError):
    code = 2


class BadEncoding(core.WorkbenchError):
    code = 7


def read_bounded(stream, max_bytes: int, label: str = "input") -> str:
    """Read at most max_bytes+1 bytes from a binary stream; reject oversize or non-UTF-8 input.

    The caller's declared byte limit therefore bounds memory before ingestion, and a malformed
    byte sequence fails loudly instead of being replaced inside a repository link.
    """
    if not isinstance(max_bytes, int) or max_bytes <= 0:
        raise InputTooLarge('max_bytes must be a positive integer')
    data = stream.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise InputTooLarge(f"{label} exceeds {max_bytes} bytes")
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BadEncoding(f"{label} is not valid UTF-8 at byte {exc.start}") from exc


def _json_strings(node: object, out: list[str]) -> None:
    if isinstance(node, str):
        out.append(node)
    elif isinstance(node, list):
        for item in node:
            _json_strings(item, out)
    elif isinstance(node, dict):
        for item in node.values():
            _json_strings(item, out)


def extract_links(text: str) -> list[str]:
    """Return candidate URLs in first-seen order from prose, Markdown or JSON."""
    found: list[str] = []
    for match in URL_RE.findall(text):
        found.append(match.rstrip(TRAILING))
    try:
        parsed = json.loads(text)
    except ValueError:
        parsed = None
    if parsed is not None:
        strings: list[str] = []
        _json_strings(parsed, strings)
        found.extend(s.strip() for s in strings if s.strip().lower().startswith("http"))
    return list(dict.fromkeys(u for u in found if u))


def _receipt(position: int, url: str, reason: str) -> dict:
    """Rejection receipt without the link. Only the parsed hostname survives; userinfo, path,
    query and fragment are dropped so secret-shaped input never reaches serialized output."""
    try:
        host = (urlsplit(url).hostname or "").lower() or None
    except ValueError:
        host = None
    return {"position": position, "host": host if host in GITHUB_HOSTS else None, "reason": reason}


def _private_host(host: str) -> bool:
    if host in {"localhost", ""} or host.endswith((".local", ".localhost", ".internal", ".lan")):
        return True
    try:
        return not ipaddress.ip_address(host).is_global
    except ValueError:
        return False


def normalize(url: str) -> tuple[str | None, str | None, str | None]:
    """Return (key, canonical_url, reason): key = accepted, reason = rejected, neither = non-GitHub host."""
    if PRIVATE_PARAMS.search(url) or SECRET_SHAPES.search(url):
        return None, None, "private-access-parameter"
    try:
        parts = urlsplit(url)
        host = (parts.hostname or "").lower()
        port = parts.port
    except ValueError:
        return None, None, "malformed"
    if parts.username or parts.password or "@" in parts.netloc:
        return None, None, "credentialed"
    if _private_host(host):
        return None, None, "private-host"
    if host not in GITHUB_HOSTS:
        return None, None, None
    if parts.scheme != "https":
        return None, None, "insecure-scheme"
    if port not in (None, 443):
        return None, None, "unsafe-port"
    raw_path = parts.path
    if "%" in raw_path or "\\" in raw_path or "//" in raw_path or ".." in raw_path.split("/"):
        return None, None, "unsafe-path"
    segments = [s for s in raw_path.split("/") if s]
    if len(segments) < 2:
        return None, None, "not-a-repository"
    owner, repo = segments[0], segments[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    if owner.lower() in RESERVED_OWNERS:
        return None, None, "reserved-route"
    if not OWNER_RE.match(owner) or owner.endswith("-"):
        return None, None, "invalid-owner"
    if not REPO_RE.match(repo) or repo in {".", ".."}:
        return None, None, "invalid-repo"
    key = f"{owner.lower()}/{repo.lower()}"
    return key, f"https://github.com/{owner}/{repo}", None


def _check_tag(name: str, value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise BadTag(f"{name} must be a non-empty string")
    if len(value) > MAX_TAG_CHARS or "\n" in value or "\r" in value:
        raise BadTag(f"{name} must be a single line of at most {MAX_TAG_CHARS} characters")
    return value.strip()


def new_record(key: str, url: str) -> dict:
    owner, repo = key.split("/", 1)
    return {
        "url": url, "owner": owner, "repo": repo, "classes": [], "projects": [], "origins": [],
        "status": "discovered", "latest_commit": None, "indexed_commit": None,
        "freshness": "pending", "sources": [],
    }


def _add_unique(values: list, item: object) -> bool:
    if item in values:
        return False
    values.append(item)
    return True


def ingest(root: Path, text: str, origin: str, project: str, max_bytes: int = MAX_INPUT_BYTES) -> dict:
    """Record origin/project associations for public GitHub repo links found in `text`.

    Budget and tag checks precede the lock and any write. Identical repeats change no bytes.
    """
    root = Path(root)
    origin = _check_tag("origin", origin)
    project = _check_tag("project", project)
    size = len(text.encode("utf-8"))
    if size > max_bytes:
        raise InputTooLarge(f"input is {size} bytes; limit is {max_bytes}")
    candidates = extract_links(text)
    accepted: list[tuple[str, str]] = []
    seen: set[str] = set()
    rejected: list[dict] = []
    ignored = 0
    for position, url in enumerate(candidates):
        key, canonical, reason = normalize(url)
        if key and canonical:
            if key not in seen:
                seen.add(key)
                accepted.append((key, canonical))
        elif reason:
            rejected.append(_receipt(position, url, reason))
        else:
            ignored += 1
    result = {
        "root": str(root), "input_bytes": size, "candidates": len(candidates),
        "accepted": [k for k, _ in accepted], "rejected": rejected, "ignored_hosts": ignored,
        "new_repos": [], "new_associations": 0, "changed": False, "empty": not accepted,
    }
    if not accepted:
        return result
    with core.writer_lock(root):
        core.init_locked(root)
        repos = core.load_repos(root)
        rows = core.load_observations(root)
        for key, canonical in accepted:
            record = repos.get(key)
            if record is None:
                record = repos[key] = new_record(key, canonical)
                result["new_repos"].append(key)
            _add_unique(record["origins"], origin)
            _add_unique(record["projects"], project)
            if _add_unique(rows, {"repo": key, "origin": origin, "project": project}):
                result["new_associations"] += 1
        # Fixed write order; both files only accumulate, so an interruption between them leaves
        # each file complete-old or complete-new, never partial. Repeating the intake heals the gap.
        wrote_repos = core.save_repos(root, repos)
        wrote_obs = core.save_observations(root, rows)
        result["changed"] = wrote_repos or wrote_obs
    return result


def status(root: Path) -> dict:
    root = Path(root)
    repos = core.load_repos(root)
    rows = core.load_observations(root)
    by_status: dict[str, int] = {}
    for record in repos.values():
        label = record.get("status", "unknown")
        by_status[label] = by_status.get(label, 0) + 1
    return {
        "root": str(root), "initialized": (root / core.REPOS_FILE).exists(),
        "repos": len(repos), "associations": len(rows), "by_status": dict(sorted(by_status.items())),
        "origins": sorted({r["origin"] for r in rows}), "projects": sorted({r["project"] for r in rows}),
        "lock_held": (root / core.LOCK_FILE).exists(),
    }
