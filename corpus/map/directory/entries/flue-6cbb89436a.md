# Flue (`flue`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: withastro
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Model-agnostic via provider/model string slugs (e.g. anthropic/claude-sonnet-4-6)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [withastro/flue](../../repos/withastro/flue.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=other, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Programmable TypeScript harness framework for building autonomous agents where the agent IS a function composed of hooks (useModel, useSandbox, useSkill, useTool). Not an SDK -- a programmable harness that gives any model the context and environment needed for autonomous work: durable sessions, secure sandboxes, skills, tools, MCP integration, observability, and multi-channel event ingestion. Deploys to Node.js, Cloudflare Workers, GitHub Actions, ...

(captured site page body (agents/flue.md), not a verified repo-code finding)
Flue's premise is that an agent should be defined in typed source code the way UIs are defined in React: a function annotated with 'agent' that declares its harness through hooks (useModel for the provider/model slug, useSandbox for execution isolation, useSkill and useTool for capabilities) and returns its instructions. The runtime supplies sessions, tools, filesystem access, durability with recovery, subagents, MCP support, and observability through OpenTelemetry, Braintrust, or Sentry, while deployment targets span Node.js, Cloudflare Workers, GitHub Actions, GitLab CI, and Render. Channels connect agents to Slack, Teams, Discord, and GitHub. Built within the Astro organization, it targets TypeScript teams who want agent behavior reviewable in code review rather than configured in YAML.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/flue.md)
