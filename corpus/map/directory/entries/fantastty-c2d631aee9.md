# Fantastty (`fantastty`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: blaine
- License: MIT
- Language: Swift (SwiftUI; uses Zig for Ghostty dependency)
- Interface: platforms=Desktop; install=Download signed/notarized DMG from GitHub Releases (requires macOS 15.0+ Sequoia, Apple Silicon); alternatively build from source with Xcode 16+, Zig, and make xcframework
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [blaine/fantastty](../../repos/blaine/fantastty.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A macOS terminal app built on Ghostty (libghostty) with workspace-based session management and persistent tmux-backed sessions. Workspaces are independent sidebar items with tabs, timestamped notes (with revision history), auto-generated names, and tracked ticket/PR URLs (via UI or shell escape sequences). Supports SSH sessions with tmux persistence on both ends, workspace archiving, and attention indicators (background workspaces light up on bell/command ...

(captured site page body (agents/fantastty.md), not a verified repo-code finding)
Fantastty wraps Ghostty's rendering core (libghostty as a static library) in a SwiftUI terminal aimed at developers whose work spans many long-lived sessions. Workspaces are sidebar items with their own tabs, notes, and metadata, auto-named for quick identification, while tmux backing keeps shell sessions alive across restarts and reconnects. Notes can be written from the shell itself via a zsh integration (fantastty-note), workspaces carry ticket or PR URLs, and SSH sessions get first-class treatment alongside local ones. It targets macOS developers — including those running AI CLI agents — who want terminal history and workspace state to survive context switches, with no AI features of its own.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fantastty.md)
