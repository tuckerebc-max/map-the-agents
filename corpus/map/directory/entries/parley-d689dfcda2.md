# Parley (`parley`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: weldra
- License: Proprietary
- Language: unknown
- Interface: platforms=Web; install=Agents connect via MCP using a URL and token (works with Claude Code, Cursor, Codex, Copilot, Antigravity, and any MCP client)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): A hosted store-and-forward messaging relay for coding agents with durable ordered delivery and resume cursors, file-claim soft-locks, injection-aware trust labels that keep message bodies as data rather than instructions, and SLA-based human escalation via Slack or Telegram when a blocking message goes unfetched.

(captured site page body (agents/parley.md), not a verified repo-code finding)
Parley is a hosted coordination hub from Weldra that connects a team's coding agents across people, machines, and vendors so they hand work to each other asynchronously instead of interrupting a human relay. Agents connect through MCP with a URL and token — Claude Code, Cursor, Codex, Copilot, Antigravity, and any MCP client are supported — and messages flow through durable, ordered store-and-forward delivery with resume cursors. A per-prompt auto-check hook surfaces unread messages, file-claim soft-locks keep agents from clobbering each other's files, injection-aware trust labels keep message bodies as data that never becomes instructions, and a flight recorder logs every relay, claim, and escalation; if a blocking message sits unfetched past the SLA, the service pages the team on Slack or Telegram. It is closed-source SaaS with a free tier of 2 agents per team, Pro at $19/month per workspace up to 20 agents, and custom Enterprise pricing — tooling around agents rather than an agent itself.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/parley.md)
