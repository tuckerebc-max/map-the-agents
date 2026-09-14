# ouijit/ouijit -- full detail

[Back to orientation](ouijit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ouijit/ouijit/b868ef792dc74f398a61e359d4bbe8df25c435e0/6945b93047da6ab2.json](../../../wiki/dossiers/ouijit/ouijit/b868ef792dc74f398a61e359d4bbe8df25c435e0/6945b93047da6ab2.json)

## specifications (2 claim(s))

- [observation/documented] Ouijit is a task and terminal manager for running coding agents in parallel, where each task gets its own git worktree and terminal, with lifecycle hooks launching the agent CLI. -- evidence: [README.md#L9-L9](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L9-L9) (`clm_71f73c843a2d483520389ce9d9367ae6786f45fe35cd7726c45c01135a4956f0`)
- [observation/documented] The project is free and open source under AGPL-3.0, with no account, sign-in, or telemetry, and distributes self-contained builds for macOS (Apple Silicon/Intel) and Linux x64. -- evidence: [README.md#L13-L15](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L13-L15), [README.md#L17-L17](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L17-L17), [README.md#L115-L115](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L115-L115) (`clm_8a85cf2bcf2aadd90fbe7a07e04d205da3e44c728452a2d3cdba0e5086a94932`)

## components (4 claim(s))

- [observation/documented] Tasks live on a kanban board; moving a card between To Do, In Progress, In Review, and Done fires a matching lifecycle hook, and starting a task creates an isolated git worktree. -- evidence: [README.md#L25-L25](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L25-L25) (`clm_5bab2cc5a333c8b903f90830f338ddf4120029d06ab19c3b5146b7f43dd22a08`)
- [observation/documented] Terminals are cards in a stack with attachable panel tabs: a script runner, a web preview, and markdown files with Mermaid diagrams; non-task shells get their own board strip. -- evidence: [README.md#L29-L29](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L29-L29) (`clm_5f894fe31fd20819adc5d4991dd48df00cd55b4ec4294797c35a2963756ceaff`)
- [observation/documented] Each task terminal shows a diff of its worktree against a merge target, uncommitted changes, or a chosen base, with word-level highlighting and per-line notes routed to the agent in that worktree. -- evidence: [README.md#L47-L47](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L47-L47) (`clm_7b8457e7f488730e822425c84f102b052d97ab59acf8fe44ee96d9dc63e7d25e`)
- [observation/documented] An experimental GitHub surface provides a pull request inbox, locally staged review comments, and merging, driven by the `gh` CLI with `gh auth login` as the only setup. -- evidence: [README.md#L47-L47](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L47-L47) (`clm_64406e474e733694ef6b6da5a3d40c5f6edd12499e028256183f06f94f8727b6`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Ouijit shadows agent binaries on PATH to inject lifecycle hooks and a CLI reference into each session, letting agents create tasks, advance the board, and open panels without setup. -- evidence: [README.md#L37-L37](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L37-L37) (`clm_270c260c280bd20f06162d692613176d1a8e56665778f643c12b5e6a57eb9c75`)

## memory-state (1 claim(s))

- [observation/documented] Quitting saves the session, and the next launch offers to restore its terminals in their worktrees, panels included; all data is stored locally in SQLite. -- evidence: [README.md#L63-L63](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L63-L63), [README.md#L79-L79](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L79-L79) (`clm_a2ffbd6fb77fddc94805bfe8e48e5e01bdb12b837d5cefc5686ed4a93d1120c9`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Any terminal can run sandboxed: in a Lima VM mounting only the task's worktree, in place under Seatbelt/Landlock via nono (experimental), or under a user-supplied launcher (experimental). -- evidence: [README.md#L59-L59](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L59-L59) (`clm_a898bebb64a0aad82979737d442811239b0cda75bffbb7a81493f1732d499b12`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product runs on macOS 13+ or Linux x64 and requires git 2.20+ on PATH; supported agent harnesses are Claude Code, Codex, Pi, and OpenCode. -- evidence: [README.md#L83-L86](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L83-L86), [README.md#L115-L115](https://github.com/ouijit/ouijit/blob/b868ef792dc74f398a61e359d4bbe8df25c435e0/README.md#L115-L115) (`clm_234cd870d6aac9a32aa5fda069a89c61d690432fcd2d258115840bf8f9d0bad7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

