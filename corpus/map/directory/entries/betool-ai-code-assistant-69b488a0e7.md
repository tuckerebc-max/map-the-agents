# betool - AI Code Assistant (`betool-ai-code-assistant`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: beTool IA
- License: unknown
- Language: unknown
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Bridges AI coding assistants with the IDE via a local server

(captured site page body (agents/betool-ai-code-assistant.md), not a verified repo-code finding)
betool addresses a specific gap: AI coding agents that propose edits outside the IDE have no native way to surface those changes inside JetBrains IDEs for review. The plugin runs a local server that receives code modification proposals from the betool CLI and presents them as interactive red/green diffs in a modal dialog, where each change is accepted or rejected with one click before being applied, with files backed up beforehand. It works across IntelliJ IDEA, WebStorm, PyCharm, GoLand, and other JetBrains IDEs, starts automatically with the project, requires no configuration, and falls back to terminal mode when IntelliJ is not running. The plugin is free; usage requires a betool.fr account and payment is by AI tokens consumed. It is aimed at JetBrains developers who want agent-proposed changes surfaced as in-IDE reviewable diffs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/betool-ai-code-assistant.md)
