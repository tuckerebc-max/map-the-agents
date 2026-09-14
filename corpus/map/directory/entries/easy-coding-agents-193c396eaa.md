# easy-coding-agents (`easy-coding-agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: yushui2022
- License: unknown
- Language: Python
- Interface: platforms=Autonomous, CLI, IDE; install=pip install -r requirements.txt then python main.py
- Model providers: OpenAI-compatible APIs
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [yushui2022/easy-coding-agents](../../repos/yushui2022/easy-coding-agents.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Evidence-gated memory system that preserves source refs across context wipe; autonomous terminal coding loop with plan/code/chat modes, custom agents, todo discipline, loop/budget guards, and final-answer quality gates; benchmarked against summary, long-context, FTS, and vector RAG memory baselines.

(captured site page body (agents/easy-coding-agents.md), not a verified repo-code finding)
easy-coding-agents is built around a failure mode common to autonomous loops: the model loses track of what it already established, repeats itself, or declares done without evidence. The engine's guards detect repeated tool calls, over-exploration of simple tasks, and empty responses, while a final-answer quality gate blocks DONE claims that lack verification evidence. The evidence-gated memory layer persists refs, tool logs, and task state across context wipes, and the repo publishes reproducible benchmark snapshots showing memory-subsystem recall after context wipe against summary, FTS, and vector baselines. It is a single-developer research project for people studying agent memory, not a production harness.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/easy-coding-agents.md)
