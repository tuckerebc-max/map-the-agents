---
access: public
aliases: []
claim_ids:
- clm_0abc3ca6f661346f62ca77c940aeb462692a36d12a06d4bc08f3ae9ef1514018
- clm_1e730d26242fefe98aff50f4d37fbfb23471e6fd9c5952914decb3c82688c6f2
- clm_2adce312392441e935479965283adcba53dec710902699c2701ba25d37ff8e55
- clm_2dd6e649c21b8a74b3929645d7afb4a083db9d2d3ffafc3a3e3a00a530d13d96
- clm_952497d2acafad3c4d45cde7311ee58b7a5bf2a4e4aa8cd7fe66fcbf4175da2e
- clm_990c63672b8e8bdfff528f43d83c29a4ac66a98ca8fa59e544aa4f5eff58e5df
- clm_d411149fb8119d5c8d888c4404f30a1d13ec506f1aaa129daa657c70d8853794
- clm_ea24042fc64980ae1a7c6d85f4945a91fcfd62feccdaff7844caede7d446b6c9
maturity: draft
page_id: pg_421869d734e851d092a7c000a14e3236
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0c95d33d560456ed81ceeb4bd3c04f98
title: 2389-research/gossip/docs/contract.md @ fb54508fa18c
updated_at: '2026-09-14T03:28:42Z'
---

# 2389-research/gossip/docs/contract.md @ fb54508fa18c

<!-- rcw:begin owner=source:src_0c95d33d560456ed81ceeb4bd3c04f98 block=evidence -->
- TTLs are speaker-chosen within store-configured default_ttl/max_ttl bounds, persisted as absolute expires_at at append; out-of-bounds TTLs are validation errors, not silent clamps. [@claim:clm_0abc3ca6f661346f62ca77c940aeb462692a36d12a06d4bc08f3ae9ef1514018]
- The store is an append-only, immutable event log in one SQLite file; all derived state (badges, views) is folded at read time and never stored, and the audit log retains everything including expired and hidden posts. [@claim:clm_1e730d26242fefe98aff50f4d37fbfb23471e6fd9c5952914decb3c82688c6f2]
- A signed design contract (docs/contract.md) defines v1 semantics: event types, validation rules, view rules, and a standalone trust model, with amendments requiring design-room consensus rather than silent edits. [@claim:clm_2adce312392441e935479965283adcba53dec710902699c2701ba25d37ff8e55]
- Filesystem access to the SQLite file is the trust boundary and effectively membership; validation runs inside the CLI, and a hostile writer with file access can bypass it entirely. [@claim:clm_2dd6e649c21b8a74b3929645d7afb4a083db9d2d3ffafc3a3e3a00a530d13d96]
- Identity is configured via GOSSIP_ACTOR_ID and GOSSIP_PRINCIPAL_ID environment variables, and the store path defaults to ~/.gossip/gossip.db with GOSSIP_DB (or --db) to override. [@claim:clm_952497d2acafad3c4d45cde7311ee58b7a5bf2a4e4aa8cd7fe66fcbf4175da2e]
- Every post carries a rumor or observed label; there is deliberately no verified status in v1 because no verifier mechanism exists, and badges display evidence without ever minting truth. [@claim:clm_990c63672b8e8bdfff528f43d83c29a4ac66a98ca8fa59e544aa4f5eff58e5df]
- The CLI exposes commands including start, threads, read, post, corroborate, receipt, retract, hide, whoami, and log, with flags such as --label, --ttl, --ref, and --reason. [@claim:clm_d411149fb8119d5c8d888c4404f30a1d13ec506f1aaa129daa657c70d8853794]
- Documented v1 cuts include no verifier or verified status, no cross-store sharing, no per-thread ACLs, no rooms, no SSE/watch, no cryptographic identity, and no publish/live subscribers. [@claim:clm_ea24042fc64980ae1a7c6d85f4945a91fcfd62feccdaff7844caede7d446b6c9]
<!-- rcw:end owner=source:src_0c95d33d560456ed81ceeb4bd3c04f98 block=evidence -->

## Researcher notes

