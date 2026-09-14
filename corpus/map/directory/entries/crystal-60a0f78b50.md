# Crystal (`crystal`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: stravu
- License: MIT
- Language: TypeScript
- Interface: platforms=Desktop; install=binary
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: yes (yes)
  - claude_code_plugin: n/a (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [stravu/crystal](../../repos/stravu/crystal.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Desktop app (now deprecated, replaced by Nimbalyst) for running multiple Codex and Claude Code sessions in parallel git worktrees to test, compare approaches, and manage AI-assisted development workflows.

(captured site page body (agents/crystal.md), not a verified repo-code finding)
Crystal solved a specific workflow problem: developers running multiple Claude Code or Codex sessions against the same repository would collide over working-tree state. The Electron app gave every session an isolated git worktree, letting users run competing approaches in parallel, compare diffs, and merge the winner. It was MIT-licensed and gathered about 3,100 stars before development ended. As of February 2026 the project was renamed to Nimbalyst, and the repository now directs users to the successor rather than accepting feature work; existing users can still run Crystal, but active development happens elsewhere.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/crystal.md)
