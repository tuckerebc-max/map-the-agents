"""CLI: python -m map_agents --root PATH {init,intake,status}. JSON on stdout, nonzero on error."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import core, intake

EXIT_EMPTY = 4


def _emit(obj: object) -> None:
    sys.stdout.write(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="map_agents")
    parser.add_argument("--root", type=Path, default=Path("corpus"), help="corpus root (default ./corpus)")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="create the corpus layout without touching existing files")
    p_in = sub.add_parser("intake", help="record public GitHub repo links from text, Markdown or JSON")
    p_in.add_argument("--origin", required=True, help="where the lead came from (tag only)")
    p_in.add_argument("--project", required=True, help="research project the lead belongs to")
    src = p_in.add_mutually_exclusive_group()
    src.add_argument("--file", type=Path, help="read input from this file (default: stdin)")
    src.add_argument("--text", help="inline input text")
    p_in.add_argument("--max-bytes", type=int, default=intake.MAX_INPUT_BYTES)
    sub.add_parser("status", help="summarize catalog counts")
    return parser


def _read_input(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.file is not None:
        with open(args.file, "rb") as fh:
            return intake.read_bounded(fh, args.max_bytes, str(args.file))
    return intake.read_bounded(sys.stdin.buffer, args.max_bytes, "stdin")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "init":
            _emit(core.init(args.root))
        elif args.command == "status":
            _emit(intake.status(args.root))
        elif args.command == "intake":
            result = intake.ingest(
                args.root, _read_input(args), args.origin, args.project, max_bytes=args.max_bytes
            )
            _emit(result)
            if result["empty"]:
                return EXIT_EMPTY
    except core.WorkbenchError as exc:
        _emit({"error": type(exc).__name__, "code": exc.code, "message": str(exc)})
        return exc.code
    except OSError as exc:
        _emit({"error": "OSError", "code": 1, "message": str(exc)})
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
