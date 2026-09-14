# atomcode (`atomcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: atomgit-atomcode
- License: MIT
- Language: Rust
- Interface: platforms=Autonomous; install=Official install script (curl/PowerShell), npm install -g @atomgit.com/atomcode, brew install --cask atomcode, or cargo install from source
- Model providers: Anthropic (Claude), OpenAI, DeepSeek, Zhipu (GLM), Qwen, SiliconFlow, Ollama, OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [atomgit-atomcode/atomcode](../../repos/atomgit-atomcode/atomcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source terminal AI coding agent written in Rust; 100% AI-generated codebase (human acts only as product manager). Includes MCP support, plugin marketplace, hooks, plan/build modes, Web UI, mobile remote access via QR code, code-graph tools, and multi-provider support - all terminal-native.

(captured site page body (agents/atomcode.md), not a verified repo-code finding)
atomcode is a terminal AI coding agent written in Rust, positioned as an open-source alternative to Claude Code and notable for being developed with 100% AI-generated code under human product management. It connects to any OpenAI-compatible API (Claude, OpenAI, DeepSeek, GLM, Qwen, SiliconFlow, Ollama), reads the codebase, edits files, runs commands, and verifies work autonomously with loop detection and step budgets. Plan mode separates read-only exploration from full execution, plus /goal autonomous looping, background sessions, an /undo file-history mechanism, a Web UI, and mobile access via QR code. MCP support, a plugin marketplace, hooks, and a skills system extend the agent, with project instructions via .atomcode.md or AGENTS.md. It is MIT-licensed, actively developed (v5.x), installable via npm, Homebrew, or install scripts, and targets developers wanting a self-hostable agent with any OpenAI-compatible provider.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/atomcode.md)
