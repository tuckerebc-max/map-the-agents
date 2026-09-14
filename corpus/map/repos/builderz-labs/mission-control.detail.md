# builderz-labs/mission-control -- full detail

[Back to orientation](mission-control.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/builderz-labs/mission-control/5483a0e1eef15b467c167e95796791112cedbb7c/8467a0c3e4579618.json](../../../wiki/dossiers/builderz-labs/mission-control/5483a0e1eef15b467c167e95796791112cedbb7c/8467a0c3e4579618.json)

## specifications (1 claim(s))

- [observation/documented] Mission Control is described as a self-hosted control plane for operating AI agents: dispatching tasks, inspecting runs, reviewing failures, tracking spend, and coordinating runtimes from a local dashboard backed by SQLite. -- evidence: [README.md#L5-L5](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L5-L5), [README.md#L7-L8](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L7-L8) (`clm_f923958367d213c9a4ff609d64378513868906b7f6820503551601c0e855a714`)

## components (1 claim(s))

- [observation/documented] Shipped surfaces include task inbox/assignment/review with an Aegis quality gate and completion receipts, agent registration and sessions, activity/schedules/alerts/webhooks/cost views, memory browser and skills registry, and governance features like roles, API keys, approvals, audits, and evals. -- evidence: [README.md#L76-L83](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L76-L83) (`clm_fbd9518347539ed3c5697cd16b12588bd40d3cd01b1aa5cc9cee0ff966be8512`)

## design-choices (1 claim(s))

- [observation/documented] The control plane sits above agent runtimes and does not replace their reasoning or tool loops; it provides operators a single place to observe and govern work around those loops. -- evidence: [README.md#L73-L74](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L73-L74) (`clm_881fd3310242eacce597cdc31baa3afa64859eeff23f9fbb4deede013d8d3894`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run pnpm install --frozen-lockfile, lint, typecheck, test, build, and test:e2e, with pnpm quality:gate running the full repository gate; commits follow Conventional Commits with no AI-attribution trailers and pnpm is the only package manager. -- evidence: [README.md#L267-L267](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L267-L267), [README.md#L258-L265](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L258-L265), [CLAUDE.md#L69-L73](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CLAUDE.md#L69-L73) (`clm_37cdac3e5f3e8fcda08363661f418cae560fc71eb6b56a4bee2a08617ac17bd1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a Web UI, CLI, MCP server, OpenAPI-described REST API, WebSocket, and SSE; a running instance serves interactive docs at /docs and OpenAPI JSON at /api/docs. -- evidence: [README.md#L168-L170](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L168-L170), [README.md#L76-L83](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L76-L83) (`clm_facf661e17006c4b425634c6ca1741d48ef902659e4a7c3cae341b855aa81e33`)
- [observation/documented] A gateway-free REST loop is documented: agents register via POST /api/agents/register, create work via POST /api/tasks, and claim queues via GET /api/tasks/queue?agent=..., authenticated with a Bearer API key. -- evidence: [README.md#L130-L134](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L130-L134), [README.md#L144-L147](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L144-L147), [README.md#L120-L121](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L120-L121), [README.md#L136-L140](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L136-L140) (`clm_acc01c493b6d65eca36cb81bbb7f8d144ffcf906033660352e97bbc14540946e`)

## memory-state (1 claim(s))

- [observation/documented] Runtime data defaults to a .data/ directory, overridable via the MISSION_CONTROL_DATA_DIR environment variable; the database defaults to <data dir>/mission-control.db. -- evidence: [CLAUDE.md#L64-L65](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CLAUDE.md#L64-L65), [README.md#L239-L241](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L239-L241) (`clm_31212c1d4d335e7942fc8bd6f87a23ae17c6ec1c7d1f146cf5e319ac534ba5af`)

## orchestration (1 claim(s))

- [observation/documented] Tasks flow through inbox, assignment, execution, review, quality review, and completion; Aegis review requires an approval record before a task reaches done, and recurring task templates create dated work on cron schedules. -- evidence: [README.md#L176-L177](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L176-L177), [README.md#L198-L199](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L198-L199) (`clm_e71168c87c92f1d92b7faf845eae5732443da0988d9706e72a13e3c8af1bc741`)

## tools-permissions (1 claim(s))

- [observation/documented] Host CLI dispatch gained opt-in sandbox flags: an allowlist-validated allowedTools, a clamped --max-budget-usd, and a workspace-scoped cwd escape-protected via MC_WORKSPACE_ROOT, sourced from agents.config with per-task overrides. -- evidence: [CHANGELOG.md#L57-L60](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CHANGELOG.md#L57-L60) (`clm_7bf0ee6e9e9ccf49e3f5e75dd8ca065cd8945fb1241cf1982dc4901dacd630e4`)

## evaluation (1 claim(s))

- [inference/documented] The README's governance row lists 'evals' among shipped surfaces, suggesting the product includes evaluation features for agent work, though the snapshot does not describe how they score agent behavior. -- evidence: [README.md#L76-L83](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L76-L83) (`clm_49dc6997e4999232c94d74715e6289759fe319031d3c8079472c66ca3b77e235`)

## dependencies (1 claim(s))

- [observation/documented] The stack is documented as Next.js 16 App Router, React 19, TypeScript 5, Tailwind CSS 4, Zustand, Recharts, xterm.js, and SQLite via better-sqlite3 in WAL mode, with Zod validation at input boundaries. -- evidence: [README.md#L229-L237](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L229-L237), [CLAUDE.md#L5-L5](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/CLAUDE.md#L5-L5) (`clm_35b971152edc765141f3e51ab6883445e05b12e0599dc358fe2d2dba684db957`)

## limitations (2 claim(s))

- [observation/documented] The project is alpha software whose APIs, schemas, and configuration may change between releases; adapter depth varies by runtime across OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, and Claude SDK workflows. -- evidence: [README.md#L113-L116](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L113-L116), [README.md#L22-L24](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L22-L24) (`clm_3db206e08ecd090e5882d84f1eeb41002c0fa7a85d6a7eca655d696c0e41a64e`)
- [observation/documented] A gateway is optional for task, project, agent, scheduler, webhook, alert, and cost work, but live session messaging requires a connected runtime gateway; strict workspaces block deployment-level integrations until resources carry workspace ownership. -- evidence: [README.md#L85-L89](https://github.com/builderz-labs/mission-control/blob/5483a0e1eef15b467c167e95796791112cedbb7c/README.md#L85-L89) (`clm_92ca659ee377200f5bb9a48f82bbb9c689f4803738b6083b3b2d932dec2612d7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

