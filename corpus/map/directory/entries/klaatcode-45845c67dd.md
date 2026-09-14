# klaatcode (`klaatcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: KlaatAI
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g klaatcode, or brew install KlaatAI/klaatcode/klaatcode, or curl installer
- Model providers: Klaatu routing, OpenAI-compatible, Claude, GPT, Gemini, DeepSeek, Kimi K3
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [klaatai/klaatcode](../../repos/klaatai/klaatcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native AI coding agent with per-request smart model routing across 6 cost tiers; real code knowledge graph (call graph, semantic search, blast-radius); no Continue button (free unlimited tool rounds); visible cost caps and burn-rate monitoring; compaction with self-check; reproducible benchmarks.

(captured site page body (agents/klaatcode.md), not a verified repo-code finding)
klaatcode targets the cost problem of terminal coding agents: most tokens are spent re-reading files the agent has already seen. Indexing the project into a call graph with semantic search lets the agent query callers, callees, and blast radius directly, and routing each request through Klaatu-o1 escalates or de-escalates the model tier per task. Tool calls within a request are free; only user messages consume quota, and cost guards with burn-rate monitoring bound runaway sessions. Subagents, lifecycle hooks, plan mode, and MCP presets cover the standard harness surface, and the claimed $0.027-per-solved-task benchmark ships as a reproducible bun run bench script for verification.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/klaatcode.md)
