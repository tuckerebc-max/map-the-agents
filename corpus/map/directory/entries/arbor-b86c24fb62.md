# arbor (`arbor`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: penso
- License: MIT
- Language: Rust
- Interface: platforms=CLI, Desktop; install=brew, binary
- Model providers: ACP agents (Claude, Codex, Pi, Gemini via acpx); OpenAI-compatible (Ollama, LM Studio, OpenRouter, OpenAI, any /v1/chat/completions)
- Feature flags (directory-reported):
  - mcp_support: yes (arbor-mcp stdio server) (yes)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (agent hooks in arbor-core; webhook notifications for agent events) (yes)
  - plan_mode: no (no)

Repository map entry: [penso/arbor](../../repos/penso/arbor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Fully native desktop app for agentic coding (Rust + GPUI) managing repos, worktrees, terminals, diffs, PRs, and AI agent activity. A single daemon unifies native desktop (GPUI), web UI, CLI, and MCP server. Built for parallel agentic coding across local repos, issue queues, and remote SSH outposts.

(captured site page body (agents/arbor.md), not a verified repo-code finding)
Arbor emerged because agentic coding outgrew the terminal: a developer juggling several agents needs worktree management, diff review, PR context, and process supervision in one native interface. The app, built in Rust on Zed's GPUI framework, orchestrates agents through the ACP protocol (acpx wrapping Claude, Codex, Pi, Gemini) plus OpenAI-compatible providers, and monitors independent agents (Claude Code, Codex, OpenCode) it didn't launch. A single shared daemon backs every surface, supports authenticated remote daemons, and streams over WebSocket, so a session started on the desktop is visible on the web or via arbor-cli. MIT-licensed, installable via Homebrew or release binaries, actively developed (520 commits, 808 stars), with mdBook documentation at penso.github.io/arbor.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/arbor.md)
