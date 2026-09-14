---
access: public
aliases: []
claim_ids:
- clm_1c0849298b95eed49532e84affd5feeb55920f7de74fe9cb490446d0f1f5d214
- clm_248bb5f6ad6f2a74156a21a49b5099cd4b92f7574cb5ecc673ba3d95375c1a5c
- clm_2d499e816f49acee5ced8448599a7e5cbb77964bccb6a79c9a23bff3c94ec308
- clm_342d88330415eee03074a448698d6dc81d70c77c9c35e4a2a2d256fc01dab58d
- clm_4468a53a68ba69156f46f849f625e23c4f984ec33835da42f218dff2c388716b
- clm_805b92d6b1a65f991c5c74d2e381d6127d71790701899ae52df4459f4bfd9ea5
- clm_94013cf1de6ea65ce1a1ea4998857a8f98f02cf6cdb04f3e64058d9480a913ac
maturity: draft
page_id: pg_67bb1a7837a2579dbff44e69f41194e6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0b9bd27fba16534894a6cc76acec9616
title: its-maestro-baby/maestro/README.md @ a10500d09983
updated_at: '2026-09-14T02:06:00Z'
---

# its-maestro-baby/maestro/README.md @ a10500d09983

<!-- rcw:begin owner=source:src_0b9bd27fba16534894a6cc76acec9616 block=evidence -->
- The app offers a dynamic 1x1 to 2x3 session grid, iTerm2-style split panes, real-time status indicators, and per-session mode selection among Claude Code, Gemini CLI, OpenAI Codex, or plain terminal. [@claim:clm_1c0849298b95eed49532e84affd5feeb55920f7de74fe9cb490446d0f1f5d214]
- Each session gets its own terminal with a full shell environment, a git worktree for code isolation, an assigned branch, and a port allocation for web development. [@claim:clm_248bb5f6ad6f2a74156a21a49b5099cd4b92f7574cb5ecc673ba3d95375c1a5c]
- A documented keyboard shortcut set covers session creation, pane splitting, terminal cycling, zoom, copy, and line navigation, with Cmd mapping to Ctrl on Windows/Linux. [@claim:clm_2d499e816f49acee5ced8448599a7e5cbb77964bccb6a79c9a23bff3c94ec308]
- A built-in MCP server lets AI sessions report their state (idle, working, needs input, finished, error) via the maestro_status tool, with updates shown in the session grid. [@claim:clm_342d88330415eee03074a448698d6dc81d70c77c9c35e4a2a2d256fc01dab58d]
- A Rust ProcessManager manages sessions whose worktrees live under ~/.claude-maestro/worktrees/{repo}/{branch}, connecting to the MCP server over stdio. [@claim:clm_4468a53a68ba69156f46f849f625e23c4f984ec33835da42f218dff2c388716b]
- The stack comprises a Tauri 2.0/Rust backend, a React + TypeScript + Tailwind CSS frontend, xterm.js terminal emulation, a Rust MCP server, and native git CLI for git operations. [@claim:clm_805b92d6b1a65f991c5c74d2e381d6127d71790701899ae52df4459f4bfd9ea5]
- Maestro is a cross-platform desktop application for running 1-6 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree. [@claim:clm_94013cf1de6ea65ce1a1ea4998857a8f98f02cf6cdb04f3e64058d9480a913ac]
<!-- rcw:end owner=source:src_0b9bd27fba16534894a6cc76acec9616 block=evidence -->

## Researcher notes

