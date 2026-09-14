# 2389-research/fleet-control

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit efe2657f5465 @ e6a4a546b9278950

## Summary (orientation draft, not independently verified)

The evidence is a design spec and implementation plan for `control`, a Go binary that observes and manages AI agents running in tmux via a daemon, CLI, TUI, and MCP server. Claims below describe the documented design; the plan also contains contributor-facing workflow instructions. Evidence coverage: 143 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 22 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

22 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The design spec describes a Go binary `control` that observes and manages running AI agents via tmux introspection, offering visibility, stopping, and session history. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L5-L5](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The architecture has three layers in one Go module: a `controld` daemon, a `control` CLI, and an MCP server, with the CLI and MCP as thin clients over the daemon's HTTP API. -- evidence: [docs/superpowers/plans/2026-03-23-control-plane.md#L7-L7](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L7-L7), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L61-L61](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L61-L61), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L19-L19](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L19-L19)
  - [observation/documented] The daemon polls tmux roughly every 5 seconds, keeps an in-memory agent registry guarded by sync.RWMutex, persists history to SQLite in WAL mode, and serves HTTP/1.1 over a Unix socket. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L25-L29](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L25-L29)
- design-choices (5 claim(s)):
  - [observation/documented] Core principles include observer-not-launcher, zero agent instrumentation, CLI/MCP parity over one internal API, a single binary, CGO-free builds, and no elevated privileges. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L9-L15](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L9-L15)
  - [observation/documented] All tmux and process interactions are specified to use exec.Command with discrete argument lists, avoiding shell interpolation to prevent injection from tmux-controlled values. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L272-L272](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L272-L272), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L9-L15](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L9-L15)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the implementation plan instructs agentic workers to use superpowers subagent-driven-development or executing-plans skills, with checkbox-tracked tasks and TDD-style test-first steps. -- evidence: [docs/superpowers/plans/2026-03-23-control-plane.md#L220-L223](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L220-L223), [docs/superpowers/plans/2026-03-23-control-plane.md#L218-L218](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L218-L218), [docs/superpowers/plans/2026-03-23-control-plane.md#L3-L3](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L3-L3)
  - [observation/documented] Repository development practice: the plan mandates commit hygiene (staging specific files, not git add -A) and test hygiene including -race for concurrent packages, 30s timeouts, and unique socket paths from t.TempDir(). -- evidence: [docs/superpowers/plans/2026-03-23-control-plane.md#L30-L30](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L30-L30), [docs/superpowers/plans/2026-03-23-control-plane.md#L28-L28](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/plans/2026-03-23-control-plane.md#L28-L28)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] CLI commands include daemon start/stop/status, ls, show, stop, history, tui, and mcp, with global flags --json, --socket, and --help, and filter flags like --project, --type, --since, --until, --limit. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L77-L77](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L77-L77), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L65-L73](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L65-L73), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L75-L75](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L75-L75)
  - [observation/documented] The daemon exposes HTTP endpoints over the Unix socket: /agents, /agents/:id, /agents/:id/stop, /history, /history/:id/actions, and /ping, all returning JSON. -- evidence: [docs/superpowers/specs/2026-03-23-control-plane-design.md#L411-L418](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L411-L418), [docs/superpowers/specs/2026-03-23-control-plane-design.md#L420-L420](https://github.com/2389-research/fleet-control/blob/efe2657f5465da3f4e8740165b6f122eb8e38035/docs/superpowers/specs/2026-03-23-control-plane-design.md#L420-L420)
- memory-state (2 claim(s)):
More evidence: [full detail](fleet-control.detail.md)

Metadata and full claim list: [full detail](fleet-control.detail.md)
Human notes ([notes](fleet-control.notes.md), never overwritten by build)

[Back to map index](../../index.md)
