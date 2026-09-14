# Continue (`continue`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: continuedev
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=VS Code Marketplace, OpenVSX, npm (@continuedev/cli), GitHub Releases (JetBrains)
- Model providers: Any (BYOK via configurable providers: Anthropic, OpenAI, Ollama, and others)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [continuedev/continue](../../repos/continuedev/continue.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Pioneering open-source coding agent available as CLI, VS Code extension, and JetBrains plugin. The repository is no longer actively maintained and is read-only; a final 2.0.0 release was published as a foundation for others.

(captured site page body (agents/continue.md), not a verified repo-code finding)
Continue spent 2023-2026 as the default open-source answer to commercial coding assistants, letting developers point one interface at any model provider across a CLI, a VS Code extension, and a JetBrains plugin. Its agent loop handled multi-file edits, plan mode structured larger changes, and MCP support connected external tools. In 2026 the maintainers ended development: the repository became read-only, and a final 2.0.0 release removed anonymous telemetry, stripped out mandatory authentication, and fixed lingering bugs specifically so the Apache-2.0 codebase would be clean to fork. The team recommended the CLI as the most durable component for anyone continuing with the code. Teams that need an in-house agent base still fork it, and its extension ecosystem influenced the generation of open-source agents that followed.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/continue.md)
