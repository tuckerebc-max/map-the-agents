# lumnicode (`lumnicode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: martian56
- License: MIT
- Language: Python, TypeScript
- Interface: platforms=IDE, Web; install=git clone + docker-compose for PostgreSQL/MinIO + backend uv sync/uvicorn + frontend npm install/dev
- Model providers: OpenAI, Anthropic, Google Gemini, Groq, Together, Fireworks, Cohere
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: no (no)

Repository map entry: [martian56/lumnicode](../../repos/martian56/lumnicode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free web-based BYOK AI code editor/generator using Monaco editor with LangGraph orchestration pipeline (plan-\>config-\>generate-\>finalize) for AI project generation and S3-compatible file storage.

(captured site page body (agents/lumnicode.md), not a verified repo-code finding)
Lumnicode packages a self-hosted alternative to subscription AI editors: operators deploy it against PostgreSQL and any S3-compatible store (MinIO in development), and users bring their own provider keys, which the backend calls directly so costs track usage and no code or keys are pooled. Project generation runs through a LangGraph state machine - plan the file structure, generate configuration, write source files to S3, finalize - with per-node progress streamed over WebSocket into the editor. For existing code, a Cmd+K palette handles explain, refactor, completion, bug-finding, and test generation. Individual developers and small teams who want editor AI without per-seat pricing or vendor lock-in are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/lumnicode.md)
