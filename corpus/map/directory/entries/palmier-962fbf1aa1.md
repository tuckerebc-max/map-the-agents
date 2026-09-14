# Palmier (`palmier`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Palmier
- License: Apache-2.0
- Language: TypeScript
- Interface: install=curl -fsSL https://palmier.me/install.sh | bash (Linux/macOS); npm install -g palmier && palmier init; requires Node.js 24+
- Model providers: reuses existing AI subscriptions (Claude Pro, ChatGPT Plus, etc.) — no API keys
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Turns your phone into a remote control for AI agent CLIs (Claude Code, Codex, Gemini CLI, GitHub Copilot, etc.) running on your computer. Uses your existing AI subscriptions — no API keys or per-token costs. Exposes an MCP server with 14 tools and 2 resources. Built-in AES-256-GCM password manager that agents can autofill into browsers without seeing credentials. Phone capability ...

(captured site page body (agents/palmier.md), not a verified repo-code finding)
Long agent runs outlive attention spans, and walking back to the laptop to check a Claude Code or Codex session interrupts everything else. Palmier runs a background daemon — systemd on Linux, launchd on macOS 13+, Task Scheduler on Windows — that installs and manages agent CLIs and exposes their control to a phone PWA or Android app, with all execution staying on the user's machine and no data stored remotely. It reuses existing subscriptions like Claude Pro or ChatGPT Plus instead of requiring API keys, and new agent CLIs are added through configuration rather than code. An MCP server on localhost:7256 hands agents tools that reach back into the phone — calendar, contacts, notifications, geolocation, SMS, email — plus an encrypted password manager for agent logins, so a session can schedule a meeting or send a message on the user's behalf. Install is a curl script or npm global under Node 24+, Apache-2.0 licensed. Developers who start agent runs and leave the desk are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/palmier.md)
