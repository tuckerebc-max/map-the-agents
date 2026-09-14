# aozyildirim/agena -- full detail

[Back to orientation](agena.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aozyildirim/agena/63db0e2736d235032dd82207b84c00cf5f296ffc/8467f4e1626576f1.json](../../../wiki/dossiers/aozyildirim/agena/63db0e2736d235032dd82207b84c00cf5f296ffc/8467f4e1626576f1.json)

## specifications (1 claim(s))

- [observation/documented] AGENA is described as an open-source agentic AI platform that autonomously writes code, reviews quality, and ships pull requests, coordinating LLM agents to analyze tasks, generate code, review changes, and create PRs. -- evidence: [README.md#L11-L11](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L11-L11), [README.md#L13-L13](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L13-L13) (`clm_951efbaf78ecb0ce3e49e3645b46c21580a06e6d355b268fe8d0ed38ad8b141a`)

## components (1 claim(s))

- [observation/documented] The backend is split into six pip-installable packages (core, models, services, agents, api, worker) with a layered dependency graph where agena-core has no internal deps and agena-api depends on all others. -- evidence: [README.md#L442-L449](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L442-L449), [README.md#L344-L344](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L344-L344) (`clm_b598c8af998e5c25854e202d05262e15ebaddad2a384ca885ec7453e3eb71936`)

## design-choices (3 claim(s))

- [observation/documented] The CLI bridge runs on the host rather than in Docker so it can access Claude/Codex CLI authentication via the system keychain; start.sh handles this, and containers reach it via host.docker.internal:9876. -- evidence: [README.md#L569-L569](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L569-L569), [README.md#L673-L673](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L673-L673), [README.md#L662-L662](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L662-L662) (`clm_0e5017f19e9a7e64d987868ab49da0e5e59e12f21c134b153cac34880a1fb38e`)
- [observation/documented] Integration credentials for GitHub, Azure DevOps, Jira, New Relic and Sentry are stored per-organization in integration_configs and managed via the dashboard rather than read from environment variables, so one deployment serves many orgs. -- evidence: [README.md#L626-L630](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L626-L630) (`clm_08216bec56d6e501ea4b10cac32ea88df342ac726818edf8388746211f9ea5df`)
- [observation/documented] The only hard-required environment variable is JWT_SECRET_KEY; LLM provider and other credentials are configured per-organization through the dashboard after the stack is running. -- evidence: [README.md#L547-L551](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L547-L551), [README.md#L618-L624](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L618-L624) (`clm_090ed8bc7be4094822860f52159a0f88cd0699da5b022fdfd43b223e20b4e9d7`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: local development instructions cover creating a Python 3.11 venv, installing all six packages in editable mode, running the API with uvicorn on port 8010, and running the worker via python -m agena_worker.workers.redis_worker. -- evidence: [README.md#L704-L706](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L704-L706), [README.md#L718-L718](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L718-L718), [README.md#L721-L722](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L721-L722), [README.md#L709-L715](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L709-L715) (`clm_83beae0d94ad48926a20a05535b4c95bb3099d4c8d453ae140d6c47919b949a1`)
- [observation/documented] Repository development practice: database migrations are managed with Alembic (upgrade head, revision, current, downgrade -1) executed inside the backend container, and the repo ships 24 migration versions. -- evidence: [README.md#L749-L750](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L749-L750), [README.md#L743-L743](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L743-L743), [README.md#L429-L438](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L429-L438), [README.md#L746-L746](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L746-L746), [README.md#L740-L740](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L740-L740) (`clm_45e31f7b7952a5f2099d1e325998e14830fe39779042f10024c6f99877abb1c4`)

## skills-patterns (1 claim(s))

- [observation/documented] A Skill Librarian asks the configured LLM to summarize completed tasks into structured skill records, and extraction is skipped when the LLM's confidence is below 50% to avoid polluting the catalog. -- evidence: [README.md#L102-L107](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L102-L107) (`clm_e43b65d6632f9c56fa2f7697f4eeb55bfb1ac29c807c7a08a0985956d1b9a191`)

## interfaces (2 claim(s))

- [observation/documented] The FastAPI backend exposes documented REST endpoints for auth, tasks (including imports from Azure DevOps, Jira, New Relic, Sentry), agents, flows, analytics/DORA, and billing, with OpenAPI docs at /docs. -- evidence: [README.md#L828-L834](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L828-L834), [README.md#L836-L836](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L836-L836), [README.md#L775-L778](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L775-L778), [README.md#L781-L794](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L781-L794), [README.md#L797-L802](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L797-L802), [README.md#L821-L825](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L821-L825) (`clm_650d3f6751a746b9fd7c4d37a02886d03612a323ef65d7afa56c19f46b8d1f88`)
- [observation/documented] An @agenaai/cli npm package drives the platform from the terminal with commands for auth/setup, daemon and runtime management, tasks, skill search, and sprint refinement backfill/analysis. -- evidence: [README.md#L478-L479](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L478-L479), [README.md#L491-L494](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L491-L494), [README.md#L507-L510](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L507-L510), [README.md#L501-L504](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L501-L504), [README.md#L497-L498](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L497-L498), [README.md#L513-L517](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L513-L517) (`clm_396427f50c0dbaac45d5795ed84fcb4f5c6f06594d3b4fb39e3bd8983da3eff6`)

## memory-state (1 claim(s))

- [observation/documented] Completed tasks are distilled into reusable skills stored as Qdrant embeddings (org-scoped, kind='skill') plus MySQL rows; before any agent runs, the top-3 skills above a relevance threshold are prepended to the system prompt. -- evidence: [README.md#L113-L117](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L113-L117), [README.md#L97-L100](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L97-L100), [README.md#L109-L111](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L109-L111) (`clm_0c0e273e8abdc29459867a529c6ea122dbc75f7a613167bcf34c31a45c595dc9`)

## orchestration (2 claim(s))

- [observation/documented] Task execution flows through a Redis queue into an OrchestrationService driving a LangGraph pipeline of five nodes (fetch_context, analyze, generate_code, review_code, finalize) executed by CrewAI role agents (PM, Developer, Reviewer, Finalizer). -- evidence: [README.md#L301-L314](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L301-L314), [README.md#L844-L851](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L844-L851) (`clm_aaf5993a4b3597edd0cd2f965aad3650bd1ec6388497c9623d4470515d925876`)
- [observation/documented] Agent roles are mapped to model tiers: Context Analyst and Finalizer use a small fast model, while PM, Planner, Reviewer use large reasoning models and the Developer uses a large model with 128K output. -- evidence: [README.md#L855-L862](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L855-L862) (`clm_59c14fef944d26c1ff1d3108a878fb90216f4c2225143e96347281e27c274c29`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack uses Python 3.11/FastAPI/SQLAlchemy 2.0 async, MySQL 8.0, Redis 7, optional Qdrant vector memory (QDRANT_ENABLED), Next.js 14/React 18 frontend, JWT+bcrypt auth, and Docker Compose with Nginx blue/green frontend deployment. -- evidence: [README.md#L463-L472](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L463-L472) (`clm_7ab6594043312f003d08710eee00e428dac05337e0035542420608b26b4df243`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] AGENA targets teams using Sentry, New Relic, Jira, YouTrack, Azure DevOps and GitHub, pulling sprint items and shipping PRs, and is positioned as self-hostable and multi-tenant with JWT auth, RBAC roles, usage-quota plans, and Stripe billing. -- evidence: [README.md#L17-L20](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L17-L20), [README.md#L194-L198](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L194-L198) (`clm_6be9bd0ee0cd9a8ef3b4725e7347f11fb6c197abcc9de6c30d05e977a98ccb9f`)

Superseded claim IDs (kept as history): clm_c858c9a8beed5ead74d4074b5672fbed06175770a416a67059d98c46723d658a

