# Ourocodus (`ourocodus`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: multiplexer
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=Web; install=git clone, go build
- Model providers: Claude Code (via ACP), OpenAI Codex, other ACP-compatible agents
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (spins up multiple Claude Code ACP processes) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/ourocodus](../../repos/2389-research/ourocodus.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent orchestrator that spins up and coordinates multiple AI coding agents (Claude Code via claude-code-acp, OpenAI Codex, or other ACP-compatible agents) working concurrently on the same codebase. Manages git worktrees, session lifecycle, and a WebSocket relay with optional Docker container isolation and NATS event logging. The agent loop belongs to the underlying agents; Ourocodus multiplexes them.

(captured site page body (agents/ourocodus.md), not a verified repo-code finding)
Ourocodus is an orchestrator and relay that runs several coding agents concurrently on one codebase and coordinates them, rather than being an agent itself. It speaks the Agent Client Protocol (ACP), so it can spin up Claude Code through claude-code-acp alongside OpenAI Codex or any other ACP-compatible agent, and route work between them over a WebSocket relay. Each agent gets its own git worktree and managed session lifecycle, with optional Docker container isolation and NATS event logging for observability. The agent loop stays with the underlying agents — Ourocodus multiplexes them, manages their worktrees, and relays their outputs. The project is early stage and aimed at users who want to experiment with multi-agent concurrency on shared code.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ourocodus.md)
