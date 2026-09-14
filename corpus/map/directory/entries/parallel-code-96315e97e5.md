# Parallel Code (`parallel-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: johannesjo
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Desktop, IDE; install=binary
- Model providers: Claude Code, Codex CLI, Gemini CLI, Antigravity CLI, Copilot CLI, MiniMax M2.7
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [johannesjo/parallel-code](../../repos/johannesjo/parallel-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Desktop app that runs multiple AI coding agents in true parallel execution, each in its own automatic git worktree/branch for isolated, reviewable code changes. Unified GUI for diff review and merge management, AI Arena for head-to-head agent racing, keyboard-first control, mobile monitoring via QR code, and per-task Docker sandboxing.

(captured site page body (agents/parallel-code.md), not a verified repo-code finding)
Parallel Code emerged to solve the isolation problem in multi-agent development: when several coding CLIs edit the same checkout, they clobber each other and reviewing the outcome means diffing by hand. The Electron desktop app runs each agent in its own automatically created git worktree and branch, then presents all results in one review surface with inline comments, merge controls, and keyboard-first navigation. An AI Arena mode runs the same task through multiple agents head-to-head for comparison, per-task Docker sandboxing contains untrusted runs, and a QR code mirrors session state to a phone for monitoring away from the desk. The app is free, MIT-licensed, and requires the user's own agent subscriptions, running on macOS and Linux with prebuilt binaries. Its users are developers who race or fan out multiple agent CLIs and need a review surface for the results.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/parallel-code.md)
