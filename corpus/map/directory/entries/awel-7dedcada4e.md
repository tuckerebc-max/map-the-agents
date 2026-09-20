# Awel (`awel`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: MarsZ42
- License: MIT (README) / Apache-2.0 (repo metadata - conflicting)
- Language: TypeScript, JavaScript (Node.js)
- Interface: platforms=IDE; install=Set at least one AI provider env var, then: npx awel create (new project) or cd existing-next-app && npx awel dev
- Model providers: Claude Code (Claude CLI), Anthropic API, OpenAI, Google AI, MiniMax, Zhipu AI, Vercel Gateway, OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [marsz42/awel](../../repos/marsz42/awel.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Awel puts an AI dev agent inside the running Next.js app rather than beside it: a proxy on port 3001 fronts the dev server on 3000, intercepts HTML responses, and injects a Shadow-DOM script that moun
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
