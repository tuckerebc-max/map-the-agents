# SWE-Dev (`swe-dev`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: THUDM
- License: MIT
- Language: Python
- Interface: install=Python packaging (setup.py/pyproject.toml) + Docker (docker build -t swedev-evaluator:latest .)
- Model providers: Qwen, GPT-4o (configurable)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [thudm/swe-dev](../../repos/thudm/swe-dev.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): SWE agent focused on training and inference scaling; pipeline to synthesize test cases and scale up agent trajectories for training data; ACL'25 Findings paper

(captured site page body (agents/swe-dev.md), not a verified repo-code finding)
SWE-Dev, from Tsinghua's THUDM lab, tackles the data bottleneck for open software-engineering agents. Its pipeline crawls top PyPI repositories, mines issues and PRs into tasks, generates Gherkin-style behavior descriptions, and synthesizes test cases with an optional revision pass driven by traceback errors, validating each case in Docker so that fail-to-pass tests prove the task is real. The same machinery scales inference: giving a single run a larger interaction budget lifted SWE-Dev-32B from 34.0% to 36.6% on SWE-bench Verified, with SWE-Dev-7B at 23.4%. Configuration is centralized in a YAML schema, and both trained models and trajectory datasets are published on Hugging Face. Agent-training researchers use it as a recipe for building test-verified training data without human annotation.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swe-dev.md)
