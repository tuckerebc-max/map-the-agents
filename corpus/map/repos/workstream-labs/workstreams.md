# workstream-labs/workstreams

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ef30f54b40fe @ e276e1598c1de89e

## Summary (orientation draft, not independently verified)

Workstreams is a macOS desktop IDE (plus a `ws` CLI) for orchestrating parallel AI coding agents in isolated git worktrees, with inline diff review and agent status tracking. Evidence is mostly README documentation plus contributor setup guidance; no source code slices are included.

## Source coverage

Source coverage (partial): 3 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Workstreams is described as an IDE for orchestrating parallel AI coding agents, each running in an isolated git worktree. -- evidence: [README.md#L3-L3](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] The project ships as a macOS desktop app distributed via DMG installers for Apple Silicon (arm64) and Intel (x64), with built-in auto-update. -- evidence: [README.md#L24-L24](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L24-L24), [README.md#L11-L11](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L11-L11), [README.md#L9-L9](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L9-L9)
  - [observation/documented] An orchestrator sidebar manages multiple git worktrees per repository, showing real-time addition/deletion counts and preserving per-worktree terminals, editors, and state. -- evidence: [README.md#L30-L30](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L30-L30)
- design-choices (1 claim(s)):
  - [observation/documented] Each workstream is defined with a natural-language prompt and an agent choice, and gets its own isolated git worktree. -- evidence: [README.md#L38-L38](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L38-L38)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors clone, run bun install and bun link, run tests with bun test, and submit small PRs from main after adding tests. -- evidence: [CONTRIBUTING.md#L14-L18](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L14-L18), [CONTRIBUTING.md#L40-L40](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L40-L40), [CONTRIBUTING.md#L35-L38](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L35-L38), [CONTRIBUTING.md#L5-L10](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L5-L10)
  - [observation/documented] Repository development practice: the codebase is organized as packages/core (shared engine), apps/cli (raw-ANSI TUI, one file per command), apps/desktop (WIP), and bun:test tests; runtime state lives in gitignored .workstreams/. -- evidence: [CONTRIBUTING.md#L22-L29](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L22-L29), [CONTRIBUTING.md#L31-L31](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/CONTRIBUTING.md#L31-L31)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is agent-agnostic and reportedly works with Claude, Codex, Aider, and other agents. -- evidence: [README.md#L5-L5](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L5-L5)
  - [observation/documented] A CLI named `ws` (in apps/cli) supports commands such as init, create, run, and dashboard for terminal-driven workstream management. -- evidence: [README.md#L46-L46](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L46-L46), [README.md#L48-L54](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L48-L54)
- memory-state (1 claim(s)):
  - [observation/documented] Claude Code lifecycle events (idle, working, awaiting permission, ready for review) are tracked per worktree via hooks and shown as animated sidebar status indicators. -- evidence: [README.md#L42-L42](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L42-L42)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Running the project requires macOS, Node.js 22, Git, and Bun for CLI installation. -- evidence: [README.md#L58-L58](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L58-L58), [README.md#L70-L72](https://github.com/workstream-labs/workstreams/blob/ef30f54b40fe58a556e100a95a0b745e842492e0/README.md#L70-L72)
- limitations (1 claim(s)):
More evidence: [full detail](workstreams.detail.md)

Metadata and full claim list: [full detail](workstreams.detail.md)
Human notes ([notes](workstreams.notes.md), never overwritten by build)

[Back to map index](../../index.md)
