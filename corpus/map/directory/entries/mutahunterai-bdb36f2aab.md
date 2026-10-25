# MutahunterAI (`mutahunterai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: codeintegrity-ai
- License: AGPL-3.0
- Language: Python
- Interface: install=pip install https://github.com/codeintegrity-ai/mutahunter
- Model providers: OpenAI (GPT-4o, gpt-4o-mini)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [codeintegrity-ai/mutahunter](../../repos/codeintegrity-ai/mutahunter.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source, language-agnostic LLM-based mutation testing tool. It generates code mutants using LLMs and runs test commands to measure mutation coverage (killed vs survived mutants).

(captured site page body (agents/mutahunterai.md), not a verified repo-code finding)
Mutahunter modernizes mutation testing, which traditionally relies on fixed operator catalogs that miss semantically meaningful mutants. Instead, an LLM reads the code under test and generates context-aware mutants — subtle behavioral variations a hand-written operator table would never produce — then the harness executes the project's test command against each mutant and classifies outcomes as killed, survived, timeout, or compile-error, yielding a mutation coverage score that reflects genuine test strength. The tool is language-agnostic by construction: it wraps whatever test command the project uses (a Maven build, pytest, anything invocable from the CLI) rather than implementing per-language integration. Per-run output includes LLM cost, making the expense of mutation testing explicit and budgetable. It installs via pip from GitHub and targets developers and QA teams assessing whether their test suites actually detect defects rather than merely execute code. Activity has slowed since early 2025, with the project sitting at a modest community size under AGPL-3.0.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/mutahunterai.md)
