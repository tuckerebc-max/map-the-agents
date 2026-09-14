# harness-terminal (`harness-terminal`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: robzilla1738
- License: MIT
- Language: Swift
- Interface: platforms=CLI, Desktop; install=Download DMG, drag Harness.app to Applications; or build from source via make release
- Model providers: none (hosts Claude Code, Codex, Cursor, Grok, Gemini, Aider, Goose, OpenCode sessions)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [robzilla1738/harness-terminal](../../repos/robzilla1738/harness-terminal.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native macOS terminal with GPU rendering, persistent daemon-owned sessions (survive app quit), CLI automation (harness-cli), remote/headless daemon support, and agent detection — monitors coding agents (Claude Code, Codex, Cursor, etc.) and notifies you when an agent stops or needs approval.

(captured site page body (agents/harness-terminal.md), not a verified repo-code finding)
harness-terminal is a macOS terminal emulator designed around the reality that its users spend their day inside coding agents. A process-tree detector identifies which agent (Claude Code, Codex, Cursor, Grok, Gemini, Aider, Goose, OpenCode, and others) is running in each session and surfaces that in the UI, with desktop notifications and a sidebell when an agent finishes or awaits permission; agents can also self-notify through harness-cli notify. Beneath the agent features sits a full terminal: Metal-based GPU rendering, 490 themes, ligatures, inline images, shell integration, and a command palette. Sessions are owned by a daemon, so tabs, splits, and scrollback survive app quits and even daemon restarts, and the same daemon runs headless on Linux for remote workflows. A harness-cli exposes send-keys, capture-pane, and attachment commands for scripting, with tmux-parity behavior across four experience modes.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/harness-terminal.md)
