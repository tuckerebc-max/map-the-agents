# sahithvibudhi/vibe-tree

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f88907703af1 @ b3c79a6d3c9ac605

## Summary (orientation draft, not independently verified)

VibeTree is a desktop/web tool that runs AI coding agents in parallel git worktrees, with a shared Express/WebSocket backend, PTY session management, worktree lifecycle hooks, and configurable authentication. Evidence is mostly README/ARCHITECTURE documentation; no source code slices are present.

## Source coverage

Source coverage (partial): 3 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] VibeTree runs each AI coding agent in its own git worktree in parallel, giving every task an isolated checkout with its own branch and terminal. -- evidence: [README.md#L6-L6](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L6-L6), [README.md#L20-L20](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L20-L20)
- components (2 claim(s)):
  - [observation/documented] The repo is a pnpm + Turborepo monorepo with apps (desktop, web, server) and packages (core, server-core, ui, auth), where desktop and web share one backend. -- evidence: [ARCHITECTURE.md#L9-L25](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L9-L25), [ARCHITECTURE.md#L5-L5](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L5-L5)
  - [observation/documented] ShellSessionManager in packages/core owns all PTYs, one per worktree+terminal, buffering bounded (~100KB) output for replay on reconnect. -- evidence: [ARCHITECTURE.md#L29-L41](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L29-L41), [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55), [ARCHITECTURE.md#L49-L49](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L49-L49)
- design-choices (2 claim(s)):
  - [observation/documented] Worktree lifecycle hooks (.vibetree/hooks/post-create and pre-remove) run around git worktree add/remove; failures warn but never block, and pre-remove cannot block deletion. -- evidence: [ARCHITECTURE.md#L59-L59](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L59-L59), [README.md#L75-L75](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L75-L75)
  - [observation/documented] Electron IPC is reserved for native OS concerns (dialogs, notifications, theme, IDE launching, settings, menus), while app logic goes through the embedded server over WebSocket. -- evidence: [ARCHITECTURE.md#L43-L45](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L43-L45)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run pnpm install, pnpm dev:desktop/dev:all, unit tests via pnpm test:run, Playwright e2e suites, and pnpm typecheck && pnpm lint; CI runs lint, typecheck, unit tests, builds, and e2e. -- evidence: [README.md#L84-L92](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L84-L92), [ARCHITECTURE.md#L72-L74](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L72-L74)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product works with terminal-based agent CLIs including Claude Code, OpenAI Codex CLI, Gemini CLI, Aider, and opencode, since agents run in a real terminal. -- evidence: [README.md#L54-L63](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L54-L63), [README.md#L12-L12](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L12-L12)
  - [observation/documented] It ships as an Electron desktop app and as a standalone server drivable from any browser or phone, including QR pairing for mobile access. -- evidence: [ARCHITECTURE.md#L9-L25](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L9-L25), [README.md#L54-L63](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L54-L63), [README.md#L20-L20](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/README.md#L20-L20)
- memory-state (2 claim(s)):
  - [observation/documented] Terminal sessions survive disconnects: session IDs are deterministic per worktree path and terminal ID, output is buffered from PTY start, and reattach returns the scrollback. -- evidence: [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55)
  - [observation/documented] The standalone server reaps sessions idle beyond SESSION_IDLE_TIMEOUT_MS (default 24h), while the desktop keeps sessions until quit. -- evidence: [ARCHITECTURE.md#L51-L55](https://github.com/sahithvibudhi/vibe-tree/blob/f88907703af1d9b287c5dd1ae93c01645c7dab78/ARCHITECTURE.md#L51-L55)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](vibe-tree.detail.md)

Metadata and full claim list: [full detail](vibe-tree.detail.md)
Human notes ([notes](vibe-tree.notes.md), never overwritten by build)

[Back to map index](../../index.md)
