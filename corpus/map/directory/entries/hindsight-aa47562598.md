# Hindsight (`hindsight`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: vectorize-io
- License: MIT
- Language: Python
- Interface: platforms=CLI; install=pip
- Model providers: OpenAI, Anthropic, Google, Groq, Bedrock, VertexAI, DeepSeek, Ollama, LMStudio, LiteLLM, 100+ via LiteLLM, subscription passthrough (openai-codex, claude-code, github-copilot)
- Feature flags (directory-reported):
  - mcp_support: yes (HTTP transport — http://localhost:8888/mcp/{bank_id}/) (yes)
  - plugin_support: yes (60+ integrations; extensibility via tenant, auth, storage extension points) (yes)
  - claude_code_plugin: yes (native integration via npx @vectorize-io/hindsight-coding-agents install claude-code) (yes)
  - subagents: no (no)
  - hooks: yes (webhooks for retain, consolidation, and refresh lifecycle events) (yes)
  - plan_mode: no (no)

Repository map entry: [vectorize-io/hindsight](../../repos/vectorize-io/hindsight.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent memory system using biomimetic data structures (world facts, experiences, observations, mental models) to make agents genuinely learn over time rather than just recall conversation history. Achieves state-of-the-art on LongMemEval with a 2-line LLM wrapper for persistent memory.

(captured site page body (agents/hindsight.md), not a verified repo-code finding)
Hindsight is a memory service that lets AI agents accumulate durable knowledge instead of treating every session as isolated. It stores memories as world facts, experiences, evidence-backed observations, and auto-refreshing mental models organized into isolated memory banks, exposing three operations: retain (extracting canonical facts from interactions), recall (fusing semantic, BM25, graph, and temporal retrieval with reranking), and reflect (reasoning across memories to derive new connections). Every deployment exposes the same operations over REST, SDKs, an MCP endpoint for coding agents like Claude Code, and LLM wrapper functions, so existing agents pick it up without architectural change. Memory consolidation is evidence-based — observations carry quotes and proof counts and are refined rather than overwritten — and LongMemEval results have been reproduced by third parties. It is used as shared memory across coding agents, with per-repo memory built from git history, and runs self-hosted (PostgreSQL/pgvector) or as a managed cloud.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hindsight.md)
