---
access: public
aliases: []
claim_ids:
- clm_234cd870d6aac9a32aa5fda069a89c61d690432fcd2d258115840bf8f9d0bad7
- clm_270c260c280bd20f06162d692613176d1a8e56665778f643c12b5e6a57eb9c75
- clm_5bab2cc5a333c8b903f90830f338ddf4120029d06ab19c3b5146b7f43dd22a08
- clm_5f894fe31fd20819adc5d4991dd48df00cd55b4ec4294797c35a2963756ceaff
- clm_64406e474e733694ef6b6da5a3d40c5f6edd12499e028256183f06f94f8727b6
- clm_71f73c843a2d483520389ce9d9367ae6786f45fe35cd7726c45c01135a4956f0
- clm_7b8457e7f488730e822425c84f102b052d97ab59acf8fe44ee96d9dc63e7d25e
- clm_8a85cf2bcf2aadd90fbe7a07e04d205da3e44c728452a2d3cdba0e5086a94932
- clm_a2ffbd6fb77fddc94805bfe8e48e5e01bdb12b837d5cefc5686ed4a93d1120c9
- clm_a898bebb64a0aad82979737d442811239b0cda75bffbb7a81493f1732d499b12
maturity: draft
page_id: pg_218a5388ade354e798b002b64210412c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ec4eba6ea092520d92853ffde0d878e8
title: ouijit/ouijit/README.md @ b868ef792dc7
updated_at: '2026-09-14T03:11:37Z'
---

# ouijit/ouijit/README.md @ b868ef792dc7

<!-- rcw:begin owner=source:src_ec4eba6ea092520d92853ffde0d878e8 block=evidence -->
- The product runs on macOS 13+ or Linux x64 and requires git 2.20+ on PATH; supported agent harnesses are Claude Code, Codex, Pi, and OpenCode. [@claim:clm_234cd870d6aac9a32aa5fda069a89c61d690432fcd2d258115840bf8f9d0bad7]
- Ouijit shadows agent binaries on PATH to inject lifecycle hooks and a CLI reference into each session, letting agents create tasks, advance the board, and open panels without setup. [@claim:clm_270c260c280bd20f06162d692613176d1a8e56665778f643c12b5e6a57eb9c75]
- Tasks live on a kanban board; moving a card between To Do, In Progress, In Review, and Done fires a matching lifecycle hook, and starting a task creates an isolated git worktree. [@claim:clm_5bab2cc5a333c8b903f90830f338ddf4120029d06ab19c3b5146b7f43dd22a08]
- Terminals are cards in a stack with attachable panel tabs: a script runner, a web preview, and markdown files with Mermaid diagrams; non-task shells get their own board strip. [@claim:clm_5f894fe31fd20819adc5d4991dd48df00cd55b4ec4294797c35a2963756ceaff]
- An experimental GitHub surface provides a pull request inbox, locally staged review comments, and merging, driven by the `gh` CLI with `gh auth login` as the only setup. [@claim:clm_64406e474e733694ef6b6da5a3d40c5f6edd12499e028256183f06f94f8727b6]
- Ouijit is a task and terminal manager for running coding agents in parallel, where each task gets its own git worktree and terminal, with lifecycle hooks launching the agent CLI. [@claim:clm_71f73c843a2d483520389ce9d9367ae6786f45fe35cd7726c45c01135a4956f0]
- Each task terminal shows a diff of its worktree against a merge target, uncommitted changes, or a chosen base, with word-level highlighting and per-line notes routed to the agent in that worktree. [@claim:clm_7b8457e7f488730e822425c84f102b052d97ab59acf8fe44ee96d9dc63e7d25e]
- The project is free and open source under AGPL-3.0, with no account, sign-in, or telemetry, and distributes self-contained builds for macOS (Apple Silicon/Intel) and Linux x64. [@claim:clm_8a85cf2bcf2aadd90fbe7a07e04d205da3e44c728452a2d3cdba0e5086a94932]
- Quitting saves the session, and the next launch offers to restore its terminals in their worktrees, panels included; all data is stored locally in SQLite. [@claim:clm_a2ffbd6fb77fddc94805bfe8e48e5e01bdb12b837d5cefc5686ed4a93d1120c9]
- Any terminal can run sandboxed: in a Lima VM mounting only the task's worktree, in place under Seatbelt/Landlock via nono (experimental), or under a user-supplied launcher (experimental). [@claim:clm_a898bebb64a0aad82979737d442811239b0cda75bffbb7a81493f1732d499b12]
<!-- rcw:end owner=source:src_ec4eba6ea092520d92853ffde0d878e8 block=evidence -->

## Researcher notes

