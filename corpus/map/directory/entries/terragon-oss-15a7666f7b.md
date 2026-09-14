# terragon-oss (`terragon-oss`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: terragon-labs
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=Autonomous, CLI, Web; install=git clone + pnpm install (prerequisites: Node.js v20+, pnpm v10.14.0+, Docker, Stripe CLI); also terragon-setup.sh script
- Model providers: Claude Code, OpenAI Codex, Amp, Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [terragon-labs/terragon-oss](../../repos/terragon-labs/terragon-oss.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Remote background agent orchestrator for coding CLIs in the cloud. Multi-agent support with sandbox isolation per agent. Seamless automatic git workflow (branches, commits, PRs). Local handoff via terry CLI. MCP server for task management. BYO subscriptions/API keys. Integrates with Slack/GitHub via @-mentions. Real-time task status streaming to browser. NOTE: This is a snapshot at time of shutdown (January 16, 2026), ...

(captured site page body (agents/terragon-oss.md), not a verified repo-code finding)
Terragon Labs operated a hosted service that ran coding CLIs such as Claude Code, Codex, Amp, and Gemini in cloud sandboxes, letting developers fire tasks at multiple agents in parallel and receive branches, commits, and pull requests automatically. After shutting the product down, the company published this repository — a single-snapshot Apache-2.0 monorepo (two commits) containing the web app, WebSocket broadcast service, docs site, sandbox provisioning, and the terry CLI for handing tasks back to a local environment. Features included per-agent sandbox isolation, automated git workflows, an MCP server for task management, Slack and GitHub integrations, and BYO subscriptions or API keys. Because the snapshot is explicitly provided as-is with no maintenance or completeness guarantees, it functions as a reference implementation of a background-agent orchestration platform rather than a live tool. Developers studying how such orchestrators are assembled, or forking the architecture, are its remaining audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/terragon-oss.md)
