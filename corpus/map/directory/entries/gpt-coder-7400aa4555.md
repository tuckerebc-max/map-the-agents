# gpt-coder (`gpt-coder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: alicheg
- License: MIT
- Language: Python
- Interface: install=git clone, pip install -r requirements.txt, configure .env with OPENAI_API_KEY, run python src/main.py
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [alicheg/gpt-coder](../../repos/alicheg/gpt-coder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-supervising AI code generation tool that iteratively generates, refines, compiles, and tests solutions against extracted test cases until they meet expected criteria.

(captured site page body (agents/gpt-coder.md), not a verified repo-code finding)
GPT Coder demonstrates the test-feedback loop that later defined agentic coding, compressed into a single Python script: GPT generates a coding challenge, a solution, and test cases, then the tool compiles, executes, and tests the solution against them, feeding failures back until they pass. The pipeline is fixed rather than open-ended — there is no general tool use, file editing, or interactivity — and configuration is just an OPENAI_API_KEY in a .env file. One commit, no releases, and 26 stars mark it as a ChatGPT-era experiment published in April 2023 and never developed further. Its value now is historical: an early example of test-driven self-refinement that later harnesses industrialized.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gpt-coder.md)
