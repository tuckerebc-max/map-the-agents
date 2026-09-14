# ref-tools-mcp (`ref-tools-mcp`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: ref-tools
- License: MIT
- Language: TypeScript
- Interface: install=npm
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (Streamable-HTTP recommended, stdio legacy) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [ref-tools/ref-tools-mcp](../../repos/ref-tools/ref-tools-mcp.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Token-efficient agentic documentation search MCP server. Reduces 'context rot' by filtering repeated results within sessions and returning only the ~5k most relevant tokens per page based on search history. Supports both public web/GitHub docs and private repos/PDFs. Includes OpenAI deep research compatibility. Works with Claude Code, Cursor, and OpenAI deep research.

(captured site page body (agents/ref-tools-mcp.md), not a verified repo-code finding)
Documentation lookups are one of the fastest ways a coding agent burns its context window: a naive page fetch returns 20k+ tokens of boilerplate, and repeated searches echo the same results. Ref's MCP server attacks this with session-aware search that filters duplicates across a session's history and returns only about five thousand of the most relevant tokens per page, calibrated to what the agent's search trajectory suggests it needs. It exposes just two tools — search documentation and read a URL — with a hosted HTTP endpoint as the recommended deployment and a legacy stdio server in this repository. Public web and GitHub documentation can be blended with private sources like internal repos and PDFs, and the tools map onto OpenAI deep research's search/fetch contract. Developers wiring Claude Code, Cursor, or other MCP clients use it to keep doc research cheap and precise.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ref-tools-mcp.md)
