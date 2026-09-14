# Smelt (`smelt`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: leonardcser
- License: MIT
- Language: Rust
- Interface: platforms=Autonomous, CLI, IDE; install=Prebuilt binaries from GitHub Releases or cargo install --git https://github.com/leonardcser/smelt.git smelt-agent
- Model providers: OpenAI, Anthropic, OpenRouter, Ollama, GitHub Copilot, Kimi Code
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [leonardcser/smelt](../../repos/leonardcser/smelt.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Small, fast, Lua-scriptable AI coding agent for the terminal (scriptable like Neovim). Custom terminal renderer (not ratatui). Built-in Vim editor (motions, text objects, registers, undo). Deterministic fuzzing with fixed clock and stubbed I/O for replayable crashes. No config needed. Mode cycle: Normal -\> Plan -\> Apply -\> Yolo.

(captured site page body (agents/smelt.md), not a verified repo-code finding)
Smelt exists because its author found mainstream coding agents bloated and wanted the extensibility model of Neovim applied to an agent: keymaps, commands, autocmds, custom tools, and modes are all defined in Lua, with bundled plugins for which-key, an LSP-backed semantic code toolset, and a local request inspector. The Rust core uses a custom grid renderer, ships a built-in Vim editor with motions, text objects, registers, and undo, and cycles through Normal, Plan, Apply, and Yolo modes. Development is tested with deterministic fuzzing — stubbed I/O, fixed clocks, replayable failures — rather than ad hoc integration tests. Authentication covers subscription providers (ChatGPT, GitHub Copilot, Kimi Code) alongside any OpenAI-compatible endpoint, and the README warns that interfaces shift between alpha releases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/smelt.md)
