# code-assistant (`code-assistant`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: stippi
- License: MIT
- Language: Rust
- Interface: platforms=Autonomous; install=Download prebuilt binary from GitHub Releases (macOS, Linux, Windows), or build from source with cargo build --release
- Model providers: Anthropic, OpenAI, Google Vertex AI, Ollama, OpenRouter, SAP AI Core, Groq, Cerebras, Mistral
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [stippi/code-assistant](../../repos/stippi/code-assistant.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source AI coding agent in Rust with native GUI, terminal mode, and MCP integration (both as MCP client and headless MCP server). Features transparent UI showing tool execution and context, format-on-save reconciliation, transparent file encoding/line endings, document support (Word, Excel, PowerPoint, PDF as Markdown), browser sessions for web app testing with human-in-the-loop login, and four interfaces (native GUI, TUI, headless ...

(captured site page body (agents/code-assistant.md), not a verified repo-code finding)
The project's differentiator is transparency and model tolerance: every tool invocation is visible as it happens, safety filters prevent editing a file before reading it, and the agent adapts its tool-call format to the model in use, so providers without reliable native function calling still work. It preserves file encodings and line endings, reconciles formatter output token-efficiently on save, reads Office and PDF files as Markdown, and runs browser sessions with human-in-the-loop logins for testing web apps. Nine providers are supported, including SAP AI Core for enterprise contexts, and reusable skills encode multi-step playbooks. Developers using Zed or editor-agnostic setups, and those who want a GUI without Electron, are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/code-assistant.md)
