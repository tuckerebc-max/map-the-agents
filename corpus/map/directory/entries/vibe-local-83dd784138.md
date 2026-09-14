# vibe-local (`vibe-local`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: ochyai
- License: MIT
- Language: Python, Shell
- Interface: install=curl install script (binary)
- Model providers: Ollama, OpenCode multi-provider
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [ochyai/vibe-local](../../repos/ochyai/vibe-local.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fully offline, free AI coding environment for Mac (also Intel Mac/Linux) using Ollama + local LLM. Built for workshops, students, and beginners. Auto model routing (vibe-router) sends chitchat to small models and coding to large models. RAM-aware model management prevents memory exhaustion. Classroom mode, three UI options (OpenCode TUI, Claude Code CLI, built-in Python engine).

(captured site page body (agents/vibe-local.md), not a verified repo-code finding)
vibe-local exists for settings where paid AI subscriptions and reliable internet are not assumptions: workshops, students, and beginners learning to operate a terminal through natural language. After a one-line install it runs entirely on local Ollama models, choosing among them by available RAM (qwen3.5:4b on 8GB machines up to qwen3-coder-next on 80GB+) so sessions never exhaust memory, and a small router model triages each input — small talk gets fast small-model answers, coding and tool tasks go to the large coder model. Users choose their surface: the OpenCode TUI, Claude Code pointed at Ollama, or a built-in stdlib-only Python agent with local RAG over project files; a classroom mode lets one Mac serve the models while students attach over the network. Safety defaults to asking before every shell action since local models can emit destructive commands. Coding workshops and self-learners, primarily in Japan, use it; it is MIT-licensed and under active development.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibe-local.md)
