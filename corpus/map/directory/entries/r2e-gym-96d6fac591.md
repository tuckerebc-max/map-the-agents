# R2E-Gym (`r2e-gym`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: R2E-Gym
- License: Apache-2.0
- Language: Python
- Interface: install=Install uv; uv venv; activate; uv sync && uv pip install -e .
- Model providers: Anthropic (Claude 3.5 Sonnet), OpenAI (GPT-4o), vLLM-hosted R2E-Gym models, DeepSWE
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [r2e-gym/r2e-gym](../../repos/r2e-gym/r2e-gym.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Largest procedurally curated environment (8.1K+ problems across 13 repos) for training real-world SWE agents. Introduces SWE-GEN (synthetic environment curation from commits, no human PRs/tests needed) and Hybrid Test-time Scaling (execution-based + execution-free verifiers). First open-weight SWE agent to reach 51% on SWE-Bench Verified, competitive with proprietary models like o1.

(captured site page body (agents/r2e-gym.md), not a verified repo-code finding)
R2E-Gym attacks the data bottleneck in training software-engineering agents: curated benchmarks like SWE-bench depend on human-written PRs and tests, which cap scale. Its SWE-GEN recipe instead synthesizes task environments directly from repository commits — Dockerized environments, executable tests, and natural-language task descriptions — producing over 8,100 problems across 13 real repos without human curation. On top of the environment it provides an agent harness (RepoEnv plus agent APIs), parallelized trajectory collection, and an SFT training pipeline that produced open-weight agents evaluated on SWE-bench Verified with hybrid test-time scaling. The pipeline and recipes were released by UC Berkeley and ANU researchers and published at COLM 2025, and Agentica used them to train the DeepSWE models. Machine-learning researchers use it to generate training environments and reproduce reinforcement-learning and SFT pipelines rather than as a day-to-day coding tool.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/r2e-gym.md)
