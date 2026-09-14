# CodeFuse-muAgent (`codefuse-muagent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: codefuse-ai
- License: Apache-2.0
- Language: Python
- Interface: install=docker, pip
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (tool registration, categorization, permission management via Swagger protocol) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (multi-agent orchestration, virtual team design) (yes)
  - hooks: no (no)
  - plan_mode: unknown (unknown)

Repository map entry: [codefuse-ai/codefuse-muagent](../../repos/codefuse-ai/codefuse-muagent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=other, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Multi-agent framework driven by a Knowledge Graph (Eventic Knowledge Graph / EKG) engine rather than purely model-based or fixed-flow approaches. Successful exploration paths are documented into the KG to reduce future token costs. Supports MultiAgent, FunctionCall, CodeInterpreter, and RAG. Visual drag-and-drop canvas for building agent workflows. Validated in complex DevOps scenarios at Ant Group.

(captured site page body (agents/codefuse-muagent.md), not a verified repo-code finding)
CodeFuse-muAgent is Ant Group's multi-agent framework built around an Eventic Knowledge Graph engine: workflows are expressed as intent, workflow, tool, and character nodes on a drag-and-drop canvas, and the graph — not free-form model prompting — drives orchestration. Successful exploration paths are written back into the knowledge graph so subsequent runs reuse proven paths and spend fewer tokens rediscovering them. The framework bundles multi-agent orchestration, function calling, a code interpreter for sandboxed execution, and RAG, with tool registration handled through a Swagger-based protocol with permission management, plus visual debugging and monitoring. It was validated in complex DevOps scenarios at Ant Group and ships as the pip package codefuse-muagent, with an SDK (v2.2, January 2025) adding ekg-sdk and parallel execution; public development activity has been quiet since early 2025.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codefuse-muagent.md)
