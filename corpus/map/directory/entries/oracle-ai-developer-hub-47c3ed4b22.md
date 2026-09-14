# oracle-ai-developer-hub (`oracle-ai-developer-hub`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: oracle-devrel
- License: UPL-1.0
- Language: Python
- Interface: install=docker
- Model providers: OCI Generative AI (xAI Grok), OpenAI, Anthropic, HuggingFace, Ollama, LiteLLM
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [oracle-devrel/oracle-ai-developer-hub](../../repos/oracle-devrel/oracle-ai-developer-hub.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Collection of technical resources (reference implementations, notebooks, workshops) for building AI applications using Oracle AI Database as a single converged engine for vectors, agent memory, checkpoints, semantic LLM cache, and chat history. Includes first-party LangChain integrations (langchain-oracledb, langgraph-oracledb, langchain-oci) and the oracleagentmemory package. Production-grade RAG, multi-agent, and hybrid retrieval reference implementations.

(captured site page body (agents/oracle-ai-developer-hub.md), not a verified repo-code finding)
Oracle positions its AI Database as a single converged engine for the agent era — vector search, agent memory via the OAMP package, checkpoints, and Duality Views in one system — and this Developer Relations repository is the working evidence. The /apps directory holds complete reference implementations (agentic RAG, a finance AI agent, a LangGraph supply-chain demand planner, intelligent document processing), /notebooks teach RAG, agent memory, and CoT/ToT/ReAct reasoning against that stack, and /workshops walk through building a memory-aware enterprise data agent, including one harness for migrating RAG corpora from MongoDB to Oracle 26ai. Framework coverage spans OpenAI Agents SDK, Claude Agent SDK, LangGraph supervisors, and Deep Agents, all pointing back to the database as the state store. Everything is UPL-licensed Python and TypeScript with devcontainer-based workshops. It serves Oracle-centric developers evaluating the platform for agentic workloads, not teams selecting a coding harness.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/oracle-ai-developer-hub.md)
