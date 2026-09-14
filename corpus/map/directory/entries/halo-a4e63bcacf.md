# HALO (`halo`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: context-labs
- License: MIT
- Language: Python, TypeScript
- Interface: install=binary, pip
- Model providers: OpenAI-compatible (OpenAI, OpenRouter, any OpenAI-compatible base URL)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [context-labs/halo](../../repos/context-labs/halo.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Uses specialized Recursive Language Models (RLMs) instead of general-purpose LLMs to analyze production agent execution traces and identify systemic failure modes. Creates a recursively self-improving loop: collect traces, analyze, fix harness, redeploy, repeat. Feeds reports into coding agents (Cursor, Claude Code) to iteratively improve the harness. Demonstrated +10-16 point improvements on AppWorld benchmarks purely through harness optimization.

(captured site page body (agents/halo.md), not a verified repo-code finding)
HALO addresses the problem that agent harnesses accumulate fixable flaws — hallucinated tool calls, redundant arguments, refusal loops — that general-purpose coding agents fail to diagnose when handed raw execution traces, because traces are long and the agent fixates on single-run errors. HALO instead feeds OpenTelemetry-compatible traces into a Recursive Language Model engine tuned for trace decomposition, which identifies systemic failure modes and emits a findings report; a separate coding agent (Cursor, Claude Code) then applies the recommended harness edits, and the cycle repeats on fresh traces. The approach treats harness improvement as a measurable loop: on AppWorld, optimizing only the harness raised Gemini 3 Flash from 36.8% to 52.6% and Sonnet 4.6 from 73.7% to 89.5% dev SGC, with held-out verification against overfitting. It ships as a pip package and desktop app aimed at teams operating production agents at scale.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/halo.md)
