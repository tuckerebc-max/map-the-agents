# fractal (`fractal`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: plasma-ai
- License: Apache-2.0
- Language: Python
- Interface: platforms=CLI; install=pip
- Model providers: Claude Code, Codex, Grok Build, OpenCode, Oh My Pi (omp), OpenRouter
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: yes (yes)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [plasma-ai/fractal](../../repos/plasma-ai/fractal.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Hierarchical agent loops with recursive self-organization — autonomous agent loops arrange into a tree; each node iterates toward a goal in its own git worktree and spawns child nodes for separable subtasks. Fractal tree grows to fit the problem rather than a fixed plan. Each node runs in an isolated git worktree with hard caps (iterations, depth, children, cost, time). ...

(captured site page body (agents/fractal.md), not a verified repo-code finding)
Fractal addresses the failure mode of long autonomous runs: a single agent loop loses coherence on large tasks and burns unbounded budget. It decomposes work recursively, running each node as an autonomous session of a backend agent such as Claude Code, Codex, Grok Build, OpenCode, or Oh My Pi, isolated in its own git worktree and capped by configurable iteration, depth, cost, and time limits. Run metadata, including per-node cost, lands in a local SQLite database that the fractal open dashboard renders live. It is installed from PyPI or as a Claude Code and Codex marketplace plugin, and because nodes run with permission prompts disabled by default, it is aimed at operators running it on tasks and hosts they are willing to leave unsupervised.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/fractal.md)
