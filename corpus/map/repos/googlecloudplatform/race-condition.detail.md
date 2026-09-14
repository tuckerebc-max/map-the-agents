# googlecloudplatform/race-condition -- full detail

[Back to orientation](race-condition.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/googlecloudplatform/race-condition/26efc1b4674344d6303ee4226ec3204c08733fec/b66130ac402fcbca.json](../../../wiki/dossiers/googlecloudplatform/race-condition/26efc1b4674344d6303ee4226ec3204c08733fec/b66130ac402fcbca.json)

## specifications (1 claim(s))

- [observation/documented] The project is a multi-agent marathon simulation built with Google ADK and Gemini in which agents plan a Las Vegas marathon route, simulate weather, traffic, and crowds, and run the race autonomously, communicating over the A2A protocol. -- evidence: [README.md#L21-L21](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L21-L21) (`clm_a7adb9593037b46708b9de4fb2ac935cca4bc2cdede2093b45f3f8b6df7b7095`)

## components (2 claim(s))

- [observation/documented] The system comprises a Go/Gin WebSocket gateway that routes requests and manages sessions, Python ADK planner, simulator, and runner agents, an Angular 21 + Three.js 3D frontend, and infrastructure including Redis, Pub/Sub, and PostgreSQL with pgvector. -- evidence: [README.md#L122-L129](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L122-L129), [README.md#L100-L109](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L100-L109), [README.md#L111-L120](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L111-L120) (`clm_07384350314468305061486cc751e66711b92108a2feef66208f0c6ab4db1f11`)
- [observation/documented] The planner ships in three variants: a base planner, one adding LLM-as-Judge evaluation, and one adding AlloyDB-backed route memory; the simulator runs a tick-based pipeline and spawns runner agents, which come in LLM-powered and deterministic autopilot variants. -- evidence: [README.md#L122-L129](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L122-L129) (`clm_ab19ed864feca7698f70ff936321f1e86841a9a3008d1abd9dac9a9b2abad6f8`)

## design-choices (2 claim(s))

- [observation/documented] The frontend boots in Cached mode by default, replaying NDJSON streams recorded from real agent runs so demos do not depend on live LLM calls or the network; Live mode instead talks to agents over WebSockets. -- evidence: [README.md#L229-L229](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L229-L229), [README.md#L227-L227](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L227-L227) (`clm_9f22814014385a78cc358b4a1dd40a6278e3de3a7971b5e92ca25fdc57794e03`)
- [observation/documented] A deterministic runner variant, runner_autopilot, makes the same shape of decisions as the LLM-powered runner with zero API calls, intended as a free baseline for load-testing the simulator. -- evidence: [README.md#L362-L367](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L362-L367), [README.md#L29-L33](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L29-L33) (`clm_8742dad4cf2c0d72d44e642c8ae2d042d4fc95c48af5e6e1dafce8ebf621bbb1`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors use make targets for tests (Go, Python, web), linting, formatting, and coverage; Python tests run offline because a root conftest.py mocks google.auth.default credentials, and Go integration tests need Redis via docker compose. -- evidence: [README.md#L406-L418](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L406-L418), [GEMINI.md#L23-L34](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/GEMINI.md#L23-L34), [README.md#L470-L470](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L470-L470) (`clm_fff2bab0bada154ab9d84941d3f32689b1f2a8663038bef381b1d6caa791448c`)
- [observation/documented] Repository development practice: the repo ships an AGENTS.md plus four skill files under .claude/skills/ (getting-started, exploring-the-codebase, deploying, contributing) that AI coding assistants are directed to read for setup, architecture, deployment, and contribution tasks. -- evidence: [GEMINI.md#L41-L45](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/GEMINI.md#L41-L45), [README.md#L61-L61](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L61-L61), [README.md#L87-L92](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L87-L92) (`clm_b0fe7b41816f8a9c7d3200b12342185ac681511119188f6b6e47a9f4f48b67af`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Agents expose agent cards at /.well-known/agent-card.json; the gateway fetches these cards at startup and routes messages to agents based on their declared skills. -- evidence: [README.md#L346-L346](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L346-L346), [GEMINI.md#L23-L34](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/GEMINI.md#L23-L34) (`clm_8caff6869983a9e3fd3980a4682fa21d6e645241026f6cf66f1b4ac7a3915e89`)
- [observation/documented] The frontend supports toggling between Cached and Live modes via Ctrl+L or a segmented control in the chat panel's Settings dropdown, with a brief on-screen mode indicator. -- evidence: [README.md#L231-L231](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L231-L231) (`clm_14d7aee4d1a81c05cbd7a1a9b74d7be831b68da85211545fe8f5e24b1530f021`)

## memory-state (1 claim(s))

- [observation/documented] The planner_with_memory variant persists route memory and embeddings in AlloyDB (PostgreSQL with pgvector locally), and the Sandbox demo exposes this agent for ad-hoc queries like listing top routes. -- evidence: [README.md#L122-L129](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L122-L129), [README.md#L29-L33](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L29-L33), [README.md#L257-L257](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L257-L257) (`clm_aad5291d227734c04b9498aecaad6f039bb91c34651fde29a79057c5917b6c11`)

## orchestration (1 claim(s))

- [observation/documented] The simulator runs a SequentialAgent pipeline: pre-race parsing and runner spawning, a LoopAgent race loop of up to 200 ticks, and post-race result compilation; each tick it updates conditions and broadcasts state to runner agents. -- evidence: [README.md#L358-L358](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L358-L358), [README.md#L352-L356](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L352-L356), [README.md#L350-L350](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L350-L350) (`clm_e6ca1c63c79bbd293614b84b5bebbb225a3824f68b7540a49142105eb584c56b`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Locally the stack runs on Docker Compose with Redis, a Pub/Sub emulator, and PostgreSQL; in the cloud it deploys to Cloud Run, Vertex AI Agent Engine, AlloyDB, Memorystore Redis, and Pub/Sub. -- evidence: [README.md#L57-L57](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L57-L57), [README.md#L422-L422](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L422-L422) (`clm_08285275a738636cff83ca2e7eb6a6f0378eefc402baa75a2f0285fc7db066ca`)
- [observation/documented] The runner model is configurable via RUNNER_MODEL in .env, defaulting to Gemini 3.1 Flash Lite, with documented Ollama (local Gemma 4) and vLLM-on-GKE alternatives. -- evidence: [README.md#L379-L381](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L379-L381), [README.md#L362-L367](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L362-L367), [README.md#L373-L373](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L373-L373), [README.md#L376-L376](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L376-L376), [README.md#L369-L369](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L369-L369) (`clm_fe24c39259f2e97ef36afe41c747ddd523e4b8cf7b25d641874d7f83fa273cb7`)

## limitations (1 claim(s))

- [observation/documented] Some keynote demo paths using private-preview products were cut from this release, and the default deployment scales compute to zero; preview-gated features are expected to return as those products reach public preview. -- evidence: [README.md#L45-L45](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L45-L45), [README.md#L41-L43](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L41-L43) (`clm_f283717fb71ff55b80ceb65eb9bf99514237773e71ab2b976d42a14cb05c2592`)

## relevance (1 claim(s))

- [observation/documented] The repository is positioned as a working reference architecture for hard-to-study patterns: cached vs live replay, a deterministic runner baseline, a planner capability ladder, a Go gateway Hub session pattern with batching, and backend-driven UI via A2UI primitives. -- evidence: [README.md#L29-L33](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L29-L33), [README.md#L27-L27](https://github.com/GoogleCloudPlatform/race-condition/blob/26efc1b4674344d6303ee4226ec3204c08733fec/README.md#L27-L27) (`clm_f5c45a1ff5abff37764c5f72b18989aa33a96c9f893c3ab6c98715f36ad94544`)

