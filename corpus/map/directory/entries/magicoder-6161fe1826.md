# Magicoder (`magicoder`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ISE-UIUC
- License: MIT
- Language: Python
- Interface: platforms=API, CLI
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ise-uiuc/magicoder](../../repos/ise-uiuc/magicoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A code-generation model family empowered by OSS-Instruct, which uses open-source code snippets to generate low-bias, high-quality instruction data, mitigating inherent biases in LLM-synthesized data. Magicoder-S-DS-6.7B outperforms GPT-3.5-turbo and Gemini Ultra on HumanEval. A model, not an agent harness.

(captured site page body (agents/magicoder.md), not a verified repo-code finding)
Magicoder attacked a data-quality problem in code-model training: instruction data synthesized purely by LLMs inherits their biases and blind spots, so the UIUC team instead seeded generation with randomly sampled snippets from real open-source code, producing 75K diverse instruction-response pairs that became the OSS-Instruct dataset. Models fine-tuned from DeepSeek and Llama-2 bases with this data (plus an Evol-Instruct set) reached state-of-the-art 6.7B-class HumanEval scores at release. ML researchers and practitioners training or serving local code models use the released checkpoints, datasets, and method; the ICML 2024 paper documents the approach. It is model and dataset work, with no agentic loop of any kind.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/magicoder.md)
