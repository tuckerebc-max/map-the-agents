# junie (`junie`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: JetBrains
- License: Proprietary (JetBrains)
- Language: Shell
- Interface: platforms=CLI, IDE; install=curl -fsSL https://junie.jetbrains.com/install.sh | bash (macOS/Linux), Homebrew, or npm install -g @jetbrains/junie
- Model providers: Anthropic, OpenAI, Google, xAI, OpenRouter, Copilot
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: yes (yes)

Repository map entry: [jetbrains/junie](../../repos/jetbrains/junie.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): LLM-agnostic terminal-native AI coding agent by JetBrains; IDE/CI-CD integration; GitHub Action for auto-responding to issues/PRs/CI failures; multiple update channels (stable, EAP, nightly, experimental).

(captured site page body (agents/junie.md), not a verified repo-code finding)
This repository is the front door for Junie, JetBrains' LLM-agnostic coding agent — installer scripts for stable, EAP, nightly, and experimental channels, version registries, and issue tracking, while the agent implementation itself stays closed under JetBrains AI Service Terms. The agent runs in terminals, JetBrains IDEs, and CI: a GitHub Action lets Junie respond to issues, review PRs, and react to CI failures autonomously. Authentication goes through JetBrains Account, Junie API keys, or BYOK across Anthropic, OpenAI, Google, xAI, OpenRouter, and Copilot. Users track bugs via /feedback or GitHub issues, and the Discord community handles support alongside docs at junie.jetbrains.com/docs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/junie.md)
