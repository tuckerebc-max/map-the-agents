# PilotDeck (`pilotdeck`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: OpenBMB
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI; install=docker
- Model providers: OpenAI, Anthropic, Google Gemini, DeepSeek, Qwen, Kimi, MiniMax, Ollama
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [openbmb/pilotdeck](../../repos/openbmb/pilotdeck.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source agent operating system (by Tsinghua THUNLP/ModelBest/OpenBMB) centered on 'WorkSpace' isolation — each project gets isolated files, memory, and skills. Traceable white-box memory (visible, editable, rollbackable with Dream Mode consolidation). Smart routing auto-detects task difficulty and routes to appropriate models (~70% cost savings). Always-on background execution that breaks the ask-answer loop. Native MCP support, open plugin architecture, lifecycle hooks. Consistent ...

(captured site page body (agents/pilotdeck.md), not a verified repo-code finding)
PilotDeck, open-sourced in May 2026 by Tsinghua's THUNLP lab with ModelBest and OpenBMB, rethinks agent architecture for people juggling multiple long-running projects, where a single global context window becomes a liability. Each project gets an isolated WorkSpace — its own files, memory store, and accreting skill set — so retrieval stays scoped and parallel projects never pollute each other, and the white-box memory design makes every entry inspectable, editable, and rollbackable, with background Dream Mode consolidating memory during idle windows. Smart Routing classifies task difficulty and dispatches accordingly: complex work goes to a flagship model, routine subtasks to lighter ones, with published figures around 70% cost savings on multi-model workloads. The system runs tasks in the background after sign-off, discovering work and delivering files with summary reports. Native MCP support, lifecycle hooks, and a plugin architecture extend it, and the AGPL-licensed platform targets professional users running multiple concurrent projects.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/pilotdeck.md)
