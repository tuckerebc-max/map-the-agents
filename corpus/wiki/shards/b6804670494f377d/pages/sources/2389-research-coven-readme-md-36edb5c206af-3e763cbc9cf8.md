---
access: public
aliases: []
claim_ids:
- clm_1472a2d327a4a10c7db33eb840a1d53c4a3766deeb6f0b800f00298177e91c4c
- clm_4db38509841e9716be85ec09dbe73641ccdc9e6540acd588791ad9afdce9197b
- clm_5799f746f16d09a9cbae122272d28b5927634007dcb7bc2a887237151e401e9c
- clm_816c30eb36f29cb2ed2cb296810b4f0cd6a4f5a9f480536df20938708c378859
- clm_868d98e2599b6b5edc43009448ec6e19a25579c99ecb6750a617480e95b5bff3
- clm_9a8f4695f1d474d673911420d4e99900af4bfd0feea9ba847c2f246c96dd81fe
- clm_a4d13de73130a2b5d860a86d65a56dd59bac6c71abe21007d58f59b62898feef
- clm_b6b8dbc159d2e78cc113998f49e5b76e4aee3c273d656907047c2715228beb19
maturity: draft
page_id: pg_98e0610b570450138cee3e763cbc9cf8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b1123ce7cf885c28b57a4a28eb90d930
title: 2389-research/coven/README.md @ 36edb5c206af
updated_at: '2026-09-14T01:26:25Z'
---

# 2389-research/coven/README.md @ 36edb5c206af

<!-- rcw:begin owner=source:src_b1123ce7cf885c28b57a4a28eb90d930 block=evidence -->
- coven-swarm provides a supervisor command for multi-workspace orchestration, documented as spawning agents per workspace. [@claim:clm_1472a2d327a4a10c7db33eb840a1d53c4a3766deeb6f0b800f00298177e91c4c]
- The project comprises a Rust monorepo (agents, CLI, TUI, packs), a Go gateway server for routing, storage and pack registry, and shared Protobuf definitions (coven-proto). [@claim:clm_4db38509841e9716be85ec09dbe73641ccdc9e6540acd588791ad9afdce9197b]
- Coven is described as a Rust-based platform for orchestrating AI agents with tool capabilities, connecting Claude-powered agents to a central gateway. [@claim:clm_5799f746f16d09a9cbae122272d28b5927634007dcb7bc2a887237151e401e9c]
- The gateway exposes an HTTP server with SSE events, a gRPC server for agent streams, and a pack service acting as a tool registry, backed by SQLite. [@claim:clm_816c30eb36f29cb2ed2cb296810b4f0cd6a4f5a9f480536df20938708c378859]
- Configuration lives under ~/.config/coven/ (config.toml, per-agent TOML files, swarm config) with data in ~/.local/share/coven/; the AgentMetadata struct includes hostname, OS, git info, workspaces, and backend fields. [@claim:clm_868d98e2599b6b5edc43009448ec6e19a25579c99ecb6750a617480e95b5bff3]
- Prerequisites include Rust 1.75+, Go 1.21+ for the gateway, protoc, and an Anthropic API key; the mux backend requires ANTHROPIC_API_KEY while the cli backend requires an authenticated claude CLI. [@claim:clm_9a8f4695f1d474d673911420d4e99900af4bfd0feea9ba847c2f246c96dd81fe]
- Repository development practice: components are built via make targets (make coven, make coven-agent, make coven-swarm) or installed with cargo install from crate paths; the gateway is built in a separate coven-gateway repository. [@claim:clm_a4d13de73130a2b5d860a86d65a56dd59bac6c71abe21007d58f59b62898feef]
- Repository development practice: development uses make targets (check+test+clippy, build, release, test, clippy, fmt), and CLAUDE.md is referenced for detailed development guidelines. [@claim:clm_b6b8dbc159d2e78cc113998f49e5b76e4aee3c273d656907047c2715228beb19]
<!-- rcw:end owner=source:src_b1123ce7cf885c28b57a4a28eb90d930 block=evidence -->

## Researcher notes

