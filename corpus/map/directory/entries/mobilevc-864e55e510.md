# MobileVC (`mobilevc`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: JayCRL
- License: MIT
- Language: Go, Dart (Flutter)
- Interface: platforms=CLI; install=npm install -g @justprove/mobilevc; mobilevc start (mobile app via TestFlight/APK)
- Model providers: Claude Code, OpenAI Codex (manages local CLI sessions)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [jaycrl/mobilevc](../../repos/jaycrl/mobilevc.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Turns a phone into a control center for AI coding assistant CLI sessions (Claude/Codex) on a computer, structuring high-frequency waiting states into actionable mobile workflows (buttons/cards) rather than mirroring a terminal. Supports LAN or encrypted Relay, diff approvals, Plan Mode advancement, and voice pre-communication.

(captured site page body (agents/mobilevc.md), not a verified repo-code finding)
Agentic CLI sessions spend most of their wall-clock time waiting for a human — to approve a permission, advance a plan, accept a diff — and that waiting usually pins the developer to their desk. MobileVC turns the phone into the approval surface: a Go server wraps local Claude Code or Codex CLI sessions in a PTY with a WebSocket event stream, and a Flutter app renders pending decisions as buttons and diff cards rather than a tiny terminal. Sessions can be started, continued, and restored from history; files, logs, and run state are browsable; and plan-mode advancement plus voice pre-communication let a user brief the agent verbally before handing off. Connectivity runs over LAN with QR-scan token auth or through an encrypted relay whose server never sees plaintext, and an ADB/WebRTC bridge adds Android emulator debugging from the phone. Developers running long unattended agent sessions use it to keep work moving from anywhere.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mobilevc.md)
