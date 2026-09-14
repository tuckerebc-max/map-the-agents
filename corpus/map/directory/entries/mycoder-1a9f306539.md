# MyCoder (`mycoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bhouston
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g mycoder
- Model providers: Anthropic Claude, OpenAI, Ollama (local)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: yes (yes)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [bhouston/mycoder](../../repos/bhouston/mycoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An open-source Claude Code alternative with distinctive GitHub-native automation: agents trigger from issue comments via /mycoder, run with githubMode for issue-and-PR workflows, spawn parallel subagents with color-coded hierarchical logging, and accept mid-run human corrections interactively; MIT-licensed, npm-installable, and developed in a monorepo with Playwright browser automation built in.

(captured site page body (agents/mycoder.md), not a verified repo-code finding)
MyCoder packages a Claude Code-style terminal agent behind a one-command npm install, with defaults tuned to get developers productive immediately. Its distinguishing surface is GitHub integration: with githubMode enabled, the agent works directly against issues and pull requests, and a /mycoder comment on an issue triggers a headless run that implements and opens a PR, turning issue triage into delegated automation. Subagents run in parallel for concurrent task processing, message compaction keeps long sessions inside the context window, and an interactive correction channel lets a developer redirect a running agent mid-task — a pattern borrowed from how parent agents message subagents. Model configuration spans Anthropic, OpenAI, and local Ollama endpoints, with MCP supplying external tools and context sources. The project maintains conventional-commit release automation through a pnpm monorepo, publishes continuously to npm, and targets developers who want GitHub workflow integration — comment-triggered PRs, issue-driven automation — rather than a purely local REPL.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mycoder.md)
