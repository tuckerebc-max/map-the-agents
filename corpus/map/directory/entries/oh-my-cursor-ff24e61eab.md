# oh-my-cursor (`oh-my-cursor`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tmcfarlane
- License: MIT
- Language: Markdown config, shell scripts
- Interface: platforms=IDE; install=curl -fsSL https://raw.githubusercontent.com/tmcfarlane/oh-my-cursor/main/install.sh | bash (macOS/Linux); irm https://raw.githubusercontent.com/tmcfarlane/oh-my-cursor/main/install.ps1 | iex (Windows)
- Model providers: Cursor model pool (composer-2.5-fast, claude-opus-4.8-thinking-high, gemini-3.1-pro, claude-4.6-opus-high-thinking, claude-4.6-sonnet-medium-thinking, claude-fable-5-thinking-high, gpt-5.3-codex-high-fast, gpt-5.5-medium, kimi-k2.5)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [tmcfarlane/oh-my-cursor](../../repos/tmcfarlane/oh-my-cursor.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Avatar: The Last Airbender-themed 8-agent team; pure Markdown config with zero runtime/CLI wrapper; per-agent model routing; hooks that deterministically block destructive commands and bad commits; Cactus Juice swarm mode (up to 10 parallel workers); cross-tool support (Cursor/Claude Code/Codex)

(captured site page body (agents/oh-my-cursor.md), not a verified repo-code finding)
oh-my-cursor turns Cursor's native subagent system into a themed eight-agent team using only Markdown configuration files, hooks, and slash commands — no plugin system or external runtime. Each specialist agent routes to a specific model chosen for its role, such as a multimodal model for image generation work. An orchestrator rule keeps the root thread dispatching while specialists execute, and cactus-juice swarm mode spawns up to ten parallel workers. Hooks deterministically block destructive shell commands and low-quality commits, while a permissions policy reduces approval prompts. The same files can also install for Claude Code and Codex, and a validation culture with per-build model-slug verification guards against Cursor's silent model downgrade behavior.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/oh-my-cursor.md)
