# supacode (`supacode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: supabitapp
- License: FSL-1.1-ALv2 (Functional Source License, converts to Apache 2.0 after 2 years)
- Language: Swift
- Interface: platforms=Desktop; install=binary
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: yes (yes)
  - plan_mode: unknown (unknown)

Repository map entry: [supabitapp/supacode](../../repos/supabitapp/supacode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native macOS command center for running coding agents in parallel with a worktree-first workflow (each task gets its own git worktree and real terminal via libghostty), background session persistence that survives app quits (via zmx), and live coding agent presence detection.

(captured site page body (agents/supacode.md), not a verified repo-code finding)
supacode is built for developers who run several agents concurrently and lose track of which session is working on what. Every task gets its own git worktree and a real terminal rendered through libghostty, with the sidebar tracking branch, file, and PR state per worktree alongside pinning, archiving, and auto-delete. Sessions persist in the background via zmx so work survives app restarts and SSH interruptions, and agent presence badges (busy, awaiting input, idle) with notifications make parallel agents legible at a glance. Remote SSH repositories are supported over a single multiplexed connection, and a CLI plus supacode:// deeplinks allow scripting. It is developed by Supabit under a Functional Source License that converts to Apache 2.0 after two years.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/supacode.md)
