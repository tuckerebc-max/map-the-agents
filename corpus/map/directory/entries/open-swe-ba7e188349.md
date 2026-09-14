# Open SWE (`open-swe`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: langchain-ai
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, Web; install=Local dev setup (backend + dashboard), Docker, or macOS desktop beta
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [langchain-ai/open-swe](../../repos/langchain-ai/open-swe.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source replica of the internal coding-agent architecture used by Stripe (Minions), Ramp (Inspect), and Coinbase (Cloudbot); built on LangGraph + Deep Agents; isolated cloud sandboxes, multi-channel invocation (Slack/Linear/GitHub), auto PR creation, server-side MCP for observability with security boundaries.

(captured site page body (agents/open-swe.md), not a verified repo-code finding)
Several frontier companies built internal coding agents — Stripe's Minions, Ramp's Inspect, Coinbase's Cloudbot — but published none of the architecture. Open SWE reconstructs that pattern as an open-source framework on LangGraph and Deep Agents: tasks arrive from Slack, Linear, or GitHub, run in isolated cloud sandboxes (Modal, Daytona, Runloop, E2B, or custom), spawn child agents through the Deep Agents task tool for parallel subtasks, and end in a pull request. Middleware hooks around the agent loop inject mid-run messages, alert Slack when step limits hit, and wrap tool errors, while optional server-side MCP integrations (Datadog, Corridor guardrails) keep observability credentials out of the sandbox. Sandboxes, models, triggers, and system prompts are all customizable per deployment, and per-user model settings live in the web dashboard. Engineering teams self-hosting an internal coding agent in the style of those proprietary systems are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-swe.md)
