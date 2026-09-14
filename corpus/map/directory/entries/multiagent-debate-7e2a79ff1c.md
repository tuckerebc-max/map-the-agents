# Multiagent Debate (`multiagent-debate`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: composable-models
- License: unknown
- Language: Python
- Interface: install=git clone; install requirements.txt; run python scripts (e.g. python gen_math.py)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [composable-models/llm_multiagent_debate](../../repos/composable-models/llm_multiagent_debate.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Official implementation of the ICML 2024 paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', using multiagent debate to enhance factuality and reasoning.

(captured site page body (agents/multiagent-debate.md), not a verified repo-code finding)
This repository holds the code behind one of the most-cited LLM-collaboration papers: multiple model instances propose, critique, and refine answers across rounds of debate, and the final answer's factuality improves over single-model baselines. The four task directories cover arithmetic and math problems, grade-school math, biography generation, and MMLU multiple choice, each runnable as standalone scripts against OpenAI models. The implementation is explicitly preliminary — the README promises future task releases that never arrived — and the repository carries no license file, so reuse beyond reading is technically unlicensed. It has served as the reference point for a wave of follow-up work, including community alternatives like LLM-Agora that extended debate to open-source models. The code is an archival research artifact from 2023: no coding tools, no agentic loop over software, and no maintenance since 2025.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/multiagent-debate.md)
