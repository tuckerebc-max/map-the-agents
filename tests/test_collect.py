"""Behavioral tests for collect: budgets, provenance, resumable catalog, immutable snapshots. Offline."""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import pytest

from map_agents import __main__ as cli
from map_agents import collect, core

API = f"https://{collect.API_HOST}"
RAW = f"https://{collect.RAW_HOST}"
SHA1, SHA2 = "a" * 40, "b" * 40
CAT = collect.CATALOG_REPO
EMPTY_BLOB = "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"  # git hash-object of an empty file
HELLO_BLOB = "ce013625030ba8dba906f756967f9e9ca394464a"  # git hash-object of "hello\n"


class FakeTransport:
    """Routes URLs to responses/callables/exceptions and records every request it sees."""

    def __init__(self, routes: dict) -> None:
        self.routes, self.calls = routes, []

    def __call__(self, url, headers, timeout, max_bytes):
        self.calls.append({"url": url, "headers": dict(headers), "timeout": timeout, "max_bytes": max_bytes})
        hit = self.routes.get(url, collect.Response(404, b"{}"))
        if isinstance(hit, Exception):
            raise hit
        return hit(url) if callable(hit) else hit

    def urls(self, host: str) -> list[str]:
        return [c["url"] for c in self.calls if collect.urlsplit(c["url"]).hostname == host]


def js(obj, status: int = 200) -> collect.Response:
    return collect.Response(status, json.dumps(obj).encode("utf-8"))


def entry(name: str, category: str, repo: str | None, **over) -> dict:
    """Actual-shaped record from _data/agents.json (all 31 fields observed 2026-09-13)."""
    base = {
        "name": name, "slug": name.lower(), "category": category, "maker": "maker", "license": "MIT",
        "url": repo or "https://www.example.org", "source_code_url": repo, "source_available": "True",
        "platforms": [], "first_released": "2025-06-11", "current_release": "2025-06-11", "stars": "854",
        "language": "Python", "homepage": None, "description": "Public blurb " * 40, "mcp_support": "no",
        "plugin_support": "no", "claude_code_plugin": "no", "subagents": "no", "hooks": "no", "plan_mode": "no",
        "model_providers": None, "pricing": "open-source", "install_method": "npm", "docs_url": None,
        "plugin_docs_url": None, "config_docs_url": None, "download_url": None, "maintained": "active",
        "sources": ["github_topic"], "source_urls": {"brad": "https://github.com/bradAGI/awesome-cli-coding-agents"},
    }
    return {**base, **over}


ENTRIES = [
    entry("Alpha", "agent", "https://github.com/Org-A/Alpha"),
    entry("Alpha-SDK", "agent-sdk", "https://github.com/Org-A/Alpha/tree/main/sdk"),  # same repository
    entry("Bravo", "multiplexer", "https://github.com/orgb/bravo"),
    entry("Charlie", "other", "https://github.com/orgc/charlie"),
    entry("Delta", "agent", None, url="https://www.delta.ai", source_available="No (proprietary)"),
    entry("Echo", "new-kind", "https://github.com/orge/echo"),
    entry("Foxtrot", "agent", "https://gitlab.com/orgf/foxtrot"),
    entry("Golf", "agent", None, url="https://github.com/orgg/golf"),  # live shape: muse-code
    entry("Hotel", "other", None, url="https://github.com/orgh"),  # live shape: github-profile (owner only)
]
TOTALS = {"entries": 9, "by_category": {"agent": 4, "agent-sdk": 1, "multiplexer": 1, "new-kind": 1, "other": 2},
          "no_repo": 3, "via_url_fallback": 1, "unique_repos": 5, "unsupported_category": 3}


def head_routes(key: str, sha: str, branch: str = "main", private: bool = False, date: str | None = "2026-01-02T03:04:05Z") -> dict:
    return {
        f"{API}/repos/{key}": js({"full_name": key, "private": private, "default_branch": branch,
                                  "license": {"spdx_id": "Apache-2.0"}}),
        f"{API}/repos/{key}/branches/{collect.quote(branch, safe='')}": js(
            {"commit": {"sha": sha, "commit": {"committer": {"date": date}}}}),
    }


def catalog_routes(sha: str, entries=ENTRIES, raw: bytes | None = None) -> dict:
    body = raw if raw is not None else json.dumps(entries).encode("utf-8")
    return {**head_routes(CAT, sha), f"{RAW}/{CAT}/{sha}/{collect.CATALOG_PATH}": collect.Response(200, body)}


def repo_routes(key: str, sha: str, files: dict[str, bytes], truncated: bool = False, **head) -> dict:
    tree = [{"path": p, "type": "blob", "size": len(b), "sha": collect.git_blob_sha(b)} for p, b in files.items()]
    tree.append({"path": "src", "type": "tree", "sha": "0" * 40})
    routes = {**head_routes(key, sha, **head), f"{API}/repos/{key}/git/trees/{sha}?recursive=1": js(
        {"sha": "t" * 40, "truncated": truncated, "tree": tree})}
    for p, b in files.items():
        routes[f"{RAW}/{key}/{sha}/{collect.quote(p, safe='/')}"] = collect.Response(200, b)
    return routes


def repos_bytes(root: Path) -> bytes:
    return (root / core.REPOS_FILE).read_bytes()


def tree_bytes(base: Path) -> dict[Path, bytes]:
    return {p: p.read_bytes() for p in base.rglob("*") if p.is_file()}


# ---------------------------------------------------------------- catalog

def test_catalog_resumes_fairly_and_repeat_does_not_churn(tmp_path: Path) -> None:
    t = FakeTransport(catalog_routes(SHA1))
    first = collect.catalog(tmp_path, 3, transport=t)
    assert first["range"] == [0, 3] and first["backlog"] == 6 and first["version_changed"] is True
    assert first["totals"] == TOTALS
    feed = tmp_path / first["feed"]
    assert feed.exists() and json.loads((feed.parent / "feed.json").read_text())["digest"] == first["digest"]
    second = collect.catalog(tmp_path, 3, transport=t)
    third = collect.catalog(tmp_path, 3, transport=t)
    assert second["range"] == [3, 6] and third["range"] == [6, 9] and third["backlog"] == 0
    assert len(t.urls(collect.RAW_HOST)) == 1, "feed fetched once and cached at its SHA"
    repos = core.load_repos(tmp_path)
    assert set(repos) == {"org-a/alpha", "orgb/bravo", "orgc/charlie", "orge/echo", "orgg/golf"}
    alpha = repos["org-a/alpha"]
    assert alpha["classes"] == ["agent", "agent-sdk"] and alpha["origins"] == [collect.CATALOG_LABEL]
    assert [s["slug"] for s in alpha["sources"]] == ["alpha", "alpha-sdk"], "shared repo keeps both identities"
    assert alpha["sources"][0]["locator"].endswith(f"/blob/{SHA1}/{collect.CATALOG_PATH}")
    assert len(alpha["sources"][0]["description"]) <= collect.MAX_DESCRIPTION
    assert repos["orge/echo"]["classes"] == [] and repos["orge/echo"]["sources"][0]["category"] == "new-kind"
    golf = repos["orgg/golf"]
    assert golf["classes"] == ["agent"] and golf["sources"][0]["repo_field"] == "url", "public url fallback"
    assert alpha["sources"][0]["repo_field"] == "source_code_url"
    assert sum(r["batch"]["no_repo"] for r in (first, second, third)) == 3
    before = repos_bytes(tmp_path)
    again = collect.catalog(tmp_path, 3, transport=t)
    assert again["processed"] == 0 and again["changed"] is False and repos_bytes(tmp_path) == before
    assert json.loads((tmp_path / collect.CURSOR_FILE).read_text())["next_index"] == 9


def test_catalog_version_change_without_entry_changes_is_quiescent(tmp_path: Path) -> None:
    collect.catalog(tmp_path, 10, transport=FakeTransport(catalog_routes(SHA1)))
    before = repos_bytes(tmp_path)
    result = collect.catalog(tmp_path, 10, transport=FakeTransport(catalog_routes(SHA2)))
    assert result["version_changed"] is True and result["commit"] == SHA2 and result["backlog"] == 0
    assert result["processed"] == 0 and result["changed"] is False and repos_bytes(tmp_path) == before
    alpha = core.load_repos(tmp_path)["org-a/alpha"]
    assert {s["commit"] for s in alpha["sources"]} == {SHA1}, "unchanged entries keep their pinned provenance"
    assert (tmp_path / collect.FEED_DIR / SHA1 / "agents.json").exists(), "old feed capture kept"
    assert json.loads((tmp_path / collect.CURSOR_FILE).read_text())["commit"] == SHA2


def test_catalog_small_batches_progress_across_evolving_feed_commits(tmp_path: Path) -> None:
    """Seam regression: limit=1 against successive head SHAs must not stay on the same prefix."""
    shas = [f"{d}" * 40 for d in "123456789"]
    seen: list[str] = []
    for sha in shas:
        res = collect.catalog(tmp_path, 1, transport=FakeTransport(catalog_routes(sha)))
        seen += res["slugs"]
        assert res["version_changed"] is True and res["processed"] == 1
    assert seen == sorted(e["slug"] for e in ENTRIES) and res["backlog"] == 0
    assert sum(1 for s in seen if s in ("delta", "foxtrot", "hotel")) == 3, "no-repo entries are counted once, truthfully"
    quiet = collect.catalog(tmp_path, 1, transport=FakeTransport(catalog_routes("a" * 40)))
    assert quiet["processed"] == 0 and quiet["backlog"] == 0 and quiet["changed"] is False
    # An earlier entry changes, one is added and one vanishes: only the two pending entries are refreshed.
    evolved = [entry("Alpha", "agent", "https://github.com/Org-A/Alpha", description="Now a multiplexer too"),
               *ENTRIES[1:8], entry("India", "agent", "https://github.com/orgi/india")]
    first = collect.catalog(tmp_path, 1, transport=FakeTransport(catalog_routes("b" * 40, entries=evolved)))
    second = collect.catalog(tmp_path, 1, transport=FakeTransport(catalog_routes("b" * 40, entries=evolved)))
    assert first["backlog"] == 1 and second["backlog"] == 0 and set(first["slugs"] + second["slugs"]) == {"alpha", "india"}
    assert first["dropped"] + second["dropped"] == 1 and first["refreshed"] + second["refreshed"] == 1
    repos = core.load_repos(tmp_path)
    assert repos["org-a/alpha"]["sources"][0]["description"] == "Now a multiplexer too"
    assert repos["org-a/alpha"]["sources"][0]["commit"] == "b" * 40 and "orgi/india" in repos
    assert collect.catalog(tmp_path, 5, transport=FakeTransport(catalog_routes("b" * 40, entries=evolved)))["processed"] == 0


def test_catalog_malformed_or_failed_feed_preserves_cursor(tmp_path: Path) -> None:
    collect.catalog(tmp_path, 2, transport=FakeTransport(catalog_routes(SHA1)))
    cursor_before, repos_before = (tmp_path / collect.CURSOR_FILE).read_bytes(), repos_bytes(tmp_path)
    bad = [catalog_routes(SHA2, raw=b'{"not": "a list"}'), catalog_routes(SHA2, raw=b"\xff\xfe"),
           catalog_routes(SHA2, entries=[{"slug": "x"}]),
           {**head_routes(CAT, SHA2), f"{RAW}/{CAT}/{SHA2}/{collect.CATALOG_PATH}": collect.Response(429, b"")}]
    for routes in bad:
        with pytest.raises(collect.CollectError):
            collect.catalog(tmp_path, 2, transport=FakeTransport(routes))
        assert (tmp_path / collect.CURSOR_FILE).read_bytes() == cursor_before
        assert repos_bytes(tmp_path) == repos_before
        assert not (tmp_path / collect.FEED_DIR / SHA2).exists()
    assert not (tmp_path / core.LOCK_FILE).exists()


def test_catalog_published_index_recorded_separately_and_partial_on_failure(tmp_path: Path, monkeypatch, capsys) -> None:
    routes = {**catalog_routes(SHA1), collect.PUBLISHED_URL: js([{"name": "x"}] * 3)}
    result = collect.catalog(tmp_path, 10, transport=FakeTransport(routes), published=True)
    pub = result["published"]
    assert pub["ok"] is True and pub["entries"] == 3 and pub["backing_entries"] == 9 and pub["discrepancy"] is True
    stored = json.loads((tmp_path / collect.PUBLISHED_FILE).read_text())
    assert stored == {"url": collect.PUBLISHED_URL, "digest": pub["digest"], "entries": 3, "backing_entries": 9}
    assert result["totals"]["entries"] == 9, "backing counts are not reconciled against the published index"
    # Optional source fails: the backing intake still lands and the failure is explicit, not a rollback.
    failing = FakeTransport({**catalog_routes(SHA2), collect.PUBLISHED_URL: collect.Response(503, b"")})
    monkeypatch.setattr(collect, "urllib_transport", failing)
    code = cli.main(["--root", str(tmp_path), "catalog", "--limit", "10", "--published"])
    out = json.loads(capsys.readouterr().out)
    assert code == collect.FetchFailed.code and out["commit"] == SHA2 and out["backlog"] == 0
    assert out["published"] == {"ok": False, "error": "FetchFailed", "code": 8,
                                "message": "http-503 after 3 attempts: https://alltheagents.org/agents.json"}
    assert json.loads((tmp_path / collect.CURSOR_FILE).read_text())["commit"] == SHA2
    assert json.loads((tmp_path / collect.PUBLISHED_FILE).read_text()) == stored, "old published record untouched"


# ---------------------------------------------------------------- transport bounds

@pytest.mark.parametrize("status,needle", [(403, "http-403"), (429, "http-429"), (404, "http-404"), (302, "redirect-refused")])
def test_fetcher_fails_closed_on_status(status: int, needle: str) -> None:
    url = f"{API}/repos/o/r"
    t = FakeTransport({url: collect.Response(status, b"", {"Location": "https://evil.example/x"})})
    with pytest.raises(collect.FetchFailed, match=needle):
        collect.Fetcher(t, collect.Budget(), None).get_bytes(url, 100)
    assert len(t.calls) == 1, "4xx and redirects are not retried"


def test_fetcher_budgets_retries_hosts_and_oversize() -> None:
    url = f"{API}/repos/o/r"
    flaky = FakeTransport({url: collect.Response(503, b"x")})
    with pytest.raises(collect.FetchFailed, match="http-503 after 3 attempts"):
        collect.Fetcher(flaky, collect.Budget(retries=2), None).get_bytes(url, 100)
    assert len(flaky.calls) == 3
    dead = FakeTransport({url: collect.TransportError("URLError")})
    with pytest.raises(collect.FetchFailed, match="transport-URLError after 2 attempts"):
        collect.Fetcher(dead, collect.Budget(retries=1), None).get_bytes(url, 100)
    big = FakeTransport({url: collect.Response(200, b"x" * 101)})
    with pytest.raises(collect.MalformedPayload, match="oversized-payload"):
        collect.Fetcher(big, collect.Budget(), None).get_bytes(url, 100)
    assert big.calls[0]["max_bytes"] == 101, "transport is asked for limit+1 bytes only"
    with pytest.raises(collect.BudgetExceeded, match="byte-budget"):
        collect.Fetcher(big, collect.Budget(max_bytes=0), None).get_bytes(url, 100)
    with pytest.raises(collect.BudgetExceeded, match="time-budget"):
        collect.Fetcher(big, collect.Budget(max_seconds=0), None).get_bytes(url, 100)
    with pytest.raises(collect.BudgetExceeded, match="request-budget"):
        collect.Fetcher(big, collect.Budget(max_requests=0), None).get_bytes(url, 100)
    for bad in ("https://evil.example/x", "http://api.github.com/repos/o/r", "https://github.com/o/r"):
        with pytest.raises(collect.CollectError, match="host-not-allowed"):
            collect.Fetcher(FakeTransport({}), collect.Budget(), None).get_bytes(bad, 100)


def test_retry_attempts_share_the_byte_and_time_budget() -> None:
    url = f"{API}/repos/o/r"
    replies = iter([collect.Response(503, b"fail"), collect.Response(200, b"good")])
    t = FakeTransport({url: lambda _u: next(replies)})
    budget = collect.Budget(max_bytes=5, retries=2)
    with pytest.raises(collect.BudgetExceeded, match=r"byte-budget exceeded .*\(http-200\)"):
        collect.Fetcher(t, budget, None).get_bytes(url, 100)
    assert [c["max_bytes"] for c in t.calls] == [6, 2], "second attempt is bounded by what the first consumed"
    assert budget.bytes_used == 8 and budget.requests == 2
    huge_failure = FakeTransport({url: collect.Response(503, b"x" * 200)})
    with pytest.raises(collect.MalformedPayload, match="oversized-payload"):
        collect.Fetcher(huge_failure, collect.Budget(retries=2), None).get_bytes(url, 100)
    assert len(huge_failure.calls) == 1, "an over-limit failure body is not retried"
    exhausted = FakeTransport({url: collect.Response(503, b"xxxx")})
    with pytest.raises(collect.BudgetExceeded, match="byte-budget"):
        collect.Fetcher(exhausted, collect.Budget(max_bytes=9, retries=5), None).get_bytes(url, 100)
    assert [c["max_bytes"] for c in exhausted.calls] == [10, 6, 2], "cumulative failure bodies exhaust the budget"

    def slow(url, headers, timeout, max_bytes):
        time.sleep(0.05)
        return collect.Response(200, b"late")

    with pytest.raises(collect.BudgetExceeded, match="time-budget exceeded during"):
        collect.Fetcher(slow, collect.Budget(max_seconds=0.01), None).get_bytes(url, 100)


def test_token_reaches_only_api_host_and_never_output(tmp_path: Path, monkeypatch) -> None:
    secret = "ghp_FAKE_TOKEN_FOR_TEST_ONLY"
    monkeypatch.setenv("GITHUB_TOKEN", secret)
    t = FakeTransport(catalog_routes(SHA1))
    result = collect.catalog(tmp_path, 10, transport=t)
    for call in t.calls:
        host = collect.urlsplit(call["url"]).hostname
        assert ("Authorization" in call["headers"]) == (host == collect.API_HOST)
    t.routes.update(head_routes(CAT, SHA2))
    t.routes[f"{RAW}/{CAT}/{SHA2}/{collect.CATALOG_PATH}"] = collect.Response(403, b"")
    with pytest.raises(collect.FetchFailed) as info:
        collect.catalog(tmp_path, 10, transport=t)
    blob = json.dumps(result) + str(info.value) + "".join(p.read_text() for p in tmp_path.rglob("*.json"))
    assert secret not in blob and "Bearer" not in blob


# ---------------------------------------------------------------- snapshot

FILES = {
    "README.md": b"# Alpha\n\nAn agent.\n", "readme.md": b"lowercase twin\n", "x.py": b"print(1)\n",
    "x.py.txt": b"notes about x\n", "src/agent.py": b"def run():\n    return 1\n", "empty.md": b"",
    "docs/my guide #1.md": b"hello\n", "docs/bin.md": b"\xff\xfe broken", "logo.png": b"\x89PNG",
    "docs/CON.md": b"device\n", "docs/bad:name.md": b"colon\n", "docs/trail. /x.md": b"alias\n",
}


def test_git_blob_sha_matches_known_git_values() -> None:
    assert collect.git_blob_sha(b"") == EMPTY_BLOB and collect.git_blob_sha(b"hello\n") == HELLO_BLOB
    assert collect.git_blob_sha(b"hello\n") != hashlib.sha1(b"hello\n").hexdigest()


def test_snapshot_flat_storage_containment_and_rcw_package(tmp_path: Path) -> None:
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, FILES))
    before = set(tmp_path.rglob("*"))
    res = collect.snapshot(tmp_path, "Org-A/Alpha", 20, 10_000, paths=["src/agent.py", "x.py", "x.py.txt"], transport=t)
    d = tmp_path / res["dir"]
    assert res["dir"] == f"sources/github/org-a/alpha/{SHA1}/{res['snapshot_id']}" and len(res["snapshot_id"]) == 16
    snap = json.loads((d / collect.SNAPSHOT_FILE).read_text())
    by_path = {f["path"]: f for f in snap["files"]}
    assert set(by_path) == {"README.md", "readme.md", "x.py", "x.py.txt", "src/agent.py", "empty.md", "docs/my guide #1.md"}
    stored = [f["stored"] for f in snap["files"]]
    assert len(set(stored)) == len(stored) and len({s.lower() for s in stored}) == len(stored), "no case collisions"
    assert all("/" not in s and s.rsplit(".", 1)[1] in ("md", "txt") for s in stored)
    assert (d / by_path["README.md"]["stored"]).read_bytes() == FILES["README.md"]
    assert (d / by_path["readme.md"]["stored"]).read_bytes() == FILES["readme.md"]
    assert (d / by_path["x.py"]["stored"]).read_bytes() == FILES["x.py"]
    assert (d / by_path["x.py.txt"]["stored"]).read_bytes() == FILES["x.py.txt"]
    assert by_path["x.py"]["stored"].endswith(".txt") and by_path["src/agent.py"]["stored"].startswith("agent.py-")
    assert by_path["empty.md"]["git_sha"] == EMPTY_BLOB and by_path["empty.md"]["size"] == 0 and by_path["empty.md"]["lines"] == 0
    assert by_path["docs/my guide #1.md"]["git_sha"] == HELLO_BLOB
    assert by_path["docs/my guide #1.md"]["url"] == f"https://github.com/org-a/alpha/blob/{SHA1}/docs/my%20guide%20%231.md"
    assert f"{RAW}/org-a/alpha/{SHA1}/docs/my%20guide%20%231.md" in t.urls(collect.RAW_HOST)
    reasons = {o["path"]: o["reason"] for o in snap["omitted"]}
    assert reasons == {"docs/bin.md": "not-utf8", "docs/CON.md": "unsafe-path:windows-alias-or-device",
                       "docs/bad:name.md": "unsafe-path:absolute-or-unsafe-characters",
                       "docs/trail. /x.md": "unsafe-path:windows-alias-or-device"}
    assert snap["selection"] == {"candidates": 11, "stored": 7, "omitted": 4, "complete": False}
    assert snap["repository"] == {"tree_truncated": False, "tree_blobs": 12, "complete": True}
    new_files = {p for p in tmp_path.rglob("*") if p.is_file()} - before
    allowed = (tmp_path / "sources/github/org-a/alpha" / SHA1, tmp_path / collect.BLOB_CACHE_DIR, tmp_path / "catalog", tmp_path / "state")
    assert all(any(p.is_relative_to(a) for a in allowed) for p in new_files), "no writes outside declared roots"
    assert all(p.parent == d for p in d.rglob("*") if p.is_file()), "package is a flat directory"
    pkg = json.loads((d / collect.RCW_MANIFEST).read_text())
    assert pkg["complete"] is True and [m["path"] for m in pkg["files"]] == stored
    meta = next(m for m in pkg["files"] if m["path"] == by_path["src/agent.py"]["stored"])["metadata"]
    assert meta["identifiers"] == {"repository": "org-a/alpha", "commit": SHA1, "path": "src/agent.py",
                                   "git_sha": by_path["src/agent.py"]["git_sha"], "snapshot_id": res["snapshot_id"]}
    assert meta["source_type"] == "webpage" and meta["access"] == "public" and meta["date"] == "2026-01-02T03:04:05Z"
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert rec["status"] == "snapshotted" and rec["latest_commit"] == SHA1 and rec["freshness"] == "pending"
    assert rec["latest_snapshot_id"] == res["snapshot_id"] and rec["latest_snapshot"]["package"] == res["package"]
    assert rec["sources"][-1] == {"kind": "snapshot", **rec["latest_snapshot"]}
    frozen, raw_calls = tree_bytes(d), len(t.urls(collect.RAW_HOST))
    again = collect.snapshot(tmp_path, "org-a/alpha", 20, 10_000, paths=["src/agent.py", "x.py", "x.py.txt"], transport=t)
    assert again["reused"] is True and again["changed"] is False and again["snapshot_id"] == res["snapshot_id"]
    assert tree_bytes(d) == frozen and len(t.urls(collect.RAW_HOST)) == raw_calls, "identical replay: no bytes, no fetches"


def test_paths_rejected_before_any_request(tmp_path: Path) -> None:
    cases = ["D:/escape.md", "C:escape.md", "//unc/share/x.md", "/abs.md", "~/x.md", "a\\b.md", "a/../b.md", "./a.md",
             "a//b.md", ".git/config", "docs/CON.md", "docs/nul.txt", "COM1", "trail. /x.md", "x.md ", "x%2e.md",
             "logo.png", "bad\x00.md", "", "a" * 600 + ".md"]
    for bad in cases:
        t = FakeTransport({})
        with pytest.raises(collect.InvalidPath):
            collect.snapshot(tmp_path, "org-a/alpha", 2, 100, paths=[bad], transport=t)
        assert t.calls == [], bad
    assert not (tmp_path / core.REPOS_FILE).exists()
    assert collect.path_problem("docs/my guide #1.md") is None and collect.path_problem("src/agent.py") is None
    assert collect.storage_name("README.md") != collect.storage_name("readme.md")
    assert collect.storage_name("x.py") != collect.storage_name("x.py.txt")
    assert collect.storage_name("CON.md").startswith("con.md-") and collect.storage_name("a/b/c.rst").endswith(".txt")


def test_snapshot_rejects_tampered_or_mismatched_bytes_without_overwriting(tmp_path: Path) -> None:
    files = {"README.md": b"# Alpha\n", "docs/guide.md": b"hello\n"}
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, files))
    res = collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    d = tmp_path / res["dir"]
    readme = d / next(f["stored"] for f in json.loads((d / "snapshot.json").read_text())["files"] if f["path"] == "README.md")
    readme.write_bytes(b"# Alpha (edited locally)\n")
    with pytest.raises(collect.IntegrityError, match="blob-mismatch"):
        collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    assert readme.read_bytes() == b"# Alpha (edited locally)\n", "corruption is reported, never silently repaired"
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert rec["freshness"] == "refresh-failed" and rec["last_error"]["code"] == "IntegrityError"
    readme.unlink()
    cache = tmp_path / collect.BLOB_CACHE_DIR / "org-a/alpha" / collect.git_blob_sha(files["README.md"])
    cache.write_bytes(b"# Alpha\n" + b"\n")
    with pytest.raises(collect.IntegrityError, match="cache"):
        collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    assert not readme.exists()
    cache.unlink()
    t.routes[f"{RAW}/org-a/alpha/{SHA1}/README.md"] = collect.Response(200, b"# Alph@\n")  # wrong bytes, right size
    with pytest.raises(collect.IntegrityError, match="download README.md"):
        collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    assert not readme.exists() and not cache.exists()
    t.routes[f"{RAW}/org-a/alpha/{SHA1}/README.md"] = collect.Response(200, files["README.md"])
    healed = collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    assert healed["snapshot_id"] == res["snapshot_id"] and readme.read_bytes() == files["README.md"]
    assert core.load_repos(tmp_path)["org-a/alpha"]["freshness"] == "pending"


def test_selection_ids_keep_earlier_packages_and_drive_freshness(tmp_path: Path) -> None:
    files = {"README.md": b"# Alpha\n", "src/agent.py": b"x = 1\n"}
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, files))
    a = collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    a_dir = tmp_path / a["dir"]
    frozen = tree_bytes(a_dir)
    repos = core.load_repos(tmp_path)
    repos["org-a/alpha"]["indexed_snapshot_id"] = a["snapshot_id"]  # what B003 sets after a real rcw apply
    core.save_repos(tmp_path, repos)
    b = collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, paths=["src/agent.py"], transport=t)
    assert b["snapshot_id"] != a["snapshot_id"] and b["commit"] == a["commit"] and b["dir"] != a["dir"]
    assert tree_bytes(a_dir) == frozen, "earlier package bytes retained"
    assert len(t.urls(collect.RAW_HOST)) == 2, "README reused from the verified cache, only agent.py fetched"
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert rec["freshness"] == "stale" and rec["latest_snapshot_id"] == b["snapshot_id"]
    assert [s["snapshot_id"] for s in rec["sources"] if s["kind"] == "snapshot"] == [a["snapshot_id"], b["snapshot_id"]]
    replay = collect.snapshot(tmp_path, "org-a/alpha", 5, 1000, transport=t)
    assert replay["snapshot_id"] == a["snapshot_id"] and replay["reused"] is True and tree_bytes(a_dir) == frozen
    assert core.load_repos(tmp_path)["org-a/alpha"]["freshness"] == "current"


def test_snapshot_failure_keeps_prior_snapshot_and_marks_record(tmp_path: Path) -> None:
    good = repo_routes("org-a/alpha", SHA1, FILES)
    first = collect.snapshot(tmp_path, "org-a/alpha", 2, 1000, transport=FakeTransport(good))
    old_dir = tmp_path / first["dir"]
    before = tree_bytes(old_dir)
    with pytest.raises(collect.FetchFailed, match="http-404"):  # tree at SHA2 answers 404
        collect.snapshot(tmp_path, "org-a/alpha", 2, 1000, transport=FakeTransport(head_routes("org-a/alpha", SHA2)))
    assert tree_bytes(old_dir) == before
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert rec["status"] == "snapshotted" and rec["latest_commit"] == SHA1 and rec["freshness"] == "refresh-failed"
    assert rec["last_error"]["code"] == "FetchFailed" and rec["last_error"]["locator"] == "https://github.com/org-a/alpha"
    assert rec["latest_snapshot_id"] == first["snapshot_id"]
    assert not (tmp_path / "sources/github/org-a/alpha" / SHA2).exists()
    truncated = repo_routes("org-a/alpha", SHA2, {"README.md": b"new\n"}, truncated=True)
    res = collect.snapshot(tmp_path, "org-a/alpha", 2, 1000, transport=FakeTransport(truncated))
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert res["repository"]["tree_truncated"] is True and res["repository"]["complete"] is False
    assert res["selection"]["complete"] is True, "selection coverage is reported apart from tree completeness"
    assert rec["freshness"] == "pending" and "last_error" not in rec and rec["latest_commit"] == SHA2
    assert tree_bytes(old_dir) == before, "old evidence survives the new head"


def test_snapshot_rejects_private_missing_paths_and_bad_repos(tmp_path: Path) -> None:
    with pytest.raises(collect.InvalidPath, match="repository rejected"):
        collect.snapshot(tmp_path, "settings/profile", 2, 100, transport=FakeTransport({}))
    assert not (tmp_path / core.REPOS_FILE).exists()
    with pytest.raises(collect.PrivateRepo):
        collect.snapshot(tmp_path, "org-a/alpha", 2, 100, transport=FakeTransport(head_routes("org-a/alpha", SHA1, private=True)))
    with pytest.raises(collect.InvalidPath, match="not in tree"):
        collect.snapshot(tmp_path, "org-a/alpha", 2, 100, paths=["missing.md"], transport=FakeTransport(repo_routes("org-a/alpha", SHA1, FILES)))
    big = repo_routes("org-a/alpha", SHA1, FILES)
    big[f"{RAW}/org-a/alpha/{SHA1}/README.md"] = collect.Response(200, b"x" * 500)
    with pytest.raises(collect.MalformedPayload, match="oversized-payload"):
        collect.snapshot(tmp_path, "org-a/alpha", 2, 1000, transport=FakeTransport(big))
    rec = core.load_repos(tmp_path)["org-a/alpha"]
    assert rec["status"] == "blocked" and rec["freshness"] == "refresh-failed" and rec["latest_commit"] is None
    assert not (tmp_path / "sources/github/org-a/alpha").exists()
    assert not (tmp_path / core.LOCK_FILE).exists()


def test_cli_catalog_and_snapshot_round_trip(tmp_path: Path, monkeypatch, capsys) -> None:
    routes = {**catalog_routes(SHA1), **repo_routes("orgb/bravo", SHA2, {"README.md": b"# Bravo\n"})}
    monkeypatch.setattr(collect, "urllib_transport", FakeTransport(routes))
    assert cli.main(["--root", str(tmp_path), "catalog", "--limit", "2"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["processed"] == 2 and out["backlog"] == 7
    assert cli.main(["--root", str(tmp_path), "snapshot", "orgb/bravo", "--max-files", "1", "--max-bytes", "100"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["commit"] == SHA2 and out["files_stored"] == 1 and (tmp_path / out["package"]).exists()
    assert cli.main(["--root", str(tmp_path), "snapshot", "nobody/missing"]) == collect.FetchFailed.code
    err = json.loads(capsys.readouterr().out)
    assert err["error"] == "FetchFailed" and "http-404" in err["message"]
    assert cli.main(["--root", str(tmp_path), "snapshot", "orgb/bravo", "--net-bytes", "1"]) == collect.BudgetExceeded.code


def test_urllib_transport_refuses_redirects_and_caps_reads() -> None:
    import threading
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 - http.server API
            if self.path == "/hop":
                self.send_response(302)
                self.send_header("Location", "/target")
                self.end_headers()
                return
            body = b"followed" if self.path == "/target" else b"z" * 1000
            self.send_response(200)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base = f"http://127.0.0.1:{server.server_port}"
        hop = collect.urllib_transport(f"{base}/hop", {}, 5.0, 100)
        assert hop.status == 302 and hop.body != b"followed" and hop.headers.get("Location") == "/target"
        big = collect.urllib_transport(f"{base}/big", {}, 5.0, 101)
        assert big.status == 200 and len(big.body) == 101, "reads stop at the caller's bound"
    finally:
        server.shutdown()
        server.server_close()
    with pytest.raises(collect.TransportError):
        collect.urllib_transport(f"{base}/big", {}, 1.0, 10)


def test_cached_catalog_bytes_must_match_recorded_digest(tmp_path: Path) -> None:
    t = FakeTransport(catalog_routes(SHA1))
    result = collect.catalog(tmp_path, 1, transport=t)
    feed = tmp_path / result["feed"]
    feed.write_bytes(feed.read_bytes().replace(b"Public blurb", b"Edited blurb"))
    before = (tmp_path / core.REPOS_FILE).read_bytes()
    with pytest.raises(collect.IntegrityError):
        collect.catalog(tmp_path, 1, transport=t)
    assert (tmp_path / core.REPOS_FILE).read_bytes() == before


def test_replay_with_larger_allowance_keeps_original_snapshot_manifest(tmp_path: Path) -> None:
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, {"README.md": b"hello\n"}))
    result = collect.snapshot(tmp_path, "org-a/alpha", 1, 100, transport=t)
    original = tree_bytes(tmp_path / result["dir"])
    repeated = collect.snapshot(tmp_path, "org-a/alpha", 10, 1000, transport=t)
    assert repeated["snapshot_id"] == result["snapshot_id"]
    assert tree_bytes(tmp_path / result["dir"]) == original


def test_snapshot_rejects_redirected_sources_directory(tmp_path: Path) -> None:
    root, outside = tmp_path / "root", tmp_path / "outside"
    core.init(root)
    outside.mkdir()
    (root / "sources").rmdir()
    try:
        (root / "sources").symlink_to(outside, target_is_directory=True)
    except OSError:
        pytest.skip("directory symlink creation unavailable")
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, {"README.md": b"hello\n"}))
    with pytest.raises(collect.InvalidPath):
        collect.snapshot(root, "org-a/alpha", 1, 100, transport=t)
    assert not list(outside.iterdir())


def test_duplicate_catalog_slugs_fail_before_intake(tmp_path: Path) -> None:
    rows = [entry("Alpha", "agent", "https://github.com/org-a/alpha"),
            entry("Alpha", "agent-sdk", "https://github.com/org-z/zulu")]
    t = FakeTransport(catalog_routes(SHA1, entries=rows))
    with pytest.raises(collect.MalformedPayload, match="duplicate.*slug"):
        collect.catalog(tmp_path, 10, transport=t)
    assert not core.load_repos(tmp_path)
    assert not (tmp_path / collect.CURSOR_FILE).exists()


def test_server_repository_name_must_match_requested_identity(tmp_path: Path) -> None:
    routes = repo_routes("org-a/alpha", SHA1, {"README.md": b"hello\n"})
    routes[f"{API}/repos/org-a/alpha"] = js({"full_name": "../../escaped/repo", "private": False, "default_branch": "main"})
    with pytest.raises(collect.MalformedPayload, match="full_name"):
        collect.snapshot(tmp_path, "org-a/alpha", 1, 100, transport=FakeTransport(routes))
    assert not (tmp_path / "escaped").exists()


def test_empty_selection_is_blocked_without_a_dangling_package(tmp_path: Path) -> None:
    with pytest.raises(collect.CollectError, match="no inspectable"):
        collect.snapshot(tmp_path, "org-a/alpha", 1, 100,
                         transport=FakeTransport(repo_routes("org-a/alpha", SHA1, {"main.py": b"x = 1\n"})))
    record = core.load_repos(tmp_path)["org-a/alpha"]
    assert record["status"] == "blocked" and not record.get("latest_snapshot")


def test_reused_capture_reports_original_omissions_and_current_request(tmp_path: Path) -> None:
    t = FakeTransport(repo_routes("org-a/alpha", SHA1, {"README.md": b"hello\n", "NOTES.md": b"notes\n"}))
    first = collect.snapshot(tmp_path, "org-a/alpha", 1, 100, transport=t)
    repeated = collect.snapshot(tmp_path, "org-a/alpha", 9, 6, transport=t)
    assert repeated["snapshot_id"] == first["snapshot_id"]
    assert repeated["omitted"] == first["omitted"]
    assert repeated["request"]["max_files"] == 9 and repeated["request"]["max_bytes"] == 6
