# Microsoft Magentic-One (`microsoft-magentic-one`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: unknown
- License: MIT
- Language: Python
- Interface: install=pip install 'autogen-agentchat' 'autogen-ext\[magentic-one,openai\]'
- Model providers: OpenAI (GPT-4o, o1-preview); model-agnostic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: yes (Orchestrator + WebSurfer + FileSurfer + Coder + ComputerTerminal) (yes)
  - hooks: unknown (unknown)
  - plan_mode: yes (Orchestrator with Task Ledger and Progress Ledger for planning and re-planning) (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): A generalist multi-agent system with a modular, plug-and-play design where agents can be added/removed without reworking the system. An Orchestrator leads four specialized agents (WebSurfer, FileSurfer, Coder, ComputerTerminal) with error recovery through re-planning. Achieves competitive performance on GAIA, AssistantBench, and WebArena benchmarks without task-specific modifications. Now integrated into autogen-agentchat as MagenticOneGroupChat.

(captured site page body (agents/microsoft-magentic-one.md), not a verified repo-code finding)
Magentic-One came out of Microsoft Research as a demonstration that a small set of generalist agents, well-coordinated, could match specialized systems on open-ended tasks — GAIA, AssistantBench, and WebArena — without task-specific tuning. The Orchestrator keeps a Task Ledger of facts, guesses, and the current plan in an outer loop, re-planning when progress stalls, and an inner Progress Ledger that each step assigns the next subtask to one of four specialists: a Chromium-driving WebSurfer using accessibility-tree and set-of-marks prompting, a FileSurfer reading documents through markdown previews, a Coder, and a ComputerTerminal. Specialists are interchangeable — the system keeps working when one is swapped or removed — and per-agent model assignments allow heterogeneous LLM configurations. It ships as part of autogen-agentchat (MagenticOneGroupChat) with AutoGenBench for isolated, repeated benchmark runs, and Microsoft positions it for research use inside sandboxed containers with human monitoring rather than as a production harness.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/microsoft-magentic-one.md)
