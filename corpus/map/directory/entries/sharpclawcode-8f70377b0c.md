# SharpClawCode (`sharpclawcode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Independent
- License: MIT
- Language: C#
- Interface: platforms=CLI; install=git clone + dotnet build; run via dotnet run --project src/SharpClaw.Code.Cli; requires .NET SDK 10
- Model providers: Anthropic, OpenAI-compatible, Ollama, llama.cpp
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [sharpclaw/sharpclawcode](../../repos/sharpclaw/sharpclawcode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): C# and .NET 10-native coding agent runtime for teams building AI developer tools, agentic CLIs, and MCP-enabled workflows. Ships a terminal-first agent runtime plus embeddable host SDK. Features durable sessions, permission-aware tool execution, provider abstraction, structured telemetry, MCP integration with lifecycle state, plugin discovery, workspace indexing, cross-session memory, and lifecycle hooks (turn/tool/share/server events). Has both 'plan' and 'spec' modes. Note: ...

(captured site page body (agents/sharpclawcode.md), not a verified repo-code finding)
SharpClawCode brings the Claude Code/opencode pattern to teams standardized on C#, built on the Microsoft Agent Framework with a modular solution of roughly twenty projects spanning runtime, agents, tools, permissions, providers, MCP, and sessions. Sessions are durable — persistent conversation state, checkpoints, append-only event logs, replay, and cross-session project memory — and permissions follow modes from readOnly to dangerFullAccess with approval gates and budgets. Providers cover Anthropic and OpenAI-compatible endpoints plus a local catalog for Ollama and llama.cpp, and plugins, workspace skills, hooks, and worktrees round out the harness surface. The repository has moved to the clawdotnet organization, so the previously listed sharpclaw URL now 404s; the census URL should be updated. It is MIT-licensed, actively developed with strong in-repo documentation, and aimed at .NET teams embedding agents rather than end users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/sharpclawcode.md)
