# tmux-assistant-resurrect (`tmux-assistant-resurrect`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: timvw
- License: MIT
- Language: Shell
- Interface: platforms=CLI; install=Tmux Plugin Manager (TPM): set -g @plugin 'timvw/tmux-assistant-resurrect' in ~/.tmux.conf, then prefix + I
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [timvw/tmux-assistant-resurrect](../../repos/timvw/tmux-assistant-resurrect.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): tmux plugin that persists and restores AI coding assistant sessions (Claude Code, GitHub Copilot CLI, OpenCode, Codex CLI, Pi, Oh My Pi, Grok) across tmux restarts and reboots. Hooks into tmux-resurrect to save assistant session IDs, CLI flags, and environment variables, then re-launches with the same config. Installs tool-native hooks (Claude Code SessionStart/SessionEnd hooks, OpenCode session-tracker plugin). Docker-based test suite ...

(captured site page body (agents/tmux-assistant-resurrect.md), not a verified repo-code finding)
tmux-assistant-resurrect solves a narrow but costly problem: AI coding assistant sessions vanish when tmux restarts or the machine reboots, taking their conversation context with them. The plugin attaches to the tmux-resurrect and tmux-continuum save cycle, snapshotting every pane with ps and recording which recognized assistant CLI each pane runs along with its session ID, flags, and environment in a JSON manifest. On restore it rebuilds the original command line and feeds it to each pane with tmux send-keys, so the seven supported CLIs resume where they left off; tool-native hooks (Claude Code SessionStart/SessionEnd, an OpenCode session-tracker plugin) are wired in alongside. Distribution is a four-line TPM block, and the project ships a Docker-based test suite of 400+ checks on GitHub Actions, though the author describes it as vibecoded with limited production exposure. Terminal-centric developers who juggle several assistant sessions across reboots are the users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tmux-assistant-resurrect.md)
