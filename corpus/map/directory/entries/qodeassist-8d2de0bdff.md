# QodeAssist (`qodeassist`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Palm1r
- License: GPL-3.0
- Language: C++, QML
- Interface: install=Via Qt Creator Extension Registry (add external repository URL) or manual plugin archive installation through Help -\> About Plugins
- Model providers: Ollama, llama.cpp, LM Studio, Anthropic Claude, OpenAI (Chat + Responses), Google Gemini, Mistral/Codestral, Qwen, DeepSeek, OpenRouter, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [palm1r/qodeassist](../../repos/palm1r/qodeassist.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered coding assistant plugin for Qt Creator providing code completion, chat, quick refactoring, and project-aware tool calling for C++ and QML; dual MCP server/client support; agent skills compatible with Claude Code/Cursor skill format. Winding down / maintenance-only; no new features, issues and PRs closed

(captured site page body (agents/qodeassist.md), not a verified repo-code finding)
QodeAssist fills a gap most AI coding tools ignore: native AI assistance inside Qt Creator for C++ and QML development. Its chat and quick-refactor modes drive project-aware tools — reading and editing files, searching, building and reading compiler diagnostics, running terminal commands with confirmation, and tracking multi-step work through a todo tool. Unusually for an IDE plugin, it works bidirectionally with MCP: it can serve its project context to external clients like Claude Code or Cursor, and consume tools from external MCP servers itself. It implements the open Agent Skills format, discovering skills from project and global .claude/skills directories compatible with the Claude Code ecosystem. Completion and chat models come from local runtimes (Ollama, llama.cpp, LM Studio) or cloud providers, with FIM completion trigger modes that control API spend. The author has placed the project in maintenance-only status, so it remains useful for Qt developers but is not gaining features.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qodeassist.md)
