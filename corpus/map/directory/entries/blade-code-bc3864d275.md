# blade-code (`blade-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: echoVic
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm install -g blade-code, or npx blade-code
- Model providers: 38+ providers via pi-ai including OpenAI, Anthropic, DeepSeek, Google, AWS Bedrock, and more
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [echovic/blade-code](../../repos/echovic/blade-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Next-generation AI coding assistant with three run modes (CLI terminal, Web UI, Headless JSONL for CI/sandbox). Features 20+ built-in tools, automatic cross-session memory that learns build commands and code patterns, precise multi-turn token cost tracking with cached pricing, four-tier permission system (default/autoEdit/plan/yolo), unified multi-model runtime with 38+ providers via pi-ai with auto-fetched model metadata, and Thinking mode support. Built with ...

(captured site page body (agents/blade-code.md), not a verified repo-code finding)
blade-code is a TypeScript coding agent built on the pi-ai runtime, which unifies more than 38 model providers behind one interface with auto-fetched model metadata such as context windows and pricing. It runs in three modes: a React+Ink terminal UI, a browser-based web UI served by a Hono server, and a headless JSONL mode for CI pipelines and sandboxed automation. Twenty-plus built-in tools cover file editing, search, shell execution, git, and browser automation through a session-isolated Chromium. A four-tier permission system (default, autoEdit, plan, yolo) plus tool allowlists governs autonomy, while a persistent memory layer learns each project's build commands and code patterns across sessions. Cost visibility is built in, with per-turn token and cost tracking that accounts for cached tokens. Individual developers and small teams use it as an open-source, multi-provider alternative to single-vendor agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/blade-code.md)
