# Vendo (`vendo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: runvendo
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Web; install=npm packages (@vendoai/vendo) in a pnpm monorepo; PGlite by default, Postgres in production; deployable on Railway
- Model providers: any AI SDK LanguageModel
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [runvendo/vendo](../../repos/runvendo/vendo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An embedded agent SDK for B2B SaaS that lets your end customers build their own features and micro-apps on top of your product: agents execute through the host product's own API as the signed-in user, build live views from the host's components, remix the UI in place, and create standing automations — all without touching the host's source code.

(captured site page body (agents/vendo.md), not a verified repo-code finding)
Vendo is a YC-backed open-source layer for B2B SaaS teams that want to give their customers in-product customization without shipping a plugin platform of their own. The embedded agent executes through the host product's own API as the signed-in user, so permissions and data boundaries come from the product itself: users ask questions and get live views composed from the host's components, hover a UI element and describe a change to remix it in place, and turn plain-language instructions into standing automations with per-tool approvals. Safety controls include policy enforcement, grants, circuit breakers, and audit logging, with generated UI running in a sandboxed iframe. For developers it is a TypeScript SDK compatible with any AI SDK LanguageModel, integrating with Claude Code, Cursor, Copilot, and MCP clients during development, self-hostable with PGlite or Postgres and optional Vendo Cloud features via API key.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vendo.md)
