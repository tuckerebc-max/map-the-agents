# Micro Agent (`micro-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Independent
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g @builder.io/micro-agent (Node.js 18+)
- Model providers: Anthropic, OpenAI, Ollama, any OpenAI-compatible endpoint (Groq)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [micro-agent/micro-agent](../../repos/micro-agent/micro-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Lightweight AI coding agent for terminal

(captured site page body (agents/micro-agent.md), not a verified repo-code finding)
BuilderIO built Micro Agent around a critique of general-purpose coding agents: given too much freedom they compound errors, so the harness narrows the loop to test-driven iteration. The user supplies a prompt and a file; the agent generates a unit test that defines correct behavior, then regenerates the target file and reruns the test command (npm test or any script) until everything passes, with an optional .prompt.md file steering generation and interactive mode asking clarifying questions. It deliberately will not install modules, write multiple files, or take other high-blast-radius actions — the README compares general agents to a Roomba stuck under a table. Providers are configured via API keys for Claude, OpenAI, Ollama, or any OpenAI-compatible endpoint such as Groq, installed globally through npm with Node 18+. Frontend teams used it for component generation, including a Figma-to-code workflow via Builder's Figma integration; development stopped after November 2024.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/micro-agent.md)
