# claude-swarm (`claude-swarm`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: affaan-m
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=pip install claude-swarm; set ANTHROPIC_API_KEY
- Model providers: Anthropic (Opus 4.6 for planning/quality review, Haiku for worker execution)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [affaan-m/claude-swarm](../../repos/affaan-m/claude-swarm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent orchestration for Claude Code: Opus 4.6 decomposes tasks into a dependency graph of subtasks, Haiku worker agents execute in parallel with pessimistic file locking, then Opus runs a quality gate review. htop-style TUI dashboard, hard budget enforcement, JSONL session replay, and declarative YAML agent topologies.

(captured site page body (agents/claude-swarm.md), not a verified repo-code finding)
Claude Swarm demonstrates a cost-tiered orchestration pattern: expensive reasoning is confined to planning and integration review while cheap, well-specified execution runs on Haiku in parallel. Dependency-ordered waves via topological sorting, file locking to avoid write collisions, and a hard dollar budget with per-agent accounting make parallel agent runs economically controllable. A quality gate scores the combined output and can reject it, and sessions record to JSONL for replay. Built for the February 2026 Cerebral Valley x Anthropic hackathon, it has seen little development since, but the pattern it demonstrates influenced later planner-worker-review harness designs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-swarm.md)
