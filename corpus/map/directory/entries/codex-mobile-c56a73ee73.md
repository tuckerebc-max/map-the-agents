# codex-mobile (`codex-mobile`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: friuns2
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop; install=npm
- Model providers: OpenAI, Claude, DeepSeek, Gemini, GLM, GPT, Grok, Kimi, MiniMax, Qwen
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [friuns2/codex-mobile](../../repos/friuns2/codex-mobile.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight bridge exposing the Codex app-server as a browser-accessible web UI; runs on Android via Termux; one-command launch (npx codexapp); Telegram bot bridge; voice dictation; project ZIP export/import with chat rewriting.

(captured site page body (agents/codex-mobile.md), not a verified repo-code finding)
Codex-mobile addresses a practical constraint: Codex's desktop experience runs on one machine, but operators often want to check on or steer sessions from a phone or another computer. The tool runs a local Express and Vue server that bridges HTTP and WebSocket traffic to the Codex app-server over RPC, making the Codex interface available in any browser on the network or, through an optional built-in Cloudflare tunnel, from anywhere with a QR-code pairing flow and password protection. Beyond remote access it adds voice dictation, a Telegram bot bridge for allowlisted users to interact with a mapped Codex thread, and project portability through ZIP export and import that rewrites chat history for a destination CODEX_HOME, project path, and provider. It runs on Linux, Windows, and Android via Termux, launched with npx codexapp, and is developed openly on GitHub.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codex-mobile.md)
