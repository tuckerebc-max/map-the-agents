# harnss (`harnss`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: OpenSource03
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Desktop, IDE, Web; install=Download latest release from GitHub Releases (.dmg macOS / .exe Windows / .AppImage+.deb Linux); or dev: git clone, pnpm install, pnpm dev
- Model providers: Anthropic (Claude Code), OpenAI (Codex), ACP-compatible agents (Gemini CLI, Goose, Docker cagent)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [opensource03/harnss](../../repos/opensource03/harnss.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unified desktop interface for multiple AI coding agents built on the Agent Client Protocol (ACP), enabling simultaneous side-by-side agent sessions without context loss. Rich tool visualization transforms raw JSON into interactive cards with word-level diffs; all-in-one workspace with terminal, browser, git, MCP, and file panels scoped per project.

(captured site page body (agents/harnss.md), not a verified repo-code finding)
harnss is a desktop application for running several AI coding agents side by side without losing context between them. It embeds Claude Code through the Anthropic Agent SDK, Codex through its JSON-RPC app-server, and any Agent Client Protocol-compatible agent such as Gemini CLI, Goose, or Docker cagent, keeping each session's state independent while allowing instant switching. The interface renders tool calls in detail — word-level diffs, syntax-highlighted code, inline command output, nested subagent trees — and layers on MCP server management per project, git operations with AI-generated commit messages, built-in terminal tabs, and a browser panel. Permission handling offers three levels from ask-first to full autonomy, with plan mode and background task agents for longer work. The project is early-stage and open about a pending rewrite, distributing unsigned binaries for macOS, Windows, and Linux.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/harnss.md)
