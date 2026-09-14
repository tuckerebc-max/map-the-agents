# Ivy Tendril (`ivy-tendril`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: Ivy-Interactive
- License: FSL-1.1-ALv2
- Language: C#
- Interface: platforms=Desktop; install=Download installer from GitHub Releases, or: curl -sSf https://cdn.ivy.app/install-tendril.sh | sh (macOS/Linux), irm https://cdn.ivy.app/install-tendril.ps1 | iex (Windows)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [ivy-interactive/ivy-tendril](../../repos/ivy-interactive/ivy-tendril.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Desktop orchestrator for parallel AI coding agents using isolated git worktrees; works with any CLI agent (Claude Code, Codex, GitHub Copilot, Gemini, OpenCode); Cloudflare Quick Tunnel remote/mobile coding, Whisper voice input, plan versioning, automated code review gates (build/test/lint/format).

(captured site page body (agents/ivy-tendril.md), not a verified repo-code finding)
Tendril is built by the Ivy-Interactive team (behind the Ivy framework) as an IDE replacement for the agentic era. The core mechanic is worktree isolation: each agent gets its own git worktree so parallel work never touches main, and humans review diffs, annotate plans (edits automatically revise agent goals), and approve merges through verification gates. GitHub webhooks convert issues and jam.dev bug reports into jobs automatically. Cloudflare Quick Tunnels expose running sessions to a phone for remote steering, and Whisper dictation feeds prompts by voice. It ships as installers or one-line scripts for macOS, Windows, and Linux under the Functional Source License, free today and Apache/MIT after the grace period.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ivy-tendril.md)
