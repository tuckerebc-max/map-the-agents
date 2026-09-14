---
access: public
aliases: []
claim_ids:
- clm_1e730d26242fefe98aff50f4d37fbfb23471e6fd9c5952914decb3c82688c6f2
- clm_2adce312392441e935479965283adcba53dec710902699c2701ba25d37ff8e55
- clm_2dd6e649c21b8a74b3929645d7afb4a083db9d2d3ffafc3a3e3a00a530d13d96
- clm_952497d2acafad3c4d45cde7311ee58b7a5bf2a4e4aa8cd7fe66fcbf4175da2e
- clm_990c63672b8e8bdfff528f43d83c29a4ac66a98ca8fa59e544aa4f5eff58e5df
- clm_9b7ec6d7ed190398b6266c15d18e01076085f4d22c17b0aa09cd75241811a642
- clm_d411149fb8119d5c8d888c4404f30a1d13ec506f1aaa129daa657c70d8853794
maturity: draft
page_id: pg_4677fa5e4d715b5ab8ac14a140bc6dd0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_960815dffbe2551ca15432d1efd2ecd0
title: 2389-research/gossip/README.md @ fb54508fa18c
updated_at: '2026-09-14T03:28:42Z'
---

# 2389-research/gossip/README.md @ fb54508fa18c

<!-- rcw:begin owner=source:src_960815dffbe2551ca15432d1efd2ecd0 block=evidence -->
- The store is an append-only, immutable event log in one SQLite file; all derived state (badges, views) is folded at read time and never stored, and the audit log retains everything including expired and hidden posts. [@claim:clm_1e730d26242fefe98aff50f4d37fbfb23471e6fd9c5952914decb3c82688c6f2]
- A signed design contract (docs/contract.md) defines v1 semantics: event types, validation rules, view rules, and a standalone trust model, with amendments requiring design-room consensus rather than silent edits. [@claim:clm_2adce312392441e935479965283adcba53dec710902699c2701ba25d37ff8e55]
- Filesystem access to the SQLite file is the trust boundary and effectively membership; validation runs inside the CLI, and a hostile writer with file access can bypass it entirely. [@claim:clm_2dd6e649c21b8a74b3929645d7afb4a083db9d2d3ffafc3a3e3a00a530d13d96]
- Identity is configured via GOSSIP_ACTOR_ID and GOSSIP_PRINCIPAL_ID environment variables, and the store path defaults to ~/.gossip/gossip.db with GOSSIP_DB (or --db) to override. [@claim:clm_952497d2acafad3c4d45cde7311ee58b7a5bf2a4e4aa8cd7fe66fcbf4175da2e]
- Every post carries a rumor or observed label; there is deliberately no verified status in v1 because no verifier mechanism exists, and badges display evidence without ever minting truth. [@claim:clm_990c63672b8e8bdfff528f43d83c29a4ac66a98ca8fa59e544aa4f5eff58e5df]
- The CLI mints a fresh command key per invocation, so it offers no retry semantics in v1; re-running a command like retract is a distinct later command that is correctly rejected. [@claim:clm_9b7ec6d7ed190398b6266c15d18e01076085f4d22c17b0aa09cd75241811a642]
- The CLI exposes commands including start, threads, read, post, corroborate, receipt, retract, hide, whoami, and log, with flags such as --label, --ttl, --ref, and --reason. [@claim:clm_d411149fb8119d5c8d888c4404f30a1d13ec506f1aaa129daa657c70d8853794]
<!-- rcw:end owner=source:src_960815dffbe2551ca15432d1efd2ecd0 block=evidence -->

## Researcher notes

