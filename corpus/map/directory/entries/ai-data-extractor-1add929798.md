# ai-data-extractor (`ai-data-extractor`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: bawadou
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE; install=python extract.py (Python 3.9+, no dependencies)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Extracts local chat history from 10 AI coding assistants (Claude Code, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, Aider, Codex CLI) into a single normalized JSONL format for fine-tuning/analytics/backup; auto-discovers data across OSes; zero dependencies; extensible two-function interface.

(captured site page body (agents/ai-data-extractor.md), not a verified repo-code finding)
Local assistant databases are scattered across platform-specific paths and formats, and they get cleared or lost when apps update. This toolkit auto-discovers storage on macOS, Linux, and Windows, and extracts messages, code context, diffs, tool calls, timestamps, and model names into timestamped JSONL files with a shared schema (guaranteed fields: messages, source, session_id). It handles ten assistants — Claude Code, Codex CLI, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, and Aider — using line-by-line JSON parsing and read-only SQLite connections so running apps are not disturbed, and corrupt files yield partial results instead of failures. A --merge flag produces a single HuggingFace-datasets-ready file for fine-tuning or analytics. It runs on the Python standard library alone, with per-assistant extractors that also run standalone.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/ai-data-extractor.md)
