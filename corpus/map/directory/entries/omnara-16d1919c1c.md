# Omnara (`omnara`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: omnara-ai
- License: MIT
- Language: TypeScript
- Interface: platforms=Mobile, Web; install=git clone; docker compose -f compose.yaml --profile app up -d (self-hosted); or Omnara Cloud
- Model providers: BYO: OpenAI Responses, Chat Completions, or Anthropic Messages APIs (OpenRouter, LiteLLM, Ollama compatible)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [omnara-ai/omnara](../../repos/omnara-ai/omnara.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Positions itself as the API for production-grade agents — durable agent state committed atomically to Postgres with auto-recovery, hot-add/remove machines mid-run, and direct SQL access to agent state for analytics when self-hosted.

(captured site page body (agents/omnara.md), not a verified repo-code finding)
Omnara provides the execution and state layer for agents that teams define themselves, separating infrastructure from model choice, tooling, and user interface. Agent state commits atomically to Postgres so runs survive crashes and disconnects, and machines — cloud sandboxes or the operator's own hardware — can join or leave a run without restarts. Tools come from built-ins, custom code, skills, or MCP servers, and access control uses organization and project roles. Teams interact through a dashboard, a Slack connector, or the REST/TypeScript API rather than a chat product. The Apache-2.0 codebase self-hosts via Docker Compose, with a hosted cloud offering alongside it.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/omnara.md)
