# .better-coding-agents (`better-coding-agents`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: bmdavis419
- License: unknown
- Language: TypeScript
- Interface: install=Clone into ~/.better-coding-agents and run the init command (copies slash commands for OpenCode & Cursor, plus an OpenCode theme)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [bmdavis419/.better-coding-agents](../../repos/bmdavis419/.better-coding-agents.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Utility that clones full source repos of libraries (Svelte/SvelteKit, Effect.ts, neverthrow, opencode) as git subtrees so coding agents can search the actual library codebase rather than relying on training data.

(captured site page body (agents/better-coding-agents.md), not a verified repo-code finding)
Coding agents answer library questions from training data, which goes stale and produces hallucinated APIs. This project's remedy is deliberately simple: clone the full source repositories of Svelte/SvelteKit, Effect, neverthrow, and opencode as git subtrees into a home-directory repo, then provide OpenCode and Cursor slash commands plus a dedicated OpenCode agent that instructs the coding agent to search those real codebases before answering. A single init command upserts agent definitions, commands, and themes into the OpenCode and Cursor config directories, so setup takes seconds and works alongside existing tooling. A custom OpenCode theme rounds out the package. It is a small community utility (168 stars) for developers who want grounded, current library answers from their existing agents.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/better-coding-agents.md)
