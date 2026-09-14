# solo-agent/solo

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9d58e66769ed @ e6a9f00ed7f2beb8

## Summary (orientation draft, not independently verified)

Solo Agent is an open-source, local-first workspace coordinating AI coding agents via channels, tasks, teams, and memory, built on a Go server, daemon, and agent CLI architecture; contributor rules in AGENTS.md govern development practice.

## Source coverage

Source coverage (partial): 3 of 35 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Solo is described as an open-source, local-first workspace for humans and AI coding agents, coordinating multiple agents through channels, threaded conversations, task boards, and channel-scoped teams. -- evidence: [README.md#L7-L10](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L7-L10)
- components (3 claim(s)):
  - [observation/documented] Solo runs three local layers: a Go API server on :8080 with WebSocket hub, auth, and PostgreSQL persistence; a daemon on :8081 that registers the machine and manages agent subprocesses; and the installed agent CLI driven over stdin/stdout. -- evidence: [README.md#L140-L142](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L140-L142), [README.md#L138-L138](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L138-L138)
  - [observation/documented] Core concepts include channels, long-lived agents, Kanban tasks with states todo/in_progress/in_review/done/closed, channel-scoped teams, memory, an inbox for mentions and DMs, and reviewable artifacts. -- evidence: [README.md#L126-L134](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L126-L134)
- design-choices (1 claim(s)):
  - [observation/documented] Solo is intentionally a workspace rather than a company simulator, where agents can be mentioned, assigned, reviewed, remembered, and trusted with visible work. -- evidence: [README.md#L55-L55](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L55-L55)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributor rules require a complete architecture design before implementation, whole-project review of changes, and E2E validation using real frontend, API server, and PostgreSQL with no mocks for HTTP routes, services, or database behavior. -- evidence: [AGENTS.md#L3-L9](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/AGENTS.md#L3-L9)
  - [observation/documented] Repository development practice: agents may restart the frontend, API server, and daemon only via `make rebuild` from the repo root, and must never use launchctl, direct binaries, go run, npm run dev, nohup, or custom background commands. -- evidence: [AGENTS.md#L13-L15](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/AGENTS.md#L13-L15)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agent team templates let users choose an official workflow or describe a goal to Lucy, preview roles and working relationships, and create agents scoped to one channel with post-creation tuning. -- evidence: [README.md#L88-L88](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L88-L88)
- interfaces (2 claim(s)):
  - [observation/documented] Agent backends are auto-detected from PATH at daemon startup: Claude Code via stream-json, Codex CLI via JSON-RPC, and OpenCode, Hermes, and OpenClaw via ACP. -- evidence: [README.md#L114-L120](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L114-L120), [README.md#L112-L112](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L112-L112)
  - [observation/documented] The runtime topology is Browser (Next.js :3000) to Server (Go :8080) over WebSocket, Server to Daemon over HTTP/SSE, and Daemon to Agent CLI over stdin/stdout. -- evidence: [README.md#L144-L147](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L144-L147)
- memory-state (1 claim(s)):
  - [observation/documented] Agents keep agent-specific MEMORY.md context that is loaded into future sessions, and the comparison table says agents retain long-term memory, their own environment, and a fixed workspace. -- evidence: [README.md#L126-L134](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L126-L134), [README.md#L45-L45](https://github.com/solo-agent/solo/blob/9d58e66769ed2479c089b531705f09223d37fff3/README.md#L45-L45)
More evidence: [full detail](solo.detail.md)

Metadata and full claim list: [full detail](solo.detail.md)
Human notes ([notes](solo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
