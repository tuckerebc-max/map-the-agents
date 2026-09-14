# codebuddy (`codebuddy`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: olasunkanmi-SE
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous; install=VS Code Marketplace, Open VSX Registry, or search 'CodeBuddy' in extension manager. Requires VS Code 1.78+
- Model providers: Anthropic, OpenAI, Google, DeepSeek, Qwen, Groq, GLM, xAI, Ollama, Docker Model Runner
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [olasunkanmi-se/codebuddy](../../repos/olasunkanmi-se/codebuddy.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Autonomous multi-agent AI engineer in VS Code; self-healing execution loop; provider failover with cooldowns; hybrid memory/search (vector + FTS4 + MMR); enterprise-grade security (credential proxy, permission profiles, access control, doctor diagnostics); Tree-sitter AST parsing for 7 languages; OpenTelemetry observability; 20+ built-in tools; 7 specialized subagents; 16 bundled skills; 17 pre-configured connectors.

(captured site page body (agents/codebuddy.md), not a verified repo-code finding)
Codebuddy embeds an autonomous software engineer into VS Code, built on the LangGraph DeepAgents framework: a Developer Agent coordinates seven specialized subagents (analyzer, architect, debugger, reviewer, tester, doc writer, file organizer) while planning, editing, running terminal commands, and self-correcting until tasks complete. It supports ten model providers with automatic failover and cooldowns, MCP integration through Docker's MCP Gateway or direct SSE/stdio servers, and hybrid memory combining vector search with SQLite FTS4 and MMR reranking. Enterprise-oriented controls include a credential proxy, permission profiles, doctor diagnostics, OpenTelemetry tracing, and cost tracking across 25+ models, alongside 20+ built-in tools, 16 bundled skills, and 17 service connectors. The public repository was archived on August 28, 2026 and development continues in a private repository.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codebuddy.md)
