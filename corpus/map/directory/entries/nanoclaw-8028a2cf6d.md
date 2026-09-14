# NanoClaw (`nanoclaw`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: nanocoai
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Desktop, Web; install=git clone, pnpm install
- Model providers: Anthropic (Claude Agent SDK), Codex, OpenCode, Ollama
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (skills system, customization by forking) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (multi-agent support, per-agent containers) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [nanocoai/nanoclaw](../../repos/nanocoai/nanoclaw.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight, containerized alternative to OpenClaw that runs AI agents (via Claude Agent SDK) in isolated Docker containers and connects them to WhatsApp, Telegram, Slack, Discord, iMessage, Matrix, email, and other messaging apps. Host process routes messages through SQLite queues into per-agent containers with memory, scheduled tasks, and web access. Philosophy of deliberate smallness — small enough to understand, customize by ...

(captured site page body (agents/nanoclaw.md), not a verified repo-code finding)
NanoClaw is a self-hosted personal AI assistant harness that trades the weight of OpenClaw for something small enough to read and fork. A host process accepts messages from WhatsApp, Telegram, Slack, Discord, iMessage, Matrix, email, and other channels, routes them through SQLite queues, and hands each to an agent runner — Bun-based, built on the Claude Agent SDK — living inside its own isolated Docker container with its own memory, scheduled tasks, and web access. The container boundary is the point: agents are sandboxed per instance rather than sharing a process, and the harness itself stays out of the agent loop, which belongs to the underlying SDK. Customization is meant to happen by forking the small codebase with Claude Code rather than configuring plugins. The audience is people who want a personal assistant reachable from their existing chat apps without ceding control to a hosted product.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nanoclaw.md)
