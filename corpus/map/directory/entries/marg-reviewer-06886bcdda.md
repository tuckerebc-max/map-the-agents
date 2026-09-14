# marg-reviewer (`marg-reviewer`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: allenai
- License: Apache-2.0
- Language: Python
- Interface: install=Docker (docker compose up --build, requires OPENAI_API_KEY in .env)
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [allenai/marg-reviewer](../../repos/allenai/marg-reviewer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): MARG (Multi-Agent Review Generation) — generates peer reviews for scientific papers using multiple AI agent strategies (SARG-B, LiZCa, MARG-S)

(captured site page body (agents/marg-reviewer.md), not a verified repo-code finding)
The repository accompanies Allen AI's study of whether multi-agent LLM pipelines can produce useful scientific peer reviews, providing the web interface used in the paper's user study alongside scripts that reproduce its alignment experiments on the ARIES dataset. A reviewer submits a paper through the Dockerized web interface, and the backend generates reviews through one of three agent strategies whose outputs the paper compares. It also includes the GPT request cache and configurations needed to replicate the paper's metrics. The artifact serves NLP researchers studying review generation; it has seen only seven commits and no maintenance since.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/marg-reviewer.md)
