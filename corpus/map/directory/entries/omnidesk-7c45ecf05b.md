# omnidesk (`omnidesk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: carloluisito
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Desktop, IDE; install=Download prebuilt binaries (.exe/.dmg/.AppImage/.deb) from GitHub Releases; or build from source via npm install and npm run package
- Model providers: Claude Code,Codex CLI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [carloluisito/omnidesk](../../repos/carloluisito/omnidesk.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Electron-based desktop terminal wrapping AI coding CLIs (Claude Code, Codex CLI) with multi-session management, grid layouts, and real-time session sharing; 'attention cockpit' classifies agent session states (working/awaiting-approval/errored/done/idle) from rendered terminal screen content; on-device voice-to-text via local Whisper; one-click Cloudflare tunnel remote access with mobile PWA; session history with cross-session search; per-account quota tracking; local-first with no telemetry.

(captured site page body (agents/omnidesk.md), not a verified repo-code finding)
omnidesk is an Electron desktop terminal that organizes Claude Code and Codex sessions around a flat repo-to-session workflow. Sessions run in xterm.js panes with grid or focus layouts, persist across restarts, and auto-rename themselves to the agent's live task summary. An attention cockpit aggregates sessions needing intervention across all repositories, and worktree-aware sessions can bind to branches with optional cleanup. Sessions persist across restarts, and transcript history supports cross-session search with markdown export. Remote access mirrors the UI to a phone through a token-secured tunnel, and push alerts to Telegram, Slack, or Discord carry deep links back into specific sessions. The project is an unofficial community tool, MIT-licensed, with no telemetry.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/omnidesk.md)
