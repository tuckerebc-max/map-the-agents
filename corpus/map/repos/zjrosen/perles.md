# zjrosen/perles

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f97afa7a7c44 @ a14eba7bf0be77df

## Summary (orientation draft, not independently verified)

Perles is a terminal UI for beads issue tracking powered by a custom BQL query language supporting boolean search, date filters, dependency traversal, and custom kanban views. The CLI supports flags including --beads-dir, --config, --version, --help, and --debug, plus subcommands: perles (TUI), themes, workflows, and playground. Evidence coverage: 168 of 233 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The Control Plane comprises ControlPlane (lifecycle entry point), Registry (in-memory workflow storage), Supervisor, ResourceScheduler, HealthMonitor, and CrossWorkflowEventBus. -- evidence: [docs/CONTROL_PLANE.md#L66-L73](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L66-L73)
- design-choices (2 claim(s)):
  - [observation/documented] Because Cursor reads MCP config only from .cursor/mcp.json, Perles writes role-specific server entries (orchestrator, per-worker, observer) into that shared file using a read-merge-write pattern. -- evidence: [docs/CURSOR_AGENT.md#L62-L62](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L62-L62), [docs/CURSOR_AGENT.md#L121-L121](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L121-L121), [docs/CURSOR_AGENT.md#L41-L41](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L41-L41), [docs/CURSOR_AGENT.md#L114-L114](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L114-L114)
  - [observation/documented] Since Cursor lacks --append-system-prompt, Perles prepends the system prompt to the main prompt with a blank line separator, the same approach used for OpenCode. -- evidence: [docs/CURSOR_AGENT.md#L66-L66](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L66-L66)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: optional Cursor integration tests are build-tagged, run via go test -tags=cursor_integration, and are intended for local/dev environments rather than CI. -- evidence: [docs/CURSOR_AGENT.md#L94-L96](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L94-L96), [docs/CURSOR_AGENT.md#L90-L92](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L90-L92), [docs/CURSOR_AGENT.md#L84-L86](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L84-L86)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Perles is a terminal UI for beads issue tracking powered by a custom BQL query language supporting boolean search, date filters, dependency traversal, and custom kanban views. -- evidence: [README.md#L3-L3](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/README.md#L3-L3)
  - [observation/documented] The CLI supports flags including --beads-dir, --config, --version, --help, and --debug, plus subcommands: perles (TUI), themes, workflows, and playground. -- evidence: [docs/getting-started.md#L62-L68](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L62-L68), [docs/getting-started.md#L72-L77](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/getting-started.md#L72-L77)
- memory-state (1 claim(s)):
  - [observation/documented] Workflow instances track identity, state, priority, labels, timestamps, runtime infrastructure/session/MCP port, token budget, and last heartbeat/progress times; the Registry stores them in memory. -- evidence: [docs/CONTROL_PLANE.md#L258-L261](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L258-L261), [docs/CONTROL_PLANE.md#L263-L267](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L263-L267), [docs/CONTROL_PLANE.md#L244-L249](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L244-L249), [docs/CONTROL_PLANE.md#L66-L73](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L66-L73), [docs/CONTROL_PLANE.md#L251-L253](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L251-L253), [docs/CONTROL_PLANE.md#L269-L273](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CONTROL_PLANE.md#L269-L273)
- orchestration (3 claim(s)):
  - [observation/documented] Orchestration mode is a multi-agent control plane where a coordinator headless agent spawns, replaces, and retires worker agents via built-in MCP tools, with multiple workflows run in parallel. -- evidence: [ORCHESTRATION.md#L10-L11](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L10-L11), [ORCHESTRATION.md#L6-L8](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L6-L8)
  - [observation/documented] Orchestration providers include Claude, Amp, Codex, OpenCode, and Cursor Agent CLI; coordinator and worker clients can be mixed, e.g. cursor coordinator with claude workers. -- evidence: [docs/CURSOR_AGENT.md#L3-L3](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L3-L3), [docs/CURSOR_AGENT.md#L19-L19](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/docs/CURSOR_AGENT.md#L19-L19), [ORCHESTRATION.md#L26-L29](https://github.com/zjrosen/perles/blob/f97afa7a7c442d7a3f3d4f3a7ed842463a865864/ORCHESTRATION.md#L26-L29)
- tools-permissions (1 claim(s)):
More evidence: [full detail](perles.detail.md)

Metadata and full claim list: [full detail](perles.detail.md)
Human notes ([notes](perles.notes.md), never overwritten by build)

[Back to map index](../../index.md)
