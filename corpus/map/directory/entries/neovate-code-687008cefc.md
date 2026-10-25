# Neovate Code (`neovate-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: neovateai
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @neovate/code
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: False (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [neovateai/neovate-code](../../repos/neovateai/neovate-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Coding agent for generating code, fixing bugs, reviewing code, and adding tests, with both interactive and headless modes and a VSCode extension.

(captured site page body (agents/neovate-code.md), not a verified repo-code finding)
Neovate Code is a terminal coding agent that proposes edits and tool calls for approval before applying them. Developers pick a provider and model through slash commands, and API keys are read from standard environment variables for every supported provider, avoiding lock-in to one vendor. Work spans code generation, bug fixing, code review, test writing, refactoring, and query optimization. The same npm package covers macOS, Linux, and Windows, and the pnpm monorepo includes an e-commerce-grade test suite with end-to-end tests and a bundled ripgrep. A VS Code extension in the repository brings the agent into the editor alongside the CLI.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/neovate-code.md)
