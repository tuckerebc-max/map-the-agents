# 9remote (`9remote`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: decolua
- License: Proprietary
- Language: TypeScript, JavaScript
- Interface: platforms=CLI, Desktop, Web; install=npm install -g 9remote  (also Desktop App via Tauri, Mobile App iOS/Android, Web Client at 9remote.cc)
- Model providers: agents bring their own providers; 9remote supplies none
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [decolua/9remote](../../repos/decolua/9remote.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): All-in-one remote access (terminal + remote desktop + file explorer + code editor + git integration) from any phone or browser; QR-based pairing; auto Cloudflare tunnel (no port forwarding); persistent PTY sessions; \<50ms latency; LAN-first mode; works with AI coding tools from anywhere. Source not yet public (proprietary until star milestone reached).

(captured site page body (agents/9remote.md), not a verified repo-code finding)
Long-running AI coding sessions keep working after you leave the desk, but checking on them from a phone usually means SSH apps, port forwarding, and half-broken mobile terminals. 9remote packages the whole remote path: install the npm package, scan a QR code, and the tool opens a Cloudflare tunnel automatically, giving a phone or browser a persistent terminal, remote desktop, file explorer, code editor, and git views with sub-50ms interaction on LAN. Sessions persist server-side so agents keep working between visits, and a LAN-first mode covers no-internet setups. It is free during development, proprietary until a GitHub-star milestone triggers MIT open-sourcing, and targets developers who steer Claude Code, Codex, Cursor, or Gemini CLI sessions from their phone.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/9remote.md)
