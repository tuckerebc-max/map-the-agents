# coze-studio (`coze-studio`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: coze-dev
- License: Apache-2.0
- Language: Go (backend), TypeScript (frontend)
- Interface: install=docker
- Model providers: OpenAI, Volcengine (extensible)
- Feature flags (directory-reported):
  - mcp_support: partial (.mcp.json file present; transport not documented) (reported)
  - plugin_support: yes (yes)
  - claude_code_plugin: partial (.claude/agents dir and CLAUDE.md present) (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [coze-dev/coze-studio](../../repos/coze-dev/coze-studio.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): All-in-one visual AI agent development platform derived from ByteDance's Coze platform, offering no-code/low-code agent building with workflows, plugins, knowledge bases, and RAG in a microservice architecture built with DDD principles.

(captured site page body (agents/coze-studio.md), not a verified repo-code finding)
Teams building LLM assistants for support, operations, or internal tools rarely want to write agent infrastructure themselves, and ByteDance's commercial Coze platform was closed. Coze Studio releases the platform's core engine under Apache-2.0 for self-hosting: agents are assembled visually from prompt-engineering surfaces, plugins, knowledge bases, RAG pipelines, databases, and drag-and-drop workflows, running on a Go microservice backend built on the Eino and FlowGram frameworks. Deployment runs through Docker Compose or Helm, and finished agents ship via OpenAPI or a Chat SDK embedded in other products. Model configuration covers OpenAI and Volcengine among others, and a commercial tier exists for features the open-source core excludes. Product and operations teams building conversational agents - not developers writing code with agents - are its users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coze-studio.md)
