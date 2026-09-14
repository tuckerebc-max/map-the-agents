# ralph-wiggum (`ralph-wiggum`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: fstandhartinger
- License: MIT
- Language: Bash, PowerShell
- Interface: platforms=Autonomous; install=npx add-skill fstandhartinger/ralph-wiggum; or openskills install fstandhartinger/ralph-wiggum
- Model providers: Claude Code, OpenAI Codex, Google Gemini, GitHub Copilot
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [fstandhartinger/ralph-wiggum](../../repos/fstandhartinger/ralph-wiggum.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Enables autonomous AI coding using spec-driven development by combining an iterative bash/PowerShell loop with SpecKit-style specifications. The AI agent picks a task, implements it, verifies it, and commits it, only outputting \<promise\>DONE\</promise\> when acceptance criteria are met. It operates with fresh context each loop and shares state via disk files.

(captured site page body (agents/ralph-wiggum.md), not a verified repo-code finding)
Ralph Wiggum packages the Ralph autonomous-loop pattern — repeatedly restarting a coding agent with clean context — on top of structured specifications rather than ad-hoc prompts. Markdown specs in a specs/ directory carry testable acceptance criteria; each loop iteration has the agent orient, pick one task, implement and test it, commit, and emit a completion phrase the outer script checks for before deciding to continue. Attempt counters flag specs that fail ten times, full logs and optional Telegram notifications keep long runs observable, and an AI-driven installer interviews you to generate a project constitution governing agent behavior. Per-agent loop scripts cover Claude Code, Codex, Gemini, Copilot, and Cursor in both bash and PowerShell, and the whole thing installs as an Agent Skill into any skills-compatible tool. Developers running long unattended builds use it to keep agents working through a spec list without context rot.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ralph-wiggum.md)
