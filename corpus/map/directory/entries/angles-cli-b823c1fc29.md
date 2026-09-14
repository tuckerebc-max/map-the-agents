# angles-cli (`angles-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ZSJ305
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=npm i -g @angleschina/angles && angles install; or curl install script; or PowerShell irm
- Model providers: OpenAI, Anthropic, Google, DeepSeek, xAI, MiniMax, OpenRouter, Qwen, GLM, Kimi, Custom
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry (renamed): original lead [zsj305/angles-cli](https://github.com/zsj305/angles-cli) (source: backing, field: `source_code_url`) now resolves to [angleschina/angles-cli](../../repos/angleschina/angles-cli.md) (github id 1306494403, verified [https://github.com/angleschina/angles-cli](https://github.com/angleschina/angles-cli)).

## Description

Highlight (site page `what_makes_it_special`): Terminal agentic coding assistant compiled into a single 1.6MB static Rust binary (no runtime needed); drives 30+ built-in tools and supports switching between 11 model providers at will; includes a local HTTP gateway (angles serve) with web console and REST API.

(captured site page body (agents/angles-cli.md), not a verified repo-code finding)
Angles targets minimal-footprint environments: one static binary, five prebuilt platforms, no Node or Python runtime, and a curated angles-* toolset spanning files, terminal, git, and web fetch/search. Reads are unrestricted, writes follow the configured approval policy, and deletions always prompt; the agent can emit operation plans before acting (\`angles plan\`) and serve a local HTTP gateway (angles serve) for browser chat and provider switching. Models are normalized across OpenAI Chat Completions, Anthropic Messages, and Gemini native protocols across OpenAI, Claude, Gemini, DeepSeek, Grok, MiniMax, OpenRouter, Qwen, GLM, Kimi, and custom endpoints. It is very early: 14 commits, 64 stars, no releases — promising on paper, immature in practice.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/angles-cli.md)
