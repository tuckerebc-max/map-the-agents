# loom (`loom`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: husu
- License: unknown
- Language: TypeScript
- Interface: install=npm
- Model providers: DeepSeek, OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [husu/loom](../../repos/husu/loom.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-driven JSON Schema API documentation generator with a TUI chat interface, built-in React-based Web viewer, and a Mock service that auto-generates realistic mock data from schemas. Supports entity modeling with x-entity-ref reuse, LLM-powered source code API scanning, in-TUI service control, and vibe-coding style doc creation.

(captured site page body (agents/loom.md), not a verified repo-code finding)
API documentation drifts out of sync with code, and Loom addresses that with a chat TUI where developers describe endpoints in natural language and an LLM writes versioned JSON Schema files into docs/, or points /scan at existing source code to derive schemas from the implementation. A four-phase scan pipeline with checkpoints and resume keeps long scans resumable, and entity references (x-entity-ref) keep shared schemas consistent across endpoints. The generated docs render in a bundled React viewer, and a Fastify mock service turns schemas into realistic test data with status-code overrides. Backend teams maintaining REST APIs are the intended users; the project is early-stage with a small commit history, silent usage telemetry, and no license file.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/loom.md)
