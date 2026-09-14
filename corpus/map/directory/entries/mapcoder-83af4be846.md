# MapCoder (`mapcoder`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Md-Ashraful-Pramanik
- License: MIT
- Language: Python
- Interface: install=git clone; pip install -r requirements.txt; set up .env; python src/main.py
- Model providers: OpenAI, Azure
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [md-ashraful-pramanik/mapcoder](../../repos/md-ashraful-pramanik/mapcoder.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent code generation framework for competitive programming using four LLM agents (retrieval, planning, coding, debugging) with an adaptive agent traversal schema that dynamically cascades; achieved SOTA pass@1 on 8 benchmarks (HumanEval 93.9%, MBPP 83.1%, CodeContests 28.5%); accepted at ACL 2024. Repo explicitly states it will no longer be maintained (successor is CodeSIM).

(captured site page body (agents/mapcoder.md), not a verified repo-code finding)
MapCoder replicated the human competitive-programming cycle across four LLM agents: a retrieval agent recalls similar solved problems from the model's own memory (no external retriever), a planner produces step-by-step solutions conditioned on those examples, a coding agent translates plans into code tested against sample I/O, and a debugging agent fixes failures using the plan as context. The adaptive traversal scheme lets agents cascade and retry dynamically rather than follow a fixed flow, which drove state-of-the-art pass@1 on eight benchmarks at publication (93.9% HumanEval, 83.1% MBPP with GPT-4). The ACL 2024 paper documents the method, and the authors have ended maintenance in favor of their successor, CodeSIM.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mapcoder.md)
