# eca (`eca`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: editor-code-assistant
- License: Apache-2.0
- Language: Clojure
- Interface: platforms=IDE; install=binary
- Model providers: OpenAI, Anthropic, GitHub Copilot, Ollama
- Feature flags (directory-reported):
  - mcp_support: yes (stdio) — supports MCP resources and prompts for additional code context (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes — configure multiple agents with different models, tools, and behaviors (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [editor-code-assistant/eca](../../repos/editor-code-assistant/eca.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Editor-agnostic AI pair programming tool using an LSP-like protocol; a central server handles tool call management, multi-LLM interaction, telemetry, and unified configuration so any editor gets the same UX.

(captured site page body (agents/eca.md), not a verified repo-code finding)
Every editor was growing its own AI plugin, each with different features and configuration; ECA borrows the LSP idea to end that: one Clojure server speaks a well-defined protocol, and editor integrations — Emacs, VS Code, IntelliJ, a desktop app — stay thin. The server owns chat, rewrite, and completion flows, multi-agent configuration with different models and tools per agent, MCP resources/prompts for context, and OpenTelemetry export of tool and prompt metrics. One global or local config makes behavior identical across editors. It appeals to developers who move between editors or use non-mainstream ones and want their AI setup to follow them.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/eca.md)
