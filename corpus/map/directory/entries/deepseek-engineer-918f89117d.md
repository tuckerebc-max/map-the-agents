# deepseek-engineer (`deepseek-engineer`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Doriandarko
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: DeepSeek
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [doriandarko/deepseek-engineer](../../repos/doriandarko/deepseek-engineer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A coding assistant using native function calling with DeepSeek-R1 (DeepSeek-Reasoner), featuring visible Chain-of-Thought reasoning, automatic file operations, triple-stream processing (reasoning + content + tool calls), and built-in security features like path normalization and binary file detection.

(captured site page body (agents/deepseek-engineer.md), not a verified repo-code finding)
deepseek-engineer is a compact Python CLI that turns DeepSeek's reasoning models into a coding assistant: the model calls read_file, create_file, and edit_file functions natively, with the distinctive trait that DeepSeek-Reasoner's chain-of-thought streams visibly in the terminal while tool calls execute. Context is supplied either automatically (the assistant reads files it references) or manually via an /add command, and safety comes from path normalization, traversal protection, file-size limits, and binary detection. The project drew around 2,000 stars as a reference for wiring R1-style reasoning models to file tools but stopped receiving commits, with 26 commits total and a handful of open issues. It suits users studying function-calling agent design more than teams needing a maintained tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deepseek-engineer.md)
