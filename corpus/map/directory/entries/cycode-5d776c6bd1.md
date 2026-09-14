# CyCode (`cycode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: vibe-cy
- License: unlicensed (no license file; README notes one is pending)
- Language: TypeScript (Node.js 18+)
- Interface: platforms=CLI, IDE; install=npm install, cp .env.example .env, npm run build, npm start
- Model providers: OpenAI, DeepSeek, DashScope/Qwen, any OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: no (no)

Repository map entry: [vibe-cy/cycode](../../repos/vibe-cy/cycode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight terminal-first AI coding agent using OpenAI-compatible Chat Completions API. Built-in tools for reading files, applying precise edits, searching code, running shell commands, and delegating work to sub-agents. Multi-provider compatibility, context compression for long conversations, token/cost tracking, dual interactive TUI + one-shot scripting mode, built-in shell command safety blocking, and programmatic API for reuse. Very early stage (5 commits).

(captured site page body (agents/cycode.md), not a verified repo-code finding)
CyCode is a self-hosted, terminal-first coding agent written to demonstrate how little a working agentic loop requires: file read/write/edit, bash (with some high-risk command blocking), grep/glob search, and a sub-agent tool, all wired through an OpenAI-compatible Chat Completions API. It runs on Node 18 with an Ink-based TUI (REPL fallback), saves and resumes sessions, compresses context, and tracks token cost, and it works with OpenAI, DeepSeek, DashScope/Qwen, or any compatible endpoint via environment keys. The project is very early: five commits, 45 stars, no releases, and no license file yet, so it functions primarily as a compact reference implementation for developers studying or forking a small agent harness.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cycode.md)
