# Claude Agent SDK (TypeScript) (`claude-agent-sdk-typescript`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent-sdk
- Provider/maker: anthropics
- License: Anthropic Commercial Terms of Service
- Language: TypeScript / Node.js
- Interface: install=npm
- Model providers: Anthropic (Claude)
- Feature flags (directory-reported):
  - mcp_support: yes (SDK MCP servers for custom tools) (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a - this IS the Claude Code agent SDK (reported)
  - subagents: yes (yes)
  - hooks: yes (yes)
  - plan_mode: yes (permission modes: default, acceptEdits, plan, bypassPermissions) (yes)

Repository map entry: [anthropics/claude-agent-sdk-typescript](../../repos/anthropics/claude-agent-sdk-typescript.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=agent-sdk, backing=agent, page=agent-sdk

## Description

Highlight (site page `what_makes_it_special`): Official Anthropic SDK that programmatically embeds Claude Code's agentic capabilities (codebase understanding, file editing, shell command execution, complex workflow orchestration) into custom TypeScript/Node.js applications. The evolution of the former 'Claude Code SDK', bridging interactive Claude Code use and production-grade automated agent systems.

(captured site page body (agents/claude-agent-sdk-typescript.md), not a verified repo-code finding)
The TypeScript Agent SDK is Anthropic's mechanism for embedding Claude Code's capabilities into custom applications and infrastructure: rather than driving the interactive CLI, programs invoke the same agent loop — codebase comprehension, file edits, shell command execution, multi-step workflow orchestration — as a library call. Renamed from the Claude Code SDK in late 2025, it exposes hooks for intercepting and controlling agent behavior at lifecycle points, custom tools registered as in-process MCP servers, permission modes that gate tool use, and sessions that persist or fork for resumable workflows. Teams use it to build production agent systems on top of Claude's coding competence without shelling out to a terminal process, from CI automation to custom internal copilots. Distribution follows Anthropic's commercial terms rather than an open-source license, and the SDK is actively developed as the sanctioned TypeScript entry point to the agent runtime.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-agent-sdk-typescript.md)
