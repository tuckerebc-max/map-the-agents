# Traycer AI (`traycer-ai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Traycer
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=VS Code / Open VSX extension
- Model providers: BYOA: Claude Code, Codex, Cursor, OpenCode, Gemini, Windsurf, custom agents, local runtimes; optional Traycer native inference on paid tiers
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Orchestration and planning layer ('Nerve Center') for coding agents — connects agents like Claude Code, Codex, Cursor, and Opencode in a shared workspace with shared context, memory, and handoff. Built-in workflow skills for planning, debugging, and reviewing. Available as VS Code / Open VSX extension. BYOA (Bring Your Own Agent) tier is free.

(captured site page body (agents/traycer-ai.md), not a verified repo-code finding)
Traycer addresses the fragmentation of running multiple coding agents: each lives in its own chat, plans live in scrollback, and handing work between agents means re-explaining everything. It sits above the agents as a shared workspace — each task carries its own filesystem, artifacts, and decision memory so models can be switched mid-task without losing context, while agents ask each other questions, request reviews, and hand off work through a defined protocol over worktrees. The built-in skills cover planning, debugging, reviewing, debating, documenting, and ticket-breaking, with Epic Mode decomposing high-level intent into specs before any code exists. Teams use it to supervise several agents from one workspace, with teammates inspecting tasks and steering work in multiplayer mode; pricing starts at $0 for BYOA, with paid tiers for cloud sync and Traycer-hosted inference.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/traycer-ai.md)
