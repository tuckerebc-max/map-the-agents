# Athena by LuckeySystems (`athena-by-luckeysystems`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: luckeyfaraday
- License: NOASSERTION
- Language: TypeScript
- Interface: install=git clone https://github.com/luckeyfaraday/Athena.git && cd Athena/client && npm install && npm run dev
- Model providers: Codex, Claude Code, OpenCode, Grok
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [luckeyfaraday/athena](../../repos/luckeyfaraday/athena.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local desktop 'command room' that orchestrates multiple isolated AI coding agents (Codex, Claude Code, OpenCode, Grok) into one unified workspace with shared project context, cross-agent session recall, and bounded handoffs. Installs a bundled agent skill (athena-context-workspace) into local directories for Codex, Claude Code, and OpenCode. Hermes MCP bridge allows Hermes to control the workspace, spawn terminals, and read sessions. Embedded ...

(captured site page body (agents/athena-by-luckeysystems.md), not a verified repo-code finding)
Athena addresses the problem that AI coding agents normally run as isolated terminal sessions with separate context windows, making it hard to see what each did or hand work between them. It embeds PTY terminals (node-pty + xterm.js with bounded streaming and snapshot replay) for Codex, OpenCode, Claude Code, Athena Code, and Hermes in one grid, discovers and resumes existing sessions on disk, and generates bounded markdown handoffs from selected sessions that get attached to fresh agent launches. Context modes start clean by default, with task/curated/immersive modes creating immutable workspace-scoped context bundles. An MCP server exposes context_workspace tools so Hermes can spawn terminals and read sessions inside Athena, secured with per-launch bearer tokens. Developers running several agent CLIs on one project use it as a command room for session-first work.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/athena-by-luckeysystems.md)
