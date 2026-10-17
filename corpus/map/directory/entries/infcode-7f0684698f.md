# InfCode (`infcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Tokfinity
- License: MIT
- Language: Python
- Interface: install=pip install -r requirements.txt (Python 3.12 recommended)
- Model providers: OpenAI, OpenRouter, DeepSeek, self-hosted
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [tokfinity/infcode](../../repos/tokfinity/infcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Adversarial multi-agent Code Agent System using dual-agent adversarial refinement (Test Patch Generator + Code Patch Generator) that iteratively improve; achieved 79.4% on SWE-Bench Verified (SOTA)

(captured site page body (agents/infcode.md), not a verified repo-code finding)
InfCode's thesis is that generation and verification should compete: a Test Patch Generator rewrites tests to expose remaining faults, and a Code Patch Generator must survive them, iterating until either side yields. Candidate patches are generated in parallel inside per-example Docker containers and ranked by a Patch Selector, with tools for file editing, ripgrep search, and bash execution. The system reports 79.4% on SWE-Bench Verified, which the team claims as SOTA at publication. Running it requires Docker for the image builder, Python 3.12, and API keys for OpenAI, OpenRouter, DeepSeek, or self-hosted endpoints. The repo is a small research artifact (17 commits) from Tokfinity's Code Research team and Beihang University.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/infcode.md)
