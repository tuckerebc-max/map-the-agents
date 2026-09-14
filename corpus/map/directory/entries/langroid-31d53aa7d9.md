# Langroid (`langroid`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: langroid
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=pip
- Model providers: OpenAI, Azure OpenAI, Anthropic, Google Gemini, Ollama, LiteLLM, OpenRouter, Cerebras, DeepSeek, Portkey, LangDB
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [langroid/langroid](../../repos/langroid/langroid.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intuitive, lightweight, extensible Python framework (from CMU/UW-Madison researchers) for building LLM-powered multi-agent applications. Agent-as-actor paradigm with hierarchical task delegation via TaskTool. Does NOT depend on LangChain. Pydantic-based tool/function definitions, built-in RAG with source citation (DocChatAgent), SQL chat, knowledge graph chat (Neo4j/ArangoDB), lineage tracking. Works with practically any LLM. Has a Claude Code plugin (claude plugin install langroid@langroid).

(captured site page body (agents/langroid.md), not a verified repo-code finding)
Langroid came out of CMU and UW-Madison research as an alternative to monolithic agent chains: each agent is an actor that transforms messages, and Task objects compose them into parent-child hierarchies with explicit delegation and addressing. The library ships RAG agents, structured extraction, SQL/table agents, and vector-store integrations (Qdrant, Chroma, Milvus, pgvector, and others), and since v0.53.0 any agent can consume MCP server tools through an adapter. It targets Python developers building multi-agent LLM applications, including production users such as Nullify, and is released under MIT with monthly releases.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/langroid.md)
