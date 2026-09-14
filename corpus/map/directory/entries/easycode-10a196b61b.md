# EasyCode (`easycode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: OrionStarAI
- License: Apache-2.0
- Language: TypeScript
- Interface: install=npm install -g easycode-ai (also via yarn/pnpm), or build from source; VS Code extensions via .vsix installation
- Model providers: Google Gemini, OpenAI, OpenAI-compatible (Azure OpenAI, LM Studio, Ollama, Groq, Together AI), Anthropic Claude, custom OpenAI/Anthropic-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [orionstarai/easycode](../../repos/orionstarai/easycode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Formerly DeepV Code; highly customizable AI coding assistant that understands entire project context, acts as an autonomous agent with Shell/File/Web tools, persistent session management, and serves as an ACP orchestrator that can delegate tasks to local Claude Code or Codex installations

(captured site page body (agents/easycode.md), not a verified repo-code finding)
EasyCode (OrionStar, formerly DeepV Code) is a Claude Code-style terminal agent built in the open: it plans before editing via /plan, executes through built-in shell, filesystem, and web tools, and keeps sessions that can be saved, restored, and compressed. MCP servers provide project context and third-party tool access, a hooks mechanism injects custom logic at workflow nodes, and a self-hostable server variant lets teams run the backend themselves. Any OpenAI-compatible or Anthropic-format model works, including local Ollama or LM Studio endpoints, with costs paid directly to providers. It targets developers — particularly in the Chinese ecosystem — who want a customizable, self-hostable alternative to Claude Code or Codex.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/easycode.md)
