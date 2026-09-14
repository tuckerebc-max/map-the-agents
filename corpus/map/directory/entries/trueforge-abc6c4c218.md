# TrueForge (`trueforge`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: truefoundry
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Web; install=npx (Node \>= 22.14), Docker/Docker Compose, or Helm chart on Kubernetes
- Model providers: OpenAI, Anthropic, Google Gemini, any OpenAI-compatible endpoint
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [truefoundry/trueforge](../../repos/truefoundry/trueforge.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): The runtime layer that turns an LLM into a working agent — model calls, MCP tools, skills, sandboxing, approvals, context management, and session state — exposed three ways: a bundled chat UI, an HTTP API with a TypeScript SDK, and an embeddable UI SDK. Runs in local single-process mode with SQLite or hosted mode with Postgres and Redis.

(captured site page body (agents/trueforge.md), not a verified repo-code finding)
TrueForge is TrueFoundry's open-source agent harness: the execution loop behind an agent rather than an agent product itself. It handles model calls across OpenAI, Anthropic, Gemini, and OpenAI-compatible endpoints; remote MCP servers with OAuth; git-backed skills; sandboxing-as-a-tool via Daytona; human approval checkpoints; and context engineering including subagents, deferred tool loading, a Code Mode, and compaction. The same runtime is exposed as a bundled chat UI, an HTTP API with the @truefoundry/trueforge-sdk TypeScript package, and an embeddable @truefoundry/trueforge-ui component, so teams can ship an agent product on top without owning the loop. Local mode runs as a single process with SQLite for development, while hosted mode scales out with Postgres and Redis via Docker Compose or a Helm chart on Kubernetes. Its users are platform teams embedding agents into their own products rather than developers looking for a ready-made coding assistant.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/trueforge.md)
