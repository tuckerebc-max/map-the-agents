# repomon (`repomon`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: AliHamzaAzam
- License: Apache-2.0
- Language: Rust
- Interface: platforms=CLI, IDE; install=Desktop app (DMG/EXE/AppImage/deb/rpm) from GitHub releases; CLI via curl install script, Homebrew, or cargo install --git
- Model providers: Claude Code, Codex, Antigravity, OpenCode, Cursor, Aider
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [alihamzaazam/repomon](../../repos/alihamzaazam/repomon.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Mission control for managing a fleet of AI coding agents across many repos x many worktrees x many agents simultaneously. Unlike tools that run parallel agents in one repo, repomon is built for developers juggling 5-15 active projects with a fleet of agents running at once. Durable tmux-backed runtime, desktop app and TUI clients, git explorer, in-app editor, fleet mail ...

(captured site page body (agents/repomon.md), not a verified repo-code finding)
Running five agents in five repos means five terminals, five notification streams, and no overview of which one is blocked; repomon exists to collapse that into one screen. A single daemon backs a Tauri desktop app and a Rust TUI with four zoom levels, from a fleet overview down to a single agent's scrollback, with agents waiting on the human floated to the top. Fleet mail routes messages between agents per lane or broadcast, a git explorer and editor resolve merge conflicts in place, and a token-gated WebSocket bridge exposes the whole board over Tailscale for remote access. It is aimed at developers who treat multiple agent sessions as a permanent part of their workflow rather than an experiment.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/repomon.md)
