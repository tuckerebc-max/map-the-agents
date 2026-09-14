# eneskirca/nodeterm

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8fd38d2c229e @ f57e03c407f29b9f

## Summary (orientation draft, not independently verified)

nodeterm is an Electron node-based terminal manager where terminals and AI agent sessions live as draggable nodes on a pan/zoom canvas, doubling as a kanban board, with a CorePlatform service seam enabling desktop, browser Server Edition, and iOS surfaces. Evidence is documentation-only (README, CONTRIBUTING, THIRD-PARTY-NOTICES); no source code slices were provided. Evidence coverage: 97 of 131 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 57 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The app is Electron with three contexts: src/main as the shell, src/preload as the sole bridge exposing window.nodeTerminal, and src/renderer as React UI, with src/shared holding types and IPC channel names used by all three. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311)
- design-choices (1 claim(s)):
  - [observation/documented] Services (PTY, workspace/settings, git, agents, hooks) live in src/core behind a CorePlatform interface and never import Electron; the browser Server Edition boots the same services over a WebSocket-RPC bridge. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm install, npm run dev, npm run typecheck (described as the fastest correctness gate), and npm test (vitest unit + integration); Windows uses bootstrap-windows.bat instead of npm install. -- evidence: [CONTRIBUTING.md#L20-L23](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L20-L23), [CONTRIBUTING.md#L13-L18](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L13-L18), [README.md#L264-L275](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L264-L275)
  - [observation/documented] Repository development practice: the process-boundary split is enforced by guard tests that fail if src/core or src/server import electron or ../main/*, and new service logic must go in src/core behind CorePlatform. -- evidence: [CONTRIBUTING.md#L47-L48](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L47-L48), [CONTRIBUTING.md#L50-L52](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L50-L52), [CONTRIBUTING.md#L36-L36](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L36-L36)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The renderer depends only on a TerminalTransport abstraction: LocalTransport talks to the local host and RemoteTransport to a remote agent over SSH, so remote projects drop in without canvas UI changes. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311)
  - [observation/documented] Node kinds include terminal (xterm + tmux), agent (Claude Code, Codex, Gemini, Copilot, opencode, Grok, custom), sticky notes linkable as agent context, groups bound to git worktrees, Monaco editors, diff views, and web/video nodes. -- evidence: [README.md#L125-L128](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L125-L128)
- memory-state (1 claim(s)):
  - [observation/documented] Terminals run in persistent tmux sessions surviving node remounts, app restarts, and machine reboots, restoring scrollback and resuming agent sessions via claude --resume; the macOS app bundles its own tmux, preferring any system tmux. -- evidence: [README.md#L132-L161](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L132-L161), [THIRD-PARTY-NOTICES.md#L32-L41](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/THIRD-PARTY-NOTICES.md#L32-L41)
- orchestration (1 claim(s)):
More evidence: [full detail](nodeterm.detail.md)

Metadata and full claim list: [full detail](nodeterm.detail.md)
Human notes ([notes](nodeterm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
