# companion (`companion`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: quack-ai
- License: Apache-2.0
- Language: Python
- Interface: platforms=IDE; install=git clone + cp .env.example .env + docker compose pull && docker compose up
- Model providers: Ollama (Phi 3, Llama 3, CodeQwen, Mistral)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [quack-ai/companion](../../repos/quack-ai/companion.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Backend API service that acts as an instantly-onboarded team member with knowledge of internal libraries and coding standards; provides code chat endpoint and REST API for guideline management, used via a VSCode extension.

(captured site page body (agents/companion.md), not a verified repo-code finding)
Quack AI's companion backend served the server side of a self-hosted, team-context alternative to GitHub Copilot. The FastAPI service sat in front of an Ollama inference container running OSS models such as Phi 3, Llama 3, CodeQwen, and Mistral, exposing a code-chat endpoint plus a REST API for storing and curating the team's coding guidelines and internal library knowledge, which were injected as context into chat responses. Docker Compose brought up the API, an APM dashboard, and a Gradio chat UI together, and the Quack Companion VS Code extension was its primary client. The premise was that a team's coding standards, not model scale, determine assistant quality. Development stopped and the repository was archived on October 11, 2024, remaining as a read-only archive.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/companion.md)
