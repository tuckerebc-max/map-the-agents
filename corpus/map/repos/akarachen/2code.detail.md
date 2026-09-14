# akarachen/2code -- full detail

[Back to orientation](2code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/akarachen/2code/fa2465aae831d6aca93f2898973ba070a3f0db9f/4ae84c4afc925ca8.json](../../../wiki/dossiers/akarachen/2code/fa2465aae831d6aca93f2898973ba070a3f0db9f/4ae84c4afc925ca8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The app is a Tauri 2 desktop shell with a React 19 + TypeScript + Vite frontend, Zustand/Immer client state, TanStack Query server state, and a Rust workspace backend with SQLite via Diesel. -- evidence: [README.md#L42-L49](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L42-L49), [AGENTS.md#L6-L6](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L6-L6) (`clm_f5cf8800e6b7e498dc4d3a3efecfdb95d5898bbc7b3248f52ee84080ead95e0d`)
- [observation/documented] The Rust backend is layered into handler (Tauri command entry points), service (business logic), repo (Diesel CRUD), infra (DB, PTY, git, watcher), and model crates. -- evidence: [README.md#L100-L117](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L100-L117), [CLAUDE.md#L99-L99](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L99-L99), [CLAUDE.md#L86-L89](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L86-L89) (`clm_487ea6b661c068529ffed753d17ab4d6fe244fb26379b816f662de479a6821cc`)
- [observation/documented] The frontend detects coding-agent state (running/waiting/idle) from xterm screen text, OSC titles, and OSC progress, with per-agent rule manifests; waiting status can trigger a system sound. -- evidence: [README.md#L33-L38](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L33-L38), [CLAUDE.md#L101-L101](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L101-L101) (`clm_e0b5edb52d7116d28f2531f6c25b47bffc428b7179bd1739c482e43f3986fa93`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors add Tauri commands in handler/*.rs, register them in lib.rs, then run cargo tauri-typegen generate; Rust tests run via cargo test with in-memory SQLite, and CI includes a Tauri smoke test on ubuntu-24.04 with xvfb-run. -- evidence: [CLAUDE.md#L162-L162](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L162-L162), [README.md#L121-L127](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L121-L127), [AGENTS.md#L79-L88](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L79-L88), [AGENTS.md#L46-L54](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/AGENTS.md#L46-L54) (`clm_a47332e375947b72cc1d351ad75760736848da406bcc167d0f40fcca95f2064e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Profiles create isolated branch workspaces via git worktree add under ~/.2code/workspace/{profile_id}, running a setup_script from 2code.json on creation and teardown_script plus worktree/branch removal on deletion. -- evidence: [README.md#L29-L29](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L29-L29), [CLAUDE.md#L138-L138](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/CLAUDE.md#L138-L138) (`clm_e75d81ee3930dbc7e1718383f453c75b8d8892881b94f43ce4102ec24365bc24`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building and developing the app requires Bun, a stable Rust toolchain, Tauri 2 prerequisites, just, and fama on PATH for TypeScript formatting. -- evidence: [README.md#L55-L60](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L55-L60) (`clm_1773df8e4126991bc781f36452a315c1ba3434ef7c5e3b7b4f7032cd16ecc3fc`)

## limitations (1 claim(s))

- [observation/documented] The project is early and under active construction; macOS is the primary supported platform while Windows and Linux builds are experimental. -- evidence: [README.md#L7-L7](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L7-L7), [README.md#L23-L23](https://github.com/AkaraChen/2code/blob/fa2465aae831d6aca93f2898973ba070a3f0db9f/README.md#L23-L23) (`clm_af0975d7da28362cf9f2612c0688712568e3b721a18908586dc37dab3d5bd3de`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

