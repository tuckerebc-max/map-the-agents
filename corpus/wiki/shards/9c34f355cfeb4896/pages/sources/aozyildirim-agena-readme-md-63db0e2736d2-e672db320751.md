---
access: public
aliases: []
claim_ids:
- clm_08216bec56d6e501ea4b10cac32ea88df342ac726818edf8388746211f9ea5df
- clm_090ed8bc7be4094822860f52159a0f88cd0699da5b022fdfd43b223e20b4e9d7
- clm_0c0e273e8abdc29459867a529c6ea122dbc75f7a613167bcf34c31a45c595dc9
- clm_0e5017f19e9a7e64d987868ab49da0e5e59e12f21c134b153cac34880a1fb38e
- clm_396427f50c0dbaac45d5795ed84fcb4f5c6f06594d3b4fb39e3bd8983da3eff6
- clm_45e31f7b7952a5f2099d1e325998e14830fe39779042f10024c6f99877abb1c4
- clm_59c14fef944d26c1ff1d3108a878fb90216f4c2225143e96347281e27c274c29
- clm_650d3f6751a746b9fd7c4d37a02886d03612a323ef65d7afa56c19f46b8d1f88
- clm_6be9bd0ee0cd9a8ef3b4725e7347f11fb6c197abcc9de6c30d05e977a98ccb9f
- clm_7ab6594043312f003d08710eee00e428dac05337e0035542420608b26b4df243
- clm_83beae0d94ad48926a20a05535b4c95bb3099d4c8d453ae140d6c47919b949a1
- clm_951efbaf78ecb0ce3e49e3645b46c21580a06e6d355b268fe8d0ed38ad8b141a
- clm_aaf5993a4b3597edd0cd2f965aad3650bd1ec6388497c9623d4470515d925876
- clm_b598c8af998e5c25854e202d05262e15ebaddad2a384ca885ec7453e3eb71936
- clm_e43b65d6632f9c56fa2f7697f4eeb55bfb1ac29c807c7a08a0985956d1b9a191
maturity: draft
page_id: pg_239a0cefe6545b56bb24e672db320751
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_65947a6f9f935bb0bdb5fdf1ac5daad1
title: aozyildirim/Agena/README.md @ 63db0e2736d2
updated_at: '2026-09-14T04:51:13Z'
---

# aozyildirim/Agena/README.md @ 63db0e2736d2

<!-- rcw:begin owner=source:src_65947a6f9f935bb0bdb5fdf1ac5daad1 block=evidence -->
- Integration credentials for GitHub, Azure DevOps, Jira, New Relic and Sentry are stored per-organization in integration_configs and managed via the dashboard rather than read from environment variables, so one deployment serves many orgs. [@claim:clm_08216bec56d6e501ea4b10cac32ea88df342ac726818edf8388746211f9ea5df]
- The only hard-required environment variable is JWT_SECRET_KEY; LLM provider and other credentials are configured per-organization through the dashboard after the stack is running. [@claim:clm_090ed8bc7be4094822860f52159a0f88cd0699da5b022fdfd43b223e20b4e9d7]
- Completed tasks are distilled into reusable skills stored as Qdrant embeddings (org-scoped, kind='skill') plus MySQL rows; before any agent runs, the top-3 skills above a relevance threshold are prepended to the system prompt. [@claim:clm_0c0e273e8abdc29459867a529c6ea122dbc75f7a613167bcf34c31a45c595dc9]
- The CLI bridge runs on the host rather than in Docker so it can access Claude/Codex CLI authentication via the system keychain; start.sh handles this, and containers reach it via host.docker.internal:9876. [@claim:clm_0e5017f19e9a7e64d987868ab49da0e5e59e12f21c134b153cac34880a1fb38e]
- An @agenaai/cli npm package drives the platform from the terminal with commands for auth/setup, daemon and runtime management, tasks, skill search, and sprint refinement backfill/analysis. [@claim:clm_396427f50c0dbaac45d5795ed84fcb4f5c6f06594d3b4fb39e3bd8983da3eff6]
- Repository development practice: database migrations are managed with Alembic (upgrade head, revision, current, downgrade -1) executed inside the backend container, and the repo ships 24 migration versions. [@claim:clm_45e31f7b7952a5f2099d1e325998e14830fe39779042f10024c6f99877abb1c4]
- Agent roles are mapped to model tiers: Context Analyst and Finalizer use a small fast model, while PM, Planner, Reviewer use large reasoning models and the Developer uses a large model with 128K output. [@claim:clm_59c14fef944d26c1ff1d3108a878fb90216f4c2225143e96347281e27c274c29]
- The FastAPI backend exposes documented REST endpoints for auth, tasks (including imports from Azure DevOps, Jira, New Relic, Sentry), agents, flows, analytics/DORA, and billing, with OpenAPI docs at /docs. [@claim:clm_650d3f6751a746b9fd7c4d37a02886d03612a323ef65d7afa56c19f46b8d1f88]
- AGENA targets teams using Sentry, New Relic, Jira, YouTrack, Azure DevOps and GitHub, pulling sprint items and shipping PRs, and is positioned as self-hostable and multi-tenant with JWT auth, RBAC roles, usage-quota plans, and Stripe billing. [@claim:clm_6be9bd0ee0cd9a8ef3b4725e7347f11fb6c197abcc9de6c30d05e977a98ccb9f]
- The stack uses Python 3.11/FastAPI/SQLAlchemy 2.0 async, MySQL 8.0, Redis 7, optional Qdrant vector memory (QDRANT_ENABLED), Next.js 14/React 18 frontend, JWT+bcrypt auth, and Docker Compose with Nginx blue/green frontend deployment. [@claim:clm_7ab6594043312f003d08710eee00e428dac05337e0035542420608b26b4df243]
- Repository development practice: local development instructions cover creating a Python 3.11 venv, installing all six packages in editable mode, running the API with uvicorn on port 8010, and running the worker via python -m agena_worker.workers.redis_worker. [@claim:clm_83beae0d94ad48926a20a05535b4c95bb3099d4c8d453ae140d6c47919b949a1]
- AGENA is described as an open-source agentic AI platform that autonomously writes code, reviews quality, and ships pull requests, coordinating LLM agents to analyze tasks, generate code, review changes, and create PRs. [@claim:clm_951efbaf78ecb0ce3e49e3645b46c21580a06e6d355b268fe8d0ed38ad8b141a]
- Task execution flows through a Redis queue into an OrchestrationService driving a LangGraph pipeline of five nodes (fetch_context, analyze, generate_code, review_code, finalize) executed by CrewAI role agents (PM, Developer, Reviewer, Finalizer). [@claim:clm_aaf5993a4b3597edd0cd2f965aad3650bd1ec6388497c9623d4470515d925876]
- The backend is split into six pip-installable packages (core, models, services, agents, api, worker) with a layered dependency graph where agena-core has no internal deps and agena-api depends on all others. [@claim:clm_b598c8af998e5c25854e202d05262e15ebaddad2a384ca885ec7453e3eb71936]
- A Skill Librarian asks the configured LLM to summarize completed tasks into structured skill records, and extraction is skipped when the LLM's confidence is below 50% to avoid polluting the catalog. [@claim:clm_e43b65d6632f9c56fa2f7697f4eeb55bfb1ac29c807c7a08a0985956d1b9a191]
<!-- rcw:end owner=source:src_65947a6f9f935bb0bdb5fdf1ac5daad1 block=evidence -->

## Researcher notes

