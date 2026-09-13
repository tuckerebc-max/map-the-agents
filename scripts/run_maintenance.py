"""Trusted hosted orchestration. Valid partial progress may publish; fatal validation errors may not."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from map_agents import automation, core, maps, wiki, workers  # noqa: E402


def run(root: Path, summary_path: Path, *, event_path: Path | None = None,
        limits: workers.Limits | None = None, transport=None) -> dict:
    summary = {"publishable": False, "status": "failed", "stage": "receive"}
    try:
        if event_path is not None:
            received = automation.receive_event(root, event_path)
            summary["received_repos"] = len(received["accepted"])
            summary["rejected_urls"] = len(received["rejected"])
        summary["stage"] = "inbox"
        inbox = automation.receive_inbox(root, "public")
        summary["inbox"] = {"processed": len(inbox["processed"]), "failed": len(inbox["failed"]),
                            "skipped": len(inbox["skipped"]), "deferred": inbox["deferred"]}
        summary["stage"] = "maintain"
        refreshed = workers.maintain(root, limits or workers.Limits(max_seconds=480), transport=transport)
        summary["refresh"] = {"status": refreshed["status"], "attempted": len(refreshed["attempted"]),
                              "snapshots": len(refreshed["snapshots"]), "failures": len(refreshed["failures"]),
                              "stopped": refreshed["stopped"], "parked": len(refreshed["parked"]),
                              "needs_distillation": len(refreshed["needs_distillation"]),
                              "queue": refreshed["queue"], "budget": refreshed["budget"]}
        summary["stage"] = "verify-sources"
        verified = 0
        for key, record in core.load_repos(root).items():
            if record.get("latest_snapshot"):
                wiki.verify_snapshot(root, key, record["latest_snapshot"])
                verified += 1
        summary["verified_snapshots"] = verified
        summary["stage"] = "build"
        built = maps.build(root)
        summary["map"] = {k: built[k] for k in ("repos", "known", "invalid_dossiers")}
        summary["stage"] = "audit"
        audited = wiki.audit(root, "working")
        summary["audit_ok"] = audited["ok"]
        if not audited["ok"] or built["invalid_dossiers"]:
            raise core.CorruptState("generated corpus validation failed")
        partial = bool(inbox["failed"] or refreshed["failures"] or refreshed["stopped"])
        summary.update(publishable=True, status="partial" if partial else "validated", stage="validated")
    except Exception as exc:
        # No arbitrary exception message, event body, private text or model output in hosted artifacts.
        summary["error"] = type(exc).__name__
    core.atomic_write_bytes(summary_path, core.dump_json(summary))
    return summary


def report(path: Path) -> int:
    summary = json.loads(path.read_text(encoding="utf-8"))
    text = (f"Maintenance: {summary['status']}. Publishable: {summary['publishable']}.\n\n"
            f"Refresh failures: {summary.get('refresh', {}).get('failures', 0)}; "
            f"inbox failures: {summary.get('inbox', {}).get('failed', 0)}; "
            f"awaiting distillation: {summary.get('refresh', {}).get('needs_distillation', 0)}.\n")
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(text)
    return 0 if summary["status"] == "validated" else 5


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("corpus"))
    parser.add_argument("--summary", type=Path, default=Path("work/maintenance-summary.json"))
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    if args.report:
        return report(args.summary)
    event = Path(os.environ["GITHUB_EVENT_PATH"]) if os.environ.get("GITHUB_EVENT_NAME") == "repository_dispatch" else None
    result = run(args.root, args.summary, event_path=event)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["publishable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
