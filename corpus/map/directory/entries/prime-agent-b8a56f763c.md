# Prime Agent (`prime-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: PrimeIntellect-ai
- License: MIT
- Language: TypeScript (TUI), Python (agent runtime)
- Interface: platforms=Autonomous, CLI, IDE; install=binary
- Model providers: subscription and API-key (BYOK) providers via /login
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (skills as importable Python packages) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (rlm(...) spawns child agents for parallel/background work) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [primeintellect-ai/prime-agent](../../repos/primeintellect-ai/prime-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Uses a Recursive Language Model (RLM) that treats context as variables and tools as function calls in a persistent IPython REPL, combined with a Continual Harness that self-improves via /refine — persisting lessons, memories, and reusable subagent specifications as durable state across sessions.

(captured site page body (agents/prime-agent.md), not a verified repo-code finding)
Prime Agent exists because long tasks break harnesses that hold all context in a shrinking window: it instead puts the model in a persistent IPython REPL where the prompt is a variable, tools are functions, and rlm(...) spawns child agents that run in parallel and message each other directly without routing through the user. Everything is programmatic — file operations, shell commands, context management — which makes the agent's behavior inspectable and composable rather than a sequence of opaque tool calls. A Continual Harness accumulates what works across a session, and /refine reviews the trajectory and applies small evidence-backed updates to memories, skills, and subagent specs, with snapshots for rollback and the base prompt left untouched. Sessions are daemon-backed with heartbeats, schedules, persistent goals, and a bounded autonomous mode with quality gates. Prime Intellect built it for long-running research and evaluation work alongside its Verifiers and PRIME-RL stack, and the README warns plainly that it is not a security sandbox.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/prime-agent.md)
