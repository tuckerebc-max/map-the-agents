---
access: public
aliases: []
claim_ids:
- clm_72b574060ff1a72f14216f97d0ee5272b79fb795f5150991d32d8891a227163a
maturity: draft
page_id: pg_3605c9fc574f5e73affb45681f5ea03d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_15a18810039757b2b445f52f5dcffbd0
title: TrafficGuard/typedai/docs/AUTO_START_POSTGRES.md @ 34139aec65bb
updated_at: '2026-09-14T04:27:59Z'
---

# TrafficGuard/typedai/docs/AUTO_START_POSTGRES.md @ 34139aec65bb

<!-- rcw:begin owner=source:src_15a18810039757b2b445f52f5dcffbd0 block=evidence -->
- Repository development practice: with `DATABASE_TYPE=postgres` set, a Postgres Docker container auto-starts during app-context initialization, skipping when the host is remote, inside Docker, or in CI. [@claim:clm_72b574060ff1a72f14216f97d0ee5272b79fb795f5150991d32d8891a227163a]
<!-- rcw:end owner=source:src_15a18810039757b2b445f52f5dcffbd0 block=evidence -->

## Researcher notes

