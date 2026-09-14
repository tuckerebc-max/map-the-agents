# OH-MY-PI (`oh-my-pi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: can1357
- License: MIT
- Language: TypeScript, Rust
- Interface: platforms=CLI; install=curl -fsSL https://omp.sh/install | sh (macOS/Linux), brew install can1357/tap/omp, bun install -g @oh-my-pi/pi-coding-agent, nix run github:can1357/oh-my-pi, irm https://omp.sh/install.ps1 | iex (Windows), mise use -g github:can1357/oh-my-pi
- Model providers: 60+ providers including Anthropic, OpenAI/Codex, Google Gemini/Vertex, xAI, DeepSeek, Mistral, Groq, Cerebras, Bedrock, Azure, OpenRouter, Ollama, LM Studio, vLLM, LiteLLM, Cursor, GitHub Copilot, GitLab Duo, Devin
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [can1357/oh-my-pi](../../repos/can1357/oh-my-pi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Coding agent with the IDE wired in. Features 31 built-in tools including LSP-integrated edits, real debugger driving (lldb/dlv/debugpy), persistent Python/JS execution cells, in-process shell, browser and desktop control, 23 web search backends, GitHub as filesystem, memory/learning, code review with verdicts, hash-anchored edits, AST-based edits, collaboration sessions, and time-traveling stream rules for hooks.

(captured site page body (agents/oh-my-pi.md), not a verified repo-code finding)
oh-my-pi is a fork of Mario Zechner's Pi rewritten as a coding-first agent with IDE-grade plumbing wired into a terminal interface. About 80,000 lines of Rust implement grep, shell, AST editing, and PTY handling in-process, eliminating fork/exec from the hot path. Every file write passes through LSP validation, and a debugger drives lldb, delve, and debugpy over DAP. A task tool fans out workspace-isolated subagents returning schema-validated results, and regex-triggered stream rules abort and retry mid-token for course correction. It inherits MCP servers, rules, and skills already on disk from eight other agent formats, so switching tools requires no migration. Ten model routing roles plus fallback chains cover sixty-plus providers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/oh-my-pi.md)
