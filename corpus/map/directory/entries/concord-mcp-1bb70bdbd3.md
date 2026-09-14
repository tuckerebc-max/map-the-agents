# Concord (`concord-mcp`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Get-Concord-AI
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm (@concord-ai/concord-mcp); state in a .concord/ folder at the repo root, shared by all agents in that repo
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [get-concord-ai/concord-mcp](../../repos/get-concord-ai/concord-mcp.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A single local-first MCP server that gives multiple coding agents a shared work state — presence, live messaging, file claims, decisions, and handoffs with review evidence — backed by SQLite in the repo, with tools start_work, inspect_work, update_work, transfer_work, and finish_work. Explicitly not an orchestrator or agent.

(captured site page body (agents/concord-mcp.md), not a verified repo-code finding)
Concord is the shared nervous system for a set of coding agents working in the same repository: a single MCP server, local-first with SQLite state in a .concord/ folder at the repo root, that lets agents like Claude Code, Codex, Cursor, Gemini CLI, and Grok Build discover each other, exchange live messages and prompts, claim files before editing to detect overlaps, share decisions, and hand off tasks with review evidence. Its MCP tools are start_work, inspect_work, update_work, transfer_work, and finish_work, plus a CLI (concord status, dashboard, doctor) and a TUI dashboard for humans watching the fleet. The project is explicit about what it is not — not an orchestrator, not an autonomous agent, not a code reviewer, not a hosted sync service — and it sends opt-out telemetry that never includes code or file paths. It is the coordination layer around agents rather than a harness, aimed at teams running several agents against one codebase without a human relaying context between them.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/concord-mcp.md)
