# legioncodeinc/honeycomb -- full detail

[Back to orientation](honeycomb.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/legioncodeinc/honeycomb/c1cb6bf5674ca169728e79433bf035e0d3d1483c/c3ac5449590e9e74.json](../../../wiki/dossiers/legioncodeinc/honeycomb/c1cb6bf5674ca169728e79433bf035e0d3d1483c/c3ac5449590e9e74.json)

## specifications (1 claim(s))

- [observation/documented] Honeycomb provides shared, persistent memory for AI coding agents: what one harness learns is recallable by others across sessions, tools, devices, and teammates. -- evidence: [README.md#L12-L15](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L12-L15), [README.md#L56-L56](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L56-L56) (`clm_41fe9389a72614698ee314e99f5fd384a4a27a3cdfeaacd4355b1a147db58c2b`)

## components (1 claim(s))

- [observation/documented] The product is a long-lived local daemon plus thin clients (hooks, CLI, MCP, SDK); the daemon is the sole process talking to storage, reached over loopback HTTP on 127.0.0.1:3850. -- evidence: [README.md#L212-L223](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L212-L223), [README.md#L210-L210](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L210-L210) (`clm_165082757878f530c9262761bd432563d42a678a9e9014567c4753cfb4044f67`)

## design-choices (2 claim(s))

- [observation/documented] At session start a bounded index of roughly 300-800 tokens of relevant keys is pushed once, with deeper detail pulled on demand rather than injected per turn. -- evidence: [README.md#L91-L97](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L91-L97) (`clm_ddf6cb96e3ce82a516ff68742ab020fb12e34502691ab1ada66df2a5cfafcbfb`)
- [observation/documented] The daemon binds loopback only (single machine); cross-device and cross-user sharing happen through Deeplake's org/workspace scope rather than a remote daemon bind. -- evidence: [README.md#L290-L293](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L290-L293) (`clm_9a3b259b09a109931c694e197051a1682108e1f4395050d7002c38e3d9436efe`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: npm run ci is the quality gate every change must pass, combining typecheck, duplication detection (jscpd), vitest tests, and a SQL-safety audit. -- evidence: [README.md#L307-L307](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L307-L307), [README.md#L301-L305](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L301-L305) (`clm_9442bbe46aabaab82ff85d5f9afadf19f3279ed83cd3695cf3021211ca2c283d`)
- [observation/documented] Repository development practice: the codebase is a single-package TypeScript monorepo with tiered import direction (tier N may import only from lower tiers), DeepLake access confined to src/daemon, and esbuild bundling per target entry root. -- evidence: [BUILD.md#L21-L27](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L21-L27), [BUILD.md#L29-L32](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L29-L32), [BUILD.md#L17-L19](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L17-L19), [BUILD.md#L3-L6](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/BUILD.md#L3-L6) (`clm_1eabe2b297ce49922c61afb6f35573bf62b246246d33ebd4085916243ca7a1a4`)
- [observation/documented] Repository development practice: releases are automated from AI-written changesets through a gated version bump (minor releases hold for human approval, major blocked), then tag-on-merge, npm publish via OIDC, and Discord notification. -- evidence: [RELEASE-AUTOMATION.md#L3-L5](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/RELEASE-AUTOMATION.md#L3-L5), [RELEASE-AUTOMATION.md#L12-L31](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/RELEASE-AUTOMATION.md#L12-L31) (`clm_490e412e95f6805f0bb0c89353f39bdcaf712b2e4a887b58c875710520bf3d58`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A unified honeycomb CLI exposes verbs such as setup, status, login, start/stop, remember, recall, sessions, and uninstall; baseline operational verbs accept --json with exit codes 2/1/0 for malformed usage, runtime failure, and success. -- evidence: [README.md#L157-L181](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L157-L181), [README.md#L155-L155](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L155-L155), [README.md#L185-L187](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L185-L187) (`clm_7267a6371ecfcd5c44006fff118690fb1183267cec9a7555503c19b39276a385`)
- [observation/documented] Besides the CLI, Honeycomb is reachable via the Hive portal dashboard at 127.0.0.1:3853, a bundled MCP server exposing read/resolve and search/mine tools, and a TypeScript SDK with /react, /vercel, and /openai subpath entries. -- evidence: [README.md#L274-L276](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L274-L276), [README.md#L146-L146](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L146-L146) (`clm_0d7a97f48fa79eb9b9198c73c29e71a1566bf737b6d503343957e0d4da72343b`)

## memory-state (1 claim(s))

- [observation/documented] Memories exist at three tiers: a one-line key, a distilled summary carrying the semantic embedding, and the full raw session dialogue; resolution is a deterministic pointer walk across three Deeplake tables. -- evidence: [README.md#L235-L239](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L235-L239), [README.md#L91-L97](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L91-L97), [README.md#L241-L241](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L241-L241) (`clm_fc6f70f475ec8d1675162d04a2fce9bc9c70b2b0e2c5c68439dbb0613555e3cb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a measured recall@5 of approximately 0.72-0.78 for the hybrid lexical-plus-semantic retrieval, and describes a smoke:golden-path script run against live Deeplake credentials. -- evidence: [README.md#L91-L97](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L91-L97), [README.md#L284-L288](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L284-L288) (`clm_a8500666d1f2648bdb760f6350d8302a160c84114a33f6156cb0b68800aa0df1`)

## dependencies (2 claim(s))

- [observation/documented] Honeycomb is built on Activeloop Deeplake (extending the open-source Hivemind agent-memory project), using BM25 lexical plus 768-dim nomic-embed-text-v1.5 semantic search fused by Reciprocal Rank Fusion. -- evidence: [README.md#L254-L254](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L254-L254), [README.md#L249-L252](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L249-L252), [README.md#L87-L87](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L87-L87) (`clm_9a3b97bde017f7ae99b837e55ae76336d9712899fedfda62cee4c69360cc7dd5`)
- [observation/documented] Storage can be self-hosted against Activeloop's pg_deeplake Postgres extension, pointed at via honeycomb login --endpoint with a postgres:// or https:// URL, without an Activeloop account. -- evidence: [README.md#L138-L138](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L138-L138), [README.md#L284-L288](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L284-L288) (`clm_8bd600f44841d38325e762b3cfa68912a8e8c05c7a2ad198ece46daf02b4352f`)

## limitations (2 claim(s))

- [observation/documented] Embeddings are opt-in: recall defaults to lexical BM25, and enabling the local embedding runtime (~600 MB fetched on first warmup) adds semantic recall; recall silently falls back and never errors when embeddings are unavailable. -- evidence: [README.md#L290-L293](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L290-L293) (`clm_e9c6db1674f7e632776380adbc6cd349d00b47ec659b703616330b430e14a84e`)
- [observation/documented] The distillation pipeline (background summarization and graph extraction) is disabled by default to avoid surprise model spend, and running Honeycomb alongside Hivemind is unsupported, though the dashboard offers migration. -- evidence: [README.md#L121-L121](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L121-L121), [README.md#L290-L293](https://github.com/legioncodeinc/honeycomb/blob/c1cb6bf5674ca169728e79433bf035e0d3d1483c/README.md#L290-L293) (`clm_06c3553dcda7bab8ab137a0a034ca23fff1ac0c2d8d332b5e4e83eb12814956d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

