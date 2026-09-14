# Galley (`galley`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: shinpr
- License: MIT
- Language: Go
- Interface: platforms=CLI, IDE; install=Plugin marketplace (/plugin marketplace add shinpr/galley), or curl installer script, or go install github.com/shinpr/galley/cmd/galley@latest
- Model providers: Claude Code, OpenAI Codex, GLM (Z.AI), Kimi, Grok
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [shinpr/galley](../../repos/shinpr/galley.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local runtime for supervised, multi-model AI coding — decouples executor and supervisor models so you can use cheap/fast/specialized models for implementation while a different model independently reviews against explicit acceptance criteria. Runs tasks in isolated git worktrees, records evidence (diffs, model output, verdicts), and hands accepted work off as pull requests for unattended (AFK) multi-model coding.

(captured site page body (agents/galley.md), not a verified repo-code finding)
Unattended agent work fails when the same model both writes and grades the code. Galley is a Go CLI and daemon that takes a task YAML with acceptance criteria, runs an executor backend — Claude Code, Codex, or Grok Build — inside an isolated worktree, then has a separately configured supervisor model review the result against those criteria before opening a PR. Executor and supervisor pairs are set per task or repo, evidence files capture diffs, model output, and verdicts for audit, and retry budgets bound runaway sessions. It installs as a marketplace skill for Claude Code, Codex, and Grok Build, and roughly half of Galley's own merged PRs were produced by Galley-managed task branches.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/galley.md)
