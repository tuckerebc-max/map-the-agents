# AppAgent (`appagent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: TencentQQGYLab
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=pip
- Model providers: OpenAI (GPT-4V), Alibaba (Qwen-VL-Max)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [mnotgod96/appagent](https://github.com/mnotgod96/appagent) (source: backing, field: `source_code_url`) now resolves to [tencentqqgylab/appagent](../../repos/tencentqqgylab/appagent.md) (github id 733899994, verified [https://github.com/TencentQQGYLab/AppAgent](https://github.com/TencentQQGYLab/AppAgent)).

## Description

Highlight (site page `what_makes_it_special`): LLM-based multimodal agent that operates smartphone apps through a simplified action space mimicking human interactions (tapping/swiping) via ADB — no system back-end access needed. Two-phase approach: exploration (autonomous or human-guided) generates a knowledge base of UI element documentation, then deployment completes user tasks. Published at CHI 2025; successor AppAgentX adds an evolving mechanism.

(captured site page body (agents/appagent.md), not a verified repo-code finding)
AppAgent addresses GUI automation without backend access: an LLM-driven agent explores an app either autonomously or by watching human demonstrations, tagging interactive elements in screenshots and writing documentation for each, then executes tasks referencing that documentation in deployment. It runs on GPT-4V (about $0.03 per request pair) or free Qwen-VL-Max, needs only ADB and USB debugging (Android Studio emulators auto-detected), and is MIT-licensed with a CHI 2025 paper. The mnotgod96 repository mirrors Tencent QQGY Lab's official project (~6.9k stars), which saw its last major update with the AppAgentX successor in March 2025 — the original is minimally maintained and focused on GUI operation research, not software development.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/appagent.md)
