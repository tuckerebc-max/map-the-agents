"""Verify the complete vendored wiki against the recorded upstream Git blob bytes."""
from pathlib import Path
import argparse
import hashlib
import json


def verify(root: Path, manifest: Path) -> dict:
    pin = json.loads(manifest.read_text(encoding="utf-8"))
    vendor = root / "vendor/research-corpus-wiki"
    problems = []
    expected = set()
    for record in pin["files"]:
        relative = record["path"]
        target = vendor / relative
        if relative in expected or not target.resolve().is_relative_to(vendor.resolve()):
            problems.append({"path": relative, "error": "invalid-manifest-path"})
            continue
        expected.add(relative)
        if not target.is_file() or target.is_symlink():
            problems.append({"path": relative, "error": "missing-or-symbolic-link"})
            continue
        data = target.read_bytes()
        blob = hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()
        if blob != record["git_blob"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            problems.append({"path": relative, "error": "byte-identity-mismatch"})
    ignored = {"__pycache__", ".pytest_cache", ".venv", ".ruff_cache"}
    actual = {p.relative_to(vendor).as_posix() for p in vendor.rglob("*")
              if p.is_file() and not ignored.intersection(p.relative_to(vendor).parts)}
    for extra in sorted(actual - expected):
        problems.append({"path": extra, "error": "unexpected-vendor-file"})
    return {"ok": not problems, "repository": pin["repository"], "commit": pin["commit"],
            "files_checked": len(expected), "problems": problems}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    result = verify(args.root, args.manifest or args.root / "vendor-pin.json")
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
