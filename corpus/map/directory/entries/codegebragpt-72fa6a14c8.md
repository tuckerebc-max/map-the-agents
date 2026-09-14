# Codegebragpt (`codegebragpt`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: sr5434
- License: MIT
- Language: Jupyter Notebook
- Interface: unknown
- Model providers: Upstage SOLAR-10.7B-Instruct-v1.0
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [sr5434/codegebragpt](../../repos/sr5434/codegebragpt.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fine-tunes SOLAR-10.7B-Instruct-v1.0 using QLoRA on ~100k STEM samples (math, physics, chemistry, biology, CS/ML, code). Not a coding agent harness -- it is an LLM fine-tuning project.

(captured site page body (agents/codegebragpt.md), not a verified repo-code finding)
CodegebraGPT is a student-scale fine-tuning project aiming to adapt the SOLAR-10.7B-Instruct model to STEM reasoning. The plan combined roughly 100,000 samples from MetaMath, Camel-AI science datasets, arXiv math and physics/CS subsets, GSM8K, MMLU, Evol Instruct Code, and Glaive Code Assistant into a training corpus published separately at sr5434/CodegebraGPT_data, with QLoRA chosen so a single consumer GPU could run the training. The repository consists mainly of two notebooks — dataset preparation and QLoRA training — plus a README describing the procedure as planned, and no fine-tuned model release is evident. The name continues the author's earlier Codegebra equation-solving program, repositioned around a natural-language interface.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codegebragpt.md)
