# dspy-compounding-engineering (`dspy-compounding-engineering`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Strategic-Automation
- License: MIT
- Language: Python
- Interface: install=curl -LsSf https://raw.githubusercontent.com/Strategic-Automation/dspy-compounding-engineering/main/scripts/install.sh | sh; or pip install dspyce-install + dspyce-install; or uv sync from source
- Model providers: OpenAI, Anthropic, Ollama, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [strategic-automation/dspy-compounding-engineering](../../repos/strategic-automation/dspy-compounding-engineering.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first AI engineering CLI implementing a 'compounding engineering' philosophy: every todo resolution automatically codifies learnings into a knowledge base that informs all future AI operations. Features 10+ parallel specialized review agents (security, performance, architecture), ReAct-based file editing with zero hallucination, isolated git worktrees, built on the DSPy framework.

(captured site page body (agents/dspy-compounding-engineering.md), not a verified repo-code finding)
Most agent tools forget everything between tasks; this CLI's premise is that each unit of engineering work should make the next one easier. Every todo resolution codifies what was learned into a local knowledge base, and that knowledge base is injected into subsequent planning, review, and editing operations, so recurring issues stop recurring. Under that loop, DSPy programs run ten-plus specialized reviewers in parallel (security, performance, architecture, data integrity), a ReAct file editor gathers context before touching files, and plans can pull live documentation from the web. Work executes in isolated git worktrees with parallel workers, and a local knowledge base keeps code on the machine. It fits solo engineers or small teams who want review-and-implementation automation that accumulates institutional memory.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/dspy-compounding-engineering.md)
