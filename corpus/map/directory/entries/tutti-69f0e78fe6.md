# tutti (`tutti`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: tutti-os
- License: Apache-2.0
- Language: Go
- Interface: install=binary
- Model providers: Anthropic, OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tutti-os/tutti](../../repos/tutti-os/tutti.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Real-time shared workspace where multiple AI coding agents (Claude Code, Codex, Hermes) collaborate and share context, files, and tasks seamlessly via 'Big @' cross-agent references and a control center.

(captured site page body (agents/tutti.md), not a verified repo-code finding)
Tutti targets the messenger role humans play between coding agents: without a shared surface, Codex cannot pick up Claude's output without losing context, and coordinating several agents means manual copy-paste. It provides a GUI-first, real-time workspace — no terminal required — where context, files, running tasks, and app outputs are shared across agents; 'Big @' references pull in past conversations or other agents' work, tasks coordinate agents across providers in parallel or sequence, and a control center centralizes conversations, approvals, and status. Both humans and agents can invoke workspace apps (image generation, UI/UX design, documentation, presentations), keeping outputs in the shared space. Teams and power users running Claude Code, Codex, or Hermes subscriptions use it; the open-source app runs locally for a single user, while Tutti · VM adds multi-user Rooms with cross-device access and localhost-preview sharing.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tutti.md)
