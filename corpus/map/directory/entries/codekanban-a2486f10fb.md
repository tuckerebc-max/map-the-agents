# CodeKanban (`codekanban`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: fy0
- License: Apache-2.0
- Language: Go (backend), Vue 3 + TypeScript (frontend)
- Interface: platforms=CLI; install=npx codekanban or npm install -g codekanban@latest
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [fy0/codekanban](../../repos/fy0/codekanban.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Manages all your terminals and AI coding tools (Claude Code / Codex) from one unified page — multi-project/terminal management, AI tool status detection (idle/working/needs approval), conversation history, Git worktree management, multi-tab notes. Ships installable Codex skill bundle (codekanban-cli).

(captured site page body (agents/codekanban.md), not a verified repo-code finding)
CodeKanban addresses the scattered-window problem of running several AI coding sessions at once: terminals for Claude Code and Codex live in one web page, organized as projects on a kanban board. The system detects each agent's state — idle, working, or waiting for approval — and notifies on completion, while conversation and prompt history stays searchable per session. Git worktree management is built in, using a hybrid of go-git and the system git binary, so parallel agents can work in isolated checkouts, and a multi-tab notes panel captures working context alongside the sessions. The backend is a single Go binary with an embedded local database and a Vue 3 frontend, launched with npx, and it ships a codekanban-cli Codex skill bundle for board interaction from inside an agent session.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codekanban.md)
