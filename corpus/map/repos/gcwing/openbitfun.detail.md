# gcwing/openbitfun -- full detail

[Back to orientation](openbitfun.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/gcwing/openbitfun/32b20c5b291d0e281b3920c84606e646e0e3524a/8a36a510244d7500.json](../../../wiki/dossiers/gcwing/openbitfun/32b20c5b291d0e281b3920c84606e646e0e3524a/8a36a510244d7500.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] OpenBitFun is described as an open-source desktop workspace for AI agents combining a Rust Agent Runtime, an Agent Harness, and a desktop experience. -- evidence: [README.md#L11-L11](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L11-L11) (`clm_b939ff66b7d240c5b52b1c64425f0d9394eaa0d72a77f46e6c19dd785f98bdf4`)
- [observation/documented] Mini Apps pair a dedicated interface with an agent conversation, can be built by describing needs to the agent, and can be installed, reused, or shared via a marketplace. -- evidence: [README.md#L65-L65](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L65-L65), [README.md#L61-L61](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L61-L61), [README.md#L63-L63](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L63-L63) (`clm_346fbd0f216a9c269cf0bb56466e0fe3f202dbe9ad890b120f862bda2f1aeedc`)

## design-choices (5 claim(s))

- [observation/documented] The Agent Harness offers four working modes: Minimal (direct collaboration), Standard (multi-step tasks), Ultimate (delegating work across agents), and Creative (building Mini Apps and extending the interface). -- evidence: [README.md#L29-L29](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L29-L29), [README.md#L33-L38](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L33-L38) (`clm_c38dd7476873e8563488efce6677d7f5362422155f605224d63accb6cc836cbe`)
- [observation/documented] The architecture keeps product logic platform-independent and exposes capabilities through platform adapter layers; shared core must avoid host APIs like Tauri's AppHandle in favor of shared abstractions. -- evidence: [AGENTS-CN.md#L7-L7](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L7-L7), [CONTRIBUTING_CN.md#L84-L90](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L84-L90), [AGENTS-CN.md#L127-L129](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L127-L129) (`clm_11c8f0bf4cd9c5ed0c5b817f74ca77c6f4b0e3e065756f756420f7b88468675b`)
- [observation/documented] Remote scenarios (remote workspaces, remote control, peer-device mode, and detached task dispatch) are treated as first-class design targets, with rules requiring explicit unsupported states and reconnect-tolerant, resumable behavior. -- evidence: [AGENTS-CN.md#L136-L141](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L136-L141), [AGENTS-CN.md#L145-L154](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L145-L154), [AGENTS-CN.md#L133-L134](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L133-L134) (`clm_44e437980b43550add7d25f9c2b5f81bd5668e9b6f4d0f381b46f8ec3ab74f6d`)
- [observation/documented] The SDLC harness design specifies a configuration hierarchy where organizational mandates and security boundaries outrank team rules, workspace config, session overrides, and user defaults. -- evidence: [docs/sdlc-harness/design.md#L143-L150](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/docs/sdlc-harness/design.md#L143-L150) (`clm_e36aaa753c71bac933786437c1ad38d6c5021363215b6559c41947e5f089a024`)
- [observation/documented] The SDLC harness design separates execution security from quality governance, keeps safety boundaries prior to user overrides, and requires every prompt, escalation, block, or override to be explainable with source and reason. -- evidence: [docs/sdlc-harness/design.md#L87-L99](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/docs/sdlc-harness/design.md#L87-L99), [docs/sdlc-harness/design.md#L8-L18](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/docs/sdlc-harness/design.md#L8-L18) (`clm_86539d6bd157bef0fd42c3377ce24be1e43930972be82d364c95ac0165b1dbce`)

## workflows (7 claim(s))

- [observation/documented] Repository development practice: contributors run `pnpm install` and `pnpm run desktop:dev` for full hot reload (Vite HMR plus automatic Rust rebuild), with a lighter `desktop:preview:debug` mode that reuses a prebuilt binary. -- evidence: [CONTRIBUTING_CN.md#L70-L70](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L70-L70), [AGENTS-CN.md#L52-L53](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L52-L53), [README.md#L125-L128](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L125-L128) (`clm_884b8370b306205f7a65ff15e4d6907816b87a3bd3a42c74d15748474e147382`)
- [observation/documented] Repository development practice: PRs go directly to the `main` branch, should use Conventional Commits-style titles, stay small and focused, and AI-assisted output must be declared with its testing level. -- evidence: [CONTRIBUTING_CN.md#L124-L129](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L124-L129), [CONTRIBUTING_CN.md#L150-L150](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L150-L150), [CONTRIBUTING_CN.md#L133-L133](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L133-L133), [CONTRIBUTING_CN.md#L146-L146](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L146-L146), [CONTRIBUTING_CN.md#L122-L122](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L122-L122) (`clm_d7be599558f7b69a28305799d16a29e259bb599963ba48fe601918e12f896695`)
- [observation/documented] Repository development practice: a repository object-size check rejects Git objects over 5 MiB, including files added and later deleted in intermediate commits, with a script available to check before pushing. -- evidence: [CONTRIBUTING_CN.md#L137-L142](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L137-L142) (`clm_8a2051265d85dda7cc4eadb003032ee852168005a1996830163403673858ecd9`)
- [observation/documented] Repository development practice: Rust files should be formatted with `pnpm run fmt:rs` targeting only changed or staged files, and repo-level checks include hygiene, GitHub config, and core-boundaries scripts. -- evidence: [AGENTS-CN.md#L56-L60](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L56-L60), [AGENTS-CN.md#L11-L15](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L11-L15) (`clm_94a5e729008de8450df67e98a4127ed817354a8284e431506314a3fc00ff3ded`)
- [observation/documented] Repository development practice: verification scope is owner-determined; contributors pick the narrowest focused command near the change and leave broad builds and platform matrices to CI. -- evidence: [AGENTS-CN.md#L276-L282](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L276-L282), [AGENTS-CN.md#L274-L274](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L274-L274), [CONTRIBUTING_CN.md#L154-L155](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L154-L155) (`clm_71e59a435c3f9c1e1adbb44c94e3aa932622c1fd0b8e50b8e76ca57f290e5b0c`)
- [observation/documented] Repository development practice: logs must be English-only without emoji, and Tauri commands use snake_case names with structured request parameters passed from TypeScript. -- evidence: [AGENTS-CN.md#L110-L111](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L110-L111), [AGENTS-CN.md#L103-L103](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L103-L103), [CONTRIBUTING_CN.md#L84-L90](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L84-L90) (`clm_a08034b0c94e5bdfa336b43231f768fd2bf16d3e40ae7cb3279f97816e295817`)
- [observation/documented] Repository development practice: a build prerequisites checker (`pnpm run check:build-prereqs`) diagnoses missing node_modules, mobile-web dist output, or sherpa-onnx libraries, with an optional --fix mode. -- evidence: [CONTRIBUTING_CN.md#L27-L29](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L27-L29), [CONTRIBUTING_CN.md#L31-L34](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L31-L34), [CONTRIBUTING_CN.md#L38-L45](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L38-L45) (`clm_aac7a47abf47c581964215b7ac990254f9a0379e4631e7b5c4114971886a05ef`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product supports connecting tools via MCP, turning repeatable processes into Skills, customizing task execution with Hooks, and installing skins or modifying UI, tools, and runtime source. -- evidence: [README.md#L71-L73](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L71-L73) (`clm_96c9a3fc45e780028dae252cdc7ceda4201741d9c18e8bf90d13c55096543670`)
- [observation/documented] Users can work over SSH on remote hosts, jump hosts, or containers, with files, commands, and agent execution in the target environment; the desktop app and CLI share core execution capabilities. -- evidence: [README.md#L53-L53](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L53-L53) (`clm_80846968bd57c2e5bd773565f6a623930cdbcb0906157d5d0f1904471d087fff`)
- [observation/documented] Cross-device account login, synchronization, and control run through a self-deployable Relay server, with mobile clients and messaging bots as additional ways to control tasks. -- evidence: [README.md#L53-L53](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L53-L53), [README.md#L55-L55](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L55-L55) (`clm_ec3d047ef60974e175befcf23d3de1847434f9ce52dbc2df978f4468430db617`)
- [observation/documented] Native user Hooks implement the Codex Hook contract, with the portable hook engine in `openbitfun-agent-runtime::native_hooks` and hooks from user config, plugins, or built-ins registered in a shared HookRegistry. -- evidence: [AGENTS-CN.md#L207-L209](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L207-L209) (`clm_dadecfda4d2a15e1bc428c991384154601d37ce0758c59e36bf5d56eaaef43a8`)

## memory-state (1 claim(s))

- [observation/documented] The Rust Agent Runtime reportedly manages session state and context, with persistent sessions, interruption recovery, long-term memory, context compression, and cache reuse for longer runs. -- evidence: [README.md#L81-L81](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L81-L81) (`clm_f0b7dbfc2de6c5fd308044162f24407bb00f5086cc01dc994ba13a21f9771643`)

## orchestration (1 claim(s))

- [observation/documented] The harness plans steps, manages context, calls tools, coordinates multiple agents, and combines their results; the Ultimate mode is aimed at dividing demanding work among agents. -- evidence: [README.md#L29-L29](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L29-L29), [README.md#L33-L38](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L33-L38) (`clm_a24a2c8ad44cba053884c9da04a3195b24c4ff18f0f471ed2a2ac7575e080d12`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A reported DeepSWE v1.1 evaluation gives OpenBitFun a 64.6% pass rate with 42.9-minute median runtime on GLM-5.3-Flash and 56.6% with 19.6 minutes on DeepSeek-V4-Flash. -- evidence: [README.md#L83-L83](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L83-L83), [README.md#L85-L86](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L85-L86) (`clm_b56111df1b6e259aad79f5765a75e60066483a6e40e5511c372d0119da6f09d3`)

## dependencies (2 claim(s))

- [observation/documented] Running from source requires Node.js 22.12+, pnpm 10.15.0, the Rust toolchain, and Tauri prerequisites; the project is a Rust workspace with a React/TypeScript frontend. -- evidence: [AGENTS-CN.md#L5-L5](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L5-L5), [CONTRIBUTING_CN.md#L5-L5](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L5-L5), [README.md#L123-L123](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L123-L123) (`clm_d44257328f992eaf2466c90d6ea982d1d2f1d151f820b74948c6c23f3ed4d06c`)
- [observation/documented] The sherpa-onnx prebuilt library is downloaded from GitHub at build time by sherpa-onnx-sys, with a `SHERPA_ONNX_LIB_DIR` fallback to a local prebuilt copy when downloads fail. -- evidence: [CONTRIBUTING_CN.md#L38-L45](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L38-L45) (`clm_c2cc43472c3d2aeb849b67cd1af27408b04cb7b7f998a23c228a9bbaef480b44`)

## limitations (1 claim(s))

- [observation/documented] Optional legacy data migration uses a separately downloaded Data Migrator that runs independently and is not bundled with or launched by the main application. -- evidence: [README.md#L108-L110](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L108-L110) (`clm_07d3cf8a7a37e4765de55ad081fc1326904f26ecc8c4f5e6690be026beb9ace1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

