# Code2Prompt (`code2prompt`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mufeedvh
- License: MIT
- Language: Rust
- Interface: platforms=CLI; install=cargo, brew, pip, binary
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mufeedvh/code2prompt](../../repos/mufeedvh/code2prompt.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Converts a codebase into a well-structured LLM prompt with source tree, Handlebars templating, token tracking, git integration, and .gitignore support. Complete ecosystem: Rust core + CLI + Python SDK + MCP server, with a TUI. Provider-agnostic — outputs prompts for any LLM.

(captured site page body (agents/code2prompt.md), not a verified repo-code finding)
Code2Prompt automates the context-building step that precedes most LLM-assisted coding work. It walks a repository, respects .gitignore and glob filters, renders the file tree and selected sources through Handlebars templates, counts tokens against configurable model budgets, and can embed git diffs, logs, and branch comparisons in the output. The engine ships as a Rust CLI with an interactive TUI, a Python SDK (code2prompt-rs on PyPI), and an MCP server mode that lets MCP-capable agents query the codebase on demand instead of receiving one large dump. It calls no model itself — output is provider-agnostic text suitable for any LLM — and is installed via Cargo, Homebrew, pip, or prebuilt binaries.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/code2prompt.md)
