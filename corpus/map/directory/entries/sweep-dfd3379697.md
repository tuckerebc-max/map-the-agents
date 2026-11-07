# Sweep (`sweep`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: sweepai
- License: MIT (Free Software) + Enterprise Edition (EE License)
- Language: Python
- Interface: platforms=IDE, Web; install=jetbrains
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [sweepai/sweep](../../repos/sweepai/sweep.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Originally a GitHub-app AI coding assistant; pivoted to an AI coding assistant for JetBrains IDEs, distributed as a JetBrains plugin. Dual-licensed: MIT for the free software portion, EE License for the enterprise portion.

(captured site page body (agents/sweep.md), not a verified repo-code finding)
Sweep began in 2023 as a GitHub app that behaved like a junior developer: assign it an issue and it planned changes, edited files across the repository, and opened a draft pull request for review. That workflow ran on GPT-4 with a repo-map and sandboxed validation loop, and the project drew roughly 7.7k stars as one of the first open-source autonomous-PR agents. The team subsequently pivoted to building an AI coding assistant distributed as a JetBrains Marketplace plugin, leaving the original GitHub-app codebase without active development while sweep.dev now points at the plugin. The repository remains available under a dual license — MIT for the free components with an Enterprise Edition license covering commercial parts — and is still referenced as a reference implementation of issue-to-PR automation. JetBrains users wanting an agent inside IntelliJ-based IDEs are its current audience.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/sweep.md)
