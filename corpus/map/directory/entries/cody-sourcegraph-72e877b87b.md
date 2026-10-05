# Cody (Sourcegraph) (`cody-sourcegraph`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=IDE, Web; install=IDE extensions for VS Code, JetBrains, and Visual Studio; also available as Cody CLI and Cody Web (in Sourcegraph web app)
- Model providers: Multiple (Anthropic, OpenAI, Google, and others routed through Sourcegraph's infrastructure)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): AI code assistant that uses Sourcegraph's code search to pull context from local and remote codebases; available as IDE extensions (VS Code, JetBrains, Visual Studio), CLI, and web app; public source snapshot archived Aug 1, 2025 (development moved to a private repo)

(captured site page body (agents/cody-sourcegraph.md), not a verified repo-code finding)
Code answers usually live outside the file a developer has open, which is the gap Sourcegraph built its search business on and Cody extends into an assistant. Chat with @-mentions reaches into files, symbols, and whole remote repositories through Sourcegraph's search index, auto-edit proposes contextual changes from the cursor, and context filters let teams exclude repositories the assistant should not see. The assistant ships as extensions for VS Code, JetBrains, and Visual Studio, plus a web app, a CLI, and an Enterprise distribution integrated with Sourcegraph Code Search. Individuals use it through Sourcegraph.com while enterprises deploy it against their own Sourcegraph instance. Privacy terms state that customer code is not used to train models. Teams already running Sourcegraph are its natural users.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/cody-sourcegraph.md)
