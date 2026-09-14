# VerbalCodeAi (`verbalcodeai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: vibheksoni
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=Clone repo + run setup_windows.bat (Windows) or setup_linux.sh (Linux/macOS); or pip install -r requirements.txt
- Model providers: Ollama, Google AI, OpenAI, Anthropic, Groq, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [vibheksoni/verbalcodeai](../../repos/vibheksoni/verbalcodeai.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered codebase navigation directly in terminal; local-first (Ollama) with privacy focus; intelligent code search via embeddings; agent mode with tool suite; MCP integration for Claude Desktop; git history analysis; memory system.

(captured site page body (agents/verbalcodeai.md), not a verified repo-code finding)
VerbalCodeAI exists for developers who would rather ask an unfamiliar codebase questions than grep through it, and who do not want that code leaving their machine. It indexes the project locally with embeddings, then answers natural-language questions through semantic search backed by grep and regex fallback; its agent mode adds a broad tool suite — file reading, directory trees, symbol lookup, cross-references, git history, a memory system, web search, and command execution — with an ask_buddy tool that solicits a second model's opinion. An MCP server wraps the HTTP API so Claude Desktop and Cursor can call ask_agent or trigger indexing as external tools, and chat mode streams answers with markdown rendering. Privacy-conscious developers and students running local Ollama models are the primary users; the project is a small hobby-scale effort (36 commits, no releases) with a website at verbalcode.xyz.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/verbalcodeai.md)
