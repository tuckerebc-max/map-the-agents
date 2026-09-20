# gpt-rag-orchestrator (`gpt-rag-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing-only.

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

(backing feed `description`, not a verified repo-code finding)
Enterprises deploying GPT-RAG need a component that decides how each question is answered — which agent, which retrieval backend, which tools — and this orchestrator is that brain within the Azure GPT
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
