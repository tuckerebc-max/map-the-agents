# aozyildirim/agena

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 63db0e2736d2 @ 8467f4e1626576f1

## Summary (orientation draft, not independently verified)

README-only evidence describes AGENA as a multi-tenant agentic AI platform that turns tasks into pull requests via a CrewAI/LangGraph pipeline, with a six-package Python monorepo, Qdrant-backed skill memory, a host-run CLI bridge, and a documented REST/CLI surface. No evaluation or contributor-workflow evidence beyond local dev commands appears in these slices. Evidence: 6 of 17 candidate files stored (README.md, docs/SKILLS.md, requirements.txt, rules.md, docs/ai-pipeline.md, docs/DESIGN_SYSTEM.md); 11 omitted by file budget, including CONTRIBUTING.md, SECURITY.md and CLAUDE.md; selection incomplete.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AGENA is described as an open-source agentic AI platform that autonomously writes code, reviews quality, and ships pull requests, coordinating LLM agents to analyze tasks, generate code, review changes, and create PRs. -- evidence: [README.md#L11-L11](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L11-L11), [README.md#L13-L13](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L13-L13)
- components (1 claim(s)):
  - [observation/documented] The backend is split into six pip-installable packages (core, models, services, agents, api, worker) with a layered dependency graph where agena-core has no internal deps and agena-api depends on all others. -- evidence: [README.md#L442-L449](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L442-L449), [README.md#L344-L344](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L344-L344)
- design-choices (3 claim(s)):
  - [observation/documented] The CLI bridge runs on the host rather than in Docker so it can access Claude/Codex CLI authentication via the system keychain; start.sh handles this, and containers reach it via host.docker.internal:9876. -- evidence: [README.md#L569-L569](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L569-L569), [README.md#L673-L673](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L673-L673), [README.md#L662-L662](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L662-L662)
  - [observation/documented] Integration credentials for GitHub, Azure DevOps, Jira, New Relic and Sentry are stored per-organization in integration_configs and managed via the dashboard rather than read from environment variables, so one deployment serves many orgs. -- evidence: [README.md#L626-L630](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L626-L630)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local development instructions cover creating a Python 3.11 venv, installing all six packages in editable mode, running the API with uvicorn on port 8010, and running the worker via python -m agena_worker.workers.redis_worker. -- evidence: [README.md#L704-L706](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L704-L706), [README.md#L718-L718](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L718-L718), [README.md#L721-L722](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L721-L722), [README.md#L709-L715](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L709-L715)
  - [observation/documented] Repository development practice: database migrations are managed with Alembic (upgrade head, revision, current, downgrade -1) executed inside the backend container, and the repo ships 24 migration versions. -- evidence: [README.md#L749-L750](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L749-L750), [README.md#L743-L743](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L743-L743), [README.md#L429-L438](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L429-L438), [README.md#L746-L746](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L746-L746), [README.md#L740-L740](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L740-L740)
- skills-patterns (1 claim(s)):
  - [observation/documented] A Skill Librarian asks the configured LLM to summarize completed tasks into structured skill records, and extraction is skipped when the LLM's confidence is below 50% to avoid polluting the catalog. -- evidence: [README.md#L102-L107](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L102-L107)
- interfaces (2 claim(s)):
  - [observation/documented] The FastAPI backend exposes documented REST endpoints for auth, tasks (including imports from Azure DevOps, Jira, New Relic, Sentry), agents, flows, analytics/DORA, and billing, with OpenAPI docs at /docs. -- evidence: [README.md#L828-L834](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L828-L834), [README.md#L836-L836](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L836-L836), [README.md#L775-L778](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L775-L778), [README.md#L781-L794](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L781-L794), [README.md#L797-L802](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L797-L802), [README.md#L821-L825](https://github.com/aozyildirim/Agena/blob/63db0e2736d235032dd82207b84c00cf5f296ffc/README.md#L821-L825)
More evidence: [full detail](agena.detail.md)

Metadata and full claim list: [full detail](agena.detail.md)
Human notes ([notes](agena.notes.md), never overwritten by build)

[Back to map index](../../index.md)
