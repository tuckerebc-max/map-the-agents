# llama-vscode (`llama-vscode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ggml.ai
- License: unknown
- Language: unknown
- Interface: platforms=IDE; install=Install from the VS Code Marketplace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Local LLM-assisted code completion using llama.cpp

(captured site page body (agents/llama-vscode.md), not a verified repo-code finding)
The extension started as a local FIM completion client: it auto-installs llama.cpp, streams fill-in-the-middle suggestions from models such as Qwen2.5-Coder, and reuses a ring context of open and edited files so completion stays viable on CPU-only hardware. A later Llama Agent mode added a chat UI with nine built-in tools, MCP server tool support, custom JavaScript tools, and configurable loop counts, letting local models actually read and modify project files. Models load from ggml's Hugging Face presets or any local GGUF, and a Telegram bot interface plus deep links extend access beyond the editor. It targets developers who want editor AI without sending code to a cloud service; a sibling llama.vim plugin covers Vim and Neovim.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/llama-vscode.md)
