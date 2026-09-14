"""Trusted hosted orchestration. Valid partial progress may publish; fatal validation errors may not."""
from __future__ import annotations

import argparse
import inspect
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from map_agents import automation, collect, core, directory, maps, wiki, workers  # noqa: E402

DIRECTORY_LIMIT = 25  # pages captured per hosted run; small and finite next to the 5-repo/50-entry refresh
DIRECTORY_BUDGET = {"max_bytes": 4_000_000, "max_seconds": 60.0, "max_requests": 80}


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
        # Snapshot repos.json before the only mutating stage in this pipeline, so "changed" is read from
        # the actual before/after catalog state -- never guessed from model text (none runs here anyway).
        before_repos = core.load_repos(root)
        refreshed = workers.maintain(root, limits or workers.Limits(max_seconds=420), transport=transport)
        summary["refresh"] = {"status": refreshed["status"], "attempted": len(refreshed["attempted"]),
                              "snapshots": len(refreshed["snapshots"]), "failures": len(refreshed["failures"]),
                              "stopped": refreshed["stopped"], "parked": len(refreshed["parked"]),
                              "needs_distillation": len(refreshed["needs_distillation"]),
                              "queue": refreshed["queue"], "budget": refreshed["budget"]}
        summary["stage"] = "directory"
        try:
            dcap = directory.capture(root, DIRECTORY_LIMIT, transport=transport,
                                     budget=collect.Budget(**DIRECTORY_BUDGET))
            summary["directory"] = {
                "pages_total": dcap["pages_total"], "captured": dcap["captured"], "backlog": dcap["backlog"],
                "processed": dcap["processed"], "newly_captured": len(dcap["newly_captured"]),
                "newly_failed": len(dcap["newly_failed"]), "failures": dcap["failures"],
                "tree_truncated": dcap["tree_truncated"], "stopped": dcap["stopped"],
                "unsafe_pages": dcap["unsafe_pages"],
            }
            # Only send leads into canonical intake after a capture that actually ran; a partial capture
            # failure stays explicit above, never papered over by intake succeeding on stale/partial data.
            leads = directory.ingest_new_leads(root, 50)
            summary["directory_intake"] = {"candidates": leads["candidates"], "picked": leads["picked"],
                                           "deferred": leads["deferred"], "new_repos": len(leads["new_repos"])}
        except directory.DirectoryError as exc:
            # Precondition not met yet (e.g. no catalog cursor on a brand-new corpus): an honest, non-fatal
            # skip. Integrity/malformed-data errors are a different class and are NOT caught here -- they
            # propagate to the outer handler so a tampered or corrupt capture never publishes as success.
            summary["directory"] = {"skipped": str(exc)[:200]}
        # Diffed after directory capture + intake, so any newly intaken lead is itself a changed key.
        after_repos = core.load_repos(root)
        changed_keys = sorted(k for k in after_repos if before_repos.get(k) != after_repos.get(k))
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
        # A scoped audit is only ever narrower than the full one this corpus already runs at release time,
        # and only once wiki.audit actually supports a `repos` filter, and only for a partitioned layout
        # (a single shared kernel audit inherently checks everything, so it always runs whole). maps.build
        # above has already byte-verified and structurally validated every dossier regardless of scope.
        layout = wiki.load_layout(root)
        supports_scope = "repos" in inspect.signature(wiki.audit).parameters
        scoped = layout.get("layout") == "partitioned" and supports_scope
        audited = wiki.audit(root, "working", repos=changed_keys) if scoped else wiki.audit(root, "working")
        summary["audit_ok"] = audited["ok"]
        summary["audit_scope"] = "scoped" if scoped else "full"
        if scoped:
            summary["audit_scoped_repos"] = len(changed_keys)
        if not audited["ok"] or built["invalid_dossiers"]:
            raise core.CorruptState("generated corpus validation failed")
        partial = bool(inbox["failed"] or refreshed["failures"] or refreshed["stopped"]
                        or summary["directory"].get("newly_failed") or summary["directory"].get("stopped"))
        summary.update(publishable=True, status="partial" if partial else "validated", stage="validated")
    except Exception as exc:
        # No arbitrary exception message, event body, private text or model output in hosted artifacts.
        summary["error"] = type(exc).__name__
    core.atomic_write_bytes(summary_path, core.dump_json(summary))
    return summary


def report(path: Path) -> int:
    summary = json.loads(path.read_text(encoding="utf-8"))
    directory_summary = summary.get("directory", {})
    if "skipped" in directory_summary:
        directory_text = f"skipped ({directory_summary['skipped']})"
    else:
        directory_text = (f"{directory_summary.get('captured', 0)} captured, "
                          f"backlog {directory_summary.get('backlog', 0)}, failures {directory_summary.get('failures', 0)}")
    audit_scope = summary.get("audit_scope", "full")
    audit_text = (f"scoped ({summary.get('audit_scoped_repos', 0)} repositories)"
                  if audit_scope == "scoped" else audit_scope)
    text = (f"Maintenance: {summary['status']}. Publishable: {summary['publishable']}.\n\n"
            f"Refresh failures: {summary.get('refresh', {}).get('failures', 0)}; "
            f"inbox failures: {summary.get('inbox', {}).get('failed', 0)}; "
            f"awaiting distillation: {summary.get('refresh', {}).get('needs_distillation', 0)}.\n\n"
            f"Directory capture: {directory_text}. Audit scope: {audit_text}.\n")
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
