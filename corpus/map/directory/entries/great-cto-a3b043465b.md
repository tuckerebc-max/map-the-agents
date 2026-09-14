# great_cto (`great-cto`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: avelikiy
- License: MIT
- Language: JavaScript
- Interface: platforms=CLI, IDE; install=npx great-cto init
- Model providers: Claude (Anthropic), OpenAI Codex
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [avelikiy/great_cto](../../repos/avelikiy/great_cto.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Orchestration layer that sits on top of coding agents (Claude Code, OpenAI Codex) to automate the full software development lifecycle using a pipeline of 69 specialist agents (architect, senior-dev, code-reviewer, QA, security, devops, etc.). User intervenes only at two approval gates: design and deploy. Ships as a Claude Code plugin (.claude-plugin), includes an mcp-servers directory, 60 known product archetypes across ...

(captured site page body (agents/great-cto.md), not a verified repo-code finding)
great_cto turns a single developer's coding agent into an assembly line for whole products. Installed as a plugin, it drives Claude Code or OpenAI Codex through a fixed sequence — architecture, data model, backend, frontend, tests, deployment — with 69 specialist agents whose scopes are enforced at write time so a stage's agent cannot modify files outside its brief. Each stage hands its output to a second model for verification, which returns a verified, rework, or unverifiable verdict before downstream work proceeds. A self-updating board on localhost:3141 shows pipeline state, pending gates, and per-session cost, and three human approval gates (product, plan, deploy) are configurable from product-only through fully automatic, with compliance gates never skipped. The developer stays in the loop at gates while the pipeline runs, and the project publishes cost benchmarks alongside its releases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/great-cto.md)
