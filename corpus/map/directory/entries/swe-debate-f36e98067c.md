# SWE-Debate (`swe-debate`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: YerbaPage
- License: Apache-2.0
- Language: Python
- Interface: install=Clone repo, pip install -r localization/requirements.txt, pip install moatless-tree-search, copy .env.example to .env and configure API key
- Model providers: OpenAI, OpenAI-compatible (examples use DeepSeek via deepseek/deepseek-chat)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [yerbapage/swe-debate](../../repos/yerbapage/swe-debate.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent, backing=other, page=agent

## Description

Highlight (site page `what_makes_it_special`): Competitive multi-agent debate framework for software issue resolution. Uses competitive multi-agent debate where multiple expert agents collaborate and debate, combined with a graph-driven Entity Localization Pipeline and MCTS-based search (via Moatless framework). Accepted at ICSE 2026.

(captured site page body (agents/swe-debate.md), not a verified repo-code finding)
SWE-Debate applies competitive debate to the two hardest stages of automated issue resolution: finding the right code and deciding what to change. An Entity Localization Pipeline extracts classes, methods, and variables from the issue, walks code dependency graphs to build localization chains, and hands candidates to a multi-agent stage where five expert agents debate over three rounds to consolidate a fault localization and repair plan; a ReAct-style coding agent then executes the plan under moatless-tree-search with a value function scoring branches. The code is a compact research artifact (Apache-2.0, ICSE 2026) driven by any OpenAI-compatible endpoint, with examples configured for DeepSeek, and trajectories persist as JSON. It targets SWE-bench researchers studying whether structured disagreement among agents outperforms single-agent localization.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/swe-debate.md)
