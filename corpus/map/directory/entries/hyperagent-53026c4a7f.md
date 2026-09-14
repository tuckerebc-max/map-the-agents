# HyperAgent (`hyperagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: FSoft-AI4Code
- License: MIT
- Language: Python
- Interface: install=conda create -n hyperagent python=3.10 then pip3 install -e . (requires pre-installing Zoekt + universal-ctags)
- Model providers: Anthropic (extensible via api_type and base_url)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [fsoft-ai4code/hyperagent](../../repos/fsoft-ai4code/hyperagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First generalist SE agent handling multiple task types (GitHub issue resolution, repo-level code generation, fault localization, program repair) across multiple programming languages (Python & Java). Multi-agent architecture (Planner, Navigator, Code Editor, Executor) mimicking human developer workflows with state-of-the-art results on SWE-Bench Verified (31.4%), RepoExec (53.3% Pass@5), and Defects4J (249 bugs fixed). Last commit November 2024.

(captured site page body (agents/hyperagent.md), not a verified repo-code finding)
HyperAgent came out of FPT Software's AI4Code research group as a generalist alternative to single-purpose repair or localization systems: one four-agent pipeline switches between patch generation and fault-prediction modes depending on the task. A Planner decomposes the issue, a Navigator locates relevant code using Zoekt and universal-ctags indexes, a Code Editor writes changes, and an Executor runs them in a Jupyter kernel, with each agent configurable to a different LLM. It reported 31.4% on SWE-Bench Verified, 25% on Lite, 53.3% Pass@5 on RepoExec, and 249 fixed Defects4J bugs. The repo has seen no commits since November 2024 and functions as archived research code accompanying the arXiv paper.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hyperagent.md)
