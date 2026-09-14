# OpenCode (`opencode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: anomalyco
- License: MIT
- Language: TypeScript, JavaScript (Node.js, Bun, Turborepo monorepo)
- Interface: platforms=CLI; install=curl -fsSL https://opencode.ai/install | bash; or npm/bun/pnpm/yarn install -g opencode-ai; or brew install opencode-ai; or scoop/choco/pacman/paru/mise/nix; or download desktop app from releases
- Model providers: Any LLM provider (via API key configuration); curated tested models via OpenCode Zen
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: yes (yes)
  - plan_mode: True (reported)

Repository map entry: [anomalyco/opencode](../../repos/anomalyco/opencode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fully open-source AI coding agent with both terminal UI and beta desktop app; built-in switchable agents (build/plan) via Tab key - the plan agent is read-only, denies file edits, and asks permission before bash commands; @general subagent for complex searches/multistep tasks; MCP server support; plugin system; 20+ language README translations; broad package manager support across all major OSes. Major project ...

(captured site page body (agents/opencode.md), not a verified repo-code finding)
OpenCode positions itself as the fully open-source alternative to closed terminal coding agents, MIT-licensed and hosted under the anomalyco organization after starting in the sst org. Its architecture separates a client/server core from every interface: the same agent serves the terminal UI, a beta desktop app, IDE extensions, and third-party clients, which is why an ecosystem of plugins, Neovim integrations, Android clients, and orchestrators has grown around it. Built in TypeScript on Bun, it exposes built-in build and read-only plan agents switchable with Tab, a @general subagent, and hooks plus plugin and config surfaces documented at opencode.ai/docs. Distribution is unusually broad — curl script, npm, Homebrew, scoop, choco, pacman, AUR, mise, nix — and the project shows 202k stars, 26k forks, and 15,600 commits. It serves developers who want a Claude Code-class terminal agent with no vendor lock-in.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode.md)
