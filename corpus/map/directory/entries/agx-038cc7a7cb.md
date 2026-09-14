# agx (`agx`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: ramarlina
- License: MIT
- Language: TypeScript/JavaScript (Node.js); Next.js + Tailwind dashboard; Electron desktop app
- Interface: platforms=CLI, Desktop, Web; install=npm install -g @mndrk/agx && agx init; or download macOS desktop app from GitHub Releases; or build from source
- Model providers: Claude (Claude Code CLI), Codex (Codex CLI), Gemini (Gemini CLI), Ollama
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [ramarlina/agx](../../repos/ramarlina/agx.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local workspace for running AI coding agents across tickets, repos, and PRs. Runs a ticket -\> implementation -\> PR -\> review loop with human-in-the-loop gates at every step. Fully local execution (code never leaves your machine), checkpointed state that survives restarts with constant-cost resumption, unified workspace where tickets/code/PRs/reviews live in one window, and provider-agnostic switching (Claude \<-\> Codex \<-\> Gemini ...

(captured site page body (agents/agx.md), not a verified repo-code finding)
Running coding agents ad hoc means state lives in terminal scrollback and review discipline depends on memory. AGX gives every ticket a durable home — objectives, scheduled jobs, chat threads, and terminal sessions under a project, with SQLite (WAL) state that survives restarts — and connects it to Jira or Linear intake. Agents draft implementations in worktree isolation, a reviewer agent does first-pass PR review so humans judge only contested changes, and nothing irreversible proceeds without an explicit approve/reject gate. Agents can be switched mid-thread between Claude, Codex, Gemini, and Ollama, and role-grouped teams route work by tag. The tool ships as a CLI, a Next.js dashboard, and an Electron macOS app, and its own repository documents 167+ merged PRs authored by the agents it manages.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agx.md)
