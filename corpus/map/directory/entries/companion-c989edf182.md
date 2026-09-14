# companion (`companion`)

[Back to directory index](../index.md)

Directory membership: backing-only.

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

(backing feed `description`, not a verified repo-code finding)
Quack AI's companion backend served the server side of a self-hosted, team-context alternative to GitHub Copilot. The FastAPI service sat in front of an Ollama inference container running OSS models s
Sources: [backing feed @ 0861b8ee1c27](https://github.com/prime-radiant-inc/alltheagents.org/blob/0861b8ee1c271047d55caa72efdfc3a6d2046174/_data/agents.json)
