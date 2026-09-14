# Greptile (`greptile`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: unknown
- License: Proprietary
- Language: unknown
- Interface: install=Sign up at app.greptile.com; GitHub/GitLab integration; also via CLI and Claude Code plugin
- Model providers: BYOK (bring your own LLM when self-hosted)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Graph index of entire codebase; swarm of parallel agents reviewing beyond the diff; learns team coding standards from PR comments over time; TREX autonomously writes and runs tests per PR; central validation layer across all coding agents; Greptile MCP connects to any AI agent.

(captured site page body (agents/greptile.md), not a verified repo-code finding)
Greptile is a hosted code-review platform that indexes a repository as a graph of files, functions, and dependencies, then runs parallel review agents over every pull request with that full-repo context rather than the diff alone, which lets it catch multi-file logic regressions that diff-only reviewers miss. Beyond review, its TREX agent writes and runs tests for each PR in a sandbox, and the platform accumulates team coding standards from PR comments and plain-English custom rules over time. It integrates as a validation layer for whichever agent produced the change: an MCP server, a Claude Code plugin that reads and resolves comments, a /greploop command that lets Claude Code, Cursor, Codex, or Devin iterate with Greptile until issues clear, and a CLI. It is delivered as SaaS with self-hosting for enterprises, used by over 22,000 teams including Brex, NVIDIA, PostHog, and Zapier.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/greptile.md)
