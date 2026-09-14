# Strands Agents SDK (`strands-agents-sdk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: strands-agents
- License: Apache-2.0
- Language: Python, TypeScript
- Interface: platforms=Web; install=pip, npm
- Model providers: Amazon Bedrock, Anthropic, OpenAI, Google Gemini, Ollama
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [strands-agents/sdk-python](https://github.com/strands-agents/sdk-python) (source: backing, field: `source_code_url`) now resolves to [strands-agents/harness-sdk](../../repos/strands-agents/harness-sdk.md) (github id 983715534, verified [https://github.com/strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)).

## Description

Highlight (site page `what_makes_it_special`): Model-driven SDK taking a minimal-code approach to building agents. Model-agnostic (any model, any cloud; swap backends without code changes). Agent loop traces every decision; hooks intercept any step to log/validate/redirect; guardrails catch mistakes before execution with self-correction via steering handlers. Built-in MCP, streaming, multi-agent patterns, and structured output. Dual Python and TypeScript SDKs.

(captured site page body (agents/strands-agents-sdk.md), not a verified repo-code finding)
Strands takes a model-driven position: instead of orchestrating explicit workflows, the developer writes a few lines, the model chooses tools, and the SDK runs the loop with production controls around it — turn limits, token budgets, cancellation, stop-reason handling, structured output, streaming, session memory, and guardrails that catch mistakes before execution. Hooks intercept any step for logging, validation, or redirection, and steering handlers let an agent self-correct rather than fail; multi-agent patterns are first-class alongside a dedicated strands-mcp server package. First-class providers are Amazon Bedrock (default), Anthropic, OpenAI, and Gemini, with the SDK running entirely in-process and no hosted control plane. The Python and TypeScript SDKs share a monorepo with a docs site at strandsagents.com, and the project evolved from an internal AWS tool into a broadly used open-source framework.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/strands-agents-sdk.md)
