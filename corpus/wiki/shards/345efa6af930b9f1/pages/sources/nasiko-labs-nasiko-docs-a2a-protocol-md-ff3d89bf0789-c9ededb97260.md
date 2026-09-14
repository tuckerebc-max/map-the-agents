---
access: public
aliases: []
claim_ids:
- clm_1bb48b93e81f236792a3a790891aec3fcc098619860dae307f968741aef32415
- clm_3263f4b7a2da679301a692afadfd27462630b41094f69ae64e45e1b62ca20d2e
- clm_d77ebb8a6fb05d87f6e6e50ceaacb6202e6252664608576c0ae95ae9388a9647
- clm_da0d11ccb87143e4d56035e52b88cd92531e2fc16f685d481a7340ac4e1a9bfb
maturity: draft
page_id: pg_9b021f6339455478baebc9ededb97260
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ede8cb603af95b5eab98765b8d70864f
title: Nasiko-Labs/nasiko/docs/A2A_PROTOCOL.md @ ff3d89bf0789
updated_at: '2026-09-14T04:11:41Z'
---

# Nasiko-Labs/nasiko/docs/A2A_PROTOCOL.md @ ff3d89bf0789

<!-- rcw:begin owner=source:src_ede8cb603af95b5eab98765b8d70864f block=evidence -->
- The A2A implementation uses the Rust libraries a2a-lf 0.3.0 and a2a-server-lf 0.4.0 from a2aproject/a2a-rs, and the workspace targets Rust edition 2024 (Rust 1.85+). [@claim:clm_1bb48b93e81f236792a3a790891aec3fcc098619860dae307f968741aef32415]
- Agent discovery fetches the agent card from /.well-known/agent-card.json on deploy or seed; the orchestrator primarily uses SendStreamingMessage while the CLI uses SendMessage for direct chat. [@claim:clm_3263f4b7a2da679301a692afadfd27462630b41094f69ae64e45e1b62ca20d2e]
- Nasiko runs as a single control-plane process with no separate gateway; every inter-agent call is proxied back through the server, which enforces flow limits, ACLs, and observability at one chokepoint. [@claim:clm_d77ebb8a6fb05d87f6e6e50ceaacb6202e6252664608576c0ae95ae9388a9647]
- Nasiko targets the A2A protocol v1.0 exactly, requiring the A2A-Version: 1.0 header on every request, and uses JSON-RPC 2.0 over HTTP(S) as its sole protocol binding with SSE for streaming. [@claim:clm_da0d11ccb87143e4d56035e52b88cd92531e2fc16f685d481a7340ac4e1a9bfb]
<!-- rcw:end owner=source:src_ede8cb603af95b5eab98765b8d70864f block=evidence -->

## Researcher notes

