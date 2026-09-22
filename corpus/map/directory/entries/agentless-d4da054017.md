# Agentless (`agentless`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: OpenAutoCoder
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI; install=git clone + conda env + pip install -r requirements.txt
- Model providers: OpenAI,Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [openautocoder/agentless](../../repos/openautocoder/agentless.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Agentless approach to automated software repair (SWE-bench): hierarchical fault localization, multi-patch diff sampling, and test-based patch selection without any agent loop.

(captured site page body (agents/agentless.md), not a verified repo-code finding)
The project demonstrates that LLM-based automated program repair does not require an agentic control loop. Its localization stage narrows from files to classes and functions to concrete edit locations; the repair stage samples many candidate diffs at those locations; and a validation stage runs regression and generated reproduction tests to re-rank and select the final patch. This decomposition keeps behavior inspectable and costs low, achieving 40.7% on SWE-bench Lite and 50.8% on SWE-bench Verified with Claude 3.5 Sonnet. Researchers use it as a baseline for agentic repair systems, and its SWE-bench Lite and Verified runs are published as reproducible artifacts. It is research software driven by an OpenAI-compatible API key, distributed as a Python 3.11 codebase under MIT.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/agentless.md)
