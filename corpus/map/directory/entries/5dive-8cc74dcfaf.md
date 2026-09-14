# 5dive (`5dive`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: 5dive-ai
- License: MIT
- Language: Bash
- Interface: platforms=IDE; install=curl -fsSL https://install.5dive.ai | sudo bash; then sudo 5dive init (Linux with systemd required)
- Model providers: Anthropic Claude, OpenAI Codex, Google Antigravity, xAI Grok, Cognition Devin, OpenRouter, DeepSeek, Moonshot/Kimi, Qwen, Z.ai/GLM
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: no (no)

Repository map entry: [5dive-ai/5dive](../../repos/5dive-ai/5dive.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Runs a 'company of AI agents' on a Linux server you own - each agent is its own Linux user running an official agentic AI CLI as a systemd service, coordinating through a shared bash CLI and SQLite task queue; pings your phone via Telegram only when a human decision is needed.

(captured site page body (agents/5dive.md), not a verified repo-code finding)
5dive exists for people who want a fleet of coding agents working unattended on hardware they control, without adopting a proprietary platform. Installation is a curl script plus 5dive init on any systemd Linux box; each named agent becomes its own Linux user running an official agent CLI (claude, codex, antigravity, grok, devin, hermes, opencode, pi, and others) as a systemd service, coordinating through a shared bash CLI and SQLite task queue. Agents sit on an org chart, hand off tasks through a shared backlog, and hit human approval gates when work needs a decision — the only moment a Telegram ping reaches the owner. Self-hosting engineers and small teams running long-lived autonomous agents are the users, with a managed option at 5dive.ai.
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json); [site page @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/agents/5dive.md)
