---
access: public
aliases: []
claim_ids:
- clm_4392c4644d8683d5d0350bdd0585546465ee72cc562a65966b19cd4a403242fe
- clm_f04c576ef81938f8218e1f4cb0f176c3d697e099fa34e111e96f767af570d276
maturity: draft
page_id: pg_7fa58c01d5b35572acf943ed9ac56d1e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_62e022182ee4512aa8fd71aa1c147e31
title: backbay-labs/clawdstrike/docs/src/hunt/architecture.md @ b01f63ae64fa
updated_at: '2026-09-14T03:37:35Z'
---

# backbay-labs/clawdstrike/docs/src/hunt/architecture.md @ b01f63ae64fa

<!-- rcw:begin owner=source:src_62e022182ee4512aa8fd71aa1c147e31 block=evidence -->
- The system depends on Ed25519 signing (ed25519-dalek for Rust primitives), RFC 8785 JSON canonicalization for cross-language signature verification, and NATS JetStream for telemetry transport. [@claim:clm_4392c4644d8683d5d0350bdd0585546465ee72cc562a65966b19cd4a403242fe]
- Defaults fail closed: the guard report aggregates per-guard results such that any deny produces an overall deny, and denials emit signed receipts. [@claim:clm_f04c576ef81938f8218e1f4cb0f176c3d697e099fa34e111e96f767af570d276]
<!-- rcw:end owner=source:src_62e022182ee4512aa8fd71aa1c147e31 block=evidence -->

## Researcher notes

