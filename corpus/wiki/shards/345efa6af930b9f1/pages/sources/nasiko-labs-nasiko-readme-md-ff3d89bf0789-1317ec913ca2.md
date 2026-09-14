---
access: public
aliases: []
claim_ids:
- clm_12b12a29348f7fb85d5c9a11a5313809641404c1a9b2e2a44bb2f534482a9ade
- clm_1b45d094ec6a6103c388659e7748d978bcd19224492a050dbf064fc43ee0f181
- clm_1bb48b93e81f236792a3a790891aec3fcc098619860dae307f968741aef32415
- clm_6dc4343205ffc3eb4dbc1b1fa56d3131616aed180c87bb0da1e70e0c1b06b474
- clm_79111a9bb7304a63b57e096898b1987d80c890b92f0490593f01fc1263afccfc
- clm_7dc90679844c867a1c2641a58e1f24e27b6156a58dba393bd4d060df644fb4ca
- clm_a1ad42a39ee764f0072ecba34c33d3c6621d5adba3b134d3194d4ea7e55bfdc8
- clm_abc1c8bb5c0c2338ec7bae3aee935b00e339afb37c248c5499b3b664cdc8f37d
- clm_b03237d243ceeca5593f03b0dadb575d909648f8484b61e3cbca7f72b39a1f6c
- clm_b6f26b39a265eb4f5c78fefdd014eb24cfb55188a3b6a8fa54176736299531a7
- clm_cfbe836b4e27a784884c35eff97c603159a36c39fef07400c1ec81524d9d52e6
- clm_d542a425b9ffaa8c2a16be5a6d61c682cedd5358b42d12cc4a64931977991860
- clm_d77ebb8a6fb05d87f6e6e50ceaacb6202e6252664608576c0ae95ae9388a9647
- clm_da0d11ccb87143e4d56035e52b88cd92531e2fc16f685d481a7340ac4e1a9bfb
- clm_f16bd83311e5233dd94af1465287283ce2b761f1d7369c136e668cb2d1e241be
maturity: draft
page_id: pg_a5094ceac206547b97221317ec913ca2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_02241ac6d72c551c87c8ecf3a88338c4
title: Nasiko-Labs/nasiko/README.md @ ff3d89bf0789
updated_at: '2026-09-14T04:11:41Z'
---

# Nasiko-Labs/nasiko/README.md @ ff3d89bf0789

<!-- rcw:begin owner=source:src_02241ac6d72c551c87c8ecf3a88338c4 block=evidence -->
- The workspace is organized into crates including server (Axum control plane), orchestrator (routing engine), mcp-gateway, llm-router, runtime (Docker via bollard), flow, secrets, oci, observability, agent-proxy, github, types, config, cli, and ui. [@claim:clm_12b12a29348f7fb85d5c9a11a5313809641404c1a9b2e2a44bb2f534482a9ade]
- Nasiko is relevant to teams operating multiple A2A-speaking agents in any language (Python, Rust, Go, TypeScript), addressing who-calls-whom, key custody, cost, and failure visibility. [@claim:clm_1b45d094ec6a6103c388659e7748d978bcd19224492a050dbf064fc43ee0f181]
- The A2A implementation uses the Rust libraries a2a-lf 0.3.0 and a2a-server-lf 0.4.0 from a2aproject/a2a-rs, and the workspace targets Rust edition 2024 (Rust 1.85+). [@claim:clm_1bb48b93e81f236792a3a790891aec3fcc098619860dae307f968741aef32415]
- The server exposes a REST API for agents, builds, and uploads, plus an embedded OCI Distribution v2 registry at /v2/*, an MCP Gateway exposing tools/list and tools/call, and an OpenAI-compatible LLM router egress. [@claim:clm_6dc4343205ffc3eb4dbc1b1fa56d3131616aed180c87bb0da1e70e0c1b06b474]
- Configuration is env-driven through a single Config struct; SECRETS_ENCRYPTION_KEY and JWT_SECRET are required, OPENAI_API_KEY and COMPOSIO_API_KEY are optional, and required keys fail fast at startup. [@claim:clm_79111a9bb7304a63b57e096898b1987d80c890b92f0490593f01fc1263afccfc]
- Per-agent secrets are AES-256-GCM encrypted at rest and injected only at deploy time; flow guards backed by Redis enforce cascade limits for depth, fan-out, token budget, timeout, and cycle detection. [@claim:clm_7dc90679844c867a1c2641a58e1f24e27b6156a58dba393bd4d060df644fb4ca]
- Repository development practice: the developer path (Path B) requires Rust, just, and Docker; just infra starts backing services, just dev runs the server with hot-reload via cargo-watch, and just run runs without hot-reload. [@claim:clm_a1ad42a39ee764f0072ecba34c33d3c6621d5adba3b134d3194d4ea7e55bfdc8]
- Agents speaking pre-1.0 A2A spec versions (e.g. 0.2.x, 0.3.0) are rejected with error -32009 VersionNotSupported. [@claim:clm_abc1c8bb5c0c2338ec7bae3aee935b00e339afb37c248c5499b3b664cdc8f37d]
- The nasiko CLI provides commands for connect, auth login, new, build/run, push/deploy, upload, ps, logs, lifecycle (stop/start/restart/scale), chat, secrets, mcp, observe, maf, registry, and github. [@claim:clm_b03237d243ceeca5593f03b0dadb575d909648f8484b61e3cbca7f72b39a1f6c]
- Agents never receive direct public requests and never hold real API keys or tool credentials; they call back into the LLM Router via OPENAI_BASE_URL and the MCP Gateway instead. [@claim:clm_b6f26b39a265eb4f5c78fefdd014eb24cfb55188a3b6a8fa54176736299531a7]
- Durable state lives in Postgres, Redis, and S3 (RustFS), with optional observability via Tempo, Loki, and the OTel Collector; the Docker-only quick start starts this full stack. [@claim:clm_cfbe836b4e27a784884c35eff97c603159a36c39fef07400c1ec81524d9d52e6]
- The routing engine uses a 3-stage pipeline: shortlisting agents by embedding similarity, reranking on conversation context, then an LLM final pick, so callers need not know the fleet. [@claim:clm_d542a425b9ffaa8c2a16be5a6d61c682cedd5358b42d12cc4a64931977991860]
- Nasiko runs as a single control-plane process with no separate gateway; every inter-agent call is proxied back through the server, which enforces flow limits, ACLs, and observability at one chokepoint. [@claim:clm_d77ebb8a6fb05d87f6e6e50ceaacb6202e6252664608576c0ae95ae9388a9647]
- Nasiko targets the A2A protocol v1.0 exactly, requiring the A2A-Version: 1.0 header on every request, and uses JSON-RPC 2.0 over HTTP(S) as its sole protocol binding with SSE for streaming. [@claim:clm_da0d11ccb87143e4d56035e52b88cd92531e2fc16f685d481a7340ac4e1a9bfb]
- Repository development practice: contributors use just recipes — just check (cargo check), just clippy with a zero-warnings policy, just test-unit for hermetic unit tests, and just test for unit plus integration tests requiring just infra. [@claim:clm_f16bd83311e5233dd94af1465287283ce2b761f1d7369c136e668cb2d1e241be]
<!-- rcw:end owner=source:src_02241ac6d72c551c87c8ecf3a88338c4 block=evidence -->

## Researcher notes

