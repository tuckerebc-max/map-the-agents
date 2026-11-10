# Verdent (`verdent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: verdent
- License: Proprietary
- Language: Kotlin
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: Anthropic, Google Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: yes (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): All-in-one coding agent orchestrating top-tier AI models; high SWE-bench Verified score

(captured site page body (agents/verdent.md), not a verified repo-code finding)
Verdent exists to bring autonomous task execution into IntelliJ-family IDEs for professional developers who need more than autocomplete: given a task, it analyzes the codebase, produces a structured plan for review, and then executes multi-step workflows with approval gates on every consequential action. A subagent architecture handles exploration, verification, and code review separately from the primary agent, and scoped checkpoints make every change reviewable — Review Changes diffs show exactly what a turn altered, with rollback available; bash approval dialogs guard dangerous commands, and temp-directory writes are handled carefully to avoid spurious prompts. Codebase context is gathered locally with bundled ripgrep and fd, so code does not leave the machine without explicit action. Professional developers in IntelliJ-family IDEs use it for refactoring, debugging, test generation, and documentation; it is distributed through the JetBrains Marketplace, requires a Verdent account, and updates every few weeks.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/verdent.md)
