# Emdash (`emdash`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: generalaction
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=IDE; install=binary
- Model providers: Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, GitHub Copilot
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [generalaction/emdash](../../repos/generalaction/emdash.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source desktop app (YC W26) for running multiple AI coding agents in parallel, each isolated in its own Git worktree/branch. Provider-agnostic — bring any CLI agent. Local-first with SQLite storage, remote SSH/SFTP support, issue tracker integrations (Linear, Jira, GitHub, GitLab, Asana), and unified diff review/PR/CI/merge workflow.

(captured site page body (agents/emdash.md), not a verified repo-code finding)
Emdash came out of General Action's YC W26 batch to solve the coordination problem of running several coding agents at once: tasks step on each other, diffs pile up unreviewed, and nobody remembers which agent did what. Each task gets its own git worktree and branch so agents cannot collide, the desktop app shows diffs, CI checks, and PR state in one place, and installed agent CLIs (Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, Copilot) are auto-detected. Issue trackers feed tasks in directly, and local projects can be complemented by remote machines over SSH/SFTP. State lives in local SQLite with no code or chats leaving the machine, which makes it usable in environments that prohibit cloud developer tools.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/emdash.md)
