# DeerFlow (`deerflow`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: bytedance
- License: MIT
- Language: Python
- Interface: platforms=Autonomous, CLI, IDE, Web; install=git clone + make setup, docker
- Model providers: OpenAI, OpenRouter, vLLM, Claude Code (OAuth), Codex CLI, MiniMax Code (ACP), OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: yes (HTTP/SSE with OAuth, stdio with per-tool timeouts) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (yes)

Repository map entry: [bytedance/deer-flow](../../repos/bytedance/deer-flow.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A batteries-included 'super agent harness' orchestrating sub-agents, long-term memory, sandbox-aware execution, and extensible skills; ships with built-in skills for research, slides, web pages, and image/video generation with progressive skill loading.

(captured site page body (agents/deerflow.md), not a verified repo-code finding)
DeerFlow started as ByteDance's deep-research framework and was rebuilt for 2.0 as a general agent harness: the lead agent decomposes work, delegates to subagents only when parallelism or context isolation pays, and verifies their structured results. Skills provide progressive-loading capabilities (research, slides, web pages), memory persists across sessions, and sandbox modes range from local processes to Docker, Kubernetes, and E2B. An extension API exposes task-lifecycle hooks and middleware, and the gateway reaches IM channels from Telegram to DingTalk. Teams use it as a self-hosted agent platform where they control models — Doubao-Seed-2.0-Code, DeepSeek, Kimi — and data.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/deerflow.md)
