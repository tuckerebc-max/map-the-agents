---
access: public
aliases: []
claim_ids:
- clm_087676e90631b7f7e584a10785e506fad53963e64aa14b73af9c0f67d5c57a76
- clm_0cd17d9257880fef00d88ec6e0623d2a933ee10f174623a99d5802addfbbbc2b
- clm_25333948595f7f979f919cdc767158311e7056a49176ff63f6d0982ab59dfa91
- clm_3d40a8e748d1b4bf9e6cecd6fe0eacf130542203168c45f8399a21b0f38182e9
- clm_3f898eaa8d37498fe04c0500d3acb5e9bd1268b603d1a4ea416ada4bc7a7d947
- clm_661d393fc66356c62e7d5a27ac9c1a6eabb725268487c261bcd2b6db718c25ec
- clm_7cff94270b1ed89720011b86265ae6f6a75efd57da92e5e0cf326e1e7ec5b742
- clm_7e02a8c44ce62f8ec6d42e2c852f68e49a5e16fb11272a16e82e0dfefaaf78a8
- clm_be7cc3e4fd93465e3cfa218f813650761bd9956dd5d486ea8c43f4afbbe2227c
- clm_d0184dba068d5c2ef3ad6babcd347df1e4ce76d794ec9f615e7a8f80f55f5deb
maturity: draft
page_id: pg_b4ee9548ad14573597d7446310a469fe
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a6ed75c969f154ae924b31a6e7e21a32
title: eneskirca/nodeterm/README.md @ 8fd38d2c229e
updated_at: '2026-09-14T01:48:25Z'
---

# eneskirca/nodeterm/README.md @ 8fd38d2c229e

<!-- rcw:begin owner=source:src_a6ed75c969f154ae924b31a6e7e21a32 block=evidence -->
- Services (PTY, workspace/settings, git, agents, hooks) live in src/core behind a CorePlatform interface and never import Electron; the browser Server Edition boots the same services over a WebSocket-RPC bridge. [@claim:clm_087676e90631b7f7e584a10785e506fad53963e64aa14b73af9c0f67d5c57a76]
- The app is Electron with three contexts: src/main as the shell, src/preload as the sole bridge exposing window.nodeTerminal, and src/renderer as React UI, with src/shared holding types and IPC channel names used by all three. [@claim:clm_0cd17d9257880fef00d88ec6e0623d2a933ee10f174623a99d5802addfbbbc2b]
- Windows support is beta: the installer is unsigned, updates are manual, and restart-to-restart session continuity is still landing because Windows lacks tmux; a standalone session host replacing it is being packaged. [@claim:clm_25333948595f7f979f919cdc767158311e7056a49176ff63f6d0982ab59dfa91]
- The project targets people with scattered workflows who want a spatial canvas of terminals and live Claude Code sessions instead of stacked terminal tabs, across desktop, self-hosted browser, and iOS surfaces. [@claim:clm_3d40a8e748d1b4bf9e6cecd6fe0eacf130542203168c45f8399a21b0f38182e9]
- Repository development practice: contributors run npm install, npm run dev, npm run typecheck (described as the fastest correctness gate), and npm test (vitest unit + integration); Windows uses bootstrap-windows.bat instead of npm install. [@claim:clm_3f898eaa8d37498fe04c0500d3acb5e9bd1268b603d1a4ea416ada4bc7a7d947]
- The Server Edition runs headless on a Linux or macOS host, accessed from any browser with single-user password auth, a WebSocket bridge, and the same renderer as the desktop app. [@claim:clm_661d393fc66356c62e7d5a27ac9c1a6eabb725268487c261bcd2b6db718c25ec]
- The renderer depends only on a TerminalTransport abstraction: LocalTransport talks to the local host and RemoteTransport to a remote agent over SSH, so remote projects drop in without canvas UI changes. [@claim:clm_7cff94270b1ed89720011b86265ae6f6a75efd57da92e5e0cf326e1e7ec5b742]
- Terminals run in persistent tmux sessions surviving node remounts, app restarts, and machine reboots, restoring scrollback and resuming agent sessions via claude --resume; the macOS app bundles its own tmux, preferring any system tmux. [@claim:clm_7e02a8c44ce62f8ec6d42e2c852f68e49a5e16fb11272a16e82e0dfefaaf78a8]
- Node kinds include terminal (xterm + tmux), agent (Claude Code, Codex, Gemini, Copilot, opencode, Grok, custom), sticky notes linkable as agent context, groups bound to git worktrees, Monaco editors, diff views, and web/video nodes. [@claim:clm_be7cc3e4fd93465e3cfa218f813650761bd9956dd5d486ea8c43f4afbbe2227c]
- Agent status is hook-driven rather than output-scraped, showing RUNNING / NEEDS YOU badges, subagent cards with live transcripts, a per-node context meter, OS notifications, and in-node permission prompts. [@claim:clm_d0184dba068d5c2ef3ad6babcd347df1e4ce76d794ec9f615e7a8f80f55f5deb]
<!-- rcw:end owner=source:src_a6ed75c969f154ae924b31a6e7e21a32 block=evidence -->

## Researcher notes

