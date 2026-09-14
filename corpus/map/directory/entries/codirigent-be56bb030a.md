# Codirigent (`codirigent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: oso95
- License: GPL-3.0
- Language: Rust
- Interface: platforms=CLI, Desktop; install=Download .msi (Windows) or .dmg (macOS) from GitHub Releases; or cargo install --path .
- Model providers: Claude Code, Codex, Gemini CLI (wrapped CLIs)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: yes (yes)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [oso95/codirigent](../../repos/oso95/codirigent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Purpose-built for parallel AI coding workflows with real-time per-session status indicators, custom saveable grid layouts with drag-and-drop, synced file tree, Git worktree support for branch-isolated agents, automatic session resume for Claude Code/Codex, and smart clipboard that converts file paths for target CLIs

(captured site page body (agents/codirigent.md), not a verified repo-code finding)
Running several coding CLIs at once means juggling terminal windows with no shared view of what each agent is doing. Codirigent gives those sessions a single workspace: multiple agent CLIs run in parallel panes with live status indicators - idle, working, needs attention, ready - driven by status hooks that the tool registers into each CLI's own configuration (Claude Code, Codex, and Gemini settings files) on first launch. Sessions arrange into custom, saveable grid layouts with drag-and-drop, a synchronized file tree follows the focused session, and git worktree support isolates each agent on its own branch so parallel work does not collide. Session resume recovers Claude Code and Codex sessions automatically after restarts. Developers running several agent CLIs in parallel are the audience; the project is an early alpha with Windows and macOS builds.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codirigent.md)
