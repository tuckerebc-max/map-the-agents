# AgentCoder (`agentcoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: huangd1999
- License: MIT
- Language: Python
- Interface: install=git clone (with CodeGeeX submodule), pip install -r requirements.txt, add API key to .env
- Model providers: OpenAI, CodeGeeX
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [huangd1999/agentcoder](../../repos/huangd1999/agentcoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent code generation framework with three specialized agents (programmer, test designer, test executor); independent test case generation and iterative code refinement through multiagent collaboration.

(captured site page body (agents/agentcoder.md), not a verified repo-code finding)
AgentCoder is a research codebase from huangd1999 that studies whether splitting code generation across specialized agents improves output quality, evaluated on the HumanEval and MBPP benchmarks. A programmer agent writes code, a test-designer agent independently generates test cases the programmer never sees, and a test executor runs them, feeding failures back for iterative refinement. The framework is deliberately modular so different LLMs can be swapped in (OpenAI models and CodeGeeX are wired up), but it is a benchmark-oriented research codebase — clone, install requirements, add an API key — not a developer product. Its users are NLP and code-generation researchers reproducing multi-agent generation experiments.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentcoder.md)
