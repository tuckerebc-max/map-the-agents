# rcarmo/piclaw

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ced7c11253c3 @ be372c19d583039d

## Summary (orientation draft, not independently verified)

PiClaw is a self-hosted, single-user AI workspace built on the Pi Coding Agent, with a web UI, SQLite persistence, Dream memory, scheduled tasks, and a lane-based agent queue. Evidence covers architecture, configuration, extensions, and known multi-user limitations; no eval harness or test results are shown. Evidence coverage: 105 of 354 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 122 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] PiClaw is a self-hosted, single-user-by-default AI workspace built on the Pi Coding Agent, letting users chat with an agent, edit files, and run commands in one browser window. -- evidence: [README.md#L7-L7](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The runtime core comprises a router, a lane-aware AgentQueue, an AgentPool of Pi SDK AgentSessions, built-in and packaged extensions, and background workers for IPC, scheduling, and Dream memory consolidation. -- evidence: [docs/architecture.md#L34-L38](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L34-L38), [docs/architecture.md#L84-L89](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L84-L89), [docs/architecture.md#L21-L26](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L21-L26)
- design-choices (1 claim(s)):
  - [observation/documented] Configuration resolves in a documented precedence chain: CLI flags, then process.env, workspace .env, .piclaw/config.json, and built-in defaults. -- evidence: [docs/configuration.md#L35-L39](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/configuration.md#L35-L39)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: code changes should follow docs/development.md and the repository workflow in AGENTS.md, and be submitted via pull request; issues use dedicated templates. -- evidence: [README.md#L84-L86](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L84-L86), [README.md#L88-L88](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L88-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The web UI supports English, Simplified Chinese and Japanese with desktop and mobile layouts, and model requests go to the configured provider including local OpenAI-compatible servers. -- evidence: [README.md#L7-L7](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L7-L7), [README.md#L9-L9](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L9-L9)
  - [observation/documented] Chat commands include /login for provider setup, /model for model selection, /dream for memory consolidation, /tasks and /scheduled for scheduled tasks, and /theme and /tint for UI theming. -- evidence: [docs/architecture.md#L164-L185](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L164-L185), [README.md#L45-L48](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L45-L48)
- memory-state (3 claim(s)):
  - [observation/documented] Durable state lives in SQLite (messages, chats, tasks, configs, token usage), session trees, and a workspace holding notes, skills and files. -- evidence: [docs/architecture.md#L84-L89](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L84-L89), [docs/architecture.md#L40-L44](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L40-L44)
  - [observation/documented] Dream/AutoDream memory consolidation runs as out-of-band model turns on a temporary dream: channel and a dedicated dream:<chatJid> queue lane, so long consolidations do not block interactive chat. -- evidence: [docs/architecture.md#L210-L219](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L210-L219)
- orchestration (1 claim(s)):
  - [observation/documented] Per-chat turns use a cursor with inflight and failed markers: transient failures recover automatically, while persistent failures roll the cursor back and hold the chat for explicit retry or skip. -- evidence: [docs/architecture.md#L336-L339](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L336-L339), [docs/architecture.md#L318-L334](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L318-L334)
- tools-permissions (1 claim(s)):
More evidence: [full detail](piclaw.detail.md)

Metadata and full claim list: [full detail](piclaw.detail.md)
Human notes ([notes](piclaw.notes.md), never overwritten by build)

[Back to map index](../../index.md)
