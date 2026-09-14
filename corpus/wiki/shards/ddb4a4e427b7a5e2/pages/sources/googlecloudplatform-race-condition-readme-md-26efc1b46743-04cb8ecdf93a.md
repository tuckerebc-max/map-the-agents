---
access: public
aliases: []
claim_ids:
- clm_07384350314468305061486cc751e66711b92108a2feef66208f0c6ab4db1f11
- clm_08285275a738636cff83ca2e7eb6a6f0378eefc402baa75a2f0285fc7db066ca
- clm_14d7aee4d1a81c05cbd7a1a9b74d7be831b68da85211545fe8f5e24b1530f021
- clm_8742dad4cf2c0d72d44e642c8ae2d042d4fc95c48af5e6e1dafce8ebf621bbb1
- clm_8caff6869983a9e3fd3980a4682fa21d6e645241026f6cf66f1b4ac7a3915e89
- clm_9f22814014385a78cc358b4a1dd40a6278e3de3a7971b5e92ca25fdc57794e03
- clm_a7adb9593037b46708b9de4fb2ac935cca4bc2cdede2093b45f3f8b6df7b7095
- clm_aad5291d227734c04b9498aecaad6f039bb91c34651fde29a79057c5917b6c11
- clm_ab19ed864feca7698f70ff936321f1e86841a9a3008d1abd9dac9a9b2abad6f8
- clm_b0fe7b41816f8a9c7d3200b12342185ac681511119188f6b6e47a9f4f48b67af
- clm_e6ca1c63c79bbd293614b84b5bebbb225a3824f68b7540a49142105eb584c56b
- clm_f283717fb71ff55b80ceb65eb9bf99514237773e71ab2b976d42a14cb05c2592
- clm_f5c45a1ff5abff37764c5f72b18989aa33a96c9f893c3ab6c98715f36ad94544
- clm_fe24c39259f2e97ef36afe41c747ddd523e4b8cf7b25d641874d7f83fa273cb7
- clm_fff2bab0bada154ab9d84941d3f32689b1f2a8663038bef381b1d6caa791448c
maturity: draft
page_id: pg_a9bbca359e515b719a7104cb8ecdf93a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cf031869ff5c57a5812245f23f1242f9
title: GoogleCloudPlatform/race-condition/README.md @ 26efc1b46743
updated_at: '2026-09-14T03:55:12Z'
---

# GoogleCloudPlatform/race-condition/README.md @ 26efc1b46743

<!-- rcw:begin owner=source:src_cf031869ff5c57a5812245f23f1242f9 block=evidence -->
- The system comprises a Go/Gin WebSocket gateway that routes requests and manages sessions, Python ADK planner, simulator, and runner agents, an Angular 21 + Three.js 3D frontend, and infrastructure including Redis, Pub/Sub, and PostgreSQL with pgvector. [@claim:clm_07384350314468305061486cc751e66711b92108a2feef66208f0c6ab4db1f11]
- Locally the stack runs on Docker Compose with Redis, a Pub/Sub emulator, and PostgreSQL; in the cloud it deploys to Cloud Run, Vertex AI Agent Engine, AlloyDB, Memorystore Redis, and Pub/Sub. [@claim:clm_08285275a738636cff83ca2e7eb6a6f0378eefc402baa75a2f0285fc7db066ca]
- The frontend supports toggling between Cached and Live modes via Ctrl+L or a segmented control in the chat panel's Settings dropdown, with a brief on-screen mode indicator. [@claim:clm_14d7aee4d1a81c05cbd7a1a9b74d7be831b68da85211545fe8f5e24b1530f021]
- A deterministic runner variant, runner_autopilot, makes the same shape of decisions as the LLM-powered runner with zero API calls, intended as a free baseline for load-testing the simulator. [@claim:clm_8742dad4cf2c0d72d44e642c8ae2d042d4fc95c48af5e6e1dafce8ebf621bbb1]
- Agents expose agent cards at /.well-known/agent-card.json; the gateway fetches these cards at startup and routes messages to agents based on their declared skills. [@claim:clm_8caff6869983a9e3fd3980a4682fa21d6e645241026f6cf66f1b4ac7a3915e89]
- The frontend boots in Cached mode by default, replaying NDJSON streams recorded from real agent runs so demos do not depend on live LLM calls or the network; Live mode instead talks to agents over WebSockets. [@claim:clm_9f22814014385a78cc358b4a1dd40a6278e3de3a7971b5e92ca25fdc57794e03]
- The project is a multi-agent marathon simulation built with Google ADK and Gemini in which agents plan a Las Vegas marathon route, simulate weather, traffic, and crowds, and run the race autonomously, communicating over the A2A protocol. [@claim:clm_a7adb9593037b46708b9de4fb2ac935cca4bc2cdede2093b45f3f8b6df7b7095]
- The planner_with_memory variant persists route memory and embeddings in AlloyDB (PostgreSQL with pgvector locally), and the Sandbox demo exposes this agent for ad-hoc queries like listing top routes. [@claim:clm_aad5291d227734c04b9498aecaad6f039bb91c34651fde29a79057c5917b6c11]
- The planner ships in three variants: a base planner, one adding LLM-as-Judge evaluation, and one adding AlloyDB-backed route memory; the simulator runs a tick-based pipeline and spawns runner agents, which come in LLM-powered and deterministic autopilot variants. [@claim:clm_ab19ed864feca7698f70ff936321f1e86841a9a3008d1abd9dac9a9b2abad6f8]
- Repository development practice: the repo ships an AGENTS.md plus four skill files under .claude/skills/ (getting-started, exploring-the-codebase, deploying, contributing) that AI coding assistants are directed to read for setup, architecture, deployment, and contribution tasks. [@claim:clm_b0fe7b41816f8a9c7d3200b12342185ac681511119188f6b6e47a9f4f48b67af]
- The simulator runs a SequentialAgent pipeline: pre-race parsing and runner spawning, a LoopAgent race loop of up to 200 ticks, and post-race result compilation; each tick it updates conditions and broadcasts state to runner agents. [@claim:clm_e6ca1c63c79bbd293614b84b5bebbb225a3824f68b7540a49142105eb584c56b]
- Some keynote demo paths using private-preview products were cut from this release, and the default deployment scales compute to zero; preview-gated features are expected to return as those products reach public preview. [@claim:clm_f283717fb71ff55b80ceb65eb9bf99514237773e71ab2b976d42a14cb05c2592]
- The repository is positioned as a working reference architecture for hard-to-study patterns: cached vs live replay, a deterministic runner baseline, a planner capability ladder, a Go gateway Hub session pattern with batching, and backend-driven UI via A2UI primitives. [@claim:clm_f5c45a1ff5abff37764c5f72b18989aa33a96c9f893c3ab6c98715f36ad94544]
- The runner model is configurable via RUNNER_MODEL in .env, defaulting to Gemini 3.1 Flash Lite, with documented Ollama (local Gemma 4) and vLLM-on-GKE alternatives. [@claim:clm_fe24c39259f2e97ef36afe41c747ddd523e4b8cf7b25d641874d7f83fa273cb7]
- Repository development practice: contributors use make targets for tests (Go, Python, web), linting, formatting, and coverage; Python tests run offline because a root conftest.py mocks google.auth.default credentials, and Go integration tests need Redis via docker compose. [@claim:clm_fff2bab0bada154ab9d84941d3f32689b1f2a8663038bef381b1d6caa791448c]
<!-- rcw:end owner=source:src_cf031869ff5c57a5812245f23f1242f9 block=evidence -->

## Researcher notes

