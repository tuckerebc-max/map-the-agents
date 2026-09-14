# Linear-Coding-Agent-Harness (`linear-coding-agent-harness`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: coleam00
- License: MIT
- Language: Python
- Interface: platforms=Autonomous; install=npm install -g @anthropic-ai/claude-code; pip install -r requirements.txt
- Model providers: Anthropic
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [coleam00/linear-coding-agent-harness](../../repos/coleam00/linear-coding-agent-harness.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Minimal harness demonstrating long-running autonomous coding with the Claude Agent SDK; two-agent pattern (initializer + coding agent) with Linear as the core project management system for tracking all work. Uses Linear MCP (HTTP) and Puppeteer MCP (stdio).

(captured site page body (agents/linear-coding-agent-harness.md), not a verified repo-code finding)
The harness demonstrates a specific architectural idea: put the agent's entire task state in Linear rather than local files, so any session — or a new machine — can resume work by querying the tracker. An initializer agent reads an app spec, creates the Linear project, issues, and a META issue; coding agents then pull Todo issues, implement with Claude, test through Puppeteer MCP, comment results, and close issues. Session handoff happens through Linear comments, making runs resumable and inspectable from anywhere Linear is. Colem00 published it as a minimal MIT-licensed reference (2 commits) that others fork to build Linear-integrated autonomous loops.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/linear-coding-agent-harness.md)
