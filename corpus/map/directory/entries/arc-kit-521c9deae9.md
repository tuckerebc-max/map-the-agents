# arc-kit (`arc-kit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tractorjuice
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: Claude Code, Gemini CLI, GitHub Copilot, OpenAI Codex CLI, OpenCode CLI, Mistral Vibe CLI, Kimi Code CLI
- Feature flags (directory-reported):
  - mcp_support: yes (bundles 6 MCP servers: AWS Knowledge, Microsoft Learn, Google Developer Knowledge, GovRepoScrape, uk-tenders, plus diagnostics) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [tractorjuice/arc-kit](../../repos/tractorjuice/arc-kit.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Enterprise architecture governance harness that transforms scattered architecture documents into systematic AI-assisted workflows covering the full lifecycle: principles, stakeholders, risk, business case, requirements, data modeling, research, procurement, design review, and compliance, with specialized compliance overlays for UK Government, EU, France, Netherlands, Austria, Canada, UAE, USA, and NHS clinical safety.

(captured site page body (agents/arc-kit.md), not a verified repo-code finding)
Enterprise architecture work is usually scattered across Word documents, Confluence pages, and slide decks with no systematic workflow, and arc-kit exists to give that material the same harness treatment coding gets. It installs as a Claude Code plugin (with Gemini, Copilot, Codex, OpenCode, Mistral, and Kimi CLI support) providing slash commands such as /arckit:principles and /arckit:requirements, 29 agent descriptors, 9 hooks, and 6 bundled MCP servers (AWS Knowledge, Microsoft Learn, Google Developer Knowledge, govreposcrape, uk-tenders). Commands map to a phase-by-phase lifecycle: principles, stakeholders, risk registers, Green Book business cases, requirements, research, procurement, design review, and compliance packs for UK, EU, NHS, and other jurisdictions. Artifacts stay under Git version control and are explicitly labeled as drafts for qualified review. It targets enterprise and government architects, with the UK MOD and public-sector compliance packs as its most distinctive deployments.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/arc-kit.md)
