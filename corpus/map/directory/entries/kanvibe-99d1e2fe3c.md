# kanvibe (`kanvibe`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: rookedsysc
- License: AGPL-3.0
- Language: TypeScript
- Interface: platforms=CLI, Desktop; install=Homebrew cask: brew install --cask rookedsysc/kanvibe/kanvibe
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [rookedsysc/kanvibe](../../repos/rookedsysc/kanvibe.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Keyboard-first Kanban workspace that ties AI coding agents to branch-based git worktrees and tmux/zellij terminal sessions; automatically tracks task status via agent hooks across four AI CLIs (Claude Code, Gemini CLI, Codex CLI, OpenCode); live AI session tracking on board cards; in-app AI account/usage management without extra API keys; built-in GitHub-style diff viewer.

(captured site page body (agents/kanvibe.md), not a verified repo-code finding)
Agentic CLI work tends to disappear into terminal windows, making it hard to track several parallel tasks. Kanvibe gives each task its own branch and worktree, runs the coding CLI in a tmux or zellij pane attached to the card, and uses the CLIs' hook mechanisms to detect status changes such as a completed edit or an agent waiting on a follow-up question. The board also tracks AI account usage in-app so no extra API keys are needed, and includes a diff viewer for reviewing what each agent changed. It targets solo developers and small teams that run multiple Claude Code, Codex, Gemini CLI, or OpenCode sessions in parallel.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/kanvibe.md)
