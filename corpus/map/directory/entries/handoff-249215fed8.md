# handoff (`handoff`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: dazuiba
- License: MIT
- Language: Python
- Interface: platforms=CLI, IDE; install=uv tool install handoff-cli
- Model providers: DeepSeek, Claude (Anthropic), Codex (OpenAI), Gemini (Google), Kimi (Moonshot)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: yes (yes)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [dazuiba/handoff](../../repos/dazuiba/handoff.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): CLI tool that lets coding agents (Claude Code, Codex) delegate tasks to other models (DeepSeek, Gemini, Opus, etc.) in the background without blocking the main session or losing context. Supports parallel tasks, session resume, TUI task browser (handoff list/tail), and Claude skills + Codex custom agents. Custom backends configurable via config.

(captured site page body (agents/handoff.md), not a verified repo-code finding)
handoff solves the cost and context problems of doing everything inside one expensive agent session. From inside Claude Code or Codex, the user dispatches a task to a named backend — DeepSeek by default, with Gemini, Codex, Claude Opus, and custom Anthropic-compatible endpoints configurable — and handoff runs the target agent's CLI in an isolated background process, streaming output to disk instead of into the parent conversation. The parent session receives only a RESULT file path it can read when convenient, and follow-up commands reattach to the same run, preserving the worker's accumulated context. Tasks can run in parallel, be followed live with handoff tail, and be reviewed in an interactive task-history TUI. The intended pattern pairs a premium planning model with inexpensive execution models, and the project documents itself primarily in Chinese with English README support.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/handoff.md)
