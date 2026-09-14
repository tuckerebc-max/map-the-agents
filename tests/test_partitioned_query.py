"""Behavioral tests: query's --include-archive across both the shared and partitioned wiki layouts.

Uses the real pinned kernel (collect.snapshot -> wiki.prepare -> wiki.apply, offline FakeTransport)
so wiki/pages/ and wiki/shards/<id>/pages/ are genuine kernel output, not hand-written fixtures.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import __main__ as cli
from map_agents import collect, maps, wiki
from test_collect import SHA1, FakeTransport, repo_routes
from test_wiki import FILES, good_proposal, write


def _distill(root: Path, key: str, sha: str = SHA1) -> dict:
    collect.snapshot(root, key, 20, 50_000, paths=["src/agent.py"], transport=FakeTransport(repo_routes(key, sha, FILES)))
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    wiki.apply(root, root / prepared["packet"], write(root / f"{key.replace('/', '-')}.json", good_proposal(packet)))
    return maps.build(root)


# --------------------------------------------------------------------------- shared layout (default)


def test_default_query_excludes_shared_archive(tmp_path):
    _distill(tmp_path, "org-a/alpha")
    assert (tmp_path / "wiki/pages").is_dir()
    default = maps.query(tmp_path, "bosun supervision")
    assert not any(r["path"].startswith("wiki/pages/") for r in default["results"])


def test_include_archive_finds_shared_pages_labeled_historical(tmp_path):
    _distill(tmp_path, "org-a/alpha")
    result = maps.query(tmp_path, "bosun supervision", include_archive=True, max_chars=12000)
    hits = [r for r in result["results"] if r["path"].startswith("wiki/pages/")]
    assert hits, "the shared kernel's own archived page must match once explicitly included"
    for h in hits:
        assert h["archive"] is True
        assert "repo" not in h and "status" not in h and "freshness" not in h
        assert h["note"] == "kernel-generated historical wiki page; not labelled with current catalog freshness"


# --------------------------------------------------------------------------- partitioned layout


def test_default_query_excludes_partitioned_shard_archive(tmp_path):
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-b/bravo")
    shard = wiki._kernel_root(tmp_path, "org-b/bravo")
    assert (shard / "pages").is_dir()
    default = maps.query(tmp_path, "bosun supervision")
    rel_prefix = shard.relative_to(tmp_path).as_posix()
    assert not any(r["path"].startswith(rel_prefix) for r in default["results"])


def test_include_archive_finds_partitioned_shard_pages_labeled_historical(tmp_path):
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-b/bravo")
    shard = wiki._kernel_root(tmp_path, "org-b/bravo")
    rel_prefix = shard.relative_to(tmp_path).as_posix() + "/pages/"
    result = maps.query(tmp_path, "bosun supervision", include_archive=True, max_chars=12000)
    hits = [r for r in result["results"] if r["path"].startswith(rel_prefix)]
    assert hits, "a repository shard's own archived page must match once explicitly included"
    for h in hits:
        assert h["archive"] is True
        assert "repo" not in h and "status" not in h and "freshness" not in h
        assert h["note"] == "kernel-generated historical wiki page; not labelled with current catalog freshness"


def test_multiple_shards_are_all_reachable_and_deterministically_ordered(tmp_path):
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-c/charlie")
    _distill(tmp_path, "org-d/delta")
    dirs = maps._archive_dirs(tmp_path)
    rels = [d.relative_to(tmp_path).as_posix() for d in dirs]
    assert rels == sorted(rels), "archive directory scan order must be deterministic, not filesystem-iteration order"
    assert all(r.endswith("/pages") for r in rels)
    assert sum(1 for r in rels if r.startswith("wiki/shards/")) == 2
    # _searchable_files is the precise reachability check; query()'s own ranking/char-budget can legitimately
    # crowd a tied-score, alphabetically-later file out of one bounded call without that being a bug.
    files, complete = maps._searchable_files(tmp_path, True)
    scanned_shards = {f.relative_to(tmp_path).parts[2] for f in files if f.relative_to(tmp_path).parts[:2] == ("wiki", "shards")}
    assert scanned_shards == {d.parts[-2] for d in dirs if "shards" in d.parts}
    assert len(scanned_shards) == 2, "both repository shards' archive files must be reachable, not just the first"
    assert complete is True


# --------------------------------------------------------------------------- exclusion of other material


def test_shard_non_pages_material_never_scanned_even_with_include_archive(tmp_path):
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-b/bravo")
    shard = wiki._kernel_root(tmp_path, "org-b/bravo")
    marker = "MARKERTOKENNOTAPAGE"
    (shard / "notes.md").write_text(f"bosun supervision {marker}", encoding="utf-8")
    for sub, name in (("data", "claims.jsonl"), ("state", "note.md"), ("packets", "note.md"), ("proposals", "note.md")):
        d = shard / sub
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_text(f"bosun supervision {marker}", encoding="utf-8")
    result = maps.query(tmp_path, marker, include_archive=True)
    assert result["results"] == [], "shard sources/JSONL/state/packets/proposals/notes must never be scanned"


def test_private_inbox_never_scanned_as_archive(tmp_path):
    _distill(tmp_path, "org-a/alpha")
    marker = "PRIVATEINBOXMARKER"
    private = tmp_path / "inbox/private/proj/origin.txt"
    private.parent.mkdir(parents=True, exist_ok=True)
    private.write_text(f"bosun supervision {marker}", encoding="utf-8")
    result = maps.query(tmp_path, marker, include_archive=True)
    assert result["results"] == []


def test_uninitialized_shard_directory_is_ignored(tmp_path):
    """A shard directory that exists on disk but has no wiki.yaml (never actually initialized) must not
    be treated as a source of historical pages, even if it happens to contain a pages/ subdirectory."""
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-b/bravo")
    fake_shard = tmp_path / "wiki/shards/not-a-real-shard"
    (fake_shard / "pages").mkdir(parents=True)
    (fake_shard / "pages" / "fake.md").write_text("bosun supervision FAKEUNINITMARKER", encoding="utf-8")
    result = maps.query(tmp_path, "FAKEUNINITMARKER", include_archive=True)
    assert result["results"] == []


# --------------------------------------------------------------------------- coverage flags preserved


def test_complete_flag_still_true_for_a_small_corpus_in_both_layouts(tmp_path):
    _distill(tmp_path, "org-a/alpha")
    assert maps.query(tmp_path, "bosun supervision", include_archive=True, max_chars=12000)["complete"] is True


def test_complete_flag_still_true_for_partitioned_corpus(tmp_path):
    wiki.enable_partitioned(tmp_path)
    _distill(tmp_path, "org-b/bravo")
    assert maps.query(tmp_path, "bosun supervision", include_archive=True, max_chars=12000)["complete"] is True


# --------------------------------------------------------------------------- CLI help


def test_cli_help_mentions_both_layouts():
    parser = cli.build_parser()
    query_parser = parser._subparsers._group_actions[0].choices["query"]
    help_text = query_parser.format_help()
    assert "wiki/pages" in help_text
    assert "shard" in help_text
