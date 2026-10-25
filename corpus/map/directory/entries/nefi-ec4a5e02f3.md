# nefi (`nefi`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Blazity
- License: MIT
- Language: TypeScript
- Interface: install=npm (npx nefi / global install); requires an Anthropic API key
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [blazity/nefi](../../repos/blazity/nefi.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI agent that automates code management and feature integration in Next.js codebases (primarily the next-enterprise boilerplate) through natural language commands, handling tasks like git operations, package management, and file modifications. Eliminates manual boilerplate configuration (e.g., 'remove storybook from my project').

(captured site page body (agents/nefi.md), not a verified repo-code finding)
nefi grew out of Blazity's maintenance of its next-enterprise Next.js boilerplate, where routine customization tasks consumed disproportionate time. It exposes natural-language commands that the agent translates into git operations, package management, and file edits against the project. The tool runs from the command line in the target repository and is built on the Vercel AI SDK with Claude models. Its scope is deliberately narrow: Next.js 14/15 codebases, primarily the next-enterprise template, rather than general-purpose coding. The repository has had no releases and modest activity, positioning it as an early-stage companion to the boilerplate.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/nefi.md)
