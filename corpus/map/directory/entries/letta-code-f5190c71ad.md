# Letta Code (`letta-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: letta-ai
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @letta-ai/letta-code
- Model providers: OpenAI,Anthropic,Z.ai
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [letta-ai/letta-code](../../repos/letta-ai/letta-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Stateful agent harness where agents self-improve by rewriting their own memory, skills, prompts, and harness; supports subagents, hooks, crons, and messaging integrations (Slack/Telegram/Discord).

(captured site page body (agents/letta-code.md), not a verified repo-code finding)
Letta Code applies the MemGPT research lineage (memory blocks, sleep-time compute) to coding: agents hold identity and experience in editable memory blocks, learn skills at global, project, and agent scope, and can rewrite their own prompts and even their harness through a mods mechanism. Memory is git-tracked and syncable to GitHub, /sleeptime runs periodic offline 'dreaming' to consolidate context, and /doctor audits memory health. Subagents, hooks, message search, and messaging integrations (Slack, Telegram, Discord) extend it beyond a single terminal session, with optional Letta Cloud for remote state and GitHub Actions. The harness is Apache-2.0 and free; the cloud layer is the paid part.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/letta-code.md)
