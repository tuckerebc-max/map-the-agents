# Graphql-Cli (`graphql-cli`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Urigo
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: none
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [urigo/graphql-cli](../../repos/urigo/graphql-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Command line tool for common GraphQL development workflows with a modular plugin architecture where each command is a separate package; integrates with GraphQL Code Generator, Graphback, and GraphQL Inspector, and supports schema init from OpenAPI/Swagger endpoints.

(captured site page body (agents/graphql-cli.md), not a verified repo-code finding)
graphql-cli is a command-line toolkit from The Guild covering routine GraphQL development workflows: project scaffolding, code generation, schema diffing, coverage analysis, validation, and a local mock server. Its architecture makes each command an independently installable npm package configured through the extensions field of a project's graphql-config file, so teams install only the commands they use and can publish their own plugins against the same interface. Because it reads the standard graphql-config file, its behavior stays consistent between the CLI and editor integrations. The project has been maintained since 2017 with a v4 line that introduced breaking changes from 3.x, and it contains no AI features — its inclusion in an agent census rests solely on its plugin architecture.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/graphql-cli.md)
