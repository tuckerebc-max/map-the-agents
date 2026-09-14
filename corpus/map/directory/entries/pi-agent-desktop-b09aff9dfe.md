# pi-agent-desktop (`pi-agent-desktop`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: abcwyc
- License: MIT
- Language: TypeScript/JavaScript (Next.js), Rust (Tauri)
- Interface: platforms=CLI, Desktop; install=Download from GitHub Releases (.dmg Apple Silicon, .deb Linux x64, x64-setup.exe Windows)
- Model providers: Multi-provider via pi runtime (model and API-key management in-app)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [abcwyc/pi-agent-desktop](../../repos/abcwyc/pi-agent-desktop.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local AI agent desktop app for macOS, Windows, and Linux that packages the agent capabilities of pi into a standalone installable application — bringing the Claude Code experience to your desktop. Manages models, OAuth/API keys, skills, and plugins.

(captured site page body (agents/pi-agent-desktop.md), not a verified repo-code finding)
pi-agent-desktop exists for developers who want pi's terminal-grade coding agent without maintaining a CLI environment, packaging the agent core, the pi-web interface, and the Pi SDK into a Tauri application for macOS (Apple Silicon), Windows, and Linux (x64). The app reads pi's existing local data directory, so prior sessions, model credentials, and configuration carry over, and it manages models, API keys, skills, and plugins through a GUI instead of CLI flags. A signed auto-updater ships complete new builds in-app, with daily GitHub workflows syncing upstream pi and pi-web releases and gating publishing on conflict-free merges. Server requests honor standard proxy variables, and keys stay local. Its users are pi-curious developers on macOS or Windows who want the agent without a terminal setup, and the project tracks upstream pi releases automatically.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pi-agent-desktop.md)
