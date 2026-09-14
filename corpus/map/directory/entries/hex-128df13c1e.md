# Hex (`hex`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=curl install script, homebrew, go install, or pre-built binaries
- Model providers: Anthropic (Claude)
- Feature flags (directory-reported):
  - mcp_support: yes (extensible via MCP servers) (yes)
  - plugin_support: yes (MCP server integration) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (Task tool for sub-agents) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/hex](../../repos/2389-research/hex.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source Claude Code–style agentic CLI built in Go with 13 built-in tools (Read, Write, Bash, Edit, Grep, Glob, AskUserQuestion, TodoWrite, WebFetch, WebSearch, Task, BashOutput, KillShell), SQLite conversation persistence with resume, streaming responses, sub-agents, background processes, and multi-agent orchestration with event-sourcing and cost tracking. Uses Bubbletea TUI, Cobra CLI, and pure-Go SQLite.

(captured site page body (agents/hex.md), not a verified repo-code finding)
Hex is a native-Go answer to Claude Code for developers who would rather run their coding agent as a single statically-linked binary than a Node stack. Inspired by Claude Code, Crush, Codex, and MaKeR, it ships 13 built-in tools — Read, Write, Bash, Edit, Grep, Glob, AskUserQuestion, TodoWrite, WebFetch, WebSearch, Task, BashOutput, and KillShell — covering file work, shell control, web fetches, and sub-agent fan-out. Conversations persist in pure-Go SQLite and can be resumed, so long tasks survive restarts, and streaming responses keep the Bubbletea TUI responsive while background processes and sub-agents run in parallel. A v1.0.0 production release reflects real polish, and MCP server integration extends the tool surface beyond the built-ins. The target user is a Go developer who wants a fast, self-contained, Claude-backed coding agent without leaving the language's toolchain.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hex.md)
