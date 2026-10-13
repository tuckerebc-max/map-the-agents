# GitHub Copilot CLI (`github-copilot-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: github
- License: Source Available
- Language: Shell
- Interface: platforms=CLI; install=curl -fsSL https://gh.io/copilot-install | bash
- Model providers: Claude Sonnet 4.5, Claude Sonnet 4, GPT-5
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [github/copilot-cli](../../repos/github/copilot-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-native synchronous AI agent powered by the same agentic harness as GitHub's Copilot coding agent; deep GitHub workflow integration (repos, issues, PRs via natural language); MCP extensibility; LSP support for code intelligence; full user control with action preview before execution; cross-platform.

(captured site page body (agents/github-copilot-cli.md), not a verified repo-code finding)
Copilot CLI moves GitHub's coding agent from github.com and IDEs into the terminal, where developers already work. It plans and executes tasks locally with explicit approval before each action, talks to repositories, issues, and pull requests in natural language, and ships the GitHub MCP server by default with custom MCP servers supported for extension. Language Server Protocol integration supplies go-to-definition, hover, and diagnostics beyond plain text, and model selection covers Claude Sonnet 4.5 (default), Sonnet 4, and GPT-5, with an experimental Autopilot mode that keeps working until a task completes. It requires an active Copilot subscription, with each prompt consuming a premium request from the monthly quota.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/github-copilot-cli.md)
