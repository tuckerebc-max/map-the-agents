# stoneforge (`stoneforge`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: stoneforge-ai
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Web; install=npm install -g @stoneforge/smithy
- Model providers: Claude Code, OpenCode, OpenAI Codex
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [stoneforge-ai/stoneforge](../../repos/stoneforge-ai/stoneforge.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Web dashboard and runtime for orchestrating AI coding agents (multi-agent orchestration platform). Two layers: Smithy (orchestrator) and Quarry (event-sourced data SDK). Features automatic git worktree isolation per worker, event-sourced state (SQLite + JSONL) with full audit trail, dispatch daemon for auto task assignment by priority, merge steward (runs tests, squash-merges on pass), multi-provider support (Claude Code, OpenCode, OpenAI Codex), multi-plan ...

(captured site page body (agents/stoneforge.md), not a verified repo-code finding)
stoneforge targets developers running three to five or more coding agents simultaneously and drowning in coordination. A Director agent converts a goal into prioritized tasks with dependencies; a dispatch daemon assigns ready tasks to idle workers, each isolated in its own git worktree so parallel edits never collide; and a Steward role runs tests and squash-merges on success or converts failures into handoff tasks. Claude Code is the default provider with OpenCode and Codex also supported, and agents run autonomously with permissions bypassed rather than approval-gated, which suits teams that pre-scope their tasks. The Quarry data layer (SQLite plus JSONL event sourcing) underpins the dashboard and can be used independently. It is Apache-2.0, installs via npm, ships weekly, and is explicitly early-stage.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stoneforge.md)
