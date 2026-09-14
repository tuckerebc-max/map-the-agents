# Ralph Workflow (`ralph-workflow`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Ralph-Workflow
- License: AGPL-3.0-or-later
- Language: Python
- Interface: platforms=CLI; install=From ralph-workflow/ directory: make install (stable) or make dev (dev build). Also available via PyPI.
- Model providers: Claude Code, Codex, OpenCode, Nanocoder, AGY (Google Anti Gravity), Pi, Cursor, Kimi Code (9 built-in agent backends)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [ralph-workflow/ralph-workflow](../../repos/ralph-workflow/ralph-workflow.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Independent reference implementation of the Ralph Loop pattern (attributed to Geoffrey Huntley). Multi-agent orchestrator supporting 9 coding agent backends. Local-first. Ralph loop workflow: plan → build → verify → fix. 5,923 commits with CI via Woodpecker.

(captured site page body (agents/ralph-workflow.md), not a verified repo-code finding)
Ralph Workflow turns the Ralph loop — popularized as a blog technique for running coding agents in iterative cycles — into an installable orchestrator with operator-grade documentation. You hand it one well-specified task and it runs a plan, build, verify, fix loop against an agent backend of your choice: Claude Code, Codex, OpenCode, Nanocoder, AGY, Pi, Cursor, or Kimi Code, authenticated once locally. The tool ships an opinionated default workflow built around spec-driven development, intended to be adopted as-is and extended later, rather than a bare loop script. Install hygiene matters to the design: a separate rdev launcher avoids shadowing an existing global ralph installation, and the project ships Sphinx documentation, CI configs, and Docker support unusual for scripts in this genre. Developers who want the Ralph pattern without hand-rolling bash loops use it for coding tasks too large to babysit and too risky to run unattended without verification.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ralph-workflow.md)
