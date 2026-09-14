# gpt-rag-orchestrator (`gpt-rag-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Azure
- License: MIT
- Language: Python, TypeScript
- Interface: install=azd init -t azure/gpt-rag-orchestrator -\> azd env refresh -\> azd deploy (recommended); or PowerShell script (scripts/deploy.ps1)
- Model providers: Azure OpenAI, Azure AI Foundry Agent Service v2
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [azure/gpt-rag-orchestrator](../../repos/azure/gpt-rag-orchestrator.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-strategy agentic RAG orchestration with dynamic routing; MCP support (SSE + streamable HTTP); NL2SQL for structured data; Work IQ (Microsoft 365) knowledge source integration; Toolbox OAuth identity passthrough for Foundry hosted agents; versioned audit events with HMAC pseudonymization; optional admin dashboard with Entra ID auth; configurable retrieval backends with Foundry IQ generic MCP knowledge sources

(captured site page body (agents/gpt-rag-orchestrator.md), not a verified repo-code finding)
Enterprises deploying GPT-RAG need a component that decides how each question is answered — which agent, which retrieval backend, which tools — and this orchestrator is that brain within the Azure GPT-RAG accelerator. Built on Azure AI Foundry Agent Service and the Microsoft Agent Framework, it selects among strategies including single-agent RAG, MCP tool orchestration over SSE or streamable HTTP, and NL2SQL against read-only SQL Server or Azure SQL sources, pulling knowledge from Azure AI Search, Blob, Foundry IQ, and Microsoft 365 Work IQ. Versioned audit events with HMAC pseudonymization, an optional Entra ID-gated dashboard, and Toolbox OAuth identity passthrough target regulated environments. It is MIT-licensed Python/TypeScript deployed via azd, and it orchestrates answers rather than code.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/gpt-rag-orchestrator.md)
