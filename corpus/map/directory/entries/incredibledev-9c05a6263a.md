# Incredible.Dev (`incredibledev`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: IncredibleDevHQ
- License: Apache-2.0
- Language: Rust
- Interface: install=Not yet available - README states documentation and run instructions coming soon
- Model providers: Up to 8 models including Ollama, Mistral, OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [incredibledevhq/incredible.dev](../../repos/incredibledevhq/incredible.dev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI coding co-worker for APIs (code, fix, document, deploy, test); multi-agent architecture with components (coordinator, code-navigator, code-search, code-understanding, ingestion, ai-gateway); the stated goal is to train smaller, task-specific models that outperform large general-purpose models on individual tasks - each agent can use its own model for a heterogeneous, per-task-optimized system. Early preview stage (561 commits, 34 stars).

(captured site page body (agents/incredibledev.md), not a verified repo-code finding)
Incredible.dev was pitched as an AI co-worker specialized for API codebases: one coordinator orchestrates ingestion, code-understanding, code-navigator, and code-search services plus an AI gateway, with each component free to run a different model. The distinguishing bet is training smaller task-specific models that beat large general-purpose ones on narrow tasks rather than routing everything through one frontier model. The Rust implementation ships Docker Compose files, but the README never published promised run instructions, and the last visible commit landed in May 2024. It remains an early research preview rather than an installable product.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/incredibledev.md)
