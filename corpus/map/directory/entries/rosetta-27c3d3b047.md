# rosetta (`rosetta`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: griddynamics
- License: Apache-2.0
- Language: Python
- Interface: install=Install via plugin (recommended) or MCP; pip install rosetta-cli / rosetta-mcp (PyPI); then initialize and configure workspace
- Model providers: Agent-agnostic: Claude Code, Cursor, Copilot, Codex, Antigravity, OpenCode, VS Code, JetBrains, Windsurf, any MCP-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [griddynamics/rosetta](../../repos/griddynamics/rosetta.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Agent-agnostic engineering governance and context layer that loads shared, versioned, layered (core/organization/project) instructions into every AI coding session. Discipline-encoded workflows (Prepare-\>Research-\>Plan-\>Act-\>Validate) with HITL approval gates, fresh-context review subagents, execution-backed validation, and Git-controlled instruction delivery by tag (not semantic search). No source code leaves your perimeter.

(captured site page body (agents/rosetta.md), not a verified repo-code finding)
Grid Dynamics built Rosetta to solve the consistency problem when dozens of engineers use different agents: each session starts from whatever context the individual remembered to paste. A workspace initialized with rosetta loads the layered instruction stack into every session, classifies the request into one of thirteen SDLC workflow types (coding, security, test generation, requirements authoring, and others), and executes each through a Prepare, Research, Plan, Act, Validate pattern with approval gates. Skills cover planning, orchestration of subagent teams, reverse engineering, and security review, while a MEMORY.md file lets sessions accumulate project-specific learning. Enforcement is structural — dangerous-action detection, PII and secrets handling rules, deviation control with fresh-context reviewers — rather than advisory. Enterprise platform teams adopt it to make agent behavior auditable and uniform across tools.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rosetta.md)
