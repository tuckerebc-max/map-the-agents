# mcp-crawl4ai-rag (`mcp-crawl4ai-rag`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: coleam00
- License: MIT
- Language: Python
- Interface: platforms=Web; install=docker
- Model providers: OpenAI
- Feature flags (directory-reported):
  - mcp_support: yes (SSE and stdio) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: yes (yes)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [coleam00/mcp-crawl4ai-rag](../../repos/coleam00/mcp-crawl4ai-rag.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Combines Crawl4AI + Supabase + optional Neo4j knowledge graph with 5 toggleable advanced RAG strategies including contextual embeddings, hybrid search, agentic RAG, cross-encoder reranking, and AI hallucination detection via knowledge graph validation of AI-generated code against real GitHub repos.

(captured site page body (agents/mcp-crawl4ai-rag.md), not a verified repo-code finding)
Coding assistants hallucinate APIs and library usage because they answer from parametric memory, so this server gives them a retrieval layer: Crawl4AI ingests documentation sites or GitHub repositories into a Supabase vector store, and the agent queries it mid-task through MCP tools. Strategy toggles adjust behavior per deployment - hybrid search, contextual embeddings, cross-encoder reranking - and an optional Neo4j knowledge graph powers a hallucination checker that validates AI-written Python against real repository code. Claude Desktop, Claude Code, Windsurf, and n8n are documented clients over SSE or stdio. The author considers the repository a testbed feeding his Archon project, so issues are not actively worked.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mcp-crawl4ai-rag.md)
