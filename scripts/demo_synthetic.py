"""Two-class synthetic end-to-end demonstration. Offline, model-free, real rcw kernel.

Everything here is invented fixture data (SYNTHETIC-* repositories). It proves the
pipeline shape: catalog lead -> bounded snapshot -> prepare -> validated proposal ->
apply -> audit -> build -> query, plus one rejected proposal. It is NOT researched
public repository fact and must never be merged into the default live corpus.

Usage: python scripts/demo_synthetic.py [--root work/demo-synthetic]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from map_agents import collect, core, maps, wiki, workers  # noqa: E402

API, RAW = f"https://{collect.API_HOST}", f"https://{collect.RAW_HOST}"
CAT_SHA, ALPHA_SHA, BRAVO_SHA = "c" * 40, "a" * 40, "b" * 40
ALPHA, BRAVO = "synthetic-org/alpha-agent", "synthetic-org/bravo-mux"
FILES = {
    ALPHA: {
        "README.md": b"# Alpha (synthetic)\n\nAlpha is an invented coding agent used only to demonstrate this workbench.\n"
                     b"It plans a task and runs tools in a sandbox.\n\n## Memory\n\nSession state lives in a local SQLite file.\n",
        "docs/design.md": b"# Design\n\nThe planner delegates to a worker loop with a bounded retry budget.\n",
        "src/agent.py": b"class Agent:\n    def run(self, task):\n        return self.loop(task, max_steps=8)\n",
    },
    BRAVO: {
        "README.md": b"# Bravo (synthetic)\n\nBravo is an invented multiplexer that fans one request out to several agents\n"
                     b"and merges their answers.\n\n## Interfaces\n\nA single HTTP endpoint accepts a task and returns a merged result.\n",
        "src/mux.py": b"def fan_out(task, agents):\n    return [a.run(task) for a in agents]\n",
    },
}


def _js(obj: object) -> collect.Response:
    return collect.Response(200, json.dumps(obj).encode("utf-8"))


def _entry(name: str, category: str, repo: str) -> dict:
    return {"name": name, "slug": name.lower(), "category": category, "url": f"https://github.com/{repo}",
            "source_code_url": f"https://github.com/{repo}", "description": f"{name}: synthetic demo entry",
            "license": "Apache-2.0", "source_urls": {}}


def routes() -> dict:
    cat = collect.CATALOG_REPO
    out = {f"{API}/repos/{cat}": _js({"full_name": cat, "private": False, "default_branch": "main"}),
           f"{API}/repos/{cat}/branches/main": _js({"commit": {"sha": CAT_SHA, "commit": {"committer": {"date": "2026-01-01T00:00:00Z"}}}}),
           f"{RAW}/{cat}/{CAT_SHA}/{collect.CATALOG_PATH}": _js([_entry("Alpha", "agent", ALPHA), _entry("Bravo", "multiplexer", BRAVO)])}
    for key, sha in ((ALPHA, ALPHA_SHA), (BRAVO, BRAVO_SHA)):
        files = FILES[key]
        tree = [{"path": p, "type": "blob", "size": len(b), "sha": collect.git_blob_sha(b)} for p, b in files.items()]
        out[f"{API}/repos/{key}"] = _js({"full_name": key, "private": False, "default_branch": "main", "license": {"spdx_id": "Apache-2.0"}})
        out[f"{API}/repos/{key}/branches/main"] = _js({"commit": {"sha": sha, "commit": {"committer": {"date": "2026-01-02T00:00:00Z"}}}})
        out[f"{API}/repos/{key}/git/trees/{sha}?recursive=1"] = _js({"sha": "t" * 40, "truncated": False, "tree": tree})
        for p, b in files.items():
            out[f"{RAW}/{key}/{sha}/{collect.quote(p, safe='/')}"] = collect.Response(200, b)
    return out


class Transport:
    """Serves only the synthetic routes above; every other URL is a 404 so no live network is possible."""

    def __init__(self) -> None:
        self.routes, self.calls = routes(), 0

    def __call__(self, url, headers, timeout, max_bytes):
        self.calls += 1
        return self.routes.get(url, collect.Response(404, b"{}"))


def _claim(facet: str, text: str, ids: list[str], kind: str = "observation", basis: str = "documented") -> dict:
    return {"facet": facet, "text": text, "slice_ids": ids, "kind": kind, "basis": basis}


def _slice(packet: dict, path: str) -> str:
    return next(s["slice_id"] for s in packet["slices"] if s["locator"]["path"] == path)


def proposal(packet: dict) -> dict:
    base = {"schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
            "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"]}
    readme = _slice(packet, "README.md")
    if packet["repo"] == ALPHA:
        claims = [_claim("components", "SYNTHETIC: a planner and a sandboxed tool runner are the documented components.", [readme]),
                  _claim("memory-state", "SYNTHETIC: session state persists in a local SQLite file.", [readme]),
                  _claim("interfaces", "SYNTHETIC: Agent.run(task) bounds the loop at eight steps.", [_slice(packet, "src/agent.py")], basis="code-inspected"),
                  _claim("relevance", "SYNTHETIC: bounded delegation resembles Navy Yard bosun supervision.", [_slice(packet, "docs/design.md")], kind="inference")]
        summary = "SYNTHETIC coding agent: planner plus sandboxed tool loop."
    else:
        claims = [_claim("components", "SYNTHETIC: a fan-out multiplexer and an answer merger are documented.", [readme]),
                  _claim("interfaces", "SYNTHETIC: one HTTP endpoint accepts a task and returns a merged result.", [readme]),
                  _claim("workflows", "SYNTHETIC: fan_out runs every agent on the same task.", [_slice(packet, "src/mux.py")], basis="code-inspected")]
        summary = "SYNTHETIC multiplexer: fan-out to several agents, merged answer."
    return {**base, "summary": summary, "claims": claims}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("work/demo-synthetic"))
    args = parser.parse_args()
    root = args.root
    if root.exists() and (not root.is_dir() or any(root.iterdir())):
        parser.error("demo root must be new or empty; existing content is never removed")
    transport = Transport()
    report: dict = {"synthetic": True, "root": str(root), "steps": []}
    limits = workers.Limits(max_repos=0, max_files=6, max_bytes=20_000, catalog_entries=10, net_bytes=200_000, net_requests=40, max_seconds=120)
    m = workers.maintain(root, limits, transport=transport)
    report["steps"].append({"maintain_catalog_only": {"status": m["status"], "catalog": m["catalog"], "failures": m["failures"]}})
    # maintain()'s automatic snapshot selection keeps README/docs only; the demo requests the code
    # file explicitly (as a small agent or trusted worker recipe would) so a code-inspected claim
    # has a real citation to check against.
    code_path = {ALPHA: "src/agent.py", BRAVO: "src/mux.py"}
    for key in (ALPHA, BRAVO):
        collect.snapshot(root, key, limits.max_files, limits.max_bytes, paths=[code_path[key]], transport=transport)
    for key in (ALPHA, BRAVO):
        prepared = wiki.prepare(root, key)
        packet_path = root / prepared["packet"]
        packet = wiki.load_packet(root, packet_path)
        good = proposal(packet)
        bad = {**good, "claims": [_claim("components", "SYNTHETIC: unsupported claim citing a slice that does not exist.", ["nope-0000"])]}
        bad_path = root / "proposals" / f"{key.replace('/', '__')}-rejected.json"
        bad_path.parent.mkdir(parents=True, exist_ok=True)
        bad_path.write_bytes(core.dump_json(bad))
        try:
            wiki.apply(root, packet_path, bad_path)
            rejected = "NOT rejected (bug)"
        except core.WorkbenchError as exc:
            rejected = f"{type(exc).__name__}: {str(exc)[:120]}"
        good_path = root / "proposals" / f"{key.replace('/', '__')}.json"
        good_path.write_bytes(core.dump_json(good))
        applied = wiki.apply(root, packet_path, good_path)
        report["steps"].append({"repo": key, "packet_slices": len(packet["slices"]), "rejected_proposal": rejected,
                                "applied": {k: applied[k] for k in applied if k in ("repo", "status", "claims", "applied", "operation_id")}})
    audit = wiki.audit(root, "working")
    built = maps.build(root)
    found = maps.query(root, "multiplexer fan-out", limit=3)
    report["steps"] += [{"audit_ok": audit["ok"]}, {"build": {k: built[k] for k in built if k in ("pages", "repos", "written", "changed")}},
                        {"query_hits": [h["path"] for h in found["results"]]}]
    report["network_calls_to_fake_transport"] = transport.calls
    report["live_network"] = False
    report["model_calls"] = 0
    print(json.dumps(report, indent=2, sort_keys=True))
    ok = audit["ok"] and all("NOT rejected" not in s.get("rejected_proposal", "") for s in report["steps"]) and m["status"] != "degraded"
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
