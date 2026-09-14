# OpenCastle (`opencastle`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: monkilabs
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npx opencastle init
- Model providers: none of its own (capability tiers premium/standard/economy resolved by each target assistant)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [monkilabs/opencastle](../../repos/monkilabs/opencastle.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Compiles one source AI assistant config into multiple assistant formats (Claude Code, GitHub Copilot, Cursor, Windsurf, OpenCode, Codex CLI, Antigravity); detects drift and keeps configs in sync across CI; includes 13 role definitions and experimental Convoy Engine that executes multi-step tasks across git worktrees with planning, execution, and quality gates

(captured site page body (agents/opencastle.md), not a verified repo-code finding)
Teams running several AI coding assistants maintain parallel config files — CLAUDE.md, .cursorrules, .windsurfrules, AGENTS.md, .github agents — that diverge the first time someone updates one and forgets the rest. OpenCastle treats the assistant config as a compiled artifact: a TypeScript CLI reads one source config, inspects the repository for frameworks and existing configs, and emits native-format outputs for Claude Code, GitHub Copilot, Cursor, Windsurf, OpenCode, Codex CLI, and Antigravity, including MCP server definitions in each assistant's expected shape. A status command reports drift across targets, sync --check gates CI against drift, and npx opencastle init scaffolds without overwriting existing files. Thirteen role agents, 31 domain skills, and nine workflow templates ship in the box, and an experimental Convoy engine adds multi-agent orchestration across isolated git worktrees with SQLite-backed resume. Platform teams standardizing assistant behavior across tool estates are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencastle.md)
