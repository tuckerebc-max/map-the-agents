# Bito (`bito`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Bito
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=Base-URL swap; point your agent at Governor via a single base URL (speaks Anthropic and OpenAI APIs); runs alongside existing gateway
- Model providers: Anthropic, OpenAI, Gemini, open models (BYOK)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Governor is a model router that grounds each request in your codebase via a code-context engine and routes to the best-sized model, cutting token count and cost; speaks the Anthropic and OpenAI APIs so any coding agent can use it via one base URL. GitHub org (github.com/gitbito) exists but product open-source status not confirmed.

(captured site page body (agents/bito.md), not a verified repo-code finding)
Bito targets the economics of agentic coding: agents spend heavily on tokens and on flagship models that simple tasks don't require, and they burn tokens wandering codebases via grep-and-read loops. Governor addresses both. A code-context engine builds a live knowledge graph of the repository and attaches the relevant map of files, symbols, and dependencies to each request, so agents stop grepping and reading their way into context; the company reports steps per task dropping from 47 to 23. A model router then scores request complexity against that graph and routes to the smallest capable model, reserving frontier models for high-blast-radius work. Deployment is a single base-URL or environment-variable swap since the service speaks the Anthropic and OpenAI APIs, and it runs alongside existing gateways on the customer's own provider keys. Engineering teams adopt it to cut agent spend roughly in half while keeping observability over tokens, spend, and routing decisions per team and key.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bito.md)
