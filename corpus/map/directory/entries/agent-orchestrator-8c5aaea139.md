# agent-orchestrator (`agent-orchestrator`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: willynikes2
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=git clone + pip install -r requirements.txt + python3 daniel.py --setup
- Model providers: Anthropic (Claude), OpenAI (Codex/GPT), Google (Gemini)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [willynikes2/agent-orchestrator](../../repos/willynikes2/agent-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Terminal-based multi-agent orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover (next-man-up); agents share context via a knowledge base server; routes messages through configurable role chains

(captured site page body (agents/agent-orchestrator.md), not a verified repo-code finding)
Three CLI subscriptions cover most frontier models, but each has separate quotas, and hitting one mid-task means losing momentum, so this orchestrator wraps the Claude, Codex, and Gemini CLIs and fails over automatically — when one agent hits a cap or errors, the next in the role chain continues the work. It is deliberately minimal: a single Python file (daniel.py, about 1,100 lines) with role-based routing chains (orchestrator, implementation, ui-docs, review), direct addressing like @claude or @codex, cooldown timers on exhausted agents, and an optional knowledge-base server for shared context. New agents are added by writing roughly 30-line wrapper functions. Solo developers running all three ~$20/month CLI subscriptions are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agent-orchestrator.md)
