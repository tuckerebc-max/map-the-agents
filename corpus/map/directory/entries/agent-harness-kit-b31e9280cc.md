# Agent-harness-kit (`agent-harness-kit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: cardor
- License: MIT
- Language: unknown
- Interface: platforms=CLI; install=npm (npx/npm install @cardor/agent-harness-kit)
- Model providers: Claude Code, OpenCode, Codex CLI, Grok Build (works with any MCP-compatible agent)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Imposes a five-role agent workflow (Lead, Explorer, Consultant, Builder, Reviewer) where only the Builder may write files, backed by a persistent SQLite log of every action, a health.sh gate that must pass before work starts, and an MCP server exposing task-claim tools to any compatible client.

(captured site page body (agents/agent-harness-kit.md), not a verified repo-code finding)
Multi-agent coding setups tend to degrade into several agents freestyling over the same files with no shared memory, so agent-harness-kit scaffolds structure first: ahk init creates a task backlog, a defined workflow with five role-separated agents, and an SQLite-backed log of every action taken. A health gate (health.sh) must pass before any work starts, and the ahk serve command runs a local MCP server exposing tasks.get, tasks.claim, and action tools to MCP-compatible clients like Claude Code, OpenCode, Codex CLI, and Grok Build. Storage works over SQLite, PostgreSQL, or MySQL, and a real-time web dashboard shows live progress. Maintainers who want AI agents to follow an auditable, health-gated process instead of improvising are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agent-harness-kit.md)
