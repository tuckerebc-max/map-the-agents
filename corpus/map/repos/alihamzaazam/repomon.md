# alihamzaazam/repomon

Status: distilled - Freshness: stale
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6fc4a8fbed31 @ 4c317c5d961f84db

## Summary (orientation draft, not independently verified)

Selected evidence records: A background daemon, repomond, owns SQLite, file watchers, the git layer, and the agent runtime, exposing a JSON-RPC API over a Unix socket or Windows named pipe; desktop, TUI, and iOS clients are thin clients over that API. The workspace is split into crates: repomon-core (data model, gix git layer, SQLite store, watchers, usage ledger, agent runtime), repomon-daemon, repomon-tui, repomon-mcp, repomon-host, and a Tauri desktop app.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] A background daemon, repomond, owns SQLite, file watchers, the git layer, and the agent runtime, exposing a JSON-RPC API over a Unix socket or Windows named pipe; desktop, TUI, and iOS clients are thin clients over that API. -- evidence: [README.md#L142-L144](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L142-L144)
  - [observation/documented] The workspace is split into crates: repomon-core (data model, gix git layer, SQLite store, watchers, usage ledger, agent runtime), repomon-daemon, repomon-tui, repomon-mcp, repomon-host, and a Tauri desktop app. -- evidence: [README.md#L146-L153](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L146-L153)
- design-choices (4 claim(s)):
  - [observation/documented] Supervision is off by default globally and per lane; enabling requires both the master switch in config.toml and an enabled lane policy, with the master switch overriding every lane. -- evidence: [docs/agent-supervision.md#L93-L96](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L93-L96), [docs/agent-supervision.md#L3-L5](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L3-L5)
  - [observation/documented] Default supervision policy auto-approves only repo-scoped command_exec and file_write dialogs; network, credential, deletion, push, install, device, and unknown classes default to hold, and nothing auto-denies out of the box. -- evidence: [docs/agent-supervision.md#L75-L85](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L75-L85), [docs/agent-supervision.md#L87-L89](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L87-L89)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's development section instructs contributors to run `cargo test --workspace` for Rust and `bun install && bun run test` in apps/desktop for the frontend. -- evidence: [README.md#L157-L161](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L157-L161)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The daemon exposes a JSON-RPC API documented for writing custom clients, plus an MCP server (`repomond mcp`) that exposes the fleet to agents. -- evidence: [README.md#L89-L97](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L89-L97), [README.md#L146-L153](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L146-L153)
  - [observation/documented] Supervision methods live under a `supervision.*` JSON-RPC namespace (get, set, audit, status, nudge) on the local daemon socket. -- evidence: [docs/agent-supervision.md#L276-L282](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L276-L282), [docs/agent-supervision.md#L274-L274](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L274-L274)
- memory-state (2 claim(s)):
  - [observation/documented] Repomon writes its own SQLite database in a platform data directory (overridable via REPOMON_DATA_DIR) and a Repomind home normally at ~/repomind when that feature is enabled. -- evidence: [README.md#L81-L81](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L81-L81)
  - [observation/documented] Every supervision action or skipped action writes exactly one row to a durable supervision_log SQLite table recording trigger, decision, keys sent, outcome, and pane excerpt. -- evidence: [docs/agent-supervision.md#L244-L263](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L244-L263), [docs/agent-supervision.md#L241-L242](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L241-L242), [docs/agent-supervision.md#L265-L270](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L265-L270)
More evidence: [full detail](repomon.detail.md)

Metadata and full claim list: [full detail](repomon.detail.md)
Human notes ([notes](repomon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
