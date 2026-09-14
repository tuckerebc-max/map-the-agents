# Nous (`nous`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: TrafficGuard
- License: MIT
- Language: TypeScript
- Interface: platforms=Autonomous; install=docker
- Model providers: OpenAI, Anthropic, Google Gemini, Groq, Fireworks, Together.ai, DeepSeek, Ollama, Cerebras, SambaNova, OpenRouter, X.ai
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry (renamed): original lead [trafficguard/nous](https://github.com/trafficguard/nous) (source: backing, field: `source_code_url`) now resolves to [trafficguard/typedai](../../repos/trafficguard/typedai.md) (github id 784586462, verified [https://github.com/TrafficGuard/typedai](https://github.com/TrafficGuard/typedai)).

## Description

Highlight (site page `what_makes_it_special`): Note: the repo at TrafficGuard/nous contains a project named 'TypedAI' (the repo may have been renamed/redirected). TypeScript-first AI platform for developing and running autonomous AI agents, LLM-based workflows, and chatbots. Does NOT use LangChain (intentional design decision). Automated LLM function schema generation via @func decorators (no JSON/zod duplication). Multi-agent extend-reasoning. Full SDLC support (code editing, PR creation, code review). Sandboxed ...

(captured site page body (agents/nous.md), not a verified repo-code finding)
TypedAI (the project in the TrafficGuard/nous repository) is a TypeScript platform for building autonomous agents, LLM workflows, and chatbots without LangChain, using static typing and simple control flow so behavior is debuggable with ordinary breakpoints. Its software-engineering agents cover local code editing with an edit-compile-lint-test-fix loop, ticket-to-PR workflows across GitHub and GitLab, and configurable code review with inline merge request comments. Function schemas are generated from source via a decorator, avoiding duplicate schema definitions. Deployment spans local CLI, Docker, or scale-to-zero Google Cloud Run with SSO, and the codebase is partly maintained by its own agents. A web UI and Slack chatbot provide interfaces beyond the terminal.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/nous.md)
