# cliclaw (`cliclaw`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: choiyounggi
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous, CLI, Desktop, Web; install=bun add -g @younggichoi/cliclaw (or npm install -g @younggichoi/cliclaw); then cliclaw init
- Model providers: Claude Code (Anthropic), Codex (OpenAI), Pi (Earendil), Gemini (Google)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [choiyounggi/cliclaw](../../repos/choiyounggi/cliclaw.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): macOS daemon that turns a Telegram chat into a remote control for local coding agent CLIs (Claude Code, Codex, Pi, Gemini). Kick off tasks, stream progress, approve/deny dangerous commands, and send follow-ups from your phone. Per-chat per-agent sessions, confirm gate, launchd auto-start, corporate TLS auto-detection. Spawns Claude Code with --permission-mode plan/bypassPermissions and injects a dangerous-command hook.

(captured site page body (agents/cliclaw.md), not a verified repo-code finding)
The tool answers a specific gap: coding agents run unattended on a development machine, but the developer is away from the keyboard. A single Bun daemon bridges Telegram to up to four local agent CLIs, streaming responses into the chat, accepting images, and requiring explicit inline-keyboard taps before dangerous commands execute, with silence meaning denial and every decision appended to an audit log. Sensitive-path reads are denied, corporate TLS interception is auto-detected, and a launchd agent keeps it running across reboots. Developers who kick off long agent tasks and leave the desk are the users; it is MIT-licensed, on npm, and actively maintained.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cliclaw.md)
