# akarachen/2code

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fa2465aae831 @ 4ae84c4afc925ca8

## Summary (orientation draft, not independently verified)

The app is a Tauri 2 desktop shell with a React 19 + TypeScript + Vite frontend, Zustand/Immer client state, TanStack Query server state, and a Rust workspace backend with SQLite via Diesel. The Rust backend is layered into handler (Tauri command entry points), service (business logic), repo (Diesel CRUD), infra (DB, PTY, git, watcher), and model crates.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 7 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

7 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The app is a Tauri 2 desktop shell with a React 19 + TypeScript + Vite frontend, Zustand/Immer client state, TanStack Query server state, and a Rust workspace backend with SQLite via Diesel. -- evidence: [README.md#L42-L49](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L42-L49), [AGENTS.md#L6-L6](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L6-L6)
  - [observation/documented] The Rust backend is layered into handler (Tauri command entry points), service (business logic), repo (Diesel CRUD), infra (DB, PTY, git, watcher), and model crates. -- evidence: [README.md#L100-L117](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L100-L117), [CLAUDE.md#L99-L99](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L99-L99), [CLAUDE.md#L86-L89](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L86-L89)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors add Tauri commands in handler/*.rs, register them in lib.rs, then run cargo tauri-typegen generate; Rust tests run via cargo test with in-memory SQLite, and CI includes a Tauri smoke test on ubuntu-24.04 with xvfb-run. -- evidence: [CLAUDE.md#L162-L162](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L162-L162), [README.md#L121-L127](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L121-L127), [AGENTS.md#L79-L88](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L79-L88), [AGENTS.md#L46-L54](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L46-L54)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Profiles create isolated branch workspaces via git worktree add under ~/.2code/workspace/{profile_id}, running a setup_script from 2code.json on creation and teardown_script plus worktree/branch removal on deletion. -- evidence: [README.md#L29-L29](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L29-L29), [CLAUDE.md#L138-L138](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L138-L138)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Building and developing the app requires Bun, a stable Rust toolchain, Tauri 2 prerequisites, just, and fama on PATH for TypeScript formatting. -- evidence: [README.md#L55-L60](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L55-L60)
- limitations (1 claim(s)):
  - [observation/documented] The project is early and under active construction; macOS is the primary supported platform while Windows and Linux builds are experimental. -- evidence: [README.md#L7-L7](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L7-L7), [README.md#L23-L23](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L23-L23)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](2code.detail.md) for every claim.)

Metadata and full claim list: [full detail](2code.detail.md)
Human notes ([notes](2code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
