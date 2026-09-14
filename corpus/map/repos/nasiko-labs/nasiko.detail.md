# nasiko-labs/nasiko -- full detail

[Back to orientation](nasiko.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nasiko-labs/nasiko/ff3d89bf07898af4f05e69f87fb3205007eaec45/7860197f8ac0b7db.json](../../../wiki/dossiers/nasiko-labs/nasiko/ff3d89bf07898af4f05e69f87fb3205007eaec45/7860197f8ac0b7db.json)

## specifications (1 claim(s))

- [observation/documented] Nasiko targets the A2A protocol v1.0 exactly, requiring the A2A-Version: 1.0 header on every request, and uses JSON-RPC 2.0 over HTTP(S) as its sole protocol binding with SSE for streaming. -- evidence: [docs/A2A_PROTOCOL.md#L54-L54](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L54-L54), [README.md#L212-L216](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L212-L216), [docs/A2A_PROTOCOL.md#L56-L60](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L56-L60) (`clm_da0d11ccb87143e4d56035e52b88cd92531e2fc16f685d481a7340ac4e1a9bfb`)

## components (2 claim(s))

- [observation/documented] The workspace is organized into crates including server (Axum control plane), orchestrator (routing engine), mcp-gateway, llm-router, runtime (Docker via bollard), flow, secrets, oci, observability, agent-proxy, github, types, config, cli, and ui. -- evidence: [README.md#L512-L533](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L512-L533) (`clm_12b12a29348f7fb85d5c9a11a5313809641404c1a9b2e2a44bb2f534482a9ade`)
- [observation/documented] Durable state lives in Postgres, Redis, and S3 (RustFS), with optional observability via Tempo, Loki, and the OTel Collector; the Docker-only quick start starts this full stack. -- evidence: [README.md#L131-L134](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L131-L134), [README.md#L244-L245](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L244-L245) (`clm_cfbe836b4e27a784884c35eff97c603159a36c39fef07400c1ec81524d9d52e6`)

## design-choices (4 claim(s))

- [observation/documented] Nasiko runs as a single control-plane process with no separate gateway; every inter-agent call is proxied back through the server, which enforces flow limits, ACLs, and observability at one chokepoint. -- evidence: [README.md#L131-L134](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L131-L134), [docs/A2A_PROTOCOL.md#L46-L46](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L46-L46), [README.md#L101-L103](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L101-L103) (`clm_d77ebb8a6fb05d87f6e6e50ceaacb6202e6252664608576c0ae95ae9388a9647`)
- [observation/documented] Agents never receive direct public requests and never hold real API keys or tool credentials; they call back into the LLM Router via OPENAI_BASE_URL and the MCP Gateway instead. -- evidence: [README.md#L204-L206](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L204-L206), [README.md#L116-L128](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L116-L128) (`clm_b6f26b39a265eb4f5c78fefdd014eb24cfb55188a3b6a8fa54176736299531a7`)
- [observation/documented] The routing engine uses a 3-stage pipeline: shortlisting agents by embedding similarity, reranking on conversation context, then an LLM final pick, so callers need not know the fleet. -- evidence: [README.md#L116-L128](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L116-L128) (`clm_d542a425b9ffaa8c2a16be5a6d61c682cedd5358b42d12cc4a64931977991860`)
- [observation/documented] Per-agent secrets are AES-256-GCM encrypted at rest and injected only at deploy time; flow guards backed by Redis enforce cascade limits for depth, fan-out, token budget, timeout, and cycle detection. -- evidence: [README.md#L116-L128](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L116-L128) (`clm_7dc90679844c867a1c2641a58e1f24e27b6156a58dba393bd4d060df644fb4ca`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use just recipes — just check (cargo check), just clippy with a zero-warnings policy, just test-unit for hermetic unit tests, and just test for unit plus integration tests requiring just infra. -- evidence: [README.md#L420-L425](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L420-L425) (`clm_f16bd83311e5233dd94af1465287283ce2b761f1d7369c136e668cb2d1e241be`)
- [observation/documented] Repository development practice: the developer path (Path B) requires Rust, just, and Docker; just infra starts backing services, just dev runs the server with hot-reload via cargo-watch, and just run runs without hot-reload. -- evidence: [README.md#L410-L410](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L410-L410), [README.md#L403-L403](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L403-L403), [README.md#L398-L399](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L398-L399), [README.md#L415-L416](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L415-L416) (`clm_a1ad42a39ee764f0072ecba34c33d3c6621d5adba3b134d3194d4ea7e55bfdc8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The nasiko CLI provides commands for connect, auth login, new, build/run, push/deploy, upload, ps, logs, lifecycle (stop/start/restart/scale), chat, secrets, mcp, observe, maf, registry, and github. -- evidence: [README.md#L466-L484](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L466-L484) (`clm_b03237d243ceeca5593f03b0dadb575d909648f8484b61e3cbca7f72b39a1f6c`)
- [observation/documented] The server exposes a REST API for agents, builds, and uploads, plus an embedded OCI Distribution v2 registry at /v2/*, an MCP Gateway exposing tools/list and tools/call, and an OpenAI-compatible LLM router egress. -- evidence: [README.md#L143-L156](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L143-L156), [README.md#L116-L128](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L116-L128) (`clm_6dc4343205ffc3eb4dbc1b1fa56d3131616aed180c87bb0da1e70e0c1b06b474`)
- [observation/documented] Agent discovery fetches the agent card from /.well-known/agent-card.json on deploy or seed; the orchestrator primarily uses SendStreamingMessage while the CLI uses SendMessage for direct chat. -- evidence: [docs/A2A_PROTOCOL.md#L139-L142](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L139-L142) (`clm_3263f4b7a2da679301a692afadfd27462630b41094f69ae64e45e1b62ca20d2e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The A2A implementation uses the Rust libraries a2a-lf 0.3.0 and a2a-server-lf 0.4.0 from a2aproject/a2a-rs, and the workspace targets Rust edition 2024 (Rust 1.85+). -- evidence: [README.md#L212-L216](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L212-L216), [docs/A2A_PROTOCOL.md#L5-L6](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/docs/A2A_PROTOCOL.md#L5-L6) (`clm_1bb48b93e81f236792a3a790891aec3fcc098619860dae307f968741aef32415`)
- [observation/documented] Configuration is env-driven through a single Config struct; SECRETS_ENCRYPTION_KEY and JWT_SECRET are required, OPENAI_API_KEY and COMPOSIO_API_KEY are optional, and required keys fail fast at startup. -- evidence: [README.md#L495-L509](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L495-L509), [README.md#L490-L493](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L490-L493) (`clm_79111a9bb7304a63b57e096898b1987d80c890b92f0490593f01fc1263afccfc`)

## limitations (1 claim(s))

- [observation/documented] Agents speaking pre-1.0 A2A spec versions (e.g. 0.2.x, 0.3.0) are rejected with error -32009 VersionNotSupported. -- evidence: [README.md#L212-L216](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L212-L216) (`clm_abc1c8bb5c0c2338ec7bae3aee935b00e339afb37c248c5499b3b664cdc8f37d`)

## relevance (1 claim(s))

- [observation/documented] Nasiko is relevant to teams operating multiple A2A-speaking agents in any language (Python, Rust, Go, TypeScript), addressing who-calls-whom, key custody, cost, and failure visibility. -- evidence: [README.md#L98-L99](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L98-L99), [README.md#L105-L106](https://github.com/Nasiko-Labs/nasiko/blob/ff3d89bf07898af4f05e69f87fb3205007eaec45/README.md#L105-L106) (`clm_1b45d094ec6a6103c388659e7748d978bcd19224492a050dbf064fc43ee0f181`)

