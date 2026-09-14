# johannesjo/parallel-code

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dcc4df2592cc @ 77106abc8209e886

## Summary (orientation draft, not independently verified)

Parallel Code is an MIT-licensed Electron/SolidJS desktop app for dispatching multiple AI coding CLIs in parallel, each isolated in its own git worktree, with diff review, Docker sandboxing, and remote phone monitoring. Evidence is mostly README/PRIVACY documentation plus contributor instructions in CLAUDE.md.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The app is an Electron desktop application with a SolidJS frontend and Node.js backend, published for macOS and Linux only. -- evidence: [CLAUDE.md#L3-L3](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L3-L3), [README.md#L20-L26](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L20-L26)
  - [observation/documented] Features include a built-in diff viewer with inline comments, per-task notes and canvas panels, per-task shell terminals, and an AI Arena head-to-head mode. -- evidence: [README.md#L40-L44](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L40-L44), [README.md#L82-L98](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L82-L98)
- design-choices (1 claim(s)):
  - [observation/documented] Docker sandboxing is supported via a project-specific Dockerfile placed at .parallel-code/Dockerfile, in which tasks then run. -- evidence: [README.md#L82-L98](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L82-L98), [PRIVACY.md#L97-L99](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L97-L99)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: build from source with git clone, npm install, and npm run dev, requiring Node.js v18+; npm run typecheck runs TypeScript checking. -- evidence: [README.md#L143-L143](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L143-L143), [README.md#L136-L141](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L136-L141), [CLAUDE.md#L13-L15](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L13-L15)
  - [observation/documented] Repository development practice: conventions require functional SolidJS components, strict TypeScript with no any, and Electron IPC with channel names in a shared enum. -- evidence: [CLAUDE.md#L27-L30](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/CLAUDE.md#L27-L30)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Creating a task makes a git branch from main, sets up a git worktree, symlinks gitignored directories like node_modules, and spawns the AI agent there. -- evidence: [README.md#L72-L75](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L72-L75)
  - [observation/documented] Completed task branches can be merged back to main from the sidebar. -- evidence: [README.md#L77-L77](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L77-L77)
- memory-state (1 claim(s)):
  - [observation/documented] State is stored locally: state.json with a rolling backup, keybindings, themes, arena files, and a .updaterId UUID in per-OS app data directories. -- evidence: [PRIVACY.md#L86-L86](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L86-L86), [PRIVACY.md#L88-L93](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L88-L93)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] For coordinator sub-tasks, the app injects a system-prompt preamble telling the sub-agent to call the signal_done MCP tool, via .claude/settings.local.json for Claude Code. -- evidence: [PRIVACY.md#L44-L44](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L44-L44), [PRIVACY.md#L97-L99](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L97-L99)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The app drives third-party AI coding CLIs the user installs, including Claude Code, Codex CLI, Gemini CLI, Copilot CLI, OpenCode, and Antigravity CLI. -- evidence: [README.md#L120-L120](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/README.md#L120-L120), [PRIVACY.md#L31-L31](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L31-L31), [PRIVACY.md#L33-L38](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L33-L38)
  - [observation/documented] Packaged macOS and Linux builds check GitHub Releases for updates via electron-updater, sending a stable per-install x-user-staging-id UUID to GitHub. -- evidence: [PRIVACY.md#L50-L70](https://github.com/johannesjo/parallel-code/blob/dcc4df2592cc271c463ef3f5e46f0e286096fb9c/PRIVACY.md#L50-L70)
More evidence: [full detail](parallel-code.detail.md)

Metadata and full claim list: [full detail](parallel-code.detail.md)
Human notes ([notes](parallel-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
