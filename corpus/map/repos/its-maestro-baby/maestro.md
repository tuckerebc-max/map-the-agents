# its-maestro-baby/maestro

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a10500d09983 @ 2540374749b8bbe4

## Summary (orientation draft, not independently verified)

Selected evidence records: Maestro is a cross-platform desktop application for running 1-6 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree. Each session gets its own terminal with a full shell environment, a git worktree for code isolation, an assigned branch, and a port allocation for web development.

## Source coverage

Source coverage (partial): 3 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Maestro is a cross-platform desktop application for running 1-6 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree. -- evidence: [README.md#L10-L10](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L10-L10)
- components (2 claim(s)):
  - [observation/documented] The stack comprises a Tauri 2.0/Rust backend, a React + TypeScript + Tailwind CSS frontend, xterm.js terminal emulation, a Rust MCP server, and native git CLI for git operations. -- evidence: [README.md#L178-L184](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L178-L184)
  - [observation/documented] The Rust backend has command handlers for git, worktrees, GitHub, marketplace, MCP, sessions, terminals, updates, and usage, plus core modules for process, plugin, worktree, and session management. -- evidence: [ARCHITECTURE-OVERVIEW.md#L99-L112](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L99-L112), [ARCHITECTURE-OVERVIEW.md#L116-L126](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L116-L126)
- design-choices (1 claim(s)):
  - [observation/documented] Each session gets its own terminal with a full shell environment, a git worktree for code isolation, an assigned branch, and a port allocation for web development. -- evidence: [README.md#L47-L51](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L47-L51)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the documented development workflow starts by running all tests, uses 'roam' and 'dora' skills to review related components, implements changes, then runs related tests and summarizes. -- evidence: [AGENTS.md#L186-L191](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/AGENTS.md#L186-L191)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The app offers a dynamic 1x1 to 2x3 session grid, iTerm2-style split panes, real-time status indicators, and per-session mode selection among Claude Code, Gemini CLI, OpenAI Codex, or plain terminal. -- evidence: [README.md#L67-L70](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L67-L70)
  - [observation/documented] A documented keyboard shortcut set covers session creation, pane splitting, terminal cycling, zoom, copy, and line navigation, with Cmd mapping to Ctrl on Windows/Linux. -- evidence: [README.md#L138-L138](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L138-L138), [README.md#L121-L136](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L121-L136)
- memory-state (1 claim(s)):
  - [observation/documented] Frontend state is organized into Zustand stores including useGitHubStore, useGitStore, useWorkspaceStore, useSessionStore, useMarketplaceStore, and useMcpStore. -- evidence: [ARCHITECTURE-OVERVIEW.md#L132-L143](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L132-L143)
- orchestration (1 claim(s)):
  - [observation/documented] A Rust ProcessManager manages sessions whose worktrees live under ~/.claude-maestro/worktrees/{repo}/{branch}, connecting to the MCP server over stdio. -- evidence: [README.md#L144-L174](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L144-L174)
- tools-permissions (1 claim(s)):
  - [observation/documented] A built-in MCP server lets AI sessions report their state (idle, working, needs input, finished, error) via the maestro_status tool, with updates shown in the session grid. -- evidence: [README.md#L80-L83](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L80-L83)
More evidence: [full detail](maestro.detail.md)

Metadata and full claim list: [full detail](maestro.detail.md)
Human notes ([notes](maestro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
