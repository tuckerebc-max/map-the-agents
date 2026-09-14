# ReCode (`recode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: FoundationAgents
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [foundationagents/recode](../../repos/foundationagents/recode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Unifies planning and action into a single representation using recursive code generation, allowing dynamic adaptation from strategic thinking to concrete actions with universal granularity control

(captured site page body (agents/recode.md), not a verified repo-code finding)
ReCode is a research framework from the FoundationAgents org (the MetaGPT team) testing a specific thesis: that planning and acting should not be separate phases in an LLM agent. It represents a plan as a tree of placeholder functions in a Python program, then lets the model recursively expand each placeholder into finer-grained executable calls, with a shared constrained executor maintaining state and validating code as nodes run. Because the representation is uniform, the agent moves fluidly between strategic decomposition and concrete action without switching modes, which the paper calls universal granularity control. Evaluations on ALFWorld, WebShop, and ScienceWorld report a 60.8 average score, roughly 10.5 points above ReAct, CodeAct, and AdaPlanner baselines, with a fine-tuned Qwen2.5-7B variant reaching 70.4%. The code is a research artifact — fourteen commits, acknowledged incomplete requirements, and benchmark-specific environment conflicts — intended for researchers reproducing the paper rather than for production use.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/recode.md)
