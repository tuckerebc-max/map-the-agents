# builderz-labs/mission-control

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5483a0e1eef1 @ 8467a0c3e4579618

## Summary (orientation draft, not independently verified)

Selected evidence records: Mission Control is described as a self-hosted control plane for operating AI agents: dispatching tasks, inspecting runs, reviewing failures, tracking spend, and coordinating runtimes from a local dashboard backed by SQLite. The control plane sits above agent runtimes and does not replace their reasoning or tool loops; it provides operators a single place to observe and govern work around those loops.

## Source coverage

Source coverage (partial): 3 of 25 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Mission Control is described as a self-hosted control plane for operating AI agents: dispatching tasks, inspecting runs, reviewing failures, tracking spend, and coordinating runtimes from a local dashboard backed by SQLite. -- evidence: [README.md#L5-L5](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L5-L5), [README.md#L7-L8](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L7-L8)
- components (1 claim(s)):
  - [observation/documented] Shipped surfaces include task inbox/assignment/review with an Aegis quality gate and completion receipts, agent registration and sessions, activity/schedules/alerts/webhooks/cost views, memory browser and skills registry, and governance features like roles, API keys, approvals, audits, and evals. -- evidence: [README.md#L76-L83](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L76-L83)
- design-choices (1 claim(s)):
  - [observation/documented] The control plane sits above agent runtimes and does not replace their reasoning or tool loops; it provides operators a single place to observe and govern work around those loops. -- evidence: [README.md#L73-L74](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L73-L74)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run pnpm install --frozen-lockfile, lint, typecheck, test, build, and test:e2e, with pnpm quality:gate running the full repository gate; commits follow Conventional Commits with no AI-attribution trailers and pnpm is the only package manager. -- evidence: [README.md#L267-L267](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L267-L267), [README.md#L258-L265](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L258-L265), [CLAUDE.md#L69-L73](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CLAUDE.md#L69-L73)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a Web UI, CLI, MCP server, OpenAPI-described REST API, WebSocket, and SSE; a running instance serves interactive docs at /docs and OpenAPI JSON at /api/docs. -- evidence: [README.md#L168-L170](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L168-L170), [README.md#L76-L83](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L76-L83)
  - [observation/documented] A gateway-free REST loop is documented: agents register via POST /api/agents/register, create work via POST /api/tasks, and claim queues via GET /api/tasks/queue?agent=..., authenticated with a Bearer API key. -- evidence: [README.md#L130-L134](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L130-L134), [README.md#L144-L147](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L144-L147), [README.md#L120-L121](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L120-L121), [README.md#L136-L140](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L136-L140)
- memory-state (1 claim(s)):
  - [observation/documented] Runtime data defaults to a .data/ directory, overridable via the MISSION_CONTROL_DATA_DIR environment variable; the database defaults to <data dir>/mission-control.db. -- evidence: [CLAUDE.md#L64-L65](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CLAUDE.md#L64-L65), [README.md#L239-L241](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L239-L241)
- orchestration (1 claim(s)):
  - [observation/documented] Tasks flow through inbox, assignment, execution, review, quality review, and completion; Aegis review requires an approval record before a task reaches done, and recurring task templates create dated work on cron schedules. -- evidence: [README.md#L176-L177](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L176-L177), [README.md#L198-L199](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L198-L199)
- tools-permissions (1 claim(s)):
More evidence: [full detail](mission-control.detail.md)

Metadata and full claim list: [full detail](mission-control.detail.md)
Human notes ([notes](mission-control.notes.md), never overwritten by build)

[Back to map index](../../index.md)
