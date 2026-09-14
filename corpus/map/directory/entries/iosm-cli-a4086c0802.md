# iosm-cli (`iosm-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rokoss21
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g iosm-cli or npx iosm-cli (requires Node.js \>=20.6.0)
- Model providers: Anthropic, OpenAI, Google, Groq, OpenRouter, Mistral, xAI, Cerebras, AWS Bedrock
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [rokoss21/iosm-cli](../../repos/rokoss21/iosm-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native AI runtime (not a chat interface) for controlled engineering execution. Features the IOSM methodology (Improve -\> Optimize -\> Shrink -\> Modularize) with 6 canonical metrics, IOSM-Index health score, deterministic orchestration (/contract -\> /singular -\> /swarm), filesystem checkpointing/rollback, session persistence, and artifact history.

(captured site page body (agents/iosm-cli.md), not a verified repo-code finding)
iosm-cli enforces a measurable engineering discipline on top of LLM execution: every change cycle passes through Improve, Optimize, Shrink, and Modularize phases in strict order, scored on six canonical metrics rolled into an IOSM-Index, with guardrail breaches blocking progression. Complex work follows /contract to define the change, /singular to pick among three trade-off options, and /swarm for deterministic parallel execution with scopes, locks, and gates. Safety tooling includes checkpoints, rollback, snapshot/restore, a trust ledger, and optional bwrap sandboxing. Profiles switch between everyday coding, read-only planning, and orchestration-first meta mode, and integrations span JSON-RPC for IDEs, a Telegram bridge, and a TypeScript SDK.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/iosm-cli.md)
