"""CLI: python -m map_agents --root PATH {init,intake,status,catalog,snapshot,prepare,apply,audit,build,query,maintain,worker}."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from . import collect, core, intake, maps, wiki, workers

EXIT_EMPTY = 4
EXIT_AUDIT_FAILED = 3  # mirrors the kernel's audit exit status


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
    p_cat = sub.add_parser("catalog", help="process a bounded batch of the alltheagents.org backing feed")
    p_cat.add_argument("--limit", type=int, default=50, help="entries to process this call")
    p_cat.add_argument("--published", action="store_true", help="also record the published index digest/count")
    p_snap = sub.add_parser("snapshot", help="store an immutable text snapshot of a public repository head")
    p_snap.add_argument("repo", help="owner/repo")
    p_snap.add_argument("--max-files", type=int, default=12)
    p_snap.add_argument("--max-bytes", type=int, default=400_000)
    p_snap.add_argument("--path", action="append", default=[], help="explicit source file (repeatable)")
    p_prep = sub.add_parser("prepare", help="prepare a real rcw ingest packet for a repository's active snapshot")
    p_prep.add_argument("repo", help="owner/repo")
    p_app = sub.add_parser("apply", help="validate a dossier proposal and apply it through the rcw kernel")
    p_app.add_argument("packet", type=Path, help="packet JSON written by prepare")
    p_app.add_argument("proposal", type=Path, help="dossier proposal JSON")
    p_aud = sub.add_parser("audit", help="run the kernel audit and reconcile dossiers with records")
    p_aud.add_argument("--level", choices=("working", "pr"), default="working")
    sub.add_parser("build", help="render map/index.md, per-repo pages and AGENTS_CORPUS.md from the catalog and dossiers")
    p_qry = sub.add_parser("query", help="search generated map/ and wiki/pages/ Markdown only")
    p_qry.add_argument("text", help="search text")
    p_qry.add_argument("--limit", type=int, default=10)
    p_qry.add_argument("--max-chars", type=int, default=4000)
    p_qry.add_argument("--include-archive", action="store_true", help="also search the kernel's wiki/pages/ archive")
    p_mnt = sub.add_parser("maintain", help="bounded model-free refresh: catalog leads, fair snapshot queue, needs-distillation")
    p_wrk = sub.add_parser("worker", help="distill one repository through a trusted worker argv given after `--` (none: manual envelope)")
    p_wrk.add_argument("--repo", help="owner/repo (default: next repository needing distillation)")
    p_wrk.add_argument("--no-build", action="store_true", help="skip the map rebuild after a successful apply")
    p_wrk.add_argument("argv", nargs=argparse.REMAINDER, help="-- trusted worker command and arguments")
    for sp in (p_mnt, p_wrk):
        sp.add_argument("--retry-parked", action="store_true", help="retry repositories parked after repeated failures")
        for name, fld in (("max-repos", "max_repos"), ("max-files", "max_files"), ("max-bytes", "max_bytes"),
                          ("catalog-entries", "catalog_entries"), ("net-bytes", "net_bytes"), ("net-requests", "net_requests"),
                          ("max-failures", "max_failures"), ("max-proposal-bytes", "max_proposal_bytes")):
            sp.add_argument(f"--{name}", dest=fld, type=int, default=getattr(workers.Limits, fld))
        for name, fld in (("net-seconds", "net_seconds"), ("max-seconds", "max_seconds"), ("worker-seconds", "worker_seconds")):
            sp.add_argument(f"--{name}", dest=fld, type=float, default=getattr(workers.Limits, fld))
    for sp in (p_cat, p_snap):
        sp.add_argument("--net-bytes", type=int, default=collect.Budget.max_bytes, help="network byte budget")
        sp.add_argument("--net-seconds", type=float, default=collect.Budget.max_seconds, help="network time budget")
    return parser


def _read_input(args: argparse.Namespace) -> str:
    if args.text is not None:
        return args.text
    if args.file is not None:
        with open(args.file, "rb") as fh:
            return intake.read_bounded(fh, args.max_bytes, str(args.file))
    return intake.read_bounded(sys.stdin.buffer, args.max_bytes, "stdin")


def _limits(args: argparse.Namespace) -> workers.Limits:
    fields = {k: getattr(args, k) for k in workers.Limits.__dataclass_fields__ if hasattr(args, k)}
    return workers.Limits(**fields, build=not getattr(args, "no_build", False))


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
        elif args.command == "catalog":
            budget = collect.Budget(max_bytes=args.net_bytes, max_seconds=args.net_seconds)
            result = collect.catalog(args.root, args.limit, budget=budget, published=args.published)
            _emit(result)
            if args.published and not result["published"]["ok"]:
                return result["published"]["code"]  # backing intake landed; the optional source did not
        elif args.command == "snapshot":
            budget = collect.Budget(max_bytes=args.net_bytes, max_seconds=args.net_seconds)
            _emit(collect.snapshot(args.root, args.repo, args.max_files, args.max_bytes, paths=args.path, budget=budget))
        elif args.command == "prepare":
            _emit(wiki.prepare(args.root, args.repo))
        elif args.command == "apply":
            _emit(wiki.apply(args.root, args.packet, args.proposal))
        elif args.command == "audit":
            result = wiki.audit(args.root, args.level)
            _emit(result)
            if not result["ok"]:
                return EXIT_AUDIT_FAILED
        elif args.command == "build":
            _emit(maps.build(args.root))
        elif args.command == "maintain":
            _emit(workers.maintain(args.root, _limits(args), retry_parked=args.retry_parked))
        elif args.command == "worker":
            argv = args.argv[1:] if args.argv[:1] == ["--"] else list(args.argv)  # strip only the parser delimiter
            argv = argv or None
            _emit(workers.run_worker(args.root, argv, _limits(args), repo=args.repo, retry_parked=args.retry_parked))
        elif args.command == "query":
            _emit(maps.query(args.root, args.text, limit=args.limit, max_chars=args.max_chars,
                              include_archive=args.include_archive))
    except core.WorkbenchError as exc:
        _emit({"error": type(exc).__name__, "code": exc.code, "message": str(exc)})
        return exc.code
    except (OSError, subprocess.TimeoutExpired) as exc:
        _emit({"error": type(exc).__name__, "code": 1, "message": str(exc)})
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
