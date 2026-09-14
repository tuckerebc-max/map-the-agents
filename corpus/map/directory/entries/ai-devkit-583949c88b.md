# ai-devkit (`ai-devkit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: codeaholicguy
- License: MIT
- Language: TypeScript / Node.js
- Interface: install=npm
- Model providers: Claude Code, Gemini CLI, Codex CLI, Grok Build, Cursor, Copilot, Devin, opencode, Pi, Amp, Junie, Cline, Antigravity, Kilo Code, Roo Code
- Feature flags (directory-reported):
  - mcp_support: yes - memory exposed through MCP; init wires up MCP servers per agent (yes)
  - plugin_support: yes - composable skills from 30+ publishers; skill add \<registry\> \<skill\> (yes)
  - claude_code_plugin: yes - .claude-plugin directory; full setup + remote control support (yes)
  - subagents: yes - multi-agent coordination (agent send, groups, dev-lifecycle phases) (yes)
  - hooks: yes - hooks/ directory, .husky (yes)
  - plan_mode: yes - dev-lifecycle skill enforces requirements -\> design -\> planning -\> implementation -\> testing -\> review (yes)

Repository map entry: [codeaholicguy/ai-devkit](../../repos/codeaholicguy/ai-devkit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first control plane for AI coding agents - unifies scattered agents (Claude Code, Codex, Gemini CLI, Cursor, Copilot, Devin, etc.) under one shared operating layer: single .ai-devkit.json config, live TUI console for supervising sessions, cross-agent messaging (agent send), local SQLite memory retrieval without context bloat, and a dev-lifecycle skill forcing disciplined engineering phases with verification gates. Not a replacement for ...

(captured site page body (agents/ai-devkit.md), not a verified repo-code finding)
Developers running several coding agents end up maintaining parallel config trees, losing session state, and re-explaining conventions to each tool. ai-devkit establishes one local .ai-devkit.json as the source of truth, from which an init wizard writes per-agent directories (.claude/, .cursor/, and peers), nine built-in skills, and a docs/ai/ phase structure spanning requirements through testing. The CLI treats running agents as infrastructure: list and inspect sessions, watch them in a live TUI console, and inject prompts, logs, or test output into sessions with optional stdin and wait semantics, or drive them from a phone over a Telegram channel. Skills follow a dev-lifecycle spine (verify, memory, tdd, structured-debug, dev-commit, and more), and additional skills install from a catalog including Anthropic, Vercel, Supabase, Microsoft, and Google publishers. Everything runs locally — SQLite memory, no telemetry — under an MIT license.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ai-devkit.md)
