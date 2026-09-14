# biscuit (`biscuit`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: tomlin7
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=pip install biscuit-editor; or uv tool install biscuit-editor
- Model providers: Gemini, Anthropic, Ollama (via extension, deprecated)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [tomlin7/biscuit](../../repos/tomlin7/biscuit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight (\<20MB), fast native code editor with AI agents, tree-sitter based code intelligence, DAP debugging, extension marketplace, ripgrep-based fast search, vim mode — all in a compact, extensible Python-based editor.

(captured site page body (agents/biscuit.md), not a verified repo-code finding)
Biscuit targets developers who want a fast, hackable editor without the gigabyte-scale installs of Electron IDEs. Built in Python on Tk, it ships tree-sitter syntax parsing, completions, LSP integration via extensions, ripgrep-powered search, git operations with split diffs, and a DAP debugging client in a package under 20MB installed with pip. Its AI layer supports Gemini and Anthropic models with a planning agent that wields ReadFile, EditFile, Grep, and RunTerminalCmd tools, plus file-attach chat context and LLM calls directly in terminals. An extension marketplace, GUI and CLI-based, adds language servers, debuggers, and themes, and vim mode plus DAP debugging round out the editing core. It is MIT-licensed, actively maintained, and aimed at developers who want a lightweight, extensible editor with built-in agentic assistance.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/biscuit.md)
