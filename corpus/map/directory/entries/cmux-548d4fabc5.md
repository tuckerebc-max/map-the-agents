# cmux (`cmux`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: manaflow-ai
- License: GPL-3.0-or-later
- Language: Swift
- Interface: platforms=CLI; install=binary (DMG), brew
- Model providers: BYOK (works with any terminal-based agent: Claude Code, Codex, OpenCode, Gemini CLI, Kiro, Aider, Goose, Amp, Cline, Cursor Agent)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: yes (skills, custom commands via cmux.json) (yes)
  - claude_code_plugin: yes (cmux claude-teams runs Claude Code's teammate mode; Claude Code hooks/resume supported) (yes)
  - subagents: yes (yes)
  - hooks: yes (cmux hooks setup for Claude Code, Codex, OpenCode, etc.) (yes)
  - plan_mode: no (no)

Repository map entry: [manaflow-ai/cmux](../../repos/manaflow-ai/cmux.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A native macOS terminal built on libghostty (not Electron) designed specifically for parallel AI coding agent workflows, with a notification system (blue rings around panes), vertical tabs showing git branch/PR status, a built-in scriptable browser, and agent orchestration as native splits.

(captured site page body (agents/cmux.md), not a verified repo-code finding)
cmux argues that the right primitive for parallel agent work is a terminal that understands agents rather than another orchestrator: panes get attention rings when an agent needs input, tabs surface branch and PR metadata, and agent subagents appear as native panes. It embeds libghostty as a rendering library rather than forking Ghostty, so existing configs carry over, and a scriptable browser pane lets agents verify web UI changes they just made. Sessions restore across restarts, an iOS app allows monitoring from a phone, and a CLI/socket API makes it scriptable. With tens of thousands of stars it is the most prominent macOS-native agent terminal in this census.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cmux.md)
