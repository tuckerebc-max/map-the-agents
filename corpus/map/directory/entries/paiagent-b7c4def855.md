# PaiAgent (`paiagent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: itwanger
- License: MIT
- Language: Java, TypeScript
- Interface: platforms=CLI; install=source
- Model providers: OpenAI, DeepSeek, Tongyi Qwen (DashScope), Zhipu AI (GLM), AIPing
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [itwanger/paiagent](../../repos/itwanger/paiagent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Dual-engine architecture (self-developed DAG + LangGraph4j state graph), zero-code visual drag-and-drop orchestration, Skills system with 3-level progressive loading to save tokens, Spring AI unified multi-model access

(captured site page body (agents/paiagent.md), not a verified repo-code finding)
PaiAgent is a self-hosted, visual platform for composing AI workflows in the style of Dify or n8n, built as a public demonstration that a complete enterprise-grade system can be produced through AI-assisted 'vibe coding'. A ReactFlow drag-and-drop editor assembles flows from LLM nodes (OpenAI, DeepSeek, Qwen, ZhiPu, AIPing), TTS nodes, and input/output nodes, with LLM calls unified through Spring AI and Spring AI Alibaba (DashScope) and SSE streaming throughout. Its differentiator is the dual engine: a hand-built DAG engine using Kahn topological sorting with DFS cycle detection runs alongside a LangGraph4j StateGraph engine, switchable per workflow via an EngineSelector, while a Skills system loads YAML-defined prompts with three-level progressive loading to economize tokens. The stack is Java 21/Spring Boot 3.4 with MySQL 8 on the backend and React 18/TypeScript on the frontend, requiring local Java and Node setup rather than a packaged binary. Java developers studying or extending AI workflow platforms — and instructors demonstrating AI-built software — are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/paiagent.md)
