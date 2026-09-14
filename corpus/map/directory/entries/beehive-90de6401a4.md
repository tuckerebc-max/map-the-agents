# beehive (`beehive`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: storozhenko98
- License: MIT
- Language: Rust, TypeScript
- Interface: install=Desktop: .dmg from Releases; TUI: curl -fsSL beehiveapp.dev/install.sh | bash; From source: npm install + npm run tauri build or cargo build --release
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [storozhenko98/beehive](../../repos/storozhenko98/beehive.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Orchestrates coding agents across isolated git workspaces; manage multiple repos, create isolated workspace clones (combs) on different branches, run terminals and AI agents side-by-side from one window; supports launching Claude Code or any CLI agent; custom buttons for per-repo agent commands

(captured site page body (agents/beehive.md), not a verified repo-code finding)
Beehive organizes AI coding agent workspaces the way tmux organizes terminals: repos are 'hives', grouped into 'nests', each with isolated full git clones ('combs') on any branch, and persistent 'panes' that hold terminal or agent sessions across context switches. Agents such as Claude Code run as ordinary CLI processes inside panes, so the app manages workspaces and sessions rather than coding itself - fitting the multiplexer category. Isolated workspace clones (combs) can be duplicated, including uncommitted changes, for safe experimentation on different branches, with per-repo quick-launch buttons and persisted pane layouts. It ships as a macOS desktop GUI (Tauri) and a Rust TUI for macOS and Linux, MIT-licensed, with beehiveapp.dev as its site. It targets developers running several agent sessions across many repos who want tmux-style isolation.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/beehive.md)
