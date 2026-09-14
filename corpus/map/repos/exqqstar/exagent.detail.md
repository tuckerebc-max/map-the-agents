# exqqstar/exagent -- full detail

[Back to orientation](exagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/exqqstar/exagent/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/7e7049df465467e0.json](../../../wiki/dossiers/exqqstar/exagent/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/7e7049df465467e0.json)

## specifications (1 claim(s))

- [observation/documented] ExAgent is a desktop-first agent workbench with a Rust runtime and Tauri/React GUI, aimed at long-running coding work in local projects with resumable sessions. -- evidence: [README.md#L21-L24](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L21-L24) (`clm_ec655c89135001641b1a84c96b750ee762cb65a7cf6d01cb2c890735a08e424b`)

## components (1 claim(s))

- [observation/documented] Each thread runs behind an actor-backed ThreadRuntime that serializes turns while streaming snapshots, status, and events back to the GUI. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109) (`clm_73b8abcfc4bcace2d4eef3909a6d42d70d53bdc8084b051ed31836579b0f9edd`)

## design-choices (2 claim(s))

- [observation/documented] The desktop UI uses a restrained neutral OKLCH-token palette with a semantic primary accent, a 4px spacing rhythm, and a sidebar/chat/inspector layout that collapses responsively below 1200px. -- evidence: [DESIGN.md#L13-L13](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L13-L13), [DESIGN.md#L92-L94](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L92-L94), [DESIGN.md#L11-L11](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L11-L11), [DESIGN.md#L98-L101](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L98-L101), [DESIGN.md#L86-L88](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L86-L88) (`clm_3aca079e67dab1ac71213b2df71d0b370a09023ea41155b149fa449f0e410334`)
- [observation/documented] The frontend uses shadcn/ui (new-york style, Radix primitives) as its component source system, with product components kept separate from low-level UI primitives. -- evidence: [DESIGN.md#L107-L110](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L107-L110), [DESIGN.md#L114-L119](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L114-L119) (`clm_87e77132903f85b0b5c6010b6c23a53e29d920560f32c22a62a282a918901dda`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run npm ci, tauri:dev, test, and build commands, plus cargo test, fmt, clippy, and cargo deny checks for verification. -- evidence: [README.md#L124-L130](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L124-L130), [README.md#L115-L120](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L115-L120) (`clm_b246bd719e68dffb364351d2812e94dc8b77841c791738109d13dc6bc7240379`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The model layer normalizes provider-specific APIs into internal conversation, tool-call, multimodal, reasoning, and streaming types. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109) (`clm_c591f429ce11725d0ecf9d96667a542347a3cbe8ff03f98460dea8b492012332`)
- [observation/documented] A typed app-server boundary exposes the local Rust runtime to the desktop; the Tauri shell stays project-aware while the runtime owns thread execution, model calls, tools, state, and live events. -- evidence: [README.md#L86-L88](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L86-L88) (`clm_2fa82defceb6b657527159a20818cff13f31664cc44bc90f22bb675ac4b9c273`)

## memory-state (2 claim(s))

- [observation/documented] Local durability is append-first: each thread has a rollout.jsonl ledger, and IndexDb stores cross-thread indexes for projects, threads, goals, memory, and review state. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109) (`clm_8db05fe039abe8bf3c7748d54d0cfe1ce3968ddbd79a8bc21fddc178bee1bb3f`)
- [observation/documented] The memory system supports automatic prompt recall, explicit memory tools, candidate saves, local promote/archive/forget flows, and audit state. -- evidence: [README.md#L33-L40](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L33-L40), [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109) (`clm_60f4b8e396cf16f26efef8bca8e617537b02d7e8120fe96379715a395f23400b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Agent policy gates both tool visibility and execution; tool contracts live in src/tools while per-turn orchestration lives in src/runtime/tool. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109) (`clm_8adf95349c5360a706a6f293ca66e49b04d0ac4912b54632bc1d26daabc64700`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is dual-licensed MIT OR Apache-2.0, and Rust dependency license policy is enforced via cargo deny configured in deny.toml. -- evidence: [README.md#L193-L194](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L193-L194), [THIRD_PARTY_NOTICES.md#L17-L19](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/THIRD_PARTY_NOTICES.md#L17-L19) (`clm_298aa49449ca42a6869151a1e905cecbeeb70ec483dac8ea42332403613b2f2d`)

## limitations (1 claim(s))

- [observation/documented] The project states it currently targets personal workstation use, with non-goals including production-grade sandbox isolation, hosted collaboration, and a stable public SDK. -- evidence: [README.md#L139-L141](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L139-L141), [README.md#L134-L135](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L134-L135) (`clm_847e79c694dfa5a025b03991ded40c5a58c15365f1aa79bfaa55dbb9f8ab2733`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

