---
access: public
aliases: []
claim_ids:
- clm_72e8b026f5814980f94e0f0da52ee12409a7a6d5b4b572dc6015125b7eaa8bf3
- clm_73e03157c9b13834c9ab42320ebf792775bb9de1f0043a8fc3e3943996ca0424
- clm_868d98e2599b6b5edc43009448ec6e19a25579c99ecb6750a617480e95b5bff3
- clm_9a8f4695f1d474d673911420d4e99900af4bfd0feea9ba847c2f246c96dd81fe
maturity: draft
page_id: pg_7aa91d787ed15268a153ccab5f590526
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f2c141fb5ce75fecbd0a181255e026cb
title: 2389-research/coven/docs/agent.md @ 36edb5c206af
updated_at: '2026-09-14T01:26:25Z'
---

# 2389-research/coven/docs/agent.md @ 36edb5c206af

<!-- rcw:begin owner=source:src_f2c141fb5ce75fecbd0a181255e026cb block=evidence -->
- Crate dependencies are layered: coven-proto, coven-ssh, and coven-swarm-core have no internal deps; coven-agent depends on coven-core, coven-pack, coven-grpc, and coven-proto. [@claim:clm_72e8b026f5814980f94e0f0da52ee12409a7a6d5b4b572dc6015125b7eaa8bf3]
- coven-agent run accepts --name and --working-dir (required), plus --gateway (default localhost:50051), --backend (mux/cli), --display (quiet/normal/verbose), and --config options. [@claim:clm_73e03157c9b13834c9ab42320ebf792775bb9de1f0043a8fc3e3943996ca0424]
- Configuration lives under ~/.config/coven/ (config.toml, per-agent TOML files, swarm config) with data in ~/.local/share/coven/; the AgentMetadata struct includes hostname, OS, git info, workspaces, and backend fields. [@claim:clm_868d98e2599b6b5edc43009448ec6e19a25579c99ecb6750a617480e95b5bff3]
- Prerequisites include Rust 1.75+, Go 1.21+ for the gateway, protoc, and an Anthropic API key; the mux backend requires ANTHROPIC_API_KEY while the cli backend requires an authenticated claude CLI. [@claim:clm_9a8f4695f1d474d673911420d4e99900af4bfd0feea9ba847c2f246c96dd81fe]
<!-- rcw:end owner=source:src_f2c141fb5ce75fecbd0a181255e026cb block=evidence -->

## Researcher notes

