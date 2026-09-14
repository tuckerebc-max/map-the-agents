# Packnplay (`packnplay`)

[Back to directory index](../index.md)

Directory membership: pages-only.

- Category: other
- Provider/maker: 2389-research
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=go install
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/packnplay](../../repos/2389-research/packnplay.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Containerization wrapper that launches coding agents (Claude Code, Codex, Gemini) inside isolated Docker containers with automated git worktree and dev container management. Handles credential mounting (git, SSH, GitHub CLI, GPG, npm, AWS), port mapping, macOS Keychain integration, and devcontainer.json support. No introspection or access control — sandboxed execution only.

(captured site page body (agents/packnplay.md), not a verified repo-code finding)
Packnplay is a containerization wrapper that launches coding agents — Claude Code, Codex, Gemini — inside isolated Docker containers so they run sandboxed rather than on the host. It automates the tedious parts of that setup: creating a git worktree, provisioning a dev container, mounting credentials (git, SSH, GitHub CLI, GPG, npm, AWS), mapping ports, and integrating with macOS Keychain and devcontainer.json. It deliberately does no introspection or access control — it is a sandboxed execution environment, not a supervisor — and the agent loop belongs entirely to the agent it wraps. The audience is developers who want their coding agent to run in a clean, credential-equipped container without hand-rolling the Docker and worktree plumbing each time.
Sources: [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/packnplay.md)
