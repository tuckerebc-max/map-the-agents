# Tembo (`tembo`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Tembo
- License: Proprietary
- Language: unknown
- Interface: platforms=Autonomous; install=Cloud (app.tembo.io), macOS desktop app, or self-hosted on AWS/GCP/Azure/on-prem (air-gapped supported)
- Model providers: Claude, GPT, Gemini, Grok via bring-your-own agents (Claude Code, Codex, Cursor, OpenCode, Pi, Amp)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Production-error-to-PR autonomous dev agent (pivoted from Postgres)

(captured site page body (agents/tembo.md), not a verified repo-code finding)
Tembo spent its first years as a managed Postgres platform and has since pivoted the entire company to infrastructure for running coding agents. The product does not replace your agent; it hosts it — users bring Claude Code, Codex, Cursor, OpenCode, or Pi along with their model credentials, and Tembo supplies cloud environments that spin up in seconds, pause and resume, and scale to substantial memory and disk for heavy runs. Work arrives as background agents triggered by Slack messages, Linear or GitHub events, Sentry or Datadog alerts, schedules, or webhooks, with templates such as diagnosing new Sentry errors and opening fix PRs, plus foreground sessions for interactive work and a Tembo Review agent for automated PR review. Every run ends in a pull request or artifact for human approval, with audit logs, session memory, and 150+ integrations, and the platform is available as cloud, desktop app, or self-hosted deployment including air-gapped installs; the company holds SOC 2 Type II and ISO 27001/42001 certifications and reports shipping about half of its own code through the platform. Engineering teams that want unattended agents working tickets and production alerts with centralized visibility are the customers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tembo.md)
