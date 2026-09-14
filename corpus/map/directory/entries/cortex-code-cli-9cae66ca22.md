# Cortex Code CLI (`cortex-code-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: Apache-2.0 (CLI); Snowflake Skills License (skills)
- Language: Python
- Interface: platforms=CLI; install=bash install.sh / ./install.ps1 / npx @snowflake-labs/ai-kit
- Model providers: Claude and OpenAI GPT models via Snowflake Cortex (auto-select available)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: yes (works as plugins for Claude Code and OpenAI Codex; auto-detects Snowflake prompts and routes them; also works natively in Cursor via 'Third-party skills') (yes)
  - claude_code_plugin: yes (yes)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: yes (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Snowflake's data-native AI coding agent CLI with 55+ built-in skills spanning SQL, data governance, dynamic tables, ML, streaming, cost intelligence, lineage, dbt, notebooks, and security investigation; lightweight keyword filter runs on every prompt (~50ms, no network) to detect Snowflake intent and auto-route; ships as plugins for Claude Code and Codex.

(captured site page body (agents/cortex-code-cli.md), not a verified repo-code finding)
Data engineering work - writing SQL, tracing lineage, tuning warehouses, building dbt projects - happens inside Snowflake's governance boundary, where generic coding agents lack both context and permissions. Cortex Code is Snowflake's terminal agent for that domain: it takes natural-language requests, orchestrates over 55 Snowflake-native skills plus MCP tools, shows its reasoning steps, and in plan mode confirms each action before executing. Skills cover catalog discovery, query optimization, dynamic tables, cost intelligence, lineage, dbt projects, and security investigation, and the same skill set installs as plugins for Claude Code, Codex, and Cursor via Snowflake's AI Kit. Access requires a paid Snowflake account with Cortex roles, with usage billed through Snowflake Cortex; Claude and OpenAI models are selectable via /model. Data engineers and analytics teams are the users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cortex-code-cli.md)
