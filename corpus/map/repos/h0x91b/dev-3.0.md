# h0x91b/dev-3.0

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e781c4265b7d @ 8a06927f2fafd0f5

## Summary (orientation draft, not independently verified)

Evidence is README plus contributor docs for dev-3.0, a Kanban-style desktop/headless app that runs AI coding agents in per-task git worktrees. Product claims come from README marketing/documentation text; contributor workflow rules come from CONTRIBUTING.md.

## Source coverage

Source coverage (partial): 3 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] dev-3.0 is described as a Kanban board where each card is a live AI coding agent, with each task getting its own git worktree, terminal, and agent so many tasks run concurrently without file conflicts. -- evidence: [README.md#L33-L35](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L33-L35), [README.md#L7-L11](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L7-L11)
- components (1 claim(s)):
  - [observation/documented] Per-task sandboxes include a fresh git worktree off the base branch, a tmux session inside it, a per-project setup script, and optionally reserved free ports for the task's dev server. -- evidence: [README.md#L56-L59](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L56-L59)
- design-choices (1 claim(s)):
  - [observation/documented] Heavy directories like node_modules or .venv are copy-on-write cloned into task sandboxes, so sandboxes cost near-zero disk and appear instantly. -- evidence: [README.md#L56-L59](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L56-L59)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must run bun run lint and bun run test:full before opening a PR, rebase on main first (PRs are squash-merged), add a dated changelog entry under change-logs/YYYY/MM/DD, and write decision records for non-obvious choices. -- evidence: [CONTRIBUTING.md#L21-L30](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L21-L30)
  - [observation/documented] Repository development practice: setup requires Bun, git, and tmux 3.6 or newer, with bun run dev as the local dev loop and bun run test as a fast subset excluding slow e2e suites that CI runs. -- evidence: [CONTRIBUTING.md#L9-L15](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L9-L15), [CONTRIBUTING.md#L7-L7](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L7-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The dev3 CLI lets agents communicate with the board: setting task overviews, leaving notes, raising attention badges, showing images or HTML artifacts, starting peer tasks, and read-only peeking at other tasks' terminals. -- evidence: [README.md#L191-L197](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L191-L197), [README.md#L201-L203](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L201-L203), [README.md#L186-L189](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L186-L189)
  - [observation/documented] A built-in review panel shows the branch diff with syntax highlighting, per-file read state, and inline comments on line ranges; the review can be copied back into the agent's terminal as a prompt. -- evidence: [README.md#L92-L94](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L92-L94)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product can launch read-only 'bug hunter' agents that comb a branch diff in parallel and report only provable findings, indicating a read-only agent mode. -- evidence: [README.md#L109-L111](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L109-L111)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](dev-3.0.detail.md)

Metadata and full claim list: [full detail](dev-3.0.detail.md)
Human notes ([notes](dev-3.0.notes.md), never overwritten by build)

[Back to map index](../../index.md)
