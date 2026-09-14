# CodingAgentExplorer (`codingagentexplorer`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: tndata
- License: MIT
- Language: C# / .NET 10 (vanilla HTML/JS/CSS frontend)
- Interface: install=git clone, dotnet build, dotnet run --project CodingAgentExplorer; configure with EnableProxy.sh/bat
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [tndata/codingagentexplorer](../../repos/tndata/codingagentexplorer.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Real-time .NET proxy and dashboard for inspecting Claude Code API calls. Transparent proxy architecture using YARP and SignalR. Captures MCP tool calls between Claude Code and HTTP-based MCP servers (port 9999). HookAgent CLI bridges Claude Code's hook system with 15 hook events. API keys automatically redacted for security. Note: this is an inspection/observability tool, not a coding agent harness itself.

(captured site page body (agents/codingagentexplorer.md), not a verified repo-code finding)
Claude Code hides its API traffic in the terminal, which makes it hard to debug hook behavior, MCP server interactions, or unexpected token usage, and it gives instructors nothing to show students. Coding Agent Explorer inserts itself as a localhost reverse proxy: Claude Code is pointed at it via ANTHROPIC_BASE_URL, the proxy forwards to the Anthropic API, and a SignalR dashboard renders every request, response, streaming event, and MCP JSON-RPC call as a live chat-style timeline with token usage and latency per request. A companion HookAgent CLI captures all fifteen Claude Code hook event types and posts them to the same dashboard. Storage is in-memory (capped at 1,000 requests), API keys are redacted, and everything stays on localhost. It is used by developers debugging MCP servers and hooks, and by .NET instructor Tore Nestenius in his AI agent workshops.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codingagentexplorer.md)
