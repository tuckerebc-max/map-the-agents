# its-maestro-baby/maestro -- full detail

[Back to orientation](maestro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/its-maestro-baby/maestro/a10500d099836e7e7185977c1cda6f263a53b55d/2540374749b8bbe4.json](../../../wiki/dossiers/its-maestro-baby/maestro/a10500d099836e7e7185977c1cda6f263a53b55d/2540374749b8bbe4.json)

## specifications (1 claim(s))

- [observation/documented] Maestro is a cross-platform desktop application for running 1-6 Claude Code (or other AI CLI) sessions simultaneously, each in its own isolated git worktree. -- evidence: [README.md#L10-L10](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L10-L10) (`clm_94013cf1de6ea65ce1a1ea4998857a8f98f02cf6cdb04f3e64058d9480a913ac`)

## components (2 claim(s))

- [observation/documented] The stack comprises a Tauri 2.0/Rust backend, a React + TypeScript + Tailwind CSS frontend, xterm.js terminal emulation, a Rust MCP server, and native git CLI for git operations. -- evidence: [README.md#L178-L184](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L178-L184) (`clm_805b92d6b1a65f991c5c74d2e381d6127d71790701899ae52df4459f4bfd9ea5`)
- [observation/documented] The Rust backend has command handlers for git, worktrees, GitHub, marketplace, MCP, sessions, terminals, updates, and usage, plus core modules for process, plugin, worktree, and session management. -- evidence: [ARCHITECTURE-OVERVIEW.md#L99-L112](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L99-L112), [ARCHITECTURE-OVERVIEW.md#L116-L126](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L116-L126) (`clm_f3e7c9bb07fec59fcbe24ebca9d4300675180b39d3ad6b9b222c822cef23db56`)

## design-choices (1 claim(s))

- [observation/documented] Each session gets its own terminal with a full shell environment, a git worktree for code isolation, an assigned branch, and a port allocation for web development. -- evidence: [README.md#L47-L51](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L47-L51) (`clm_248bb5f6ad6f2a74156a21a49b5099cd4b92f7574cb5ecc673ba3d95375c1a5c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the documented development workflow starts by running all tests, uses 'roam' and 'dora' skills to review related components, implements changes, then runs related tests and summarizes. -- evidence: [AGENTS.md#L186-L191](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/AGENTS.md#L186-L191) (`clm_4f9fb081fd17219cfaa0db3634f7e9e7838ccef8014f0d9f0c87f41a6aca60a4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The app offers a dynamic 1x1 to 2x3 session grid, iTerm2-style split panes, real-time status indicators, and per-session mode selection among Claude Code, Gemini CLI, OpenAI Codex, or plain terminal. -- evidence: [README.md#L67-L70](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L67-L70) (`clm_1c0849298b95eed49532e84affd5feeb55920f7de74fe9cb490446d0f1f5d214`)
- [observation/documented] A documented keyboard shortcut set covers session creation, pane splitting, terminal cycling, zoom, copy, and line navigation, with Cmd mapping to Ctrl on Windows/Linux. -- evidence: [README.md#L138-L138](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L138-L138), [README.md#L121-L136](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L121-L136) (`clm_2d499e816f49acee5ced8448599a7e5cbb77964bccb6a79c9a23bff3c94ec308`)

## memory-state (1 claim(s))

- [observation/documented] Frontend state is organized into Zustand stores including useGitHubStore, useGitStore, useWorkspaceStore, useSessionStore, useMarketplaceStore, and useMcpStore. -- evidence: [ARCHITECTURE-OVERVIEW.md#L132-L143](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L132-L143) (`clm_26603713113acd85c431057d86988577713fe8d6e8ebfcff966d31b8076ffadf`)

## orchestration (1 claim(s))

- [observation/documented] A Rust ProcessManager manages sessions whose worktrees live under ~/.claude-maestro/worktrees/{repo}/{branch}, connecting to the MCP server over stdio. -- evidence: [README.md#L144-L174](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L144-L174) (`clm_4468a53a68ba69156f46f849f625e23c4f984ec33835da42f218dff2c388716b`)

## tools-permissions (1 claim(s))

- [observation/documented] A built-in MCP server lets AI sessions report their state (idle, working, needs input, finished, error) via the maestro_status tool, with updates shown in the session grid. -- evidence: [README.md#L80-L83](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/README.md#L80-L83) (`clm_342d88330415eee03074a448698d6dc81d70c77c9c35e4a2a2d256fc01dab58d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Key frontend dependencies include @tauri-apps/api ^2.10.1, @xterm/xterm ^5.5.0, react ^18.3.0, zustand ^5.0.10, and tailwindcss ^3.4.0; the backend uses Tauri 2.0, tokio, serde, and DashMap. -- evidence: [ARCHITECTURE-OVERVIEW.md#L191-L195](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L191-L195), [ARCHITECTURE-OVERVIEW.md#L198-L201](https://github.com/its-maestro-baby/maestro/blob/a10500d099836e7e7185977c1cda6f263a53b55d/ARCHITECTURE-OVERVIEW.md#L198-L201) (`clm_039bd1db609224cd2a16193080f49bd8d77b87d9aa9efb44dbbfd4d55a1fc7d8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

