# stacklit (`stacklit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: glincker
- License: MIT
- Language: Go
- Interface: platforms=IDE; install=npx stacklit init (recommended), npm install -g stacklit, go install ...@latest, or binary from GitHub Releases
- Model providers: Claude (optional --summary flag); otherwise runs locally with no LLM needed
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: True (reported)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [glincker/stacklit](../../repos/glincker/stacklit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): ~250-token structured index vs 50k-500k full-dump approaches (Repomix, code2prompt); committable JSON + Merkle diagram; interactive HTML visual map (4 views); works with any AI tool that reads files; no server/setup required

(captured site page body (agents/stacklit.md), not a verified repo-code finding)
stacklit attacks the token cost of codebase orientation: where full-dump tools paste 50,000-500,000 tokens, it parses eleven languages with tree-sitter and writes a committable ~250-4,000 token index of modules, exports with signatures, dependencies, and hints such as where a feature belongs and what the test command is. A post-commit git hook regenerates the index using Merkle hashes to skip unchanged subtrees, taking roughly 50 ms on a 10k-line repo. stacklit serve exposes seven MCP tools that Claude Desktop and Cursor can call, and stacklit setup writes the navigation map into CLAUDE.md, .cursorrules, or aider config automatically. An optional --summary flag is the only network call; everything else runs locally. It targets teams whose agents waste context exploring rather than editing.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stacklit.md)
