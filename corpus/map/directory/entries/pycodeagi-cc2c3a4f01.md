# PyCodeAGI (`pycodeagi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: chakkaradeep
- License: unknown
- Language: Python
- Interface: install=pip install -r requirements.txt (inferred from requirements.txt)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [chakkaradeep/pycodeagi](../../repos/chakkaradeep/pycodeagi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Early experimental AGI that generates a Python app from a user description. Uses LangChain and adopts the BabyAGI concept from @yoheinakajima. Very early-stage project with only 11 commits.

(captured site page body (agents/pycodeagi.md), not a verified repo-code finding)
PyCodeAGI was one of the early 2023 experiments that applied the BabyAGI task-loop pattern to software generation: describe the app you want, and the agent decomposes the goal into tasks, executes them with GPT-4 via LangChain, and iterates toward a working Python application. The implementation is minimal — a main script, a GPT-4 variant, and a config file — reflecting the era when agent projects fit in a few hundred lines. It adopted the task-driven loop Yohei Nakajima published as BabyAGI and pointed it at code generation rather than general research tasks. Development stopped after eleven commits in May 2023, and the README still describes the project as just started. Its main interest now is historical, as an early data point in the line from BabyAGI-style loops to modern coding agents.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pycodeagi.md)
