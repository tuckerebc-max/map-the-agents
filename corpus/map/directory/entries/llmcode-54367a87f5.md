# LLMCode (`llmcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: syscalldev
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=git clone + pip install -r requirements.txt
- Model providers: OpenAI-compatible API (configurable baseUrl and model)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [syscalldev/llmcode](../../repos/syscalldev/llmcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agentic terminal-based coding assistant that understands your codebase and helps you code faster via natural language commands (file ops, context gathering, AI assistance)

(captured site page body (agents/llmcode.md), not a verified repo-code finding)
LLMCode demonstrates how much of the Claude Code workflow a compact terminal REPL can reproduce: gather context with /context or /#, request changes in natural language, and write the result with /write or /append, with workspace navigation and configuration handled by further commands. Because any OpenAI-compatible endpoint works, it ran against DeepSeek-R1 and local Llama 3 servers as readily as OpenAI itself, with settings stored in ~/.llm_code_config.json. The repository describes itself as under active development and partially built with its own assistance, but work stalled at 11 commits, leaving a prototype rather than a maintained tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/llmcode.md)
