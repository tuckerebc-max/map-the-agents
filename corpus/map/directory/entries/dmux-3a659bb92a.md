# dmux (`dmux`)

[Back to directory index](../index.md)

Directory membership: published+backing.

- Category: multiplexer
- Provider/maker: standardagents
- License: MIT
- Language: TypeScript / Node.js
- Interface: install=npm
- Model providers: API-key providers, OpenAI-compatible endpoints, Codex/ChatGPT login, Grok Build/SpaceXAI login
- Feature flags (directory-reported):
  - mcp_support: no - .playwright-mcp dir present but not a documented feature (no)
  - plugin_support: no - extensibility via lifecycle hooks only (no)
  - claude_code_plugin: n/a - Claude Code is a first-class supported agent, not a plugin target (reported)
  - subagents: no (no)
  - hooks: yes - lifecycle hooks (.dmux-hooks/ dir): worktree create, pre-merge, post-merge (yes)
  - plan_mode: partial - 'goal launches' optionally start agents in goal mode (reported)

Repository map entry: [standardagents/dmux](../../repos/standardagents/dmux.md) (source: backing, field: `source_code_url`).

## Description

(published index `description`, not a verified repo-code finding)
dmux treats a coding task as a tmux pane with an isolated worktree: press n, type the prompt, pick one or more agents, and it creates the branch, worktree, and agent launch, then merges or opens a Git
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json)
