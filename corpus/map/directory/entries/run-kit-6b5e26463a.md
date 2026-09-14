# run-kit (`run-kit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: sahil87
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=curl -fsSL https://shll.ai/install | sh (Homebrew); desktop app via run-kit desktop install
- Model providers: Agent-agnostic (Claude Code, Codex, Gemini)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [sahil87/run-kit](../../repos/sahil87/run-kit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent-agnostic remote tmux console with no database, state derived from tmux + filesystem; phone-first, keyboard-first; spawns parallel agent worktrees via git worktrees; outlives agent tooling churn.

(captured site page body (agents/run-kit.md), not a verified repo-code finding)
The tool exists for the failure mode where an agent is running on a desk machine and the developer is elsewhere — it exposes every tmux session and pane as a live terminal in a phone-first PWA or a macOS desktop app, over Tailscale HTTPS if desired. It deliberately understands nothing about agents: a pane is a pane, and Claude Code, Codex, builds, and htop are equal citizens, which insulates it from changes in agent tooling. Optional Claude Code hooks feed lifecycle states into status dots (busy, waiting, idle), and riff provisions worktree-plus-tmux workspaces in bulk for parallel runs. It is part of the shll toolkit alongside wt for worktrees, installs in one curl line requiring tmux 3.4+, and targets developers supervising long-running agent sessions from a phone or a second screen.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/run-kit.md)
