# peerd (`peerd`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: NotASithLord
- License: Apache-2.0
- Language: JavaScript
- Interface: platforms=Web; install=git clone + load unpacked extension (chrome://extensions); no build step
- Model providers: Anthropic, OpenRouter, Ollama (BYOK)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [notasithlord/peerd](../../repos/notasithlord/peerd.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs the agent inside the browser itself — the live DOM replaces MCP, a WASM Debian VM replaces the shell, and agents coordinate peer-to-peer over WebRTC with Ed25519 identities — deliberately refusing MCP as an exfiltration risk.

(captured site page body (agents/peerd.md), not a verified repo-code finding)
peerd is a bet that the browser, not the terminal, is the right runtime for a personal AI agent: the extension turns an existing Chrome or Firefox installation into the harness, inheriting the user's real logins and sessions instead of proxying them. Its act layer drives tabs through the live DOM, the think layer routes models (Anthropic, OpenRouter, local Ollama), spawns subagents, and plans, and a compute layer runs JavaScript notebooks, WASI/WASM tools, and a full Debian VM in WebAssembly. The design rejects MCP entirely — tabs stand in for app access, fetch for APIs, the WebVM for shell — on the argument that MCP dilutes the browser-native thesis and creates exfiltration paths. Agents coordinate peer-to-peer over WebRTC with Ed25519 identities and share signed app bundles through a DHT. It is Apache-2.0, free, accountless, and run-from-source as a v0.x developer preview, aimed at developers who want local, user-owned agent infrastructure.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/peerd.md)
