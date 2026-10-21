# LoopTroop (`looptroop`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: looptroop-ai
- License: MIT
- Language: TypeScript
- Interface: install=curl -fsSL https://www.looptroop.ovh/install | sh; or npm install -g looptroop; or brew install looptroop-ai/tap/looptroop; or docker pull looptroopai/looptroop:latest; requires Node 24.15.0+, git, gh, OpenCode
- Model providers: Anthropic, OpenAI, NVIDIA NIM (via OpenCode)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [looptroop-ai/looptroop](../../repos/looptroop-ai/looptroop.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local GUI orchestrator for long-running, high-correctness AI software delivery; turns a coding ticket into a planned, reviewable, agent-executed PR through three stages (Planning with LLM Council interview/PRD/bead generation, Execution with isolated OpenCode worktrees and multi-loop automated testing, Shipping with final verification); cross-model councils with independent voting

(captured site page body (agents/looptroop.md), not a verified repo-code finding)
LoopTroop is built for tickets too large for chat-style coding: an interactive interview (allowed to run over an hour) produces a PRD, which decomposes into beads - the smallest independently implementable units, each with acceptance criteria, target files, and validation steps. OpenCode implements each bead in an isolated git worktree, and because worktrees isolate code but not command execution, the project recommends running inside a disposable VM. State lives outside the model in SQLite, JSONL logs, and YAML artifacts, with the agent receiving only the context its current step needs to prevent context rot; runs are expected to take ten or more hours, unattended. Teams with long-horizon, correctness-sensitive feature work who already run OpenCode are the intended users.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/looptroop.md)
