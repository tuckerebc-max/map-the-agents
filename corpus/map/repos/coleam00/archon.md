# coleam00/archon

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a7e300b2a740 @ dfc91846333717e8

## Summary (orientation draft, not independently verified)

Archon is a self-hostable workflow engine for AI coding agents: development processes are defined as YAML workflows mixing deterministic and AI nodes, exposed via CLI, web dashboard, and optional chat-platform adapters, backed by SQLite/PostgreSQL. Evidence is documentation-only (README, AGENTS.md, SECURITY.md); no runtime code slices were supplied. Evidence coverage: 121 of 156 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Archon is described as a workflow engine for AI coding agents in which development processes (planning, implementation, validation, review, PR creation) are defined as YAML workflows. -- evidence: [README.md#L23-L23](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L23-L23)
  - [observation/documented] The project ships 19 default workflows, and a router can select an appropriate workflow when the user describes what they want. -- evidence: [README.md#L258-L258](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L258-L258)
- components (1 claim(s)):
  - [observation/documented] The documented architecture layers platform adapters above an orchestrator, with a slash command handler, YAML workflow executor, AI assistant clients (Claude/Codex/Pi), and a SQLite/PostgreSQL store of 14 core tables covering codebases, conversations, sessions, and workflow runs. -- evidence: [README.md#L277-L310](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L277-L310)
- design-choices (2 claim(s)):
  - [observation/documented] Workflows compose deterministic nodes (bash scripts, tests, git operations) with AI nodes, so AI runs only where it adds value; the example includes a test loop iterating until tests pass and an interactive human approval gate. -- evidence: [README.md#L64-L69](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L64-L69), [README.md#L49-L54](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L49-L54), [README.md#L33-L37](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L33-L37), [README.md#L56-L58](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L56-L58)
  - [observation/documented] Telemetry sends anonymous categorical events (bundled workflow names only, run outcomes, token/cost totals, machine context) with no PII; it can be disabled via environment variables and is auto-disabled when CI=true. -- evidence: [README.md#L344-L344](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L344-L344), [README.md#L333-L333](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L333-L333), [README.md#L335-L342](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L335-L342), [README.md#L354-L354](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L354-L354), [README.md#L348-L352](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L348-L352)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The setup wizard copies the Archon skill into target projects, and users are told to run Claude Code from the target repo rather than the Archon repo. -- evidence: [README.md#L153-L153](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L153-L153), [README.md#L214-L214](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L214-L214), [README.md#L104-L104](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L104-L104)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI includes commands such as `archon serve` (start the web dashboard), `archon workflow list`, `archon telemetry status/reset`, and `archon doctor`. -- evidence: [README.md#L356-L356](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L356-L356), [README.md#L258-L258](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L258-L258), [README.md#L218-L218](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L218-L218)
  - [observation/documented] The web dashboard offers a chat page with streaming and tool-call visualization, a workflow monitoring dashboard, a drag-and-drop workflow builder for DAG workflows, and per-run execution views. -- evidence: [README.md#L222-L226](https://github.com/coleam00/Archon/blob/a7e300b2a74051711b7de2262c267cb96d3002d2/README.md#L222-L226)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
More evidence: [full detail](archon.detail.md)

Metadata and full claim list: [full detail](archon.detail.md)
Human notes ([notes](archon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
