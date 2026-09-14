# trafficguard/typedai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: trafficguard/nous (github id 784586462).
Latest snapshot: commit 34139aec65bb @ 05c891535de024b4

## Summary (orientation draft, not independently verified)

TypedAI is a TypeScript-first platform for agents, LLM workflows and chatbots, with autonomous and workflow agents, CLI/Web UIs, GitLab code review, and Postgres/Firestore persistence; the prior extraction's claims were all supported and are retained with integer slice citations. Evidence coverage: 167 of 227 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 33 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The platform ships software-developer agents including a Code Editing Agent with a compile/lint/test/fix loop, a ticket-to-PR Software Engineer Agent, and a Code Review agent that posts comments on GitLab merge requests. -- evidence: [README.md#L67-L83](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L67-L83)
  - [observation/documented] TypedAI includes two autonomous agent types, XML and CodeGen, which apply reasoning to break a user request into a plan executed via available function calls. -- evidence: [docs/docs/agent-concepts.md#L15-L16](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L15-L16)
- design-choices (3 claim(s)):
  - [observation/documented] LLM function-calling schemas are auto-generated from a `@func` decorator on class methods, avoiding duplicate schema definitions via zod or JSON. -- evidence: [README.md#L215-L216](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L215-L216)
  - [observation/documented] Agent state, current user, tool configuration, and default LLMs are looked up through Node's AsyncLocalStorage, requiring agent code to run within an AsyncLocalStorage context. -- evidence: [docs/docs/agent-concepts.md#L29-L30](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L29-L30), [docs/docs/agent-concepts.md#L32-L34](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L32-L34)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors set up the project with `./bin/setup` and run it locally with `./bin/serve`. -- evidence: [docs/README.md#L5-L5](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/README.md#L5-L5), [docs/README.md#L9-L9](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/README.md#L9-L9)
  - [observation/documented] Repository development practice: with `DATABASE_TYPE=postgres` set, a Postgres Docker container auto-starts during app-context initialization, skipping when the host is remote, inside Docker, or in CI. -- evidence: [docs/AUTO_START_POSTGRES.md#L9-L9](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L9-L9), [docs/AUTO_START_POSTGRES.md#L13-L23](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L13-L23), [docs/AUTO_START_POSTGRES.md#L68-L75](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/AUTO_START_POSTGRES.md#L68-L75)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] TypedAI offers both CLI and Web UI interfaces, and the `ai` wrapper script runs locally while `aid` runs in Docker for isolation; both expose CLI agents including a codeAgent for autonomous code editing. -- evidence: [README.md#L50-L50](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L50-L50), [README.md#L25-L37](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L25-L37)
  - [observation/documented] The CLI supports commands such as `ai query`, `ai code`, and `ai research` for automation and development workflows. -- evidence: [README.md#L45-L48](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/README.md#L45-L48)
- memory-state (2 claim(s)):
  - [observation/documented] Workflows run with a persisted agent context whose state is saved as 'completed' or 'error', so agent actions can be reviewed and resumed in the UI. -- evidence: [docs/docs/agent-concepts.md#L36-L65](https://github.com/TrafficGuard/typedai/blob/34139aec65bb70f7062cf7f92667c11ffde4fcb1/docs/docs/agent-concepts.md#L36-L65)
More evidence: [full detail](typedai.detail.md)

Metadata and full claim list: [full detail](typedai.detail.md)
Human notes ([notes](typedai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
