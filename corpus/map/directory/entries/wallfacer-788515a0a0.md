# wallfacer (`wallfacer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: changkun
- License: MIT
- Language: Go
- Interface: platforms=Autonomous; install=curl -fsSL https://raw.githubusercontent.com/changkun/wallfacer/main/install.sh | sh
- Model providers: Claude Code (Anthropic), Codex (OpenAI), Cursor, OpenCode, Pi
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [changkun/wallfacer](../../repos/changkun/wallfacer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source, locally-run autonomous engineering platform that coordinates AI coding agents across multiple abstraction levels: chat (exploration), specs (structured design), tasks (parallel execution), and code (surgical edits). Provides a task board, plan mode, oversight audit trails, and cost/usage tracking. Works with coding agent harnesses (Claude Code, Codex, Cursor, OpenCode, Pi) through a pluggable harness layer; user-authored agents/flows as YAML in ~/.wallfacer/. ...

(captured site page body (agents/wallfacer.md), not a verified repo-code finding)
wallfacer exists to keep AI-assisted engineering organized as projects grow, instead of scattering work across chat sessions. Ideas enter as chat, become versioned Markdown specs arranged in a dependency tree with a seven-state lifecycle, and dispatch as tasks onto a kanban board where each task runs as a host process in its own git worktree with auto-test, auto-retry, circuit breakers, and per-task token/cost budgets. A pluggable harness layer lets each task or agent role be pinned to Claude Code, Codex, Cursor, OpenCode, or Pi, and oversight surfaces provide event timelines, diffs, and AI-generated summaries for review. The system is locally run with no cloud dependency and notably has developed much of its own recent functionality. It targets developers who want spec-driven, parallel agent execution on their own machines.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/wallfacer.md)
