# CLITrigger (`clitrigger`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: HyperAITeam
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, Web; install=Desktop app (Windows .exe, macOS .dmg, Linux .AppImage) from GitHub Releases; or npm i -g clitrigger (requires Node.js 22+ LTS, Git, \>=1 AI CLI)
- Model providers: Claude Code, Antigravity, Codex, Gemini
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: True (reported)

Repository map entry: [hyperaiteam/clitrigger](../../repos/hyperaiteam/clitrigger.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): An 'IDE for AI CLI agents.' Unifies the AI-coding workflow into a single five-stage pipeline — Docs -\> Plan -\> Terminal -\> Autonomous Tasks -\> Version Control — where each stage inherits the context of the previous one. Runs multiple AI CLIs (Claude Code, Antigravity, Codex) in parallel, each in its own isolated git worktree, with scheduling around rate limits, ...

(captured site page body (agents/clitrigger.md), not a verified repo-code finding)
CLITrigger's thesis is that the AI-coding workflow scatters across five applications, and that a single workspace where each stage inherits context eliminates the re-explanation tax. Documentation lives in an Obsidian-style vault whose pages can be injected into prompts; planned tasks dispatch to multiple CLI agents in parallel worktrees with cron scheduling and rate-limit retry; multi-agent discussion (architect, developer, reviewer) runs before output reaches a review queue tied to a built-in Git client. An MCP endpoint and optional Cloudflare Tunnel extend it. It wraps the CLIs via adapters and runs no model loop itself. Individual developers managing several agent CLIs are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/clitrigger.md)
