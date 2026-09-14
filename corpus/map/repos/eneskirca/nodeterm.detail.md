# eneskirca/nodeterm -- full detail

[Back to orientation](nodeterm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/eneskirca/nodeterm/8fd38d2c229e2ba1f18822df30c48afdefe83e37/f57e03c407f29b9f.json](../../../wiki/dossiers/eneskirca/nodeterm/8fd38d2c229e2ba1f18822df30c48afdefe83e37/f57e03c407f29b9f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The app is Electron with three contexts: src/main as the shell, src/preload as the sole bridge exposing window.nodeTerminal, and src/renderer as React UI, with src/shared holding types and IPC channel names used by all three. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311) (`clm_0cd17d9257880fef00d88ec6e0623d2a933ee10f174623a99d5802addfbbbc2b`)

## design-choices (1 claim(s))

- [observation/documented] Services (PTY, workspace/settings, git, agents, hooks) live in src/core behind a CorePlatform interface and never import Electron; the browser Server Edition boots the same services over a WebSocket-RPC bridge. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311) (`clm_087676e90631b7f7e584a10785e506fad53963e64aa14b73af9c0f67d5c57a76`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run npm install, npm run dev, npm run typecheck (described as the fastest correctness gate), and npm test (vitest unit + integration); Windows uses bootstrap-windows.bat instead of npm install. -- evidence: [CONTRIBUTING.md#L20-L23](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L20-L23), [CONTRIBUTING.md#L13-L18](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L13-L18), [README.md#L264-L275](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L264-L275) (`clm_3f898eaa8d37498fe04c0500d3acb5e9bd1268b603d1a4ea416ada4bc7a7d947`)
- [observation/documented] Repository development practice: the process-boundary split is enforced by guard tests that fail if src/core or src/server import electron or ../main/*, and new service logic must go in src/core behind CorePlatform. -- evidence: [CONTRIBUTING.md#L47-L48](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L47-L48), [CONTRIBUTING.md#L50-L52](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L50-L52), [CONTRIBUTING.md#L36-L36](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L36-L36) (`clm_36c34b27f25898c9ea153d3d4bc65b66f48916b9dff2036ebc70a7fdd2f1a3d7`)
- [observation/documented] Repository development practice: house rules require atomic file writes via renameAtomic/writeFileAtomic, an 'error' listener on child stdin before the first write, and credentials never passed on argv, each backed by guard tests that fail PRs. -- evidence: [CONTRIBUTING.md#L187-L195](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L187-L195), [CONTRIBUTING.md#L267-L271](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L267-L271), [CONTRIBUTING.md#L165-L173](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/CONTRIBUTING.md#L165-L173) (`clm_897141901f4d7d443af844eafbad34eac0a0b294dcf626b3cb507b0b77601353`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The renderer depends only on a TerminalTransport abstraction: LocalTransport talks to the local host and RemoteTransport to a remote agent over SSH, so remote projects drop in without canvas UI changes. -- evidence: [README.md#L297-L311](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L297-L311) (`clm_7cff94270b1ed89720011b86265ae6f6a75efd57da92e5e0cf326e1e7ec5b742`)
- [observation/documented] Node kinds include terminal (xterm + tmux), agent (Claude Code, Codex, Gemini, Copilot, opencode, Grok, custom), sticky notes linkable as agent context, groups bound to git worktrees, Monaco editors, diff views, and web/video nodes. -- evidence: [README.md#L125-L128](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L125-L128) (`clm_be7cc3e4fd93465e3cfa218f813650761bd9956dd5d486ea8c43f4afbbe2227c`)
- [observation/documented] The Server Edition runs headless on a Linux or macOS host, accessed from any browser with single-user password auth, a WebSocket bridge, and the same renderer as the desktop app. -- evidence: [README.md#L165-L168](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L165-L168) (`clm_661d393fc66356c62e7d5a27ac9c1a6eabb725268487c261bcd2b6db718c25ec`)

## memory-state (1 claim(s))

- [observation/documented] Terminals run in persistent tmux sessions surviving node remounts, app restarts, and machine reboots, restoring scrollback and resuming agent sessions via claude --resume; the macOS app bundles its own tmux, preferring any system tmux. -- evidence: [README.md#L132-L161](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L132-L161), [THIRD-PARTY-NOTICES.md#L32-L41](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/THIRD-PARTY-NOTICES.md#L32-L41) (`clm_7e02a8c44ce62f8ec6d42e2c852f68e49a5e16fb11272a16e82e0dfefaaf78a8`)

## orchestration (1 claim(s))

- [observation/documented] Agent status is hook-driven rather than output-scraped, showing RUNNING / NEEDS YOU badges, subagent cards with live transcripts, a per-node context meter, OS notifications, and in-node permission prompts. -- evidence: [README.md#L76-L79](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L76-L79) (`clm_d0184dba068d5c2ef3ad6babcd347df1e4ce76d794ec9f615e7a8f80f55f5deb`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Bundled components include Electron, React, React Flow, xterm, Monaco, node-pty, zustand, electron-updater/builder, ws, and tweetnacl, plus tmux/libevent/utf8proc in macOS builds; the Anthropic agent SDK is proprietary. -- evidence: [THIRD-PARTY-NOTICES.md#L8-L25](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/THIRD-PARTY-NOTICES.md#L8-L25) (`clm_737518d05fb0451597e68b750ca1d8e529ab692c5da2529c48ed95fb018cb2b5`)

## limitations (1 claim(s))

- [observation/documented] Windows support is beta: the installer is unsigned, updates are manual, and restart-to-restart session continuity is still landing because Windows lacks tmux; a standalone session host replacing it is being packaged. -- evidence: [README.md#L207-L226](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L207-L226) (`clm_25333948595f7f979f919cdc767158311e7056a49176ff63f6d0982ab59dfa91`)

## relevance (1 claim(s))

- [observation/documented] The project targets people with scattered workflows who want a spatial canvas of terminals and live Claude Code sessions instead of stacked terminal tabs, across desktop, self-hosted browser, and iOS surfaces. -- evidence: [README.md#L44-L50](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L44-L50), [README.md#L9-L12](https://github.com/eneskirca/nodeterm/blob/8fd38d2c229e2ba1f18822df30c48afdefe83e37/README.md#L9-L12) (`clm_3d40a8e748d1b4bf9e6cecd6fe0eacf130542203168c45f8399a21b0f38182e9`)

