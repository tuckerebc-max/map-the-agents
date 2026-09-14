---
access: public
aliases: []
claim_ids:
- clm_05b338388db00e1953361e1fec360ebd07ee8cdf92a5aee08d3f298e53a22a04
- clm_a1a4692a07a47c5a390306622ba5d6831a7c2387dc56bb1ad9af16920a256934
maturity: draft
page_id: pg_98e04594d54658f0a509cf28b728e63c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_90b0c78528935a3e8e11aa0e72f252c5
title: the-open-engine/zeroshot/docs/reference/cluster/api.md @ b550c15279c9
updated_at: '2026-09-14T03:18:50Z'
---

# the-open-engine/zeroshot/docs/reference/cluster/api.md @ b550c15279c9

<!-- rcw:begin owner=source:src_90b0c78528935a3e8e11aa0e72f252c5 block=evidence -->
- The apply method supports dryRun, ifGeneration optimistic concurrency, and idempotencyKey parameters, suggesting the cluster API is designed for safe, repeatable graph applications. [@claim:clm_05b338388db00e1953361e1fec360ebd07ee8cdf92a5aee08d3f298e53a22a04]
- Subscription methods use generic framing: watch, logs, and agent/attach (and run/* equivalents) establish subscriptions via one JSON-RPC result, then use generic event, subscription/cancel, subscription/closed, and $/cancelRequest notifications; no method-specific event/cancel/closed methods exist on the wire. [@claim:clm_a1a4692a07a47c5a390306622ba5d6831a7c2387dc56bb1ad9af16920a256934]
<!-- rcw:end owner=source:src_90b0c78528935a3e8e11aa0e72f252c5 block=evidence -->

## Researcher notes

