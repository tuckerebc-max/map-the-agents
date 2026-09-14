# piclaw (`piclaw`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rcarmo
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=docker
- Model providers: multi-provider, OpenAI-compatible, Azure OpenAI, llama.cpp
- Feature flags (directory-reported):
  - mcp_support: yes (built-in via pi-mcp-adapter) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (workspace env hook via /workspace/.env.sh) (yes)
  - plan_mode: no (no)

Repository map entry: [rcarmo/piclaw](../../repos/rcarmo/piclaw.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted, single-user, mobile-friendly AI workspace packaging the Pi coding agent with a trilingual (English/Chinese/Japanese) streaming web UI, SQLite-backed persistent state, built-in tools (code editing, viewers, VNC, browser automation), optional auth (passkeys/TOTP), WhatsApp integration, and an extensible add-on system.

(captured site page body (agents/piclaw.md), not a verified repo-code finding)
piclaw packages the pi coding agent into a self-contained workspace for people who want it reachable from a phone: one Docker container serves a streaming web UI with an editor, terminal, and file viewers, with state in SQLite and sessions persistent across reconnects. The workspace is deliberately single-user and local-first, with optional passkey or TOTP authentication, staged tool loading to keep prompts lean, and an add-on system that layers on Ghostty terminal, Draw.io, Office document rendering, Windows desktop automation, Proxmox, and a WhatsApp bridge. MCP support arrives via the pi-mcp-adapter, and an experimental Electrobun desktop shell wraps the same stack natively. With over four thousand commits and an active issue triage board, development is continuous, and the author runs it as a personal infrastructure project documented in depth. Its audience is self-hosters who want their coding agent reachable, authenticated, and persistent from any device.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/piclaw.md)
