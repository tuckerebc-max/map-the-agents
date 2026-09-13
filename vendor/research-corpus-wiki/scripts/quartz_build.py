"""Build exported content with an explicitly pinned, official Quartz checkout."""

import argparse
import json
import re
import subprocess
from pathlib import Path


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=True).stdout.strip()


def build_quartz(checkout, content, output, pin):
    if not re.fullmatch("[0-9a-f]{40}", pin):
        raise ValueError("Quartz requires a full 40-character commit pin")
    checkout, content, output = Path(checkout).resolve(), Path(content).resolve(), Path(output).resolve()
    head = run(["git", "rev-parse", "HEAD"], checkout)
    if head != pin:
        raise ValueError("Quartz checkout differs from the requested commit pin")
    origin = run(["git", "remote", "get-url", "origin"], checkout)
    if origin not in {"https://github.com/jackyzha0/quartz.git", "https://github.com/jackyzha0/quartz"}:
        raise ValueError("Expected the official Quartz repository as origin")
    if run(["git", "status", "--porcelain"], checkout):
        raise ValueError("Quartz checkout must be clean before the build")
    if not (content / "index.md").is_file():
        raise ValueError("Pass the exported content directory, including index.md")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Use an empty output directory for a Quartz build")
    if (
        output == checkout
        or output.is_relative_to(checkout)
        or output == content
        or output.is_relative_to(content)
        or content.is_relative_to(output)
    ):
        raise ValueError("Output must be separate from checkout and content")
    run(["npm", "ci"], checkout)
    build_log = run(
        ["npx", "--no-install", "quartz", "build", "--directory", str(content), "--output", str(output)],
        checkout,
    )
    if not (output / "index.html").is_file():
        raise ValueError("Quartz did not produce index.html")
    return {
        "commit": head,
        "output": str(output),
        "index": str(output / "index.html"),
        "build_log": build_log,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", required=True, type=Path)
    parser.add_argument("--content", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--pin", required=True)
    args = parser.parse_args()
    print(json.dumps(build_quartz(args.checkout, args.content, args.output, args.pin), indent=2))
