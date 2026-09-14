# refakts (`refakts`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: devill
- License: PolyForm Noncommercial License 1.0.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g refakts
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [devill/refakts](../../repos/devill/refakts.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI refactoring tool built 'by AI agents, for AI agents' that enables surgical refactoring operations (rename, extract variable, inline variable, find usages, move file) via AST manipulation instead of regenerating whole files; features automated quality habits via post-commit hooks that detect code smells and prompt agents to refactor.

(captured site page body (agents/refakts.md), not a verified repo-code finding)
RefakTS exists because AI coding agents are bad at refactoring: regenerating whole files wastes tokens and risks breaking untouched code, while string replacement misses multi-location changes. Built on ts-morph and tsquery, it exposes location-based operations — select, rename, extract-variable, inline-variable, find-usages, move-file, sort-methods — that an agent invokes through the shell to make precise, syntax-aware edits without touching surrounding code. The project doubles as an experiment in agent-driven development: its roadmap is managed by Claude instances that vote on features, humans contribute by pointing Claude Code at the issue tracker, and automated post-commit hooks detect code smells like duplication and dead code, prompting the agent to fix them in line with XP habits. It is labeled a proof of concept, with core operations working and more commands in development. Developers use it as a tool their coding agent calls for safe, token-efficient refactors under a PolyForm Noncommercial license.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/refakts.md)
