# gpt-all-star (`gpt-all-star`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: kyaukyuai
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, Web; install=pip install gpt-all-star; or Docker + Poetry for development
- Model providers: OpenAI, Azure OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [kyaukyuai/gpt-all-star](../../repos/kyaukyuai/gpt-all-star.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI-powered code generation tool for scratch development of web applications using a team collaboration of autonomous AI agents — users assemble a group of AI agents, choose leaders for each step, leaders create action plans, and team members work together to complete every task. Supports Plan-and-Solve Prompting via --plan_and_solve flag.

(captured site page body (agents/gpt-all-star.md), not a verified repo-code finding)
The project frames app generation as team management: the user picks which AI agents join the team and who leads each phase, and leaders break work into tasks that agent members execute toward a finished React application. It is built on LangChain/LangGraph in Python, supports OpenAI, Azure OpenAI, and Anthropic models, and ships as a pip package with a companion Streamlit web UI for watching the team work. Development has been quiet since its 2023-2024 burst of activity, with the last release activity trailing off and open PRs unmerged, and output quality is bounded by its validated stack of React plus Chakra UI plus JavaScript. It remains a readable demonstration of agentic team workflows more than a production tool.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gpt-all-star.md)
