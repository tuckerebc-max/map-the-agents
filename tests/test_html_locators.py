"""Real-kernel regression: HTML/HTM source line-locator fidelity.

Reproduced defect: the pinned kernel's own parser (vendor/research-corpus-wiki
scripts/rcw_core/sources.py:text_content) extracts rendered *visible text* from any file stored
with an `.html`/`.htm` suffix -- discarding `<script>`/`<style>` and reflowing the rest -- so its
reported slice line numbers describe that reflowed text, not the original file. `wiki.py` then
built a real GitHub `#L<start>-L<end>` locator directly from those numbers, and `source_review.py`
re-read the *original* stored bytes at those same line numbers: both wrong, silently.

Fix: `collect.storage_name` now stores HTML/HTM bytes verbatim under a `.txt` wrapper (exactly like
`.py`/`.ts`/... code today), so the kernel reads the real lines. Only fresh captures carry the new
`format: "verbatim"` marker (in the snapshot's per-file record and everywhere it flows: source,
locator, packet). A pre-fix ("legacy") HTML/HTM snapshot -- one with no such marker -- makes
`wiki.prepare` and `wiki.load_dossier` fail closed, rather than silently trusting its locators or
relabeling it code-inspected. Offline, model-free, real pinned kernel throughout.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from map_agents import collect, core, wiki
from test_collect import SHA1, FakeTransport, repo_routes

# 22 lines: 10 head/style lines, a blank-line-isolated body fact (line 15), then a blank-line-isolated
# <script> block holding a code fact (lines 17-19) -- exactly "multiple head/style lines before a
# distinctive body/code fact", with real blank-line block boundaries the kernel's own slicer respects.
HTML_LINES = [
    "<!DOCTYPE html>", "<html lang=\"en\">", "<head>", "<meta charset=\"UTF-8\">",
    "<title>Sample</title>", "<style>", ".rule0 { color: red; }", ".rule1 { color: blue; }",
    "</style>", "</head>",
    "",
    "<body>", "<h1>Welcome</h1>",
    "",
    "<p>DISTINCTIVE_BODY_FACT_7f3a</p>",
    "",
    "<script>", "function computeAnswer() { return 42; } // DISTINCTIVE_CODE_FACT_9c1b", "</script>",
    "",
    "</body>", "</html>",
]
HTML_BYTES = ("\n".join(HTML_LINES) + "\n").encode("utf-8")
BODY_LINE, CODE_START, CODE_END = 15, 17, 19


def _snap(root: Path, key: str, sha: str, path: str, data: bytes = HTML_BYTES) -> dict:
    return collect.snapshot(root, key, 5, 50_000, paths=[path], transport=FakeTransport(repo_routes(key, sha, {path: data})))


def _slice_by_substring(packet: dict, needle: str) -> dict:
    return next(s for s in packet["slices"] if needle in s["text"])


def _claim(facet: str, text: str, ids: list[str], basis: str = "documented") -> dict:
    return {"facet": facet, "text": text, "slice_ids": ids, "kind": "observation", "basis": basis}


def _apply(root: Path, prepared: dict, packet: dict, claims: list[dict], summary: str) -> dict:
    proposal = {"schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
                "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
                "summary": summary, "claims": claims}
    path = root / "proposals" / "p.json"
    path.write_bytes(core.dump_json(proposal))
    return wiki.apply(root, root / prepared["packet"], path)


def _strip_format(root: Path, snap: dict, path_in_repo: str) -> None:
    """Simulate a pre-fix ('legacy') capture: drop the verbatim marker from the on-disk snapshot
    record, as if this snapshot had been collected before the fix existed. Never used to claim a
    real pre-fix repository state -- only to exercise the fail-closed guard deterministically."""
    snap_path = root / snap["dir"] / collect.SNAPSHOT_FILE
    record = json.loads(snap_path.read_bytes())
    for f in record["files"]:
        if f["path"] == path_in_repo:
            f.pop("format", None)
    core.atomic_write_bytes(snap_path, core.dump_json(record))


@pytest.mark.parametrize("path", ["index.html", "page.htm"])
def test_html_slice_locators_match_original_source_lines_and_round_trip(tmp_path, path):
    root = tmp_path / "corpus"
    key = "org-a/htmltest"
    snap = _snap(root, key, SHA1, path)
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())

    stored_bytes = (root / snap["dir"] / json.loads((root / snap["dir"] / collect.SNAPSHOT_FILE).read_bytes())["files"][0]["stored"]).read_bytes()
    assert stored_bytes == HTML_BYTES, "stored bytes must be the exact original source, never re-encoded"
    original_lines = stored_bytes.decode("utf-8").splitlines()

    # Every emitted slice -- not just the two named facts -- must match the actual original file span.
    for s in packet["slices"]:
        start, end = s["locator"]["line_start"], s["locator"]["line_end"]
        assert s["text"] == "\n".join(original_lines[start - 1:end]), f"slice {s['slice_id']} span mismatch"
        assert s["locator"]["url"].endswith(f"/{path}#L{start}-L{end}")
        assert s["locator"]["format"] == "verbatim"

    body = _slice_by_substring(packet, "DISTINCTIVE_BODY_FACT_7f3a")
    assert body["locator"]["line_start"] == body["locator"]["line_end"] == BODY_LINE
    assert body["text"] == original_lines[BODY_LINE - 1] == "<p>DISTINCTIVE_BODY_FACT_7f3a</p>"
    assert body["locator"]["url"].endswith(f"/{path}#L{BODY_LINE}-L{BODY_LINE}")
    assert body["locator"]["format"] == "verbatim"

    code = _slice_by_substring(packet, "DISTINCTIVE_CODE_FACT_9c1b")
    assert (code["locator"]["line_start"], code["locator"]["line_end"]) == (CODE_START, CODE_END)
    assert code["text"] == "\n".join(original_lines[CODE_START - 1:CODE_END])
    assert code["locator"]["url"].endswith(f"/{path}#L{CODE_START}-L{CODE_END}")

    # code-inspected is admissible on this corrected, verbatim representation
    claims = [_claim("components", "The script defines a computeAnswer function returning 42.", [code["slice_id"]], "code-inspected"),
              _claim("specifications", "The page shows a distinctive marked paragraph in its body.", [body["slice_id"]])]
    result = _apply(root, prepared, packet, claims, "Synthetic HTML page with a script fact and a body fact.")
    assert result["changed"] is True and result["claims"] == 2

    dossier = wiki.load_dossier(root, key)  # full real round trip: prepare -> apply -> load_dossier
    dossier_code = next(c for c in dossier["claims"] if c["basis"] == "code-inspected")
    assert dossier_code["locators"][0]["line_start"] == CODE_START and dossier_code["locators"][0]["line_end"] == CODE_END
    assert dossier_code["locators"][0]["format"] == "verbatim"
    assert dossier_code["locators"][0]["url"].endswith(f"/{path}#L{CODE_START}-L{CODE_END}")

    from map_agents import source_review  # not modified; verifying its re-read now agrees, end to end
    review_body, _raw = source_review.packet_for(root, key)
    review_code = next(c for c in review_body["claims"] if c["basis"] == "code-inspected")
    assert review_code["evidence"][0]["text"] == "\n".join(original_lines[CODE_START - 1:CODE_END])
    report = wiki.audit(root)  # never writes
    assert report["ok"] is True and report["problems"] == 0, report


def test_renamed_html_storage_with_retained_marker_is_rejected_not_trusted(tmp_path):
    """Reproduces the parent's concrete acceptance hole (work/population/html-parent-probe.json):
    a genuinely, correctly captured verbatim `.txt`-stored file is renamed to `.html`
    (`snapshot.files[].stored` and `manifest.files[].path` adjusted consistently, bytes/git blob
    byte-for-byte unchanged) but `format: "verbatim"` is left untouched. The marker alone must not
    establish the source-preserving kernel path: prepare() and load_dossier() must both fail closed
    on this exact mismatch, since the pinned kernel would once again line-number the file's own
    kernel-rendered visible text (the renamed `.html` file, read fresh, reproduces the same
    line-5-for-line-15 mismatch the original defect had)."""
    root = tmp_path / "corpus"
    key = "org-a/probe"
    snap = _snap(root, key, SHA1, "index.html")
    prepared = wiki.prepare(root, key)  # genuinely correct and trusted at this point
    packet = json.loads((root / prepared["packet"]).read_bytes())
    body = _slice_by_substring(packet, "DISTINCTIVE_BODY_FACT_7f3a")
    assert body["locator"]["line_start"] == BODY_LINE  # correct before the tamper below
    _apply(root, prepared, packet, [_claim("specifications", "A distinctive marked paragraph is shown.", [body["slice_id"]])],
           "Synthetic page.")
    wiki.load_dossier(root, key)  # currently valid

    snap_path = root / snap["dir"] / collect.SNAPSHOT_FILE
    record = json.loads(snap_path.read_bytes())
    file_record = next(f for f in record["files"] if f["path"] == "index.html")
    assert file_record["format"] == "verbatim"  # the marker, retained throughout the tamper below
    old_stored, new_stored = file_record["stored"], "index.html"
    assert old_stored.endswith(".txt") and old_stored != new_stored
    (root / snap["dir"] / old_stored).rename(root / snap["dir"] / new_stored)  # bytes/git blob unchanged
    file_record["stored"] = new_stored
    core.atomic_write_bytes(snap_path, core.dump_json(record))
    manifest_path = root / snap["package"]
    manifest = json.loads(manifest_path.read_bytes())
    for m in manifest["files"]:
        if m["path"] == old_stored:
            m["path"] = new_stored
    core.atomic_write_bytes(manifest_path, core.dump_json(manifest))

    with pytest.raises(wiki.UnsafeHtmlSource, match="recapture"):
        wiki.prepare(root, key)
    with pytest.raises(wiki.DossierInvalid, match="recapture"):
        wiki.load_dossier(root, key)
    report = wiki.audit(root)
    assert report["ok"] is False and report["problems"] >= 1


def test_code_inspected_html_claim_rejected_on_a_locator_lacking_the_verbatim_marker():
    packet = {"operation_id": "op_" + "a" * 32, "repo": "x/y", "commit": "c" * 40, "snapshot_id": "s" * 16,
              "base_digest": "sha256:aa",
              "slices": [{"slice_id": "slc_" + "e" * 64,
                          "locator": {"path": "index.html", "line_start": 1, "line_end": 1}}]}
    proposal = {"schema_version": wiki.DOSSIER_SCHEMA, "operation_id": packet["operation_id"], "repo": packet["repo"],
                "commit": packet["commit"], "snapshot_id": packet["snapshot_id"], "base_digest": packet["base_digest"],
                "summary": "x", "claims": [_claim("components", "A legacy HTML slice claims code inspection.",
                                                   ["slc_" + "e" * 64], "code-inspected")]}
    with pytest.raises(wiki.ProposalRejected, match="documentation only"):
        wiki.validate_proposal(proposal, packet)


def test_unsafe_legacy_html_snapshot_refuses_to_prepare_before_touching_the_kernel(tmp_path):
    root = tmp_path / "corpus"
    key = "org-a/legacy"
    snap = _snap(root, key, SHA1, "index.html")
    _strip_format(root, snap, "index.html")  # simulate: this snapshot predates the verbatim-text fix
    with pytest.raises(wiki.UnsafeHtmlSource, match="recapture"):
        wiki.prepare(root, key)
    assert not (root / "wiki" / "wiki.yaml").exists(), "must fail before any kernel call, not after"


def test_unsafe_legacy_html_dossier_fails_closed_in_load_dossier(tmp_path):
    root = tmp_path / "corpus"
    key = "org-a/wasgood"
    snap = _snap(root, key, SHA1, "index.html")
    prepared = wiki.prepare(root, key)
    packet = json.loads((root / prepared["packet"]).read_bytes())
    body = _slice_by_substring(packet, "DISTINCTIVE_BODY_FACT_7f3a")
    _apply(root, prepared, packet, [_claim("specifications", "A distinctive marked paragraph is shown.", [body["slice_id"]])],
           "Synthetic page.")
    wiki.load_dossier(root, key)  # currently valid

    _strip_format(root, snap, "index.html")  # simulate the same snapshot becoming legacy-unsafe
    with pytest.raises(wiki.DossierInvalid, match="recapture"):
        wiki.load_dossier(root, key)


def test_non_html_snapshot_identity_is_unaffected_by_the_fix(tmp_path):
    root = tmp_path / "corpus"
    key = "org-a/plain"
    files = {"src/agent.py": b"class Agent:\n    def run(self):\n        return 1\n"}
    result = collect.snapshot(root, key, 5, 50_000, paths=["src/agent.py"], transport=FakeTransport(repo_routes(key, SHA1, files)))
    manifest = json.loads((root / result["package"]).parent.joinpath(collect.SNAPSHOT_FILE).read_bytes())
    pre_fix_selection = [{"path": f["path"], "git_sha": f["git_sha"]} for f in manifest["files"]]
    pre_fix_id = collect._sha256(core.dump_json({"commit": SHA1, "files": pre_fix_selection}))[:16]
    assert result["snapshot_id"] == pre_fix_id, "a repo with no HTML/HTM file must get the exact pre-fix snapshot_id"
    assert all("format" not in f for f in manifest["files"])


def test_html_snapshot_gets_a_new_distinct_identity_and_old_bytes_stay_immutable(tmp_path):
    root = tmp_path / "corpus"
    key = "org-a/htmlid"
    result = collect.snapshot(root, key, 5, 50_000, paths=["index.html"],
                              transport=FakeTransport(repo_routes(key, SHA1, {"index.html": HTML_BYTES})))
    new_id = result["snapshot_id"]
    pre_fix_id = collect._sha256(core.dump_json({"commit": SHA1, "files": [{"path": "index.html", "git_sha": collect.git_blob_sha(HTML_BYTES)}]}))[:16]
    assert new_id != pre_fix_id, "the corrected representation must not collide with the old snapshot_id formula"

    # Fabricate an old, immutable, already-existing legacy capture at the OLD identity: same commit,
    # same file selection, .html-suffixed stored bytes, no format marker -- exactly what a real
    # pre-fix snapshot on disk looks like.
    legacy_dir = root / collect.SOURCE_DIR / "org-a" / "htmlid" / SHA1 / pre_fix_id
    legacy_stored = "index-legacy.html"
    core.atomic_write_bytes(legacy_dir / legacy_stored, HTML_BYTES)
    legacy_record = {"snapshot_id": pre_fix_id, "dir": legacy_dir.relative_to(root).as_posix(),
                     "package": f"{legacy_dir.relative_to(root).as_posix()}/{collect.RCW_MANIFEST}",
                     "files": [{"path": "index.html", "stored": legacy_stored, "size": len(HTML_BYTES),
                               "sha256": collect._sha256(HTML_BYTES), "git_sha": collect.git_blob_sha(HTML_BYTES), "lines": len(HTML_LINES)}]}
    core.atomic_write_bytes(legacy_dir / collect.SNAPSHOT_FILE, core.dump_json(legacy_record))
    before = ((legacy_dir / collect.SNAPSHOT_FILE).read_bytes(), (legacy_dir / legacy_stored).read_bytes())

    result2 = collect.snapshot(root, key, 5, 50_000, paths=["index.html"],
                               transport=FakeTransport(repo_routes(key, SHA1, {"index.html": HTML_BYTES})))
    assert result2["snapshot_id"] == new_id, "resuming the fixed snapshot must reuse its own (new) identity"
    after = ((legacy_dir / collect.SNAPSHOT_FILE).read_bytes(), (legacy_dir / legacy_stored).read_bytes())
    assert after == before, "the old, immutable legacy snapshot's bytes must be completely untouched"
    assert legacy_dir != root / result2["dir"], "the corrected snapshot lives in a distinct directory from the old one"
    new_stored = json.loads((root / result2["dir"] / collect.SNAPSHOT_FILE).read_bytes())["files"][0]["stored"]
    assert new_stored.endswith(".txt"), "the corrected representation is stored as .txt, never .html"
