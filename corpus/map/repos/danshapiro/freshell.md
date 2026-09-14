# danshapiro/freshell

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e68ae40a2b3e @ 101631a4d3dba4f6

## Summary (orientation draft, not independently verified)

Selected evidence records: The stack includes React 18, Redux Toolkit, xterm.js, Monaco, Express, node-pty, WebSocket, Vite, TypeScript, and Vitest-based testing tools. An extension system supports three pane-type categories: client (static HTML/JS), server (freshell-managed HTTP server with auto port allocation), and CLI (terminal tool wrapped as a pane), installed via a freshell.json manifest in ~/.freshell/extensions/.

## Source coverage

Source coverage (partial): 3 of 525 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The stack includes React 18, Redux Toolkit, xterm.js, Monaco, Express, node-pty, WebSocket, Vite, TypeScript, and Vitest-based testing tools. -- evidence: [AGENTS.md#L209-L211](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L209-L211), [README.md#L263-L267](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L263-L267)
  - [observation/documented] An extension system supports three pane-type categories: client (static HTML/JS), server (freshell-managed HTTP server with auto port allocation), and CLI (terminal tool wrapped as a pane), installed via a freshell.json manifest in ~/.freshell/extensions/. -- evidence: [README.md#L271-L271](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L271-L271), [README.md#L273-L275](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L273-L275), [README.md#L277-L277](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L277-L277)
- design-choices (1 claim(s)):
  - [observation/documented] Desktop profiles let multiple independent clients run on one machine, each with its own settings, storage dir, and single-instance lock, configured via ~/.freshell/profiles.json. -- evidence: [README.md#L62-L65](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L62-L65), [README.md#L69-L75](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L69-L75), [README.md#L79-L79](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L79-L79)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors must work in .worktrees worktrees, branch from origin/main, and land all behavior changes via PRs to main; direct pushes to main are forbidden. -- evidence: [AGENTS.md#L14-L27](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L14-L27), [AGENTS.md#L52-L57](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L52-L57)
  - [observation/documented] Repository development practice: the project mandates Red-Green-Refactor TDD for all but trivial changes, with both unit and e2e coverage required. -- evidence: [AGENTS.md#L6-L11](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/AGENTS.md#L6-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Freshell indexes local session history for Claude Code, Codex, OpenCode, and Amplifier, and can launch terminals for those plus Gemini and Kimi; OpenCode sessions are read directly from its local session database. -- evidence: [README.md#L245-L252](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L245-L252), [README.md#L243-L243](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L243-L243), [README.md#L254-L255](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L254-L255)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] For OpenCode sessions, freshell does not set OPENCODE_PERMISSION or pass --dangerously-skip-permissions; OpenCode's own config and OS filesystem permissions govern access. -- evidence: [README.md#L257-L257](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L257-L257)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The app requires Node.js 18+ (20+ recommended) plus platform build tools for native modules, and runs on Windows, macOS, and Linux. -- evidence: [README.md#L56-L56](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L56-L56), [README.md#L1-L5](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L1-L5)
- limitations (2 claim(s)):
  - [observation/documented] Stream Deck integration requires Chrome or Edge via WebHID and is not supported inside the freshell desktop app. -- evidence: [README.md#L175-L176](https://github.com/danshapiro/freshell/blob/e68ae40a2b3ed59318a8a4ca849cb00ab4205413/README.md#L175-L176)
More evidence: [full detail](freshell.detail.md)

Metadata and full claim list: [full detail](freshell.detail.md)
Human notes ([notes](freshell.notes.md), never overwritten by build)

[Back to map index](../../index.md)
