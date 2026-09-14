# dmux (`dmux`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

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

Highlight (site page `what_makes_it_special`): tmux-based multiplexer for parallel AI coding agents in isolated git worktrees. Each agent gets its own tmux pane + worktree + branch, preventing file conflicts. Agent-agnostic with 12+ supported CLIs (Claude Code, Codex, OpenCode, Gemini CLI, etc.). Durable/resumeable terminals, smart merging with GitHub PR creation, AI-generated branch/commit names, multi-project sessions, and a built-in file browser.

(captured site page body (agents/dmux.md), not a verified repo-code finding)
dmux treats a coding task as a tmux pane with an isolated worktree: press n, type the prompt, pick one or more agents, and it creates the branch, worktree, and agent launch, then merges or opens a GitHub PR when the work finishes. It stays agent-agnostic — Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, Cursor CLI, Copilot CLI, Crush and more — and never intercepts the agent's protocol, so MCP servers and permission flows keep working. Durable terminals resume the tracked agent conversation when a pane is recreated, and lifecycle hooks run scripts around worktree creation and merges. Solo developers running several tasks at once are the target user.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/dmux.md)
