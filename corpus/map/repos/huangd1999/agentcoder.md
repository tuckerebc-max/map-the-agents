# huangd1999/agentcoder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d8538d63675c @ 7625ad548ee3dbae

## Summary (orientation draft, not independently verified)

AgentCoder is a multi-agent LLM code generation framework with programmer, test designer, and test executor agents, driven by per-benchmark Python scripts and OpenAI API access. Evidence is limited to README and requirements; no code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The framework comprises three specialized agents: a programmer agent, a test designer agent, and a test executor agent that collaborate in an iterative feedback loop. -- evidence: [README.md#L3-L3](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L3-L3)
- design-choices (2 claim(s)):
  - [observation/documented] The test designer agent generates diverse, objective test cases independently of code generation, and the test executor runs them against generated code to feed refinement feedback. -- evidence: [README.md#L7-L10](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L7-L10)
  - [observation/documented] The README describes a modular structure intended to allow easy integration with advanced models and future enhancements. -- evidence: [README.md#L7-L10](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L7-L10)
- workflows (2 claim(s)):
  - [observation/documented] Installation involves cloning the repo (plus CodeGeeX), running pip install -r requirements.txt, and adding an API key to a .env file. -- evidence: [README.md#L22-L25](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L22-L25), [README.md#L14-L20](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L14-L20), [README.md#L27-L30](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L27-L30)
  - [observation/documented] The README invites contributions via GitHub issues or pull requests. -- evidence: [README.md#L61-L61](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L61-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Usage is via per-benchmark scripts: programmer_[humaneval/mbpp].py, test_designer_[humaneval/mbpp].py, and test_executor_[humaneval/mbpp].py. -- evidence: [README.md#L36-L40](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L36-L40), [README.md#L44-L48](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L44-L48), [README.md#L52-L56](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L52-L56)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] Script names referencing humaneval and mbpp suggest the framework targets the HumanEval and MBPP code generation benchmarks. -- evidence: [README.md#L36-L40](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L36-L40), [README.md#L44-L48](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L44-L48), [README.md#L52-L56](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L52-L56)
- dependencies (3 claim(s)):
  - [observation/documented] requirements.txt pins datasets 3.3.1, openai 0.28.0, and python-dotenv 1.0.1. -- evidence: [requirements.txt#L1-L3](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/requirements.txt#L1-L3)
  - [observation/documented] The project requires an OpenAI or similar third-party provider API key, configured in a .env file as OPENAI_API_KEY. -- evidence: [README.md#L14-L20](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L14-L20), [README.md#L27-L30](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L27-L30)
- limitations (1 claim(s)):
  - [observation/documented] The project is released under the MIT License and acknowledges AIOHUB for funding and support. -- evidence: [README.md#L65-L65](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L65-L65), [README.md#L69-L69](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L69-L69)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](agentcoder.detail.md) for every claim.)

Metadata and full claim list: [full detail](agentcoder.detail.md)
Human notes ([notes](agentcoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
