# HASS-AI-Orchestrator (`hass-ai-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ITSpecialist111
- License: MIT
- Language: Python, TypeScript
- Interface: platforms=Autonomous; install=Home Assistant add-on: Settings -\> Add-ons -\> Add-on Store -\> Repositories -\> add https://github.com/ITSpecialist111/HASS-AI-Orchestrator -\> install AI Orchestrator
- Model providers: Ollama, OpenAI, Anthropic, GitHub Models, Microsoft Foundry
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [itspecialist111/hass-ai-orchestrator](../../repos/itspecialist111/hass-ai-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Policy-aware control plane for the home combining LLM reasoning with deterministic safety controls: Model proposes, Code validates, Humans remain in control, Home Assistant executes. Dry-run-by-default, schema validation, plan interception/approval, atomic checkpointed replay, audit trails, sandboxed generated dashboards, episodic memory (RAG via ChromaDB).

(captured site page body (agents/hass-ai-orchestrator.md), not a verified repo-code finding)
HASS-AI-Orchestrator brings LLM reasoning to Home Assistant without giving the model unsupervised control. An agent observes entity states, areas, and device metadata, then proposes changes as recorded intents with risk summaries; a deterministic kernel validates each proposal against tool schemas, domain allowlists, and blocked domains (such as shell_command), and a human approves before checkpointed, replayable execution — the model never holds authority over what actually runs. Three reasoning profiles (Rapid, Balanced, Deep) trade iteration depth against latency on a single local or cloud model, and proactive triggers fire on schedules or state changes with cooldowns. Memory combines ChromaDB-backed entity knowledge and past episodes with RAG over manuals, and a React dashboard handles audits, approvals, and generated dashboards in a sandboxed studio. It targets Home Assistant users who want agentic automation under explicit human policy control.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hass-ai-orchestrator.md)
