# claudecode-orchestrator (`claudecode-orchestrator`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: darrenapfel
- License: unknown
- Language: TypeScript, JavaScript (shell script entry point)
- Interface: platforms=Autonomous; install=./orchestrator.sh global (replaces ~/.claude/claude.md); ./orchestrator.sh local in any project
- Model providers: Claude Code
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [darrenapfel/claudecode-orchestrator](../../repos/darrenapfel/claudecode-orchestrator.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): Orchestration framework that runs Claude Code as a 12-persona software team (Orchestrator, PM, Architect, SWE, UX, SDET, Test, Integration, Performance, Security, DevOps, Docs) working in parallel; enforces evidence-based validation where every task produces an EVIDENCE.md; milestones end with a live, running service started and smoke-tested for the user; documented fix cycles on validation failures; structured human feedback loop. DEPRECATED in ...

(captured site page body (agents/claudecode-orchestrator.md), not a verified repo-code finding)
The framework imposes software-team process on a single agent: personas with explicit file-ownership boundaries prevent two roles from editing the same area, and the orchestrator is required to dispatch independent work simultaneously, with a parallel-execution detector flagging lapses into sequential behavior. Milestones structure work from discovery through requirements, parallel implementation, integration, validation, and fix cycles, with every task producing evidence files and automatic git commits so progress is auditable. The author has deprecated the project in favor of a commercial successor (limeriq.ai), so it no longer receives maintenance.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claudecode-orchestrator.md)
