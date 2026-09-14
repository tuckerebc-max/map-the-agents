# CodeMachine-CLI (`codemachine-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: moazbuilds
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=CLI; install=npm
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: n/a (reported)
  - subagents: yes (yes)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [moazbuilds/codemachine-cli](../../repos/moazbuilds/codemachine-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Orchestration layer that runs AI coding CLIs (Claude Code, Codex, Cursor) through structured, long-running, repeatable workflows with parallel execution, context engineering, and multi-agent coordination.

(captured site page body (agents/codemachine-cli.md), not a verified repo-code finding)
CodeMachine-CLI starts from the observation that a coding workflow — the sequence of steps an operator runs an agent through to fix a bug or build a feature — normally exists only in the operator's head and gets rebuilt each session. The tool captures such workflows as definitions and re-executes them, spawning headless coding-agent CLIs (Claude Code, Codex, Cursor, and others), passing context between agents, running steps in parallel, and persisting state across runs that can span hours or days. It positions itself as an orchestration layer rather than an agent: the underlying coding engines do the work while CodeMachine handles coordination, agent-to-agent communication, and reproducibility. It is installed via npm, documented at docs.codemachine.co, and developed openly on GitHub with an active community.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codemachine-cli.md)
