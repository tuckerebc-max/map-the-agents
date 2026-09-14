# PrivateCode (`privatecode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Legorobotdude
- License: MIT
- Language: Python 3.6+
- Interface: install=git clone; pip install -r requirements.txt; ensure Ollama running locally; ollama pull codellama
- Model providers: Ollama (local LLMs only)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [legorobotdude/privatecode](../../repos/legorobotdude/privatecode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Privacy-first terminal coding assistant (VibeCoder) running entirely on local Ollama models with no data sent to external services; uses DuckDuckGo for untracked web searches and URL content extraction; partial file reading with line ranges for token efficiency; intelligent file editing with diff preview; safe command execution; AI thinking blocks (toggleable reasoning display); plan:/vibecode: mode breaks complex tasks into executable JSON-formatted ...

(captured site page body (agents/privatecode.md), not a verified repo-code finding)
PrivateCode exists for developers who want AI coding help without sending proprietary code to a cloud provider. It runs entirely against local Ollama models, with DuckDuckGo search and URL extraction as the only optional external calls, chosen because that engine does not track queries. Work happens through explicit commands — search:, edit:, run:, create:, plan: — and the vibecode mode decomposes a task into JSON steps that execute one at a time with user approval, so nothing runs without review. Edits produce .bak backups and colored diff previews, and dangerous command prefixes trigger warnings before execution. It is a single-file Python tool aimed at developers on offline machines or anyone unwilling to leak code to hosted models.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/privatecode.md)
