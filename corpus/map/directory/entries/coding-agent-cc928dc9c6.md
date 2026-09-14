# coding-agent (`coding-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: embabel
- License: Apache-2.0
- Language: Kotlin, Java
- Interface: install=Run via shell; finds Maven projects under peer directories of the startup directory
- Model providers: OpenAI (via the Embabel agent platform's model abstraction)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [embabel/coding-agent](../../repos/embabel/coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Headless coding agent built on the Embabel agent platform; aims to accelerate development with AI without using any commercial coding agents; explains code, creates projects, multi-file changes, writes docs, combines project code access with internet access for API research.

(captured site page body (agents/coding-agent.md), not a verified repo-code finding)
The Embabel team wanted a coding agent for JVM codebases without adopting a commercial product, and built one on their own agent platform as both a tool and a demonstration of the platform. The headless agent discovers Maven projects under peer directories of its startup directory and handles code explanation, new project creation, multi-file edits, documentation writing, and combinations of local code access with internet research such as API investigation. Shell commands provide focus management - pointing the agent at a named project - and a chat mode exists without conversational memory yet. The project is early stage with a roadmap covering non-Maven builds, token reduction, and automated PR review. JVM developers who want an agent in their native ecosystem, and Embabel platform users, are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coding-agent.md)
