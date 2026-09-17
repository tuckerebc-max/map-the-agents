# Blueprints (`blueprints`)

[Back to directory index](../index.md)

Directory membership: backing-only.

- Category: agent
- Provider/maker: sublayerapp
- License: MIT
- Language: Ruby
- Interface: platforms=IDE; install=Clone repo, bundle install, bin/rails db:create, bin/rails db:migrate, bin/rails tailwindcss:build, bin/rails s
- Model providers: OpenAI (GPT-4), Google (Gemini)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [sublayerapp/blueprints](../../repos/sublayerapp/blueprints.md) (source: backing, field: `source_code_url`).

## Description

(backing feed `description`, not a verified repo-code finding)
Blueprints emerged from the Sublayer team's observation that LLM code generation drifts from a team's idioms unless it is grounded in that team's actual code. The system is a self-hosted Rails app whe
Sources: [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
