# rookedsysc/kanvibe -- full detail

[Back to orientation](kanvibe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rookedsysc/kanvibe/05b9c147299aea8f2b6159f4305a19057382af15/ba6f843443fcb995.json](../../../wiki/dossiers/rookedsysc/kanvibe/05b9c147299aea8f2b6159f4305a19057382af15/ba6f843443fcb995.json)

## specifications (1 claim(s))

- [observation/documented] KanVibe is a keyboard-first Kanban workspace for AI coding agents that tracks branch-based tasks on a real-time board and opens each task's tmux/zellij session in browser or desktop app. -- evidence: [README.md#L7-L7](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L7-L7), [README.md#L5-L5](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L5-L5) (`clm_f065f41ad9c123b2e8360c8d16107a54b6417fbc9538e673b403ae7e3b7e57b8`)

## components (4 claim(s))

- [observation/documented] The stack is Next.js 16 with React 19 and TypeScript, SQLite via TypeORM and better-sqlite3, xterm.js with WebSocket and node-pty for terminals, and Electron for desktop packaging. -- evidence: [README.md#L377-L386](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L377-L386) (`clm_1ad4b9c42679f4ec3450dd944ef01fbe0189930ccc40e8c30d9e1a032273b2c2`)
- [observation/documented] KanVibe integrates Claude Code Hooks, Gemini CLI Hooks, Codex CLI, and OpenCode to track task status automatically; hooks are auto-installed when a project is registered or a worktree task is created. -- evidence: [README.md#L275-L275](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L275-L275), [README.md#L328-L328](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L328-L328) (`clm_593ae9d5329599f43d4115183dc45781b7706df70038abe2c62baa1e86fa1134`)
- [observation/documented] For OpenCode, KanVibe generates a TypeScript plugin at .opencode/plugins/kanvibe-plugin.ts using the @opencode-ai/plugin SDK, handling status updates in-process rather than via shell hooks. -- evidence: [README.md#L326-L326](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L326-L326) (`clm_82aa1ea312ded4869fbf47eb5fab4caf2fe50efb067f20e87f66e6307d4d7931`)
- [observation/documented] An AI usage panel reads remaining Claude, Codex, and Gemini subscription quota using each CLI's locally stored sign-in, requiring no extra API key, and manages accounts under Settings → AI accounts. -- evidence: [README.md#L238-L247](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L238-L247) (`clm_8c7dd8321f1703af716d4508d7638d974d3543df8707fbce8c20fb970d6f3b63`)

## design-choices (2 claim(s))

- [observation/documented] Tasks move through five statuses (TODO, PROGRESS, PENDING, REVIEW, DONE); moving a task to DONE automatically deletes its branch, worktree, and terminal session. -- evidence: [README.md#L277-L283](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L277-L283), [README.md#L177-L177](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L177-L177), [README.md#L175-L175](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L175-L175) (`clm_af04defe85e1125653f219c31c115eb2661244a2b13403735da90ccab9769ef1`)
- [observation/documented] Creating a task with a branch name automatically creates a git worktree, spawns a tmux window or zellij tab, and links the terminal session to the task. -- evidence: [README.md#L168-L171](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L168-L171) (`clm_5f8b496ccf247f5a46663244fd35038467ebeae2b1480461bd42c99c372b3d94`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors must run pnpm build, pnpm check, and pnpm test before submitting, use Conventional Commits, and attach a screenshot or GIF; PRs without visual proof will not be merged. -- evidence: [CONTRIBUTING.md#L73-L79](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L73-L79), [CONTRIBUTING.md#L56-L61](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L56-L61), [CONTRIBUTING.md#L63-L63](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L63-L63) (`clm_5ba47ef0fd8583966ae4f3143cb80d70217000aa612750f84eef48bf9d6160be`)
- [observation/documented] Repository development practice: CLAUDE.md forbids code that mutates process-wide or shell-wide environment variables, permitting only KanVibe-scoped KANVIBE_* names, with tmux set-clipboard as a narrowly approved exception. -- evidence: [CLAUDE.md#L19-L23](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L19-L23), [CLAUDE.md#L5-L13](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L5-L13), [CLAUDE.md#L17-L17](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CLAUDE.md#L17-L17) (`clm_c699d39b52ad9f2d79adbf28fe0d790c563408118ce84b6c0e3ad5bb47f9bc43`)
- [observation/documented] Repository development practice: all user-facing strings must be added to messages/ko.json, en.json, and zh.json, and all three language versions of README and CONTRIBUTING docs must be updated together. -- evidence: [CONTRIBUTING.md#L96-L98](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L96-L98), [CONTRIBUTING.md#L94-L94](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L94-L94), [CONTRIBUTING.md#L126-L126](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L126-L126) (`clm_ea4d716f1733d3488d669bfd8661eb68370e5f2cd8268605032f3ea0c144a7e7`)
- [observation/documented] Repository development practice: the contributing guide lists Node.js 24.x, pnpm, and tmux or zellij as prerequisites, with pnpm dev serving on localhost:4885 and pnpm dist producing a macOS DMG. -- evidence: [CONTRIBUTING.md#L13-L15](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L13-L15), [CONTRIBUTING.md#L37-L37](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L41-L43](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L41-L43), [CONTRIBUTING.md#L45-L45](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L45-L45) (`clm_af512e617b1631dd0a657f87220eea01c6f8dec7440b76e497e7703b111c818d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Agent hooks call HTTP endpoints: POST /api/hooks/start creates a task, and POST /api/hooks/status updates status by branchName plus projectName, returning 404 with a notification if the target is missing. -- evidence: [README.md#L350-L353](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L350-L353) (`clm_0ad2729d4952797d7caa3424355902ac4cde1d08fb26097c26c6960bf3a3d8ad`)
- [observation/documented] The app exposes keyboard shortcuts including quick task search (Cmd/Ctrl+Shift+O), project filter, notifications, board navigation, and numbered task-detail dock shortcuts intercepted before terminal input. -- evidence: [README.md#L270-L270](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L270-L270), [README.md#L251-L268](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L251-L268) (`clm_0a7062891d8cc62cedc12374008b53656688d9ee91e7ff80fd80e0175a48f251`)
- [observation/documented] The task detail page offers a GitHub-style diff view with a file tree sidebar, Monaco-based inline diff, browser edit mode, and viewed-file checkboxes, comparing changes against the base branch. -- evidence: [README.md#L359-L362](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L359-L362), [README.md#L357-L357](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L357-L357) (`clm_97b463905edc294543936e167727b1f677b765ad76e88638f67b02bd6827451e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Required runtime dependencies are git, tmux, and gh (with gh auth login); zellij is optional. -- evidence: [README.md#L118-L123](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L118-L123) (`clm_bc765022e56c859aa3acc83b8fe891692833a9d6fbb59749923b4ab6a40ca784`)
- [observation/documented] Installation is via a Homebrew cask from the rookedsysc/kanvibe tap until the app is accepted into the official Homebrew Cask repository. -- evidence: [README.md#L131-L131](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L131-L131), [README.md#L133-L136](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L133-L136) (`clm_cd2b61c0beaf27b55bbe1d4a8c85486acedb55b3b8967218c61a0f5901d7cfdb`)

## limitations (3 claim(s))

- [observation/documented] Gemini CLI lacks an equivalent to Claude Code's AskUserQuestion, so the PENDING status is not available for Gemini-driven tasks. -- evidence: [README.md#L299-L299](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L299-L299) (`clm_685481ab31e97e3a957cbdc4cf588edfc8ab5ccea3bd5a2bf5143546f5050ab2`)
- [observation/documented] Subtask counts in live session tracking are unavailable for Gemini CLI, version-dependent for OpenCode, and sessions outside tmux are judged only by transcript activity, so waiting sessions may appear idle. -- evidence: [README.md#L221-L228](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L221-L228) (`clm_726403198d6dc35d67962823619f1e2f2288872a2160a78e061bb0ae5a6331d3`)
- [inference/documented] The contributing guide states only Claude Code Hooks support is implemented with Gemini and Codex hooks under development, which appears to conflict with the README's claim of all four agents supported; the README is likely the more current document. -- evidence: [CONTRIBUTING.md#L134-L134](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/CONTRIBUTING.md#L134-L134), [README.md#L275-L275](https://github.com/rookedsysc/kanvibe/blob/05b9c147299aea8f2b6159f4305a19057382af15/README.md#L275-L275) (`clm_f6348db81bbc336f2504697f79efe11ae90440f55f076863f41c0cb19145cc14`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

