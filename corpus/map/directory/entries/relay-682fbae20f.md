# Relay (`relay`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: jcast90
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm install -g @jcast90/relay && rly welcome; or from source: git clone https://github.com/jcast90/relay && cd relay && ./install.sh; GUI app downloadable from GitHub releases (.dmg/.AppImage/.deb/.msi)
- Model providers: Claude, Codex, any OpenAI- or Anthropic-compatible HTTP API (MiniMax, OpenRouter, DeepSeek, Groq, Together, LiteLLM, vLLM)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [jcast90/relay](../../repos/jcast90/relay.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cross-repo agent-to-agent delegation via a single orchestrator that reaches into multiple repos and coordinates a delegation tree — unlike single-repo agent harnesses. Local-first, all state in ~/.relay/, no cloud/telemetry. Three dashboards (CLI, TUI, GUI) sharing one source of truth. MCP server exposes 19 tools. Classifier → planner → decomposer pipeline with user approval for complex tiers.

(captured site page body (agents/relay.md), not a verified repo-code finding)
Relay addresses the problem that coding agents operate inside one checkout at a time, while real work spans several repositories — a schema change in one repo breaks consumers in three others. A user hands the orchestrator a sentence, GitHub issue, or Linear ticket; it classifies complexity, produces a plan, decomposes it into a dependency DAG of tickets, and dispatches agents that verify their work and open PRs. State lives entirely in ~/.relay as atomic file writes, so there is no server and no telemetry, and sessions approaching context limits emit handoff briefs for their successors. It suits maintainers who already live in Claude Code or Codex CLI and want delegation across repos without adopting a hosted coordination service.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/relay.md)
