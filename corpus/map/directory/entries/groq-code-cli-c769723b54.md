# Groq Code CLI (`groq-code-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: build-with-groq
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: Groq, OpenRouter (community fork)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [build-with-groq/groq-code-cli](../../repos/build-with-groq/groq-code-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Intentionally minimal and hackable coding CLI — the antithesis of feature-rich CLIs. Designed as a blueprint/building block that developers modify directly (no plugin layer). Includes familiar CLI features (slash commands, tools, TUI). Leverages Groq's fast inference for rapid iteration. Invites developers to add their own slash commands, tools, and UI customizations.

(captured site page body (agents/groq-code-cli.md), not a verified repo-code finding)
groq-code-cli is a deliberately small coding agent published under Groq's build-with-groq organization, positioned as a starting point rather than a finished product. It provides an interactive TUI with file tools, slash commands, model switching across Groq's catalog, session token stats, and reasoning display, while omitting the plugin systems and permission layers found in larger agent CLIs. The codebase is intentionally small and documented — tools, commands, and UI live in clearly separated directories — and the README walks through adding tools, commands, and even renaming the binary, with a community OpenRouter fork showing the fork-and-extend workflow in practice. It is aimed at developers who want to understand or build a coding CLI rather than adopt a finished product, and Groq's low-latency inference keeps the edit-test loop fast.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/groq-code-cli.md)
