# MiniCode (`minicode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: LiuMengxuan04
- License: MIT
- Language: TypeScript, Rust, Python, Go, Java
- Interface: platforms=CLI; install=npm
- Model providers: Anthropic-compatible (via ANTHROPIC_BASE_URL)
- Feature flags (directory-reported):
  - mcp_support: yes (stdio, HTTP) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [liumengxuan04/minicode](../../repos/liumengxuan04/minicode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intentionally compact implementation of a Claude Code-like agent loop suitable for study, modification, and as a reference architecture. Available in 5 languages. Features full-screen TUI with session persistence, review-before-write edits, layered memory, context auto-compact/collapse, oversized-result offloading to disk, and local skills via SKILL.md files.

(captured site page body (agents/minicode.md), not a verified repo-code finding)
MiniCode exists to be read: it reproduces the Claude Code interaction model — terminal session, tool calls, review-before-write edits, persistent sessions — in a codebase small enough to study and modify, and then makes the architecture portable by maintaining equivalent implementations in Rust, Python, Go, and Java alongside the TypeScript original. The agent loop supports multiple tool calls per turn, and up to three concurrent read-only subagents explore while the root agent retains sole ownership of writes. Tool results that would bloat context are offloaded to disk with a preview left in place, and context auto-compacts as sessions grow. MCP servers attach over stdio or HTTP, and skills are discovered from SKILL.md files for local capability extension. Configuration runs through Anthropic-compatible environment variables, so any Anthropic-API-compatible backend — including local proxies — works, with a mock mode for offline development. Developers use it as a reference implementation, a hackable base for custom tooling, and a compact daily-driver alternative.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/minicode.md)
