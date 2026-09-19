# AgentPack (`agentpack`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: vishal2612200
- License: AGPL-3.0
- Language: Python
- Interface: platforms=CLI; install=pipx install agentpack-cli (recommended), or npm install --global @vishal2612200/agentpack
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [vishal2612200/agentpack](../../repos/vishal2612200/agentpack.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local, agent-neutral reliability layer for AI software development — no repository upload required, everything stored locally under .agentpack/. Provides evidence-backed context selection with receipts, cited PR review artifacts, structured handoffs across sessions/agents, and a four-command workflow (work, learn, finish, doctor). Connects project evidence across multiple coding agents without replacing them.

(captured site page body (agents/agentpack.md), not a verified repo-code finding)
Coding agents lose time rediscovering project structure, ownership rules, and prior decisions on every task, and context injected by generic retrieval is rarely auditable. AgentPack keeps task state, repository rules, prior decisions, and review evidence under .agentpack/ and exposes them through a four-command loop (work, learn, finish, doctor) plus an MCP server that surfaces readiness, related files, and cited PR evidence to agents like Claude Code, Codex, and Cursor. Every context selection is recorded with a receipt explaining inclusion or omission, and a trust order keeps source files, diffs, and test results above any summary it produces. The project publishes measured numbers for what it can prove (file-selection recall and token precision) and explicitly declines to claim improvements it has not benchmarked. Python and JavaScript/TypeScript repositories get the strongest semantic mapping; coordination remains advisory by design.
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agentpack.md)
