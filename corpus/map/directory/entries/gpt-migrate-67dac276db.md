# GPT Migrate (`gpt-migrate`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: joshpxyne
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenRouter, OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [0xpayne/gpt-migrate](https://github.com/0xpayne/gpt-migrate) (source: backing, field: `source_code_url`) now resolves to [joshpxyne/gpt-migrate](../../repos/joshpxyne/gpt-migrate.md) (github id 658136967, verified [https://github.com/joshpxyne/gpt-migrate](https://github.com/joshpxyne/gpt-migrate)).

## Description

Highlight (site page `what_makes_it_special`): Automated full-codebase migration across languages/frameworks using LLMs. Spins up a Docker environment for the target language, recursively rebuilds code from a source entry file, iteratively debugs using logs/errors/context, generates and validates unit tests. Hierarchical prompt design system (p1-p4 preference levels). Currently development alpha.

(captured site page body (agents/gpt-migrate.md), not a verified repo-code finding)
GPT Migrate attacks the problem most coding assistants avoid: porting an entire codebase from one language or framework to another, such as Flask to Node.js. It stands up a Docker environment for the destination language, recursively rebuilds the application outward from a source entry file, generates unit tests, and iteratively debugs the rewritten code against them using error logs and context. A hierarchical prompt system (p1 through p4 preference levels) organizes instructions, and OpenAI or OpenRouter keys drive the model calls. It is MIT-licensed but explicitly a development alpha with high token costs for full-codebase rewrites; with 75 commits and no releases since 2024, it remains a well-known alpha rather than a maintained tool.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/gpt-migrate.md)
