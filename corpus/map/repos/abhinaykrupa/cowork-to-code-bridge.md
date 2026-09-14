# abhinaykrupa/cowork-to-code-bridge

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 30b06c2fb24a @ b7f65c950b933f92

## Summary (orientation draft, not independently verified)

Selected evidence records: The system has four parts: a Cowork skill auto-loaded in each session, a shared bridge folder with queue/, results/, and progress/ subfolders, a daemon managed by launchd or systemd (or started manually), and run_claude.sh which hands tasks to a local Claude Code agent. Tasks are JSON files written to a queue/ folder and results are JSON files in results/, with the daemon polling roughly every second; no network connection exists between the Cowork sandbox and the machine.

## Source coverage

Source coverage (partial): 3 of 48 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The system has four parts: a Cowork skill auto-loaded in each session, a shared bridge folder with queue/, results/, and progress/ subfolders, a daemon managed by launchd or systemd (or started manually), and run_claude.sh which hands tasks to a local Claude Code agent. -- evidence: [README.md#L139-L144](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L139-L144)
  - [observation/documented] Bundled whitelisted scripts include run_claude.sh, mac_health.sh, mac_ram.sh, mac_disk.sh, mac_top.sh, mac_network.sh, process_kill.sh, port_check.sh, docker_ps.sh, docker_logs.sh, git_status.sh, pkg_outdated.sh, and list_scripts.sh, many supporting --json structured output. -- evidence: [README.md#L229-L248](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L229-L248)
- design-choices (3 claim(s)):
  - [observation/documented] Rather than a network connection, the bridge uses files on a shared folder that Cowork mounts; the README notes this is slower (about one second per call versus milliseconds for MCP) but works because Cowork's sandbox cannot reach localhost services. -- evidence: [README.md#L504-L504](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L504-L504), [README.md#L502-L502](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L502-L502), [README.md#L498-L498](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L498-L498)
  - [observation/documented] Requests are idempotent: results are cached by an idempotency key so a retry after a dropped connection returns the cached result instead of re-running the agent or script; tasks are journaled and marked in-flight, and a reboot mid-task is detected rather than silently re-run. -- evidence: [README.md#L35-L35](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L35-L35), [README.md#L146-L146](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L146-L146)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Tasks are JSON files written to a queue/ folder and results are JSON files in results/, with the daemon polling roughly every second; no network connection exists between the Cowork sandbox and the machine. -- evidence: [README.md#L496-L496](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L496-L496), [README.md#L486-L494](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L486-L494)
  - [observation/documented] The pip install provides console scripts cowork-to-code-bridge-daemon, -uninstall, and -selfcheck; selfcheck checks six items, prints PASS/FAIL per check, and exits 0 if all pass or 1 if any fail. -- evidence: [README.md#L305-L310](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L305-L310), [README.md#L315-L315](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L315-L315), [README.md#L69-L72](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L69-L72), [README.md#L298-L298](https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/30b06c2fb24a916c835a2928d2d274727faab09b/README.md#L298-L298)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](cowork-to-code-bridge.detail.md)

Metadata and full claim list: [full detail](cowork-to-code-bridge.detail.md)
Human notes ([notes](cowork-to-code-bridge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
