# Blueprints (`blueprints`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
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

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Stores chunks of code (blueprints) and uses them as a base for LLMs (GPT-4/Gemini) to generate new code based on patterns in your codebase; editor plugins for Vim, VSCode, IntelliJ, SublimeText

(captured site page body (agents/blueprints.md), not a verified repo-code finding)
Blueprints emerged from the Sublayer team's observation that LLM code generation drifts from a team's idioms unless it is grounded in that team's actual code. The system is a self-hosted Rails app where developers save code chunks as named, described 'blueprints'; each save triggers GPT-4 to name and describe the chunk, and its vector embedding lands in Postgres via pgvector. Later, from Vim, VS Code, IntelliJ, or Sublime Text, a developer highlights code, and the plugin finds the most similar blueprint, sends its code and description to GPT-4 or Gemini, and splices the generated variant back over the selection. This turns a codebase's own patterns into reusable generation context, predating the now-common embedding-backed codebase retrieval in coding agents. Development has been dormant since 2024, with 61 stars and no recent commits, but it remains a readable example of retrieval-grounded code generation.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/blueprints.md)
