# cuga-agent (`cuga-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing.

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

(published index `description`, not a verified repo-code finding)
CUGA, developed at IBM Research, targets enterprises that need agents to operate web applications and APIs under policy constraints rather than a developer's local code editor. Its architecture compos
Sources: [published index (sha256:9bbe35d19750)](https://alltheagents.org/agents.json); [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
