# plasma-ai/fractal

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 18793200c0d7 @ 448057f9da1ad062

## Summary (orientation draft, not independently verified)

Fractal is a Python CLI/TUI tool that organizes autonomous agent loops into a tree of git worktrees with hard caps, SQLite-tracked state, and five agent backends; evidence is mostly README/CHANGELOG documentation plus contributor guidance in AGENTS.md. Evidence coverage: 108 of 117 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 27 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Agent loops arrange into a tree of git worktrees: a node iterates toward a goal and spawns child nodes for separable subtasks, so the tree grows to fit the problem rather than following a fixed plan. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19), [README.md#L101-L105](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L101-L105)
  - [observation/documented] Each loop is bounded by hard caps on iterations, depth, children, cost, and time, and an operator can steer or stop it at any point. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the test suite runs with pytest and --doctest-modules, and integration tests create real git repositories and worktrees, session-scoped to avoid repeated node-init overhead. -- evidence: [AGENTS.md#L72-L74](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/AGENTS.md#L72-L74), [README.md#L206-L207](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L206-L207), [README.md#L202-L204](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L202-L204)
  - [observation/documented] Repository development practice: pull requests should branch from and target 'dev' rather than 'main', which advances only at releases; setup uses install.sh or uv sync with pre-commit hooks. -- evidence: [README.md#L176-L178](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L176-L178), [README.md#L229-L230](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L229-L230), [README.md#L213-L215](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L213-L215), [README.md#L184-L186](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L184-L186)
- skills-patterns (1 claim(s)):
  - [observation/documented] The fractal skill can be installed via plugin marketplace for Claude Code and Codex, or via 'fractal install', which copies or symlinks skills into ~/.claude/skills and ~/.agents/skills. -- evidence: [README.md#L84-L86](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L84-L86), [README.md#L80-L81](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L80-L81), [README.md#L75-L76](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L75-L76), [README.md#L92-L94](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L92-L94), [README.md#L88-L90](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L88-L90)
- interfaces (3 claim(s)):
  - [observation/documented] Five agent backends are supported — Claude Code, Codex, Grok Build, OpenCode, and Oh My Pi — selected per node with --agent, with OpenRouter routing available via --provider=openrouter or native model ids. -- evidence: [README.md#L107-L112](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L107-L112)
  - [observation/documented] The /fractal skill takes a plain-language directive, distills NODE.md instructions and a parameter table, asks for anything it could not infer, and launches the node in a tmux session once approved. -- evidence: [README.md#L114-L116](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L114-L116), [README.md#L118-L124](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L118-L124)
- memory-state (1 claim(s)):
  - [observation/documented] All state — runs, iterations, steps, costs, and signals — is tracked in a local SQLite database that can be interacted with live in a terminal UI. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19), [README.md#L101-L105](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L101-L105)
- orchestration (1 claim(s)):
More evidence: [full detail](fractal.detail.md)

Metadata and full claim list: [full detail](fractal.detail.md)
Human notes ([notes](fractal.notes.md), never overwritten by build)

[Back to map index](../../index.md)
