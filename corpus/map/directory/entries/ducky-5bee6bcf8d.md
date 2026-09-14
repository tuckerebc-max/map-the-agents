# Ducky (`ducky`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ParthSareen
- License: MIT
- Language: Python
- Interface: install=uv tool install rubber-ducky, or uvx rubber-ducky
- Model providers: Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [parthsareen/ducky](../../repos/parthsareen/ducky.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Inline terminal companion that turns natural language into bash commands. Features a 'Crumbs' system for saving and reusing command shortcuts with argument substitution, piped input support, interactive REPL with rich keyboard shortcuts, and clipboard support across macOS/Windows/Linux. Works with both local and cloud Ollama models.

(captured site page body (agents/ducky.md), not a verified repo-code finding)
Ducky sits between the shell prompt and an LLM: describe what you want in English, get a concrete bash command back, inspect it, and run it — the human stays in the loop at every step. Rather than shipping its own models, it rides a local or cloud Ollama endpoint, so it works offline with qwen3-class models and costs nothing beyond compute. Its Crumbs system turns one-off suggestions into persistent parameterized shortcuts (with $variable substitution), which turns ad-hoc LLM answers into a personal command library. It is built for terminal-comfortable users who want command synthesis and explanation without a full agentic coding loop.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ducky.md)
