# googlecloudplatform/race-condition

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 26efc1b46743 @ b66130ac402fcbca

## Summary (orientation draft, not independently verified)

Selected evidence records: The project is a multi-agent marathon simulation built with Google ADK and Gemini in which agents plan a Las Vegas marathon route, simulate weather, traffic, and crowds, and run the race autonomously, communicating over the A2A protocol. The system comprises a Go/Gin WebSocket gateway that routes requests and manages sessions, Python ADK planner, simulator, and runner agents, an Angular 21 + Three.js 3D frontend, and infrastructure including Redis, Pub/Sub, and PostgreSQL with pgvector.

## Source coverage

Source coverage (partial): 6 of 27 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is a multi-agent marathon simulation built with Google ADK and Gemini in which agents plan a Las Vegas marathon route, simulate weather, traffic, and crowds, and run the race autonomously, communicating over the A2A protocol. -- evidence: [README.md#L21-L21](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L21-L21)
- components (2 claim(s)):
  - [observation/documented] The system comprises a Go/Gin WebSocket gateway that routes requests and manages sessions, Python ADK planner, simulator, and runner agents, an Angular 21 + Three.js 3D frontend, and infrastructure including Redis, Pub/Sub, and PostgreSQL with pgvector. -- evidence: [README.md#L122-L129](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L122-L129), [README.md#L100-L109](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L100-L109), [README.md#L111-L120](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L111-L120)
  - [observation/documented] The planner ships in three variants: a base planner, one adding LLM-as-Judge evaluation, and one adding AlloyDB-backed route memory; the simulator runs a tick-based pipeline and spawns runner agents, which come in LLM-powered and deterministic autopilot variants. -- evidence: [README.md#L122-L129](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L122-L129)
- design-choices (2 claim(s)):
  - [observation/documented] The frontend boots in Cached mode by default, replaying NDJSON streams recorded from real agent runs so demos do not depend on live LLM calls or the network; Live mode instead talks to agents over WebSockets. -- evidence: [README.md#L229-L229](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L229-L229), [README.md#L227-L227](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L227-L227)
  - [observation/documented] A deterministic runner variant, runner_autopilot, makes the same shape of decisions as the LLM-powered runner with zero API calls, intended as a free baseline for load-testing the simulator. -- evidence: [README.md#L362-L367](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L362-L367), [README.md#L29-L33](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L29-L33)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use make targets for tests (Go, Python, web), linting, formatting, and coverage; Python tests run offline because a root conftest.py mocks google.auth.default credentials, and Go integration tests need Redis via docker compose. -- evidence: [README.md#L406-L418](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L406-L418), [GEMINI.md#L23-L34](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/GEMINI.md#L23-L34), [README.md#L470-L470](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L470-L470)
  - [observation/documented] Repository development practice: the repo ships an AGENTS.md plus four skill files under .claude/skills/ (getting-started, exploring-the-codebase, deploying, contributing) that AI coding assistants are directed to read for setup, architecture, deployment, and contribution tasks. -- evidence: [GEMINI.md#L41-L45](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/GEMINI.md#L41-L45), [README.md#L61-L61](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L61-L61), [README.md#L87-L92](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L87-L92)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
More evidence: [full detail](race-condition.detail.md)

Metadata and full claim list: [full detail](race-condition.detail.md)
Human notes ([notes](race-condition.notes.md), never overwritten by build)

[Back to map index](../../index.md)
