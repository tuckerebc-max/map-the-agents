# Claude Agent SDK (Python) (`claude-agent-sdk-python`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: anthropics
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [anthropics/claude-agent-sdk-python](../../repos/anthropics/claude-agent-sdk-python.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Official Anthropic Python SDK for building agentic applications powered by Claude Code. In-process SDK MCP servers let custom tools run in the same Python process (no subprocess overhead, better performance, easier debugging, type safety). Auto-bundled Claude Code CLI -- no separate installation needed. Programmable hooks (PreToolUse etc.) for intercepting and controlling agent behavior at lifecycle points. Bidirectional conversations via ClaudeSDKClient ...

(captured site page body (agents/claude-agent-sdk-python.md), not a verified repo-code finding)
The Claude Agent SDK for Python is Anthropic's supported way to embed Claude Code's agent loop inside Python applications: it drives the same codebase-aware, tool-using agent programmatically rather than interactively. Custom tools are defined as plain Python functions through a @tool decorator backed by in-process MCP servers, avoiding subprocess overhead while remaining interoperable with external stdio MCP servers; hooks intercept lifecycle events such as PreToolUse for permission and safety control, and the SDK supports subagents and session forking for multi-step workflows. The package bundles the Claude Code CLI automatically, so installation is a single pip install without separate setup. Teams use it to build production automation on top of Claude's agentic capabilities — CI pipelines, internal tooling, and custom agent products — with usage governed by Anthropic's commercial terms. It is actively maintained alongside the TypeScript SDK.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-agent-sdk-python.md)
