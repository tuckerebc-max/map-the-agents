# FastAgency (`fastagency`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: ag2ai
- License: Apache-2.0
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, AG2
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [airtai/fastagency](https://github.com/airtai/fastagency) (source: backing, field: `source_code_url`) now resolves to [ag2ai/fastagency](../../repos/ag2ai/fastagency.md) (github id 829825571, verified [https://github.com/ag2ai/fastagency](https://github.com/ag2ai/fastagency)).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=other, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Unified programming interface for deploying AG2 (AutoGen) multi-agent workflows to production; seamless OpenAPI integration with few lines of code; Tester class for CI; CLI for orchestration; multiple UI options (Console, Mesop web) and network adapters (FastAPI REST, NATS via FastStream)

(captured site page body (agents/fastagency.md), not a verified repo-code finding)
FastAgency was built because multi-agent workflows that work in a notebook rarely survive contact with production: it provides one programming interface over AG2 workflows with pluggable UIs (console, Mesop web chat) and serving options (REST API, NATS-based distributed deployment). OpenAPI integration lets agents call existing REST services with minimal glue code, a Tester class runs workflows inside CI, and Cookiecutter scaffolding generates a complete project with devcontainer and deployment scripts for Docker and Fly.io behind GitHub Actions. Maintained by the ag2ai organization alongside AG2 itself, it targets Python teams moving multi-agent systems from prototypes to operated services rather than individual developers picking a coding assistant.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fastagency.md)
