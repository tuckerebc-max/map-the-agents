# claude-code-merge-queue (`claude-code-merge-queue`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: funador
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm (claude-code-merge-queue); requires Node 18+
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: yes (yes)
  - plan_mode: no (no)

Repository map entry: [funador/claude-code-merge-queue](../../repos/funador/claude-code-merge-queue.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): A local, zero-cost merge queue that serializes landings when multiple parallel Claude Code agents work in the same repo: numbered lanes in git worktrees, a FIFO queue onto the integration branch, a WorktreeCreate hook, a machine-wide build lock, and a pre-push hook that blocks direct pushes so agents must pass the checkCommand gate via land.

(captured site page body (agents/claude-code-merge-queue.md), not a verified repo-code finding)
claude-code-merge-queue is the git plumbing for running many Claude Code agents in parallel on one repository. It manages numbered lanes as git worktrees so several agents can build and test simultaneously, then serializes landings onto the integration branch through a FIFO queue that prevents push races, redundant builds, and test flakiness from shared resources. A Husky pre-push hook blocks direct pushes to the integration branch, forcing agents through the land command, which runs a configurable checkCommand gate before merging, and its init writes the config file, CLAUDE.md instructions, Claude settings, and package.json scripts. It is a free, local alternative to GitHub Merge Queue with no PRs and no cloud costs, single-machine only, and explicitly not a security boundary — the companion tooling around the agents rather than an agent itself.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/claude-code-merge-queue.md)
