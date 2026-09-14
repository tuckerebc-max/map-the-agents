# InsForge (`insforge`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

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

Highlight (site page `what_makes_it_special`): All-in-one open-source backend platform designed specifically for agentic coding, providing AI coding agents with database, auth, storage, compute, hosting, and an AI gateway through MCP server and CLI+Skills interfaces, enabling agents to operate the backend like backend engineers.

(captured site page body (agents/insforge.md), not a verified repo-code finding)
InsForge inverts the usual relationship between coding agents and backends: instead of the agent writing Supabase glue code, the backend exposes itself as MCP tools and CLI skills the agent calls directly — run migrations, deploy edge functions, create buckets, configure auth, fetch logs. Postgres with pgvector, OAuth-ready auth, S3-compatible storage, Deno edge functions, and an OpenAI-compatible model gateway cover the full-stack surface, and self-hosting is one curl script plus Docker Compose, with Railway, Zeabur, and Sealos templates for one-click deploys. Teams building with Claude Code or Codex use it to let the agent operate infrastructure like a backend engineer rather than generating boilerplate against a foreign API.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/insforge.md)
