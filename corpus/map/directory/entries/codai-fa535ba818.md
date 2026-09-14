# codai (`codai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: meysamhadeli
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=go install github.com/meysamhadeli/codai@latest
- Model providers: OpenAI, Ollama, Azure OpenAI, Anthropic, Gemini, Mistral, Grok, Qwen, DeepSeek, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [meysamhadeli/codai](../../repos/meysamhadeli/codai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal AI coding agent with context-aware code completions; summarizes full project context using Tree-sitter; maintains conversational/code context per session; supports multi-file modifications simultaneously; tracks token consumption per request.

(captured site page body (agents/codai.md), not a verified repo-code finding)
Codai targets developers who want a terminal-native assistant that understands whole-project structure rather than single files: Tree-sitter parsing produces a summarized context of the codebase in six languages, which the assistant uses for multi-file edits, refactoring, test generation, and review, with per-session conversational and code context and per-request token accounting. Configuration is a single YAML file plus environment variables, with provider, model, and temperature switchable per invocation. It is a solo Go project, self-described work in progress, whose development has been intermittent, with the most recent commits in August 2025.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codai.md)
