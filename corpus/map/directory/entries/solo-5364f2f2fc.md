# solo (`solo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: solo-agent
- License: MIT
- Language: Go, TypeScript
- Interface: install=git clone + make dev (requires Go 1.22+, Node.js 20+, npm, Docker, and a supported agent CLI)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [solo-agent/solo](../../repos/solo-agent/solo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first workspace where multiple AI coding agents (Claude Code, Codex, OpenCode, Hermes, OpenClaw) collaborate with humans via channels, threaded tasks, Kanban boards, team graphs, persistent memory, and artifacts — treating agents as teammates rather than CLI tools. Has a 'Thinking mode' that branches conversations into focused reasoning lines.

(captured site page body (agents/solo.md), not a verified repo-code finding)
Solo solves the fragmentation of running several agent CLIs in terminal tabs by giving each one a persistent identity inside a shared workspace: a Go server, a local daemon that auto-detects agent CLIs on PATH, and a Next.js front end. Agents join channels, receive mentions and tasks, and keep per-agent memory files loaded into later sessions; work items carry their discussion threads, kanban state, and reviewable artifacts. Five backends are supported out of the box — Claude Code, Codex, OpenCode, Hermes, and OpenClaw — each with per-agent system prompt, model, and environment overrides, and the daemon auto-detects whatever is installed. Everything runs locally with PostgreSQL persistence, and observability views expose run traces and usage. It targets developers who coordinate multiple agents daily and want chat-style collaboration rather than another agent runtime.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/solo.md)
