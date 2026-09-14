# mindwalk (`mindwalk`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: cosmtrek
- License: MIT
- Language: Go
- Interface: install=binary
- Model providers: Anthropic, OpenAI
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [cosmtrek/mindwalk](../../repos/cosmtrek/mindwalk.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A visualization tool that replays coding-agent sessions on a 3D map of your codebase — draws the repo as a 'night map' and replays sessions as light moving through it (glowing where the agent searched/read/edited, dark elsewhere). Fully local; one Go binary reads Claude Code, Codex, and pi session logs. LLM-judge session evaluation with evidence-anchored findings, deterministic citymap layout, client-side ...

(captured site page body (agents/mindwalk.md), not a verified repo-code finding)
mindwalk addresses the opacity of agent runs: after an agent spends an hour and a budget, the session log is the only record, and it is effectively unreadable. The tool builds a deterministic 3D map of the repository — height from lines of code, a 'night map' aesthetic — and replays sessions as light moving across it, with color separating observation from mutation and deleted files persisting as wireframe ghosts. Playback includes scrubbing, speed control, marks for compactions and subagent launches, subagent lenses for replaying nested traces, and client-side video export for postmortems. An inspector per file reconstructs visit history, and a HUD surfaces friction signals such as error rate, churn, and edits made after the last verification. An optional analyze command sends a session summary through the user's own claude or codex CLI for judge scoring; everything else stays fully local. Teams reviewing agent behavior, auditing spent budgets, or teaching agent mechanics use it as a replay instrument rather than a coding tool.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mindwalk.md)
