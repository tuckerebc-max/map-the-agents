# OpenCodeReview (`opencodereview`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: agent
- Provider/maker: alibaba
- License: Apache-2.0
- Language: Go
- Interface: platforms=CLI; install=npm
- Model providers: OpenAI, Anthropic, BYOK (custom endpoints)
- Feature flags (directory-reported):
  - mcp_support: yes (transport not documented; MCP server at open-codereview.ai/docs/mcp) (yes)
  - plugin_support: yes (plugins for Claude Code, Codex, Cursor, OpenCode, VSCode extension) (yes)
  - claude_code_plugin: yes (review slash commands plugin) (yes)
  - subagents: yes (smart file bundling, each bundle runs as a sub-agent with isolated context) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [alibaba/open-code-review](../../repos/alibaba/open-code-review.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
Running a general-purpose coding agent over every pull request is expensive and imprecise, which is why Alibaba built OpenCodeReview: two years of internal use across tens of thousands of developers s
Sources: [published index (sha256:9880388de40d)](https://alltheagents.org/agents.json); [backing feed @ 31f43ac34715](https://github.com/prime-radiant-inc/alltheagents.org/blob/31f43ac34715aad88b365d22cea660ea6f41b81d/_data/agents.json)
