# context-hub (`context-hub`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: andrewyng
- License: MIT
- Language: JavaScript
- Interface: install=npm
- Model providers: None (a CLI serving markdown documentation; no model inference)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (agent skills via SKILL.md files) (yes)
  - claude_code_plugin: yes (drop SKILL.md into ~/.claude/skills/) (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [andrewyng/context-hub](../../repos/andrewyng/context-hub.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Provides curated, versioned API documentation as open markdown that coding agents can fetch via CLI, reducing API hallucinations. Enables self-improving agents through local annotations that persist across sessions and community feedback (up/down ratings) that flows back to doc authors.

(captured site page body (agents/context-hub.md), not a verified repo-code finding)
Coding agents hallucinate APIs because their training data lags current library versions, and pasting entire documentation sites into context wastes tokens. Context Hub maintains curated, versioned API documentation as plain markdown in a git repository: an agent searches the catalog, fetches exactly the pages needed for its language and version, and writes correct calls against current APIs. Two feedback mechanisms make the corpus self-improving - agents leave local annotations that persist across sessions and are re-injected into later fetches, and users vote pages up or down so authors see which content needs fixing. Installation is a global npm package, and a SKILL.md lets Claude Code load it as a skill. Developers wiring agents to third-party APIs are the users, and the corpus grows through community pull requests.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/context-hub.md)
