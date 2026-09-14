# ouijit/ouijit

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b868ef792dc7 @ 6945b93047da6ab2

## Summary (orientation draft, not independently verified)

Selected evidence records: Ouijit is a task and terminal manager for running coding agents in parallel, where each task gets its own git worktree and terminal, with lifecycle hooks launching the agent CLI. The project is free and open source under AGPL-3.0, with no account, sign-in, or telemetry, and distributes self-contained builds for macOS (Apple Silicon/Intel) and Linux x64.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Ouijit is a task and terminal manager for running coding agents in parallel, where each task gets its own git worktree and terminal, with lifecycle hooks launching the agent CLI. -- evidence: [README.md#L9-L9](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L9-L9)
  - [observation/documented] The project is free and open source under AGPL-3.0, with no account, sign-in, or telemetry, and distributes self-contained builds for macOS (Apple Silicon/Intel) and Linux x64. -- evidence: [README.md#L13-L15](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L13-L15), [README.md#L17-L17](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L17-L17), [README.md#L115-L115](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L115-L115)
- components (4 claim(s)):
  - [observation/documented] Tasks live on a kanban board; moving a card between To Do, In Progress, In Review, and Done fires a matching lifecycle hook, and starting a task creates an isolated git worktree. -- evidence: [README.md#L25-L25](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L25-L25)
  - [observation/documented] Terminals are cards in a stack with attachable panel tabs: a script runner, a web preview, and markdown files with Mermaid diagrams; non-task shells get their own board strip. -- evidence: [README.md#L29-L29](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L29-L29)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Ouijit shadows agent binaries on PATH to inject lifecycle hooks and a CLI reference into each session, letting agents create tasks, advance the board, and open panels without setup. -- evidence: [README.md#L37-L37](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L37-L37)
- memory-state (1 claim(s)):
  - [observation/documented] Quitting saves the session, and the next launch offers to restore its terminals in their worktrees, panels included; all data is stored locally in SQLite. -- evidence: [README.md#L63-L63](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L63-L63), [README.md#L79-L79](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L79-L79)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Any terminal can run sandboxed: in a Lima VM mounting only the task's worktree, in place under Seatbelt/Landlock via nono (experimental), or under a user-supplied launcher (experimental). -- evidence: [README.md#L59-L59](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L59-L59)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product runs on macOS 13+ or Linux x64 and requires git 2.20+ on PATH; supported agent harnesses are Claude Code, Codex, Pi, and OpenCode. -- evidence: [README.md#L83-L86](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L83-L86), [README.md#L115-L115](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L115-L115)
More evidence: [full detail](ouijit.detail.md)

Metadata and full claim list: [full detail](ouijit.detail.md)
Human notes ([notes](ouijit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
