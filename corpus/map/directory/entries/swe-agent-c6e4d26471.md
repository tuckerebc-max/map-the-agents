# SWE-agent (`swe-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: SWE-agent
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI; install=From source via pip (pyproject.toml), or GitHub Codespaces
- Model providers: GPT-4o, Claude Sonnet 4, open-weights models (SWE-agent-LM-32b), your LM of choice
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [swe-agent/swe-agent](../../repos/swe-agent/swe-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Takes a GitHub issue and tries to automatically fix it using your LM of choice. State-of-the-art on SWE-bench among open-source projects (NeurIPS 2024). Configurable via a single YAML file. Development effort has shifted to mini-swe-agent which has superseded SWE-agent.

(captured site page body (agents/swe-agent.md), not a verified repo-code finding)
SWE-agent was built to answer a research question: does the interface an LM uses to operate on a repository matter as much as the model behind it? Its answer was a custom Agent-Computer Interface — compact file viewers, search tools with bounded output, and guarded edit commands — which drove state-of-the-art SWE-bench results at publication and a NeurIPS 2024 paper. In operation the agent receives a GitHub issue, explores a sandboxed copy of the repository with its custom shell tools, edits files, and runs tests before emitting a patch; all behavior is configured through a single YAML file. Beyond issue fixing, the same scaffold powers cybersecurity research through its EnIGMA configuration. Development attention has moved to mini-swe-agent, which the README explicitly recommends as the successor, leaving SWE-agent in maintenance mode.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/swe-agent.md)
