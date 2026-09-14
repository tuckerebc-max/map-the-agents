# DenchClaw (`denchclaw`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: DenchHQ
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop; install=npx denchclaw@latest bootstrap (Node 22+)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [denchhq/denchclaw](../../repos/denchhq/denchclaw.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): MIT-licensed framework that boots a dedicated OpenClaw gateway profile ('openclaw --profile dench') with its own gateway (~/.openclaw-dench, port 19001) and web UI (localhost:3100) for CRM automation and outreach agents; installed via npx denchclaw bootstrap with a Dench API key; 1.6k+ stars; maker now points users to dench.com, whose hosted product is $99/seat/month.

(captured site page body (agents/denchclaw.md), not a verified repo-code finding)
DenchClaw repackages the OpenClaw local-agent runtime into a personal CRM: contacts live in object tables, agents browse the web through your Chrome profile, answer questions by generating SQL against a local DuckDB, and update kanban pipelines automatically. Bootstrap provisions a separate OpenClaw gateway profile so DenchClaw coexists with a vanilla OpenClaw install, and skills from the Skills Store extend what agents can do. Scheduled 'Routines' run cron-style automations such as weekly reports or lead enrichment. It targets solo operators and small teams doing sales and outreach work who want agent automation on their own machine rather than a hosted SaaS.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/denchclaw.md)
