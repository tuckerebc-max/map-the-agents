# Qwen Code (`qwen-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: QwenLM
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=Standalone install scripts (Linux/macOS/Windows), npm install -g @qwen-code/qwen-code@latest (requires Node.js 22+), brew install qwen-code
- Model providers: OpenAI, Anthropic, Gemini, Qwen APIs, any third-party provider or local model (Ollama/vLLM)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [qwenlm/qwen-code](../../repos/qwenlm/qwen-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Feature-rich agentic coding assistant with auto-memory, auto-skills, subagents, agent teams, MCP support, plan mode, hooks, LSP integration, Git worktrees, and computer use for desktop automation. Multiple interaction modes: interactive terminal UI, headless mode, IDE plugins (VS Code, JetBrains, Zed), desktop app, daemon mode, and IM bot channels.

(captured site page body (agents/qwen-code.md), not a verified repo-code finding)
Qwen Code is Alibaba's open-source terminal coding agent, forked from Gemini CLI v0.8.2 and developed independently since, with the explicit goal of matching Claude Code's capabilities while running on any model provider. It supports subagents, hooks, plan mode, MCP, skills, and agent teams, with providers — OpenAI, Anthropic, Gemini, Qwen, or local Ollama/vLLM models — switchable at runtime rather than fixed at install. The project extends beyond the terminal into IDE plugins, a desktop app, SDKs, a daemon mode exposing a shared agent session over HTTP+SSE, and IM bots for Telegram, DingTalk, WeChat, and Feishu. Its development is partly self-referential: the team runs its own agent to file issues, submit pull requests, review code, and run tests on the codebase itself. An Agent Arena runs multiple models head-to-head on the same task, and headless mode supports CI pipelines. Developers who want a Claude Code-shaped tool without vendor lock-in use it across Qwen and non-Qwen models alike.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qwen-code.md)
