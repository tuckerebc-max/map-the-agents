# Devx (`termux-devx`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: apvcode
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g termux-dev (Node.js \>= 20)
- Model providers: OpenRouter, Google Gemini, DeepSeek, Groq, Mistral, OpenAI, Anthropic, Alibaba, Ollama, LM Studio
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [apvcode/termux-dev](../../repos/apvcode/termux-dev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A coding agent built Android-first for Termux: PLAN mode asks requirements questions before any edits, AGENT mode runs autonomously, and a built-in live web server previews web apps on the phone via termux-open-url. Self-healing diagnostics auto-detect and fix TypeScript, JavaScript, Python, and Rust errors before finishing a turn.

(captured site page body (agents/termux-devx.md), not a verified repo-code finding)
Devx (npm package termux-dev) is a terminal AI coding agent whose primary target is Android via Termux, though it also runs on Windows, macOS, and Linux. Its dual-mode architecture separates an interactive PLAN-mode architect that asks requirements questions without touching code from an AGENT mode that performs autonomous file edits, terminal commands, and package installs, with Tab toggling between them and one-click plan approval. It supports multimodal vision via pasted screenshots, snapshot rollback, git commits with AI-generated semantic messages, a per-project memory bank, MCP server support, and a headless one-shot mode for CI/CD and Termux:Widget. The live web server on port 3000 auto-opens in the Android browser, making it practical to build and preview web apps entirely on a phone.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/termux-devx.md)
