# OpenGiraffe (`opengiraffe`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: zclllyybb
- License: unknown
- Language: Python
- Interface: platforms=Autonomous; install=git clone + pip install -r requirements.txt + configure config.yaml + python cli.py start
- Model providers: opencode CLI (any LLM backend)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [zclllyybb/opengiraffe](../../repos/zclllyybb/opengiraffe.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=multiplexer, backing=agent, page=multiplexer

## Description

Highlight (site page `what_makes_it_special`): Autonomous batch task queue (not interactive copilot); continuous codebase Explorer that proactively finds work; Plan-\>Code-\>Review loop with multi-reviewer voting (all must approve) and automatic retry on rejection; persistent SQLite state for resume-after-reboot; each task isolated in its own git worktree/branch; web dashboard for runtime model editing and task management

(captured site page body (agents/opengiraffe.md), not a verified repo-code finding)
Interactive copilots wait for a prompt, so the backlog of small fixes and TODOs scattered through a codebase never gets touched. OpenGiraffe runs as a persistent daemon that flips the model: a continuous Explorer scans the repository for work (including TODO/FIXME mining and optional Jira-issue skills), feeds it through a Planner-Coder-Reviewer pipeline, and executes tasks in parallel across isolated git worktrees with retry logic. Nothing lands without review — the pipeline requires reviewer approval, and a local web dashboard on port 8778 visualizes the queue and active work. It drives the opencode CLI rather than talking to model APIs directly, so model choice and keys come from the opencode configuration. Setup is clone, pip install, configure YAML, and start, under Python 3.11+. Maintainers who want a codebase to accumulate autonomous progress between human sessions are the audience.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opengiraffe.md)
