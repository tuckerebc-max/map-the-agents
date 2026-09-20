# InsForge (`insforge`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: other
- Provider/maker: InsForge
- License: Apache-2.0
- Language: TypeScript/JavaScript (Next.js, Deno for edge functions)
- Interface: install=docker
- Model providers: multiple LLM providers via OpenAI-compatible Model Gateway
- Feature flags (directory-reported):
  - mcp_support: yes (MCP server, both self-hosted and cloud; likely stdio) (yes)
  - plugin_support: yes (CLI + Skills system; .claude/skills and .codex/skills directories) (yes)
  - claude_code_plugin: yes (.claude-plugin directory and CLAUDE_PLUGIN.md present) (yes)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [insforge/insforge](../../repos/insforge/insforge.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
InsForge inverts the usual relationship between coding agents and backends: instead of the agent writing Supabase glue code, the backend exposes itself as MCP tools and CLI skills the agent calls dire
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
