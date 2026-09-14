---
access: public
aliases: []
claim_ids:
- clm_31212c1d4d335e7942fc8bd6f87a23ae17c6ec1c7d1f146cf5e319ac534ba5af
- clm_35b971152edc765141f3e51ab6883445e05b12e0599dc358fe2d2dba684db957
- clm_37cdac3e5f3e8fcda08363661f418cae560fc71eb6b56a4bee2a08617ac17bd1
- clm_3db206e08ecd090e5882d84f1eeb41002c0fa7a85d6a7eca655d696c0e41a64e
- clm_49dc6997e4999232c94d74715e6289759fe319031d3c8079472c66ca3b77e235
- clm_881fd3310242eacce597cdc31baa3afa64859eeff23f9fbb4deede013d8d3894
- clm_92ca659ee377200f5bb9a48f82bbb9c689f4803738b6083b3b2d932dec2612d7
- clm_acc01c493b6d65eca36cb81bbb7f8d144ffcf906033660352e97bbc14540946e
- clm_e71168c87c92f1d92b7faf845eae5732443da0988d9706e72a13e3c8af1bc741
- clm_f923958367d213c9a4ff609d64378513868906b7f6820503551601c0e855a714
- clm_facf661e17006c4b425634c6ca1741d48ef902659e4a7c3cae341b855aa81e33
- clm_fbd9518347539ed3c5697cd16b12588bd40d3cd01b1aa5cc9cee0ff966be8512
maturity: draft
page_id: pg_1fdeabf9dfb35c5c85da3b8cca936bda
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c2986d600f5f5b2c8e00b90b7dbea97b
title: builderz-labs/mission-control/README.md @ 5483a0e1eef1
updated_at: '2026-09-14T01:59:56Z'
---

# builderz-labs/mission-control/README.md @ 5483a0e1eef1

<!-- rcw:begin owner=source:src_c2986d600f5f5b2c8e00b90b7dbea97b block=evidence -->
- Runtime data defaults to a .data/ directory, overridable via the MISSION_CONTROL_DATA_DIR environment variable; the database defaults to <data dir>/mission-control.db. [@claim:clm_31212c1d4d335e7942fc8bd6f87a23ae17c6ec1c7d1f146cf5e319ac534ba5af]
- The stack is documented as Next.js 16 App Router, React 19, TypeScript 5, Tailwind CSS 4, Zustand, Recharts, xterm.js, and SQLite via better-sqlite3 in WAL mode, with Zod validation at input boundaries. [@claim:clm_35b971152edc765141f3e51ab6883445e05b12e0599dc358fe2d2dba684db957]
- Repository development practice: contributors run pnpm install --frozen-lockfile, lint, typecheck, test, build, and test:e2e, with pnpm quality:gate running the full repository gate; commits follow Conventional Commits with no AI-attribution trailers and pnpm is the only package manager. [@claim:clm_37cdac3e5f3e8fcda08363661f418cae560fc71eb6b56a4bee2a08617ac17bd1]
- The project is alpha software whose APIs, schemas, and configuration may change between releases; adapter depth varies by runtime across OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, and Claude SDK workflows. [@claim:clm_3db206e08ecd090e5882d84f1eeb41002c0fa7a85d6a7eca655d696c0e41a64e]
- The README's governance row lists 'evals' among shipped surfaces, suggesting the product includes evaluation features for agent work, though the snapshot does not describe how they score agent behavior. [@claim:clm_49dc6997e4999232c94d74715e6289759fe319031d3c8079472c66ca3b77e235]
- The control plane sits above agent runtimes and does not replace their reasoning or tool loops; it provides operators a single place to observe and govern work around those loops. [@claim:clm_881fd3310242eacce597cdc31baa3afa64859eeff23f9fbb4deede013d8d3894]
- A gateway is optional for task, project, agent, scheduler, webhook, alert, and cost work, but live session messaging requires a connected runtime gateway; strict workspaces block deployment-level integrations until resources carry workspace ownership. [@claim:clm_92ca659ee377200f5bb9a48f82bbb9c689f4803738b6083b3b2d932dec2612d7]
- A gateway-free REST loop is documented: agents register via POST /api/agents/register, create work via POST /api/tasks, and claim queues via GET /api/tasks/queue?agent=..., authenticated with a Bearer API key. [@claim:clm_acc01c493b6d65eca36cb81bbb7f8d144ffcf906033660352e97bbc14540946e]
- Tasks flow through inbox, assignment, execution, review, quality review, and completion; Aegis review requires an approval record before a task reaches done, and recurring task templates create dated work on cron schedules. [@claim:clm_e71168c87c92f1d92b7faf845eae5732443da0988d9706e72a13e3c8af1bc741]
- Mission Control is described as a self-hosted control plane for operating AI agents: dispatching tasks, inspecting runs, reviewing failures, tracking spend, and coordinating runtimes from a local dashboard backed by SQLite. [@claim:clm_f923958367d213c9a4ff609d64378513868906b7f6820503551601c0e855a714]
- The product exposes a Web UI, CLI, MCP server, OpenAPI-described REST API, WebSocket, and SSE; a running instance serves interactive docs at /docs and OpenAPI JSON at /api/docs. [@claim:clm_facf661e17006c4b425634c6ca1741d48ef902659e4a7c3cae341b855aa81e33]
- Shipped surfaces include task inbox/assignment/review with an Aegis quality gate and completion receipts, agent registration and sessions, activity/schedules/alerts/webhooks/cost views, memory browser and skills registry, and governance features like roles, API keys, approvals, audits, and evals. [@claim:clm_fbd9518347539ed3c5697cd16b12588bd40d3cd01b1aa5cc9cee0ff966be8512]
<!-- rcw:end owner=source:src_c2986d600f5f5b2c8e00b90b7dbea97b block=evidence -->

## Researcher notes

