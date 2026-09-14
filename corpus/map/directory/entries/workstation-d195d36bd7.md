# workstation (`workstation`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: varie-ai
- License: MIT
- Language: TypeScript
- Interface: install=Download DMG from GitHub Releases (recommended); install Claude Code plugin via /plugin marketplace add; or build from source (npm install && npm run dev)
- Model providers: Gemini, Claude, GPT
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [varie-ai/workstation](../../repos/varie-ai/workstation.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic coding orchestrator that lets you control Claude Code from your phone via Telegram or WhatsApp (through OpenClaw). Voice control (WhisperKit/Apple Speech), multi-session management, smart routing by repo name, live notifications with screenshots, plan approvals from phone, and work reports/checkpoints. Ships as an Electron app plus a Claude Code plugin with skills.

(captured site page body (agents/workstation.md), not a verified repo-code finding)
workstation exists for the case where Claude Code runs autonomously on a Mac but the developer is away from the desk: it pairs with OpenClaw so plans can be approved, questions answered, and commands dispatched from Telegram or WhatsApp, with the bridge detecting finishes and questions and replying with screenshots and notifications. It manages multiple Claude Code sessions with smart routing by repo name, a manager session, checkpoints, and work reports generated through a bundled Claude Code plugin/skills. Voice input uses WhisperKit or Apple Speech entirely on-device, with optional LLM-based routing (Gemini/Claude/GPT) as an opt-in. It is a free, MIT-licensed macOS Electron app installed as a Claude Code plugin marketplace package plus DMG, fully local with no telemetry. Its users are Claude Code developers who want to supervise autonomous sessions from a phone.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/workstation.md)
