"""Behavioral tests: the JSON wire contract stays parseable, with Unicode values intact, under a
narrow-codepage pipe (e.g. Windows PowerShell's cp1252, utf8_mode=0).

The fix is `ensure_ascii=True` at every stdout/stderr JSON emission point: the wire *text* becomes
pure ASCII (non-ASCII characters escaped as \\uXXXX), so writing it never depends on the host
console's encoding, while `json.loads` on the reading side decodes those escapes back to the exact
original Unicode string -- nothing is transliterated, replaced, truncated or dropped. This is the
same reasoning `json.dumps`'s own default already encodes; the bug was `map_agents.__main__._emit`
explicitly opting out of it with `ensure_ascii=False`.

The first test reproduces the concrete pre-fix failure mode (an inline throwaway script matching the
old `_emit` shape, run as a real subprocess under a forced cp1252 pipe) without reverting the owned
source files. Every other test exercises the actual, currently-fixed CLI/adapter entry points.
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from map_agents import core, lunaroute, wiki
from map_agents.workers import ENVELOPE_SCHEMA

UNICODE_SAMPLE = "世界 → café"  # "世界 → café": CJK ideographs, an arrow, and a Latin-1 accented letter
REPO_ROOT = Path(__file__).resolve().parents[1]


def _cp1252_env() -> dict:
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "cp1252"
    env.pop("PYTHONUTF8", None)
    return env


# --------------------------------------------------------------------------- before: reproduce the failure


def test_before_fix_pattern_raises_unicodeencodeerror_under_cp1252(tmp_path):
    """Demonstrates the exact mechanism this change fixes. `json.dumps(..., ensure_ascii=False)` (the
    pre-fix shape of `_emit`) followed by `sys.stdout.write` puts real CJK/arrow/accented characters
    directly on the pipe; under a real subprocess forced to PYTHONIOENCODING=cp1252 (no utf8_mode),
    Python's default strict stdout error handler raises UnicodeEncodeError and the process exits
    non-zero -- a worker consuming this stdout would see a crash, not a well-formed JSON error.
    """
    script = tmp_path / "before_fix_pattern.py"
    script.write_text(
        "import json, sys\n"
        f"sys.stdout.write(json.dumps({{'name': {UNICODE_SAMPLE!r}}}, ensure_ascii=False))\n",
        encoding="utf-8",
    )
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, env=_cp1252_env())
    assert proc.returncode != 0
    assert b"UnicodeEncodeError" in proc.stderr


# --------------------------------------------------------------------------- after: __main__.query CLI


def _build_corpus_with_unicode(root: Path) -> None:
    """A minimal already-generated map (build() is not re-run here) containing the sample text, in the
    same map/build.json + map/ page shape maps.query actually reads."""
    core.init(root)
    page_rel = "map/repos/example/repo.md"
    (root / page_rel).parent.mkdir(parents=True, exist_ok=True)
    (root / page_rel).write_text(f"# example/repo\n\nexample project: {UNICODE_SAMPLE}\n", encoding="utf-8")
    manifest = {"schema_version": 1, "catalog_digest": "x", "directory_digest": "x", "aliases_digest": "x",
                "files": [page_rel], "file_repos": {}, "records": {}}
    (root / "map/build.json").write_text(json.dumps(manifest), encoding="utf-8")


def test_query_cli_subprocess_under_cp1252_returns_parseable_json_preserving_unicode(tmp_path):
    """The real `python -m map_agents query` CLI, run as an actual subprocess forced to a cp1252 pipe
    (matching the reported host), exits 0 and its stdout is parseable JSON whose value is byte-for-byte
    the original Unicode text -- not transliterated, replaced, truncated or dropped.
    """
    root = tmp_path / "corpus"
    _build_corpus_with_unicode(root)
    proc = subprocess.run(
        [sys.executable, "-m", "map_agents", "--root", str(root), "query", "example", "--limit", "5"],
        capture_output=True, cwd=REPO_ROOT, env=_cp1252_env(),
    )
    assert proc.returncode == 0, proc.stderr.decode("utf-8", "replace")
    assert proc.stdout.isascii(), "the wire text itself must be pure ASCII regardless of console encoding"
    result = json.loads(proc.stdout.decode("ascii"))
    assert result["results"], "the unicode-bearing generated page must actually be matched by the query"
    assert UNICODE_SAMPLE in result["results"][0]["excerpt"], "decoded value must be byte-identical to the source text"


def test_query_cli_preserves_empty_result_behavior_under_cp1252(tmp_path):
    """An empty query result keeps its exit-zero JSON contract under the constrained encoding."""
    root = tmp_path / "corpus"
    _build_corpus_with_unicode(root)
    proc = subprocess.run(
        [sys.executable, "-m", "map_agents", "--root", str(root), "query", "zzz-no-match-zzz"],
        capture_output=True, cwd=REPO_ROOT, env=_cp1252_env(),
    )
    assert proc.returncode == 0  # a genuine empty match set is not itself an error for `query`
    result = json.loads(proc.stdout.decode("ascii"))
    assert result["results"] == []


# --------------------------------------------------------------------------- after: lunaroute adapter stdout


OP = "op_" + "d" * 32
COMMIT = "b" * 40
SNAPSHOT = "c" * 16
SLICE_DOC = "slc_" + "a" * 64


def _packet() -> dict:
    return {
        "schema_version": wiki.PACKET_SCHEMA, "operation_id": OP, "repo": "example/repo",
        "commit": COMMIT, "snapshot_id": SNAPSHOT, "base_digest": "sha256:aaaa",
        "slices": [
            {"slice_id": SLICE_DOC, "source_id": "src1", "heading": "Overview",
             "locator": {"path": "README.md", "line_start": 1, "line_end": 5},
             "text": f"This project's evidence mentions {UNICODE_SAMPLE} in its documented overview.", "truncated": False},
        ],
    }


def _envelope(packet: dict) -> bytes:
    return json.dumps({
        "schema_version": ENVELOPE_SCHEMA, "task": "dossier-proposal", "packet": packet,
        "coverage": {"notice": "Evidence is a bounded selection of one commit."},
        "output_contract": {"format": "exactly one JSON object on stdout, nothing else",
                            "schema": wiki.PROPOSAL_JSON_SCHEMA, "manual_models": []},
    }).encode("utf-8")


def _chat_response(content: object) -> bytes:
    body = content if isinstance(content, str) else json.dumps(content)
    return json.dumps({"choices": [{"message": {"content": body}}], "usage": {"prompt_tokens": 10}}).encode()


def test_adapter_stdout_under_constrained_cp1252_stream_preserves_unicode_claim_text(monkeypatch):
    """A fake completed provider response (never a real model call) whose claim text carries the same
    Unicode sample. The adapter's own `sys.stdout` is replaced with a real io.TextIOWrapper bound to a
    strict cp1252 encoder -- a write that is not pure ASCII would raise here exactly as it would on a
    real narrow-codepage console. The proposal that comes out the other end must still validate against
    the real kernel-facing schema and carry the exact original Unicode text.
    """
    packet = _packet()
    reduced = {"summary": f"The project documents {UNICODE_SAMPLE} in its overview text.",
               "claims": [{"facet": "specifications", "kind": "observation", "basis": "documented",
                          "text": f"The README's overview names {UNICODE_SAMPLE} as part of the documented scope.",
                          "slices": [1]}]}
    monkeypatch.setenv("LUNAROUTE_API_KEY", "test-key")
    monkeypatch.setattr(lunaroute, "_transport", lambda req, timeout: (200, _chat_response(reduced)))
    buf = io.BytesIO()
    constrained_stdout = io.TextIOWrapper(buf, encoding="cp1252", errors="strict", write_through=True)
    monkeypatch.setattr(lunaroute.sys, "stdout", constrained_stdout)
    code = lunaroute.main([], stdin=io.BytesIO(_envelope(packet)))
    assert code == 0
    raw = buf.getvalue()
    assert raw.isascii(), "the wire bytes on the constrained stream must be pure ASCII"
    proposal = json.loads(raw.decode("ascii"))
    assert UNICODE_SAMPLE in proposal["claims"][0]["text"]
    assert UNICODE_SAMPLE in proposal["summary"]
    claims = wiki.validate_proposal(proposal, packet)  # still satisfies the real, unchanged kernel-facing gate
    assert len(claims) == 1


def test_adapter_stdout_stream_separation_and_redaction_unaffected_by_encoding_fix(monkeypatch, capsys):
    """The encoding fix touches only how bytes are written, not what is written: stdout carries only
    the proposal, the API key never appears on either stream, and the receipt still lands on stderr."""
    packet = _packet()
    reduced = {"summary": "A plain-ASCII summary for this check.",
               "claims": [{"facet": "specifications", "kind": "observation", "basis": "documented",
                          "text": "The README documents an overview of the project's scope.", "slices": [1]}]}
    secret = "sk-super-secret-lunaroute-key"
    monkeypatch.setenv("LUNAROUTE_API_KEY", secret)
    monkeypatch.setattr(lunaroute, "_transport", lambda req, timeout: (200, _chat_response(reduced)))
    code = lunaroute.main([], stdin=io.BytesIO(_envelope(packet)))
    out = capsys.readouterr()
    assert code == 0
    proposal = json.loads(out.out)  # stdout is exactly one parseable JSON object, nothing else
    assert secret not in out.out and secret not in out.err
    receipt = json.loads(out.err.strip().splitlines()[-1])
    assert receipt["status"] == "ok" and "claims" in receipt
