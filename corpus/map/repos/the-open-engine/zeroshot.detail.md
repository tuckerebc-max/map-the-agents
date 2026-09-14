# the-open-engine/zeroshot -- full detail

[Back to orientation](zeroshot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/the-open-engine/zeroshot/b550c15279c9972a541f04c6d5925a5fa174363a/2ab85c8a6208f2d8.json](../../../wiki/dossiers/the-open-engine/zeroshot/b550c15279c9972a541f04c6d5925a5fa174363a/2ab85c8a6208f2d8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A run consists of three authored values: a graph defining control flow and typed state, a runtime plan binding each executable node to a harness, provider, model, and named connections, and caller-owned initial input validated against the graph before execution. -- evidence: [docs/index.md#L17-L21](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L17-L21), [docs/index.md#L15-L15](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L15-L15) (`clm_0bf189be40418d5352fa500818c5d34366893c975a0305374c19194d3d815d4e`)
- [observation/documented] Besides the software-change template, a single-worker template exists for work that does not need the review loop, and custom graphs follow the same protocol contracts. -- evidence: [docs/index.md#L40-L41](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L40-L41) (`clm_246f7f6c5217275aa6f4507f546b7ae82c5504c858d4240f3bc115fd1fce90a0`)

## design-choices (3 claim(s))

- [observation/documented] Control flow is authored data rather than hidden in prompts: sequence, parallel review, retry paths, delivery, and exit conditions are explicit before a run starts, and no runtime agent chooses the next step. -- evidence: [README.md#L44-L46](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L44-L46), [README.md#L56-L57](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L56-L57) (`clm_83ac5da94762939e603a1f3c8de18751326c883212be1f91ba75b9281a196049`)
- [observation/documented] Three execution targets share the same graph and runtime plan: local mode in the current Git worktree reusing Codex or Claude Code logins, a self-hosted Docker target image bundling the engine plus pinned Codex and Claude harness CLIs, and a managed Zeroshot Cloud target. -- evidence: [README.md#L74-L74](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L74-L74), [docs/index.md#L63-L64](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L63-L64), [README.md#L109-L110](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L109-L110), [README.md#L92-L93](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L92-L93), [README.md#L78-L79](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L78-L79) (`clm_0b36816531b234873ae6b87619536c3d41015b7014f52bae6ea833c7181fe4a4`)
- [inference/documented] The apply method supports dryRun, ifGeneration optimistic concurrency, and idempotencyKey parameters, suggesting the cluster API is designed for safe, repeatable graph applications. -- evidence: [docs/reference/cluster/api.md#L76-L82](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/reference/cluster/api.md#L76-L82) (`clm_05b338388db00e1953361e1fec360ebd07ee8cdf92a5aee08d3f298e53a22a04`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors run `npm ci`, `npm run check`, and `cargo test --workspace`; Node.js is repository tooling and the npm delivery mechanism only. -- evidence: [README.md#L133-L137](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L133-L137), [README.md#L139-L140](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L139-L140) (`clm_3d7f16957cc3edf5b02e5eb85c29ab46993c957f3da6345feb27984c9b136078`)
- [observation/documented] Repository development practice: releases publish one canonical version across GitHub tag, native archives, checksum manifest, npm package, target image, Python wheels, and versioned docs via a release workflow using GitHub OIDC trusted publishing, with no long-lived npm or PyPI tokens. -- evidence: [PUBLISHING.md#L10-L19](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L10-L19), [PUBLISHING.md#L37-L37](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L37-L37), [PUBLISHING.md#L3-L4](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L3-L4) (`clm_1e78f5ad236b981937399a0a2c600ce61826b2de844ff2aa0c9369a95b00ea6e`)
- [observation/documented] Repository development practice: release jobs verify already-published immutable artifacts before completing missing steps, and recovery must use the same version, tag, and source commit without overwriting different artifacts. -- evidence: [PUBLISHING.md#L97-L99](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L97-L99) (`clm_de70252ddfbb707f3760df8955f60a739f681e71e19939772634fdbc98dafdb1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is a native `zeroshot` executable (v8 hard cutover, former Node.js runtime retired), installed via npm and providing commands like `zeroshot run`, `zeroshot version`, and `zeroshot template list/show`. -- evidence: [README.md#L29-L30](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L29-L30), [README.md#L81-L88](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L81-L88), [README.md#L67-L70](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L67-L70), [README.md#L34-L37](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L34-L37) (`clm_0c374aeaa18fbc6ff6b01e3a2e06bef25ff39748067004a4a869353ca43ae0ea`)
- [observation/documented] Subscription methods use generic framing: watch, logs, and agent/attach (and run/* equivalents) establish subscriptions via one JSON-RPC result, then use generic event, subscription/cancel, subscription/closed, and $/cancelRequest notifications; no method-specific event/cancel/closed methods exist on the wire. -- evidence: [docs/reference/cluster/api.md#L21-L21](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/reference/cluster/api.md#L21-L21), [docs/reference/cluster/api.md#L23-L28](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/reference/cluster/api.md#L23-L28) (`clm_a1a4692a07a47c5a390306622ba5d6831a7c2387dc56bb1ad9af16920a256934`)
- [observation/documented] A Python SDK is provided with public objects including LocalTarget, DirectTarget, HostedTarget, Target, Preset, GraphSpec, UniformRuntime, RuntimePlan, RunRequest, and MergePlanRequest. -- evidence: [README.md#L121-L129](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L121-L129), [docs/reference/python/configuration.md#L3-L18](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/reference/python/configuration.md#L3-L18) (`clm_40fc69a90fc002613f7a30a1c6064415511c6b0478f2b0a5eab373826fffe3c5`)

## memory-state (1 claim(s))

- [observation/documented] Every graph transition event is written to a durable SQLite ledger; after validating graph, runtime plan, and input, Zeroshot opens a durable ledger recording each node result. -- evidence: [README.md#L56-L57](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L56-L57), [docs/index.md#L23-L24](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L23-L24) (`clm_818463f4c2fa684eb98b22c72ada80d4bbad26936c4723c22692fa2849cc23b6`)

## orchestration (2 claim(s))

- [observation/documented] Zeroshot turns a software goal into an explicit multi-agent graph: one agent implements, independent agents review, failures route into bounded repair, and delivery happens only after the graph's checks pass. -- evidence: [README.md#L25-L27](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L25-L27) (`clm_a4795b7829a32e794d7ffaa6710fc796bae5316f23f6a7b22d0b3d60fba598e9`)
- [observation/documented] The built-in software-change graph gives the goal to a worker, runs acceptance and code review in parallel, routes rejections to a repair worker with repeated reviews, and delivers accepted changes through Git, CI, and merge, routing delivery conflicts back through repair. -- evidence: [README.md#L50-L54](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L50-L54) (`clm_44cf8958e4c800f453c1a19c8554b615d2ed9a324fbda16a9e7d5ebf8ec742ec`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The npm package installs a verified native binary for Linux x64/arm64, macOS x64/arm64, and Windows x64; native archives and SHA256 checksums are attached to each canonical vX.Y.Z GitHub Release. -- evidence: [PUBLISHING.md#L10-L19](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L10-L19), [README.md#L39-L40](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L39-L40) (`clm_5e8d6d2cd50de0453cfb951f727b93071589e7c5f0dbcc7b3e2ab91ab8bd7145`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

