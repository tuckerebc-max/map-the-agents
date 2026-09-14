# workstreams (`workstreams`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: workstream-labs
- License: Elastic License 2.0
- Language: TypeScript
- Interface: platforms=IDE; install=macOS DMG installer (desktop app); CLI: git clone && bun install && bun link
- Model providers: Claude (Anthropic), Codex (OpenAI), Aider
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [workstream-labs/workstreams](../../repos/workstream-labs/workstreams.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): IDE for orchestrating parallel AI coding agents in isolated git worktrees. Features a worktree sidebar with live diff stats, inline review comments on diffs, create workstreams with agent selection, and agent session state tracking. Agent-agnostic, works with Claude, Codex, Aider, and more. Built with Node.js 22, Electron, and Bun.

(captured site page body (agents/workstreams.md), not a verified repo-code finding)
workstreams is a macOS desktop IDE for running multiple AI coding agents in parallel, each isolated in its own git worktree so parallel tasks cannot interfere. The worktree sidebar tracks live diff stats and agent session state, and reviewers leave inline comments on split diffs that are sent back to agents as structured prompts, creating a review-feedback loop with Claude Code, Codex, Aider, and other agent CLIs. A companion ws CLI (built on Bun) handles init, create, run, and dashboard operations, while the Electron desktop app provides the sidebar, diff stats, and review surface. It is free to download (DMG for Apple Silicon and Intel) under the Elastic License 2.0, macOS-only and early-stage. Its users are developers running several agents on separate tasks concurrently.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/workstreams.md)
