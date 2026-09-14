# codex-multi-agents (`codex-multi-agents`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: violetDelia
- License: unknown
- Language: Shell, Bash
- Interface: install=Clone repo; use bash scripts under skills/codex-multi-agents/scripts/. No formal install steps provided.
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [violetdelia/codex-multi-agents](../../repos/violetdelia/codex-multi-agents.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Multi-agent task management and coordination using pure shell scripts and tmux sessions; manages agent rosters, task lifecycle (new -\> dispatch -\> pause -\> continue -\> done), inter-agent communication via tmux, and a kanban-style task board; worktree-based isolation per task. Only 2 commits, 36 stars - early/abandoned stage.

(captured site page body (agents/codex-multi-agents.md), not a verified repo-code finding)
Codex-multi-agents coordinates several Codex sessions working on the same repository through shell scripts rather than a dedicated application. A roster script registers named agents with roles and synchronized prompts, a task script manages each task's lifecycle — create, dispatch, pause, resume, complete — with worktree paths, acceptance criteria, and logs recorded in a shared TODO file, and a tmux script relays messages between agent sessions. Each task runs in its own git worktree so parallel agents do not conflict on the working tree. The tool is structured as an agent skill package with scripts under skills/, documentation in Chinese, and a recommended workflow of spec, implementation, review, merge, and sync confirmation; the repository holds only two commits and no license file, indicating an early personal project.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codex-multi-agents.md)
