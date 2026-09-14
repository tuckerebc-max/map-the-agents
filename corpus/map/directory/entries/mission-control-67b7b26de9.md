# mission-control (`mission-control`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: builderz-labs
- License: MIT
- Language: TypeScript
- Interface: install=docker, source
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [builderz-labs/mission-control](../../repos/builderz-labs/mission-control.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted control plane for operating AI agents that sits ABOVE agent runtimes (OpenClaw, Claude Code, Codex, CrewAI, LangGraph, AutoGen, Claude SDK) rather than replacing them. SQLite-backed, runs locally. Single dashboard for task dispatch, agent management, spend tracking, quality review (Aegis gate), memory/skills, scheduling, and governance. Multiple interfaces: Web UI, CLI, built-in MCP server, REST API (OpenAPI), WebSocket, SSE. Alpha software.

(captured site page body (agents/mission-control.md), not a verified repo-code finding)
Mission Control addresses the operations layer that appears once someone runs several agents across several runtimes: which task belongs to which agent, what it cost, whether the output passed review, and what failed overnight. Agents register with heartbeats against runtime adapters for Claude Code, Codex, CrewAI, LangGraph, AutoGen, and others, and tasks flow through an inbox-assignment-execution-review pipeline whose Aegis gate checks quality before a completion receipt issues. The plane tracks token spend and cost per run, schedules cron jobs, raises alerts and webhooks, and exposes memory and skills registries alongside role-based governance, API keys, and audit logs — all over SQLite on a single host with no external services. Interfaces span a Next.js dashboard, a CLI, an OpenAPI REST surface, WebSocket/SSE streams, and an MCP server that lets Claude query the control plane directly. Operators running multiple heterogeneous agents use it for dispatch, audit, and cost control; it explicitly does not replace any runtime's reasoning or tool loop, and remains alpha software.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mission-control.md)
