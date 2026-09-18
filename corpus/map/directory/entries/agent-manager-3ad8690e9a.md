# Agent-Manager (`agent-manager`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: YoanWai
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=Homebrew, install script, Arch AUR, mise, go install, or prebuilt binaries; requires tmux 3.1+ and git
- Model providers: delegates to the connected agents (Claude Code, Codex, OpenCode, Grok Build, Gemini CLI, Pi, Command Code, Hermes Agent)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [yoanwai/agent-manager](../../repos/yoanwai/agent-manager.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A tmux-based Bubbletea TUI that runs every AI coding agent side by side, each in its own persistent tmux session with your own logins, configs, and MCP servers intact — with live status detection grouped in a project tree, spacebar quick-prompts into any session, ctrl+r diff review that sends line comments back as one review prompt, and git worktree spawning.

(captured site page body (agents/agent-manager.md), not a verified repo-code finding)
Agent-Manager is a thin layer over the agent CLIs you already have installed: each agent — Claude Code, Codex, OpenCode, Grok Build, Gemini CLI, Pi, Command Code, or Hermes Agent — runs in its own persistent tmux session, so your subscriptions, config files, and MCP servers stay exactly as they were. The Go/Bubbletea TUI shows live status detection of which agents are done, waiting, or stuck, grouped in a project tree, and the workflow keys are built for fleet supervision: space sends a prompt into any session without attaching, v revives a dead session on its own conversation, f forks a conversation into a separate named session, and ctrl+r opens syntax-highlighted full-file diffs of an agent's changes whose line comments get sent back to the agent as a single review prompt. Arbitrary CLI tools can be registered through a \[tools.\<name\>\] config block with custom status rules, and agents spawn into isolated git worktrees. It targets macOS and Linux (Windows via WSL2) developers juggling several agent subscriptions at once.
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json); [site page @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/agents/agent-manager.md)
