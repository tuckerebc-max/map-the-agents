# olasunkanmi-se/codebuddy

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a9b8cd08ebaa @ 345f3ad884e40c16

## Summary (orientation draft, not independently verified)

The snapshot is README-only documentation for CodeBuddy, a VS Code multi-agent AI software engineer extension; the public repo is archived/deprecated. Claims below rest on documented descriptions, not code inspection. Evidence coverage: 114 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CodeBuddy is described as a multi-agent AI software engineer running inside VS Code that plans, writes, debugs, tests, documents, and deploys features autonomously. -- evidence: [README.md#L11-L11](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L11-L11)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] AgentSafetyGuard enforces configurable hard limits per session (e.g. 2,000 stream events, 400 tool calls, 10-minute runtime) plus per-tool caps and loop detection on repeated file edits. -- evidence: [README.md#L136-L136](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L136-L136), [README.md#L138-L142](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L138-L142)
  - [observation/documented] ProviderFailoverService switches to backup LLM providers on failure, classifying HTTP errors with per-reason cooldowns and probing providers before cooldown expiry. -- evidence: [README.md#L202-L202](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L202-L202), [README.md#L204-L209](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L204-L209)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] 16 skills ship bundled, each defined by a SKILL.md with optional install scripts; workspace (.codebuddy/skills/) and global (~/.codebuddy/skills/) skills are also discovered, with workspace precedence on name collisions. -- evidence: [README.md#L425-L428](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L425-L428), [README.md#L402-L402](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L402-L402)
- interfaces (2 claim(s)):
  - [observation/documented] The extension host and React webview communicate over a bidirectional postMessage protocol with structured commands and typed events. -- evidence: [README.md#L84-L84](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L84-L84)
  - [observation/documented] Agent-proposed file changes pass through a diff review pipeline with a Pending Changes panel, per-change apply/reject, composer sessions, and an optional auto-approve setting. -- evidence: [README.md#L342-L349](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L342-L349), [README.md#L340-L340](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L340-L340)
- memory-state (2 claim(s)):
  - [observation/documented] Persistence spans a TTL in-memory cache, .codebuddy/ file storage, SQLite with FTS4, a SQLite-backed LangGraph checkpointer, VS Code SecretStorage, and a vector store for embeddings. -- evidence: [README.md#L88-L96](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L88-L96)
  - [observation/documented] Persistent memory is file-backed at .codebuddy/memory.json with Knowledge/Rule/Experience categories, user and project scopes, and automatic injection into the agent's system prompt. -- evidence: [README.md#L473-L473](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L473-L473), [README.md#L475-L478](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L475-L478)
- orchestration (2 claim(s)):
  - [observation/documented] A singleton Orchestrator event bus mediates all subsystem communication via typed publish/subscribe events, decoupling agent, webview, and service layers. -- evidence: [README.md#L61-L61](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L61-L61)
  - [observation/documented] A Developer Agent coordinates seven specialized subagents (analyzer, doc writer, debugger, file organizer, architect, reviewer, tester) built on the LangGraph DeepAgents framework, each with role-filtered tools. -- evidence: [README.md#L120-L128](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L120-L128), [README.md#L118-L118](https://github.com/olasunkanmi-SE/codebuddy/blob/a9b8cd08ebaa894af091b39ed9c0d601d036f64e/README.md#L118-L118)
- tools-permissions (2 claim(s)):
More evidence: [full detail](codebuddy.detail.md)

Metadata and full claim list: [full detail](codebuddy.detail.md)
Human notes ([notes](codebuddy.notes.md), never overwritten by build)

[Back to map index](../../index.md)
