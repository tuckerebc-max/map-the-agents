# Prometheus (`prometheus`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: EuniAI
- License: GPL-3.0
- Language: Python
- Interface: install=docker
- Model providers: OpenAI, Anthropic, Google Gemini (BYOK)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [euniai/prometheus](../../repos/euniai/prometheus.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent collaborative reasoning across files and commits using a Neo4j-powered Unified Codebase Knowledge Graph and long-term memory (Athena). Full detect-reproduce-repair-verify (DRRV) automation pipeline with specialized agents for issue classification, bug reproduction, patch generation, and context retrieval. Ranked top on SWE-bench with GPT-5; research-backed (arXiv paper).

(captured site page body (agents/prometheus.md), not a verified repo-code finding)
Prometheus was built to close the gap between chat-based coding assistants and verifiable issue resolution: given a GitHub issue, it classifies it, reproduces the bug, generates a repair, and verifies the fix in a containerized environment before responding. Its codebase understanding comes from a Unified Codebase Knowledge Graph built with Tree-sitter ASTs and stored in Neo4j, enabling graph-based semantic search over code structure rather than embedding similarity, with a long-term memory component called Athena. LangGraph state machines orchestrate specialized agents for bug reproduction, feature analysis, and question answering, with PostgreSQL checkpointing so long pipelines resume after failure. The system ships as a FastAPI service backed by Docker-isolated test execution rather than an interactive terminal tool. EuniAI reports top-five SWE-bench leaderboard placement (top-1 with GPT-5), and engineering teams use it as an autonomous service for triaging and fixing repository issues.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/prometheus.md)
