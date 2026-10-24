# Multistack (`multistack`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: gi-dellav
- License: GPL-3.0-only
- Language: Rust
- Interface: platforms=CLI; install=curl -fsSL https://raw.githubusercontent.com/gi-dellav/multistack/main/install.sh | bash
- Model providers: zerostack (OpenRouter, OpenAI, Anthropic, Gemini, Ollama, custom providers via zerostack)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [gi-dellav/multistack](../../repos/gi-dellav/multistack.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A lightweight Rust TUI for running multiple zerostack agents side by side in the terminal, with live status glyphs, per-agent timers, and desktop notifications when an agent waits for input.

(captured site page body (agents/multistack.md), not a verified repo-code finding)
Multistack is a lightweight Rust TUI that runs multiple zerostack agents side by side in the terminal, giving each agent its own PTY and Unix-socket status channel. It spawns parallel agents with zerostack --parallel, tracks live status (working, waiting, done, dead, conflict) with per-agent timers, and lets you drop into any agent's terminal output or signal an agent parked on a permission prompt. Keybindings spawn, rename, kill, and remove agents and projects, with support for git-worktree isolation, lazygit and shell popouts, and protocol v1.1 blocked/working signals. The tool requires Linux, BSD, or macOS, zerostack v1.5+ with the status-signals feature, and Rust 1.85+, and installs via Homebrew tap, curl script, or cargo. As a native open-source alternative to Conductor, it targets developers who orchestrate several zerostack sessions from one keyboard-driven dashboard rather than coding directly.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/multistack.md)
