# cuga-agent (`cuga-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: cuga-project
- License: Apache-2.0
- Language: Python
- Interface: platforms=Web; install=pip
- Model providers: OpenAI, IBM WatsonX, Azure OpenAI, Groq, OpenRouter, LiteLLM
- Feature flags (directory-reported):
  - mcp_support: yes — full MCP support; wire MCP servers via mcp_servers.yaml; CUGA can also act as an MCP server itself (CUGA-as-MCP) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes — CugaSupervisor orchestrates multiple agents; delegates tasks to specialized sub-agents; mixes local CugaAgent instances with remote A2A agents (yes)
  - hooks: yes — human-in-the-loop (HITL) approval gates at critical decision points; Tool Approval policy requiring human approval before tool execution (yes)
  - plan_mode: yes — planner-executor pattern with structured planning and task decomposition; Playbook policies provide step-by-step workflow guidance (yes)

Repository map entry: [cuga-project/cuga-agent](../../repos/cuga-project/cuga-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): "Open-source generalist agent harness ranked

(captured site page body (agents/cuga-agent.md), not a verified repo-code finding)
CUGA, developed at IBM Research, targets enterprises that need agents to operate web applications and APIs under policy constraints rather than a developer's local code editor. Its architecture composes tools from OpenAPI specs, MCP servers, and LangChain integrations, layers a five-type policy system and human-in-the-loop approval gates over execution, and can delegate to specialized sub-agents through a supervisor that mixes local and remote A2A agents. The project's benchmark record (top of AppWorld from July 2025 and WebArena from February 2025) anchors its credibility, and deployment paths range from a local uv-managed install to Docker and Helm charts on Kubernetes. Users are enterprise automation teams, with models provisioned through OpenAI-compatible endpoints, watsonx, and other providers.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/cuga-agent.md)
