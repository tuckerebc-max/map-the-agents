# rookedsysc/kanvibe

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 05b9c147299a @ ba6f843443fcb995

## Summary (orientation draft, not independently verified)

KanVibe is a keyboard-first Kanban workspace for AI coding agents, integrating tmux/zellij terminal sessions, git worktrees, and agent hooks for Claude Code, Gemini CLI, Codex CLI, and OpenCode. Evidence is mostly README product documentation plus contributor guides (CLAUDE.md, CONTRIBUTING.md) covering development practice.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] KanVibe is a keyboard-first Kanban workspace for AI coding agents that tracks branch-based tasks on a real-time board and opens each task's tmux/zellij session in browser or desktop app. -- evidence: [README.md#L7-L7](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L7-L7), [README.md#L5-L5](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L5-L5)
- components (4 claim(s)):
  - [observation/documented] The stack is Next.js 16 with React 19 and TypeScript, SQLite via TypeORM and better-sqlite3, xterm.js with WebSocket and node-pty for terminals, and Electron for desktop packaging. -- evidence: [README.md#L377-L386](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L377-L386)
  - [observation/documented] KanVibe integrates Claude Code Hooks, Gemini CLI Hooks, Codex CLI, and OpenCode to track task status automatically; hooks are auto-installed when a project is registered or a worktree task is created. -- evidence: [README.md#L275-L275](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L275-L275), [README.md#L328-L328](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L328-L328)
- design-choices (2 claim(s)):
  - [observation/documented] Tasks move through five statuses (TODO, PROGRESS, PENDING, REVIEW, DONE); moving a task to DONE automatically deletes its branch, worktree, and terminal session. -- evidence: [README.md#L277-L283](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L277-L283), [README.md#L177-L177](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L177-L177), [README.md#L175-L175](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L175-L175)
  - [observation/documented] Creating a task with a branch name automatically creates a git worktree, spawns a tmux window or zellij tab, and links the terminal session to the task. -- evidence: [README.md#L168-L171](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L168-L171)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors must run pnpm build, pnpm check, and pnpm test before submitting, use Conventional Commits, and attach a screenshot or GIF; PRs without visual proof will not be merged. -- evidence: [CONTRIBUTING.md#L73-L79](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L73-L79), [CONTRIBUTING.md#L56-L61](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L56-L61), [CONTRIBUTING.md#L63-L63](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L63-L63)
  - [observation/documented] Repository development practice: CLAUDE.md forbids code that mutates process-wide or shell-wide environment variables, permitting only KanVibe-scoped KANVIBE_* names, with tmux set-clipboard as a narrowly approved exception. -- evidence: [CLAUDE.md#L19-L23](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L19-L23), [CLAUDE.md#L5-L13](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L5-L13), [CLAUDE.md#L17-L17](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L17-L17)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Agent hooks call HTTP endpoints: POST /api/hooks/start creates a task, and POST /api/hooks/status updates status by branchName plus projectName, returning 404 with a notification if the target is missing. -- evidence: [README.md#L350-L353](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L350-L353)
  - [observation/documented] The app exposes keyboard shortcuts including quick task search (Cmd/Ctrl+Shift+O), project filter, notifications, board navigation, and numbered task-detail dock shortcuts intercepted before terminal input. -- evidence: [README.md#L270-L270](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L270-L270), [README.md#L251-L268](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L251-L268)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](kanvibe.detail.md)

Metadata and full claim list: [full detail](kanvibe.detail.md)
Human notes ([notes](kanvibe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
