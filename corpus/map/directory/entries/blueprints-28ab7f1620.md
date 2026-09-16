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
Sources: [backing feed @ 8664d24144c7](https://github.com/prime-radiant-inc/alltheagents.org/blob/8664d24144c79ac7400a6799c00f070897d856a6/_data/agents.json)
