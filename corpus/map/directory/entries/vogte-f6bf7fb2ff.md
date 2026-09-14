# vogte (`vogte`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: piqoni
- License: MIT
- Language: Go
- Interface: install=go install github.com/piqoni/vogte@latest
- Model providers: OpenAI, Anthropic, AWS Bedrock
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [piqoni/vogte](../../repos/piqoni/vogte.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic TUI for existing Go codebases that uses AST parsing to extract compressed, relevant context for the LLM. Two-step context approach: first extracts structs/interfaces/methods/signatures, asks LLM which files it needs in full, then provides full content. Runs go vet as a sanity check after patching. Stateless design (each message is a new chat) for cost-effectiveness. Features local PR review and ...

(captured site page body (agents/vogte.md), not a verified repo-code finding)
vix-like tools send whole repositories to the model; vogte exists to keep context small and Go-specific. It parses a codebase into abstract syntax trees, extracts structs, interfaces, methods, and signatures, and in a first step asks the LLM which files it needs in full before providing their complete contents, treating each request as a fresh one-shot chat rather than a retry-on-failure agentic loop. With the -agent flag it applies line-based patches directly to files and then runs go vet as a sanity check. It works with any OpenAI-compatible API and Anthropic models including via AWS Bedrock. The audience is Go developers maintaining existing codebases who want low-cost, one-shot context delivery rather than long interactive sessions.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vogte.md)
