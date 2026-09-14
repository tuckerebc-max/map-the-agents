# core-termux (`core-termux`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: DevCoreXOfficial
- License: MIT
- Language: Shell (Bash)
- Interface: platforms=IDE; install=curl -fsSL https://raw.githubusercontent.com/DevCoreXOfficial/core-termux/main/install.sh | bash
- Model providers: OpenAI-compatible (Cactus Engine, Ollama), Gemini, Qwen, Mistral
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [devcorexofficial/core-termux](../../repos/devcorexofficial/core-termux.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Turns Android/Termux into a complete dev workstation with 30+ AI coding agents, modular install/update/uninstall, project scaffolding, voice-to-agent, second-brain memory system, and local LLM inference — all from one \`core\` CLI.

(captured site page body (agents/core-termux.md), not a verified repo-code finding)
Coding agents assume a laptop, which leaves phone-first developers and tinkerers without a path to use them. core-termux is a modular package manager for Termux that closes that gap: a single \`core\` CLI installs and updates language toolchains, databases, editors, and - through its \`ai\` module - 35-plus coding agent CLIs including Claude Code, Codex, Gemini CLI, OpenCode, Kimi Code, and Hermes Agent, each selectable with install flags. Beyond packaging, it adds a small built-in agent backed by a local OpenAI-compatible endpoint (Gemma via the Cactus Engine) with plan and build modes, voice-to-agent input, and a \`core brain\` markdown store for cross-session memory. Modules cover languages, databases, Neovim, shell tooling, and project scaffolding for common frameworks. It runs only on Termux and serves Android users building a mobile development environment.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/core-termux.md)
