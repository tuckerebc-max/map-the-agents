# eca (`eca`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
Every editor was growing its own AI plugin, each with different features and configuration; ECA borrows the LSP idea to end that: one Clojure server speaks a well-defined protocol, and editor integrat
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
