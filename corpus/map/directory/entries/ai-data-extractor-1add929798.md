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

Repository map entry: [bawadou/ai-data-extractor](../../repos/bawadou/ai-data-extractor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Extracts local chat history from 10 AI coding assistants (Claude Code, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, Aider, Codex CLI) into a single normalized JSONL format for fine-tuning/analytics/backup; auto-discovers data across OSes; zero dependencies; extensible two-function interface.

(captured site page body (agents/ai-data-extractor.md), not a verified repo-code finding)
Local assistant databases are scattered across platform-specific paths and formats, and they get cleared or lost when apps update. This toolkit auto-discovers storage on macOS, Linux, and Windows, and extracts messages, code context, diffs, tool calls, timestamps, and model names into timestamped JSONL files with a shared schema (guaranteed fields: messages, source, session_id). It handles ten assistants — Claude Code, Codex CLI, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, and Aider — using line-by-line JSON parsing and read-only SQLite connections so running apps are not disturbed, and corrupt files yield partial results instead of failures. A --merge flag produces a single HuggingFace-datasets-ready file for fine-tuning or analytics. It runs on the Python standard library alone, with per-assistant extractors that also run standalone.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ai-data-extractor.md)
