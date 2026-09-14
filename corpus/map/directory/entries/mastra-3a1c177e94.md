# Mastra (`mastra`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: mastra-ai
- License: NOASSERTION
- Language: TypeScript
- Interface: platforms=CLI, Web; install=npm (npx create-mastra)
- Model providers: 40+ providers via unified model routing (OpenAI, Anthropic, Google, Groq, Cohere, local)
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mastra-ai/mastra](../../repos/mastra-ai/mastra.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): It is a TypeScript-native agent framework from the Gatsby creators: graph-based workflows with durable human-in-the-loop suspend/resume, Observational Memory, a Harness subsystem (workspace, shell tools, task tracking) for building coding agents, and MCP support in both directions - exposing Mastra agents as MCP servers and consuming external MCP servers.

(captured site page body (agents/mastra.md), not a verified repo-code finding)
Mastra gives TypeScript teams the primitives usually associated with Python agent frameworks: agents with tool calling and stopping conditions, workflows composed with .then()/.branch()/.parallel() that can suspend for human approval and resume with durable state, and memory that spans conversation history and retrieval. Model routing abstracts 40+ providers behind one interface, Mastra Studio provides a local UI for inspecting and testing agents, and evals integrate with deployment. A dedicated Harness subsystem packages workspace, shell tools, memory, and task tracking for building coding agents, and Mastracode skills integrate with Claude Code and Cursor. YC-backed and very actively maintained (27k+ stars), it targets product engineers embedding agents in applications.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mastra.md)
