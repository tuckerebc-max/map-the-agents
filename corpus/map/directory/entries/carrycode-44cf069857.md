# carrycode (`carrycode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: zhangliang605
- License: Custom (source-available; commercial use allowed but prohibits modifying Logo/Banner/identifying marks without permission)
- Language: Rust and TypeScript
- Interface: platforms=CLI, IDE; install=curl -fsSL https://carrycode.ai/install.sh | sudo sh (macOS/Linux) or irm https://carrycode.ai/install.ps1 | iex (Windows); VSCode Extension marketplace search 'carrycode'; build from source using Rust, Node.js, Bun
- Model providers: OpenAI, Anthropic, Google Gemini, DeepSeek, Moonshot/Kimi, ZhipuAI, MiniMax, Alibaba Cloud, xAI, SiliconFlow, Ollama, vLLM, any OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [zhangliang605/carrycode](../../repos/zhangliang605/carrycode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native AI coding agent connecting to 17+ LLM providers with beautiful terminal UI (themes, syntax highlighting, code diff previews, Mermaid diagram rendering). Supports MCP protocol (via /mcp), VSCode extension plugin, AGENTS.md project instructions, LSP diagnostics integration, smart context compaction, Skills system compatible with Claude Code, SkillHub integration (Tencent), approval modes for autonomy control. Dual Build and Plan modes.

(captured site page body (agents/carrycode.md), not a verified repo-code finding)
carrycode is a terminal-first coding agent built in Rust with a TypeScript layer, aimed at developers who live in the shell and want agent capability without leaving it. It renders a rich TUI with themes, syntax-highlighted diffs, and Mermaid diagrams rendered as ASCII, and supports MCP servers, a skills system compatible with Claude Code, AGENTS.md project rules, LSP diagnostics, and context compaction for long sessions. Agent autonomy is governed through explicit modes — a read-only Plan mode for analysis and a Build mode gated by approval levels — and a single-shot CLI mode supports scripting. Model access spans 17+ providers (OpenAI, Anthropic, Gemini, DeepSeek, Kimi, GLM, MiniMax, Qwen, xAI, SiliconFlow, Ollama, vLLM, and OpenAI-compatible endpoints). The project is source-available under a custom license, installs via curl or a VS Code extension, and is actively maintained with frequent releases; a VS Code extension extends the same engine into the editor.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/carrycode.md)
