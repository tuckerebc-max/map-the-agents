# agentrove (`agentrove`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Mng-dev-ai
- License: Apache-2.0
- Language: Python, TypeScript, Rust
- Interface: install=git clone; cp .env.example .env; set SECRET_KEY via openssl rand -hex 32; docker compose up -d (open http://localhost:3000)
- Model providers: Claude Code, Codex, Copilot, Cursor, Grok, OpenCode (via ACP adapters)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [mng-dev-ai/agentrove](../../repos/mng-dev-ai/agentrove.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted AI coding workspace that orchestrates multiple AI coding agents (not just one) from one interface via ACP adapters, each in its own Docker/host sandbox. Multi-agent 'agent fleet' orchestration: a lead agent on a strong model decomposes work and routes tasks to specialized worker agents/models/personas running in parallel git worktrees. Ships as Docker web app, macOS Tauri desktop, and native ...

(captured site page body (agents/agentrove.md), not a verified repo-code finding)
Running several coding agents usually means juggling terminal windows, scattered config, and no shared history. Agentrove bundles chat, editor, terminal, diffs, secrets, and git tooling into one self-hosted web workspace, with each agent (Antigravity, Claude Code, Codex, Copilot, Cursor, Grok, OpenCode) connected through ACP adapters and each workspace isolated in its own Docker or host sandbox. A bundled MCP server exposes the instance as orchestrator tools, enabling sub-threads where a lead chat spawns worker chats in isolated worktrees, fans reviewer personas over diffs, and delegates accepted fixes back. Workers can run unattended in full-execution mode while the lead polls and evaluates results. It ships as a Docker Compose stack with a Tauri macOS desktop app and an iOS thin client, under Apache 2.0.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentrove.md)
