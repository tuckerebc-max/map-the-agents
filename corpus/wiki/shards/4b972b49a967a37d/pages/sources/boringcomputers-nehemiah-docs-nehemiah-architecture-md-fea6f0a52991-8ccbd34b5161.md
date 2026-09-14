---
access: public
aliases: []
claim_ids:
- clm_2e3794f01aab746fc7dda899a695426344f9c6c9a78fbc6579a0ba48eafd8831
- clm_f730ad3510737a84b75bedd0560736e078d47424bb18529a606e56cb6c785f7c
maturity: draft
page_id: pg_4fcb33c902b351a0b0088ccbd34b5161
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6e8b487ed9c85c17a5aa3ee67e177818
title: boringcomputers/nehemiah/docs/nehemiah/architecture.md @ fea6f0a52991
updated_at: '2026-09-14T03:39:33Z'
---

# boringcomputers/nehemiah/docs/nehemiah/architecture.md @ fea6f0a52991

<!-- rcw:begin owner=source:src_6e8b487ed9c85c17a5aa3ee67e177818 block=evidence -->
- Managed machines move through persisted lifecycle states (requested, placing, starting, running, stopping, stopped, failed, lost); terminal records never regress, and a machine declared lost is never presented as recovered. [@claim:clm_2e3794f01aab746fc7dda899a695426344f9c6c9a78fbc6579a0ba48eafd8831]
- The scheduler filters hosts by region, architecture, size, template availability, health, and hard quotas, reserving capacity in one PostgreSQL transaction and preferring hosts with the requested template cached. [@claim:clm_f730ad3510737a84b75bedd0560736e078d47424bb18529a606e56cb6c785f7c]
<!-- rcw:end owner=source:src_6e8b487ed9c85c17a5aa3ee67e177818 block=evidence -->

## Researcher notes

