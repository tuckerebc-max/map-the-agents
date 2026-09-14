# Bernstein (`bernstein`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: sipyourdrink-ltd
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI, IDE; install=pip
- Model providers: Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor, Aider, Goose, Ollama, OpenCode, OpenHands, and 39+ more CLI agent adapters
- Feature flags (directory-reported):
  - mcp_support: yes — MCP server mode, .mcp.json present (yes)
  - plugin_support: yes — .plugin directory, plugin.json, agent catalogs (yes)
  - claude_code_plugin: no (no)
  - subagents: yes — manager decomposes goals into tasks with roles; 49 selectable agent adapters (yes)
  - hooks: yes — hooks/ directory in repo (yes)
  - plan_mode: yes — bernstein run plan.yaml for multi-stage plans (yes)

Repository map entry (renamed): original lead [chernistry/bernstein](https://github.com/chernistry/bernstein) (source: backing, field: `source_code_url`) now resolves to [sipyourdrink-ltd/bernstein](../../repos/sipyourdrink-ltd/bernstein.md) (github id 1188762020, verified [https://github.com/sipyourdrink-ltd/bernstein](https://github.com/sipyourdrink-ltd/bernstein)).

## Description

Highlight (site page `what_makes_it_special`): Deterministic orchestrator for CLI coding agents with no LLM in the coordination loop — replay yesterday's plan and get yesterday's task graph byte-identical; cryptographic checkability with Ed25519-signed receipts; each task gets its own git worktree; air-gap deployable.

(captured site page body (agents/bernstein.md), not a verified repo-code finding)
Bernstein exists because parallel AI coding agents are expensive and nondeterministic: its author was paying $400/month for three parallel agents producing inconsistent results. It coordinates any CLI agent (Claude Code, Codex, Gemini CLI, Copilot CLI, Aider, Goose, Cursor, 40+ more, plus a generic --prompt mode) through a four-stage pipeline: one LLM call decomposes the goal into tasks, agents run in isolated git worktrees, a 'janitor' verifies concrete signals (tests, files, lint, types), and verified work merges while failures retry or reroute to a different model. No LLM participates in scheduling, so replays are reproducible, and every run produces an Ed25519-signed receipt plus an opt-in HMAC-chained audit log with Merkle seal. Mix-and-match agent backends, a TUI dashboard, MCP server mode, and 51 integrations round it out. It is Apache-2.0, beta, solo-maintained, and aimed at developers running multiple coding agents in parallel who need reproducibility.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bernstein.md)
