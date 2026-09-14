# Microsoft Agent Framework (`microsoft-agent-framework`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: unknown
- License: MIT
- Language: Python, C#
- Interface: install=Python: pip install agent-framework; .NET: dotnet add package Microsoft.Agents.AI; Go: go get github.com/microsoft/agent-framework-go
- Model providers: Microsoft Foundry, Anthropic, Azure OpenAI, OpenAI, Ollama, GitHub Copilot SDK
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (middleware, tools, Agent Skills, AF Labs) (yes)
  - claude_code_plugin: unknown (unknown)
  - subagents: yes (multi-agent graph-based workflows) (yes)
  - hooks: yes (middleware for intercepting agent actions) (yes)
  - plan_mode: yes (Harness Agent with planning and todo tracking) (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): The direct successor to both Semantic Kernel and AutoGen (created by the same teams), merging AutoGen's simple agent abstractions with Semantic Kernel's enterprise-grade features. Adds graph-based workflows for explicit multi-agent orchestration, robust state management, durability, human-in-the-loop control, OpenTelemetry observability, declarative YAML agents, and an interactive DevUI for development/debugging.

(captured site page body (agents/microsoft-agent-framework.md), not a verified repo-code finding)
Microsoft merged its two agent lineages — AutoGen's research abstractions and Semantic Kernel's enterprise machinery — into a single framework maintained by the same teams, so organizations no longer choose between them. Core mechanics center on graph-based workflows that connect agents and functions with typed state, checkpoints, and human-in-the-loop nodes, while middleware intercepts agent actions and MCP supplies tools. A batteries-included Harness Agent adds planning, todo tracking, context compaction, and tool approval for long multi-step tasks, and declarative YAML lets agents be defined without code. Distribution follows conventional SDK channels — Microsoft.Agents.AI for .NET, agent-framework on PyPI, and a public-preview Go module — with OpenTelemetry observability and a DevUI for stepping through workflow graphs. The audience is enterprise .NET and Python teams standardizing on Microsoft Foundry, Azure OpenAI, OpenAI, Anthropic, or Ollama; teams migrating from AutoGen or Semantic Kernel use it as the consolidation path.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/microsoft-agent-framework.md)
