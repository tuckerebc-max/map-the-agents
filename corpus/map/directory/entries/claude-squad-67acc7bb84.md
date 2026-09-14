# Claude Squad (`claude-squad`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: smtg-ai
- License: AGPL-3.0
- Language: Go
- Interface: platforms=CLI, IDE; install=brew
- Model providers: Claude Code, OpenAI Codex, Google Gemini, Aider, OpenCode, Amp
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [smtg-ai/claude-squad](../../repos/smtg-ai/claude-squad.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal app (TUI) that manages multiple AI coding agents in separate isolated git worktrees, letting you run multiple tasks simultaneously in the background via tmux. Auto-accept/yolo mode. Review, commit, checkout, and push changes from a single terminal interface. Agent-agnostic -- works with virtually any CLI-based AI coding assistant (Claude Code, Codex, Gemini, Aider, OpenCode, Amp) through configurable profiles.

(captured site page body (agents/claude-squad.md), not a verified repo-code finding)
Claude Squad addresses the constraint that one terminal and one branch limit agents to one task at a time. It creates a tmux session plus git worktree per task so agents work on isolated branches without conflicting, while a single TUI lists sessions, shows previews and diffs, and handles review, commit, and push across all of them. A profiles system in ~/.claude-squad/config.json makes it agent-agnostic, so any terminal coding assistant can be dropped in. Background completion with auto-accept (-y) supports unattended runs. It is AGPL-3.0, written in Go, brew-installable, actively maintained by smtg-ai, and among the most widely adopted multiplexers in this census.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-squad.md)
