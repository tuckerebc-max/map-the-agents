# little-coder (`little-coder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: itayinbarr
- License: Apache-2.0
- Language: TypeScript
- Interface: install=npm
- Model providers: llama.cpp, Ollama, LM Studio, Anthropic, OpenAI, local
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [itayinbarr/little-coder](../../repos/itayinbarr/little-coder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Coding agent tuned for small local models, built on pi, with plan mode, dispatch sub-coders, per-phase model selection, read-before-edit enforcement, and a lifecycle-hook extension system.

(captured site page body (agents/little-coder.md), not a verified repo-code finding)
Small local models fail at agentic coding mostly because harnesses assume frontier-model context discipline, so little-coder wraps the pi agent with extensions that enforce read-before-edit, gate permissions, inject skills per turn, watch for compaction, and monitor output quality — all as lifecycle hooks rather than core patches. Plan mode dispatches isolated read-only sub-coders for research and hands a written plan to a fresh session on the action model, with separate /plan-model and /action-model commands for big-plan/small-implement economics. Everything ships as extensions and skills around pi, keeping cold-start context near 7k tokens. Hobbyists running Qwen-class models on consumer laptops are the target audience, with published Terminal-Bench and GAIA results.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/little-coder.md)
