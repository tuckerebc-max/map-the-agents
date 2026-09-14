# open-aware (`open-aware`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: qodo-ai
- License: MIT
- Language: TypeScript
- Interface: install=Add MCP server config: {'mcpServers':{'open-aware':{'url':'https://open-aware.qodo.ai/mcp'}}}  (or via npm install -g mcp-remote proxy)
- Model providers: none (model-agnostic; the calling client's model invokes the MCP tools)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [qodo-ai/open-aware](../../repos/qodo-ai/open-aware.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Semantic code intelligence across multiple repositories simultaneously (cross-repo analysis) exposed via MCP, with daily updated indexes of popular OSS libraries and vector embeddings. Provides get_context (semantic code search), deep_research (architecture/implementation analysis), and ask (coding questions) tools.

(captured site page body (agents/open-aware.md), not a verified repo-code finding)
Coding agents frequently misanswer questions about third-party libraries because their training data is stale and the repositories involved are too large to clone on demand. Qodo's Open Aware closes that gap by maintaining daily-updated indexes of popular open-source repositories and exposing them over a public MCP endpoint with three tools: get_context for semantic code search across multiple repositories at once, deep_research for architecture analysis and implementation planning, and ask for direct coding questions. Clients connect via Streamable HTTP or an mcp-remote proxy with no local indexing, and a Gemini CLI extension exists for that ecosystem. The free tier is rate-limited to roughly ten calls per minute and covers only the pre-indexed public repositories; private repos and custom indexing require the commercial Qodo Aware product. It suits developers whose agents need ground truth about dependencies and cross-repository architecture rather than another local search tool.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-aware.md)
