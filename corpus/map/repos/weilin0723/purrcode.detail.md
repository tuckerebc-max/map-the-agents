# weilin0723/purrcode -- full detail

[Back to orientation](purrcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/weilin0723/purrcode/156d83206ed74a89398c0adf8d4fccd3e070ae59/f386a16ac8aceb42.json](../../../wiki/dossiers/weilin0723/purrcode/156d83206ed74a89398c0adf8d4fccd3e070ae59/f386a16ac8aceb42.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture defines four subsystems: PawGate (policy/judgment/authorization), Claw (tool execution and sandboxing), Whisker (repository context and risk signals), and NineLives (checkpoints, recovery, rollback). -- evidence: [docs/src/architecture.md#L9-L14](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L9-L14), [docs/architecture.md#L3-L5](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L3-L5) (`clm_9e1ea18de2a265f9ddefe5ce33d2a8a30ba18c64dd2408acee3103dd6ea3b96e`)

## design-choices (2 claim(s))

- [observation/documented] Model output is treated as a proposal, never authority: every native action is bound to a durable authorization, re-checked before execution, and followed by recorded validation; repository content, model output, and downloaded skills are untrusted. -- evidence: [README.md#L24-L24](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L24-L24), [docs/src/architecture.md#L38-L43](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L38-L43) (`clm_dc882e293cc6bbf333c6cc8763fda4fbd852f066f70ab74ed02a8a299436960b`)
- [observation/documented] Actions are strongly typed (Command, RepositoryRead, WriteFile, DeleteFile, ExternalTool) with no shell-string parsing in the trusted path; ExternalTool actions are MCP-only and always require approval. -- evidence: [docs/architecture.md#L43-L50](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L43-L50), [docs/architecture.md#L38-L41](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L38-L41) (`clm_a7726638ccbcdda382c04e7437a79979e71f1c287e1b708a694dc34c40f5cb8f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: repository checks run cargo fmt --check, clippy with -D warnings, cargo test --workspace, plus npm tests for the purrcode package and TypeScript SDK and Python unittest discovery for the Python SDK. -- evidence: [README.md#L172-L179](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L172-L179) (`clm_6cec5f10685cc227fa13b9ac1578c1c1f4e78d00858143fbb240ea8f944a3c4f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a terminal Workbench (bare `purrcode`), a native Rust desktop IDE (`purrcode ide`/`gui`), and a browser Studio client (`purrcode studio`) for daemon health, sessions, and environment inspection. -- evidence: [README.md#L116-L116](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L116-L116), [README.md#L30-L32](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L30-L32) (`clm_c749e9d12bd6ef1a66876f15b3241e62251a11601fc619725cdf50092957b3ab`)
- [observation/documented] TUI slash commands include /connect (provider discovery/import), /mode (Ask/Plan/Build/Review), /permission (Ask/Auto/Full Access), and /ide; one-shot commands include plan, run, review, approve, doctor, sessions, resume, and rollback. -- evidence: [README.md#L120-L126](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L120-L126), [README.md#L132-L133](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L132-L133), [README.md#L136-L139](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L136-L139), [README.md#L142-L144](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L142-L144) (`clm_8bca330ca74031fbc29ebff32dd74a6bfdcc231c5c6872c4bd416b4fb727a147`)

## memory-state (1 claim(s))

- [observation/documented] Authorization is stored in append-only SQLite with exact action/constraint digest verification and atomic single-use consumption; NineLives owns durable events, checkpoints, restart reconciliation, and conservative recovery that never blindly replays interrupted actions. -- evidence: [docs/implementation-status.md#L7-L12](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/implementation-status.md#L7-L12), [docs/architecture.md#L9-L18](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L9-L18), [docs/architecture.md#L3-L5](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L3-L5), [docs/src/architecture.md#L38-L43](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L38-L43) (`clm_86d62b313efbde48d7a496c122a8635013e556fa3a7fa4135473d0c71e61da27`)

## orchestration (1 claim(s))

- [observation/documented] TUI, IDE, and CLI share one daemon-owned session model; the IDE holds no session store, model state, permission state, or execution path, and the daemon exposes typed presentation endpoints (activity, validation, summary, usage). -- evidence: [README.md#L155-L164](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L155-L164), [docs/src/architecture.md#L51-L51](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L51-L51), [docs/implementation-status.md#L16-L53](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/implementation-status.md#L16-L53) (`clm_3b8a94e5cfe6f5795bc5b5e474ecf2723dca41f43dc91df56f7c55b6c607077a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Building from source requires Rust 1.88 or newer, Git, and platform build tools; the npm launcher requires Node.js 18+, and optional isolation dependencies are sandbox-exec (macOS) and bubblewrap (Linux). -- evidence: [README.md#L72-L72](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L72-L72), [docs/installation.md#L70-L72](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/installation.md#L70-L72), [README.md#L60-L60](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L60-L60) (`clm_2fd468cddbb832af7d6a5c090acd44764815cb0e773cd00360ae897414dbc9da`)
- [inference/documented] The IDE appears to depend on the Rust eframe/egui stack, since the docs describe it as a pure-Rust eframe/egui desktop application with no browser, Electron, Tauri, or VS Code dependency. -- evidence: [README.md#L116-L116](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L116-L116), [docs/implementation-status.md#L16-L53](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/implementation-status.md#L16-L53) (`clm_f9c45bb610ee0070d1d3204492ee4eaa5f943a72d02a1f29c820bfb1911f04c1`)

## limitations (1 claim(s))

- [observation/documented] The macOS PurrCode.app is not notarized, so Gatekeeper may block first launch until the user right-clicks and chooses Open; the project plans to notarize future releases. -- evidence: [README.md#L44-L44](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L44-L44) (`clm_2c4d3e8d3cebfd554a8f5fae8cb0f170a696238cef3182b6a4f46f5b0b014685`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

