# looper (`looper`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: nexu-io
- License: MIT
- Language: Go
- Interface: platforms=Autonomous; install=curl -fsSL https://raw.githubusercontent.com/nexu-io/looper/main/scripts/install.sh | sh then looper bootstrap
- Model providers: opencode, claude-code, codex, cursor-cli, grok-build, pi, omp
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [nexu-io/looper](../../repos/nexu-io/looper.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Loop-based agents with success criteria (not fixed steps); forge is source of truth (no external tracker/YAML); parallel-safe git worktrees; local/inspectable/stoppable daemon; multi-repo support; bring-your-own-agent with no vendor lock-in

(captured site page body (agents/looper.md), not a verified repo-code finding)
Looper automates the issue-to-merge pipeline for maintainers who cannot babysit every ticket: register a repo, and the looperd daemon polls the forge for assigned or looper-labeled issues, then runs a planner (until the spec is reviewable), a worker (implements the spec when checks pass), and a reviewer-fixer pair that ping-pongs until no actionable threads remain, all gated by a label state machine. A takeover mode drives a single PR through review-and-fix cycles to merge, and a multi-node loopernet mode distributes webhook-driven work. The vendor layer is pluggable - opencode, claude-code, codex, cursor-cli, grok-build, pi, omp - so teams keep their existing agent subscriptions, and everything runs locally as two Go binaries with no hosted control plane. Open-source maintainers drowning in labeled issues are the target user.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/looper.md)
