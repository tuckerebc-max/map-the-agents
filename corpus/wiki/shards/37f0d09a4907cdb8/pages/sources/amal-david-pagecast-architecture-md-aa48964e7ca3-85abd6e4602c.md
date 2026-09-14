---
access: public
aliases: []
claim_ids:
- clm_41379d14674209083b678ced0e72c0744b2a85dbf605a76c8a69045abf00c80f
- clm_64e83370fdf4dab1cd06a1405bde61e11698f79bde41735c679819444c155e6e
- clm_73ded06d5466c3940b395905e7e1219f667e7ae68f3adbc86b763b783509db83
- clm_9a3b8265e207bfdfd82e32542c9e08f8bd6b3f8999c3fe06c8901fd7f19c06ea
- clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d
maturity: draft
page_id: pg_4d5f66b485f85c9e9b2a85abd6e4602c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4613dabcb13457d2add7c7d457d6203c
title: Amal-David/pagecast/ARCHITECTURE.md @ aa48964e7ca3
updated_at: '2026-09-14T03:33:49Z'
---

# Amal-David/pagecast/ARCHITECTURE.md @ aa48964e7ca3

<!-- rcw:begin owner=source:src_4613dabcb13457d2add7c7d457d6203c block=evidence -->
- Cross-system managed mutations write durable intent before remote side effects, checkpoint remote success, and retry or compensate; incomplete reconciliation stays visible in an operation journal. [@claim:clm_41379d14674209083b678ced0e72c0744b2a85dbf605a76c8a69045abf00c80f]
- Optional analytics deploys a Cloudflare Worker plus D1 database showing views, anonymous uniques, and recent events; raw IPs are HMACed with a per-Home secret and detailed events expire after 30 days. [@claim:clm_64e83370fdf4dab1cd06a1405bde61e11698f79bde41735c679819444c155e6e]
- New unlisted links combine a memorable prefix with 128 bits of entropy; unlisted is a bearer capability, not authentication, while password protection is the access-control feature and short vanity slugs are intentionally public drops. [@claim:clm_73ded06d5466c3940b395905e7e1219f667e7ae68f3adbc86b763b783509db83]
- A user-level ~/.pagecast/home/ owns the managed Cloudflare target, publication registry, analytics config, operation journal, and exclusive lease; workspace .pagecast/ holds only identity and Home mappings. [@claim:clm_9a3b8265e207bfdfd82e32542c9e08f8bd6b3f8999c3fe06c8901fd7f19c06ea]
- The admin API is loopback-only and separate from MCP; non-loopback binds are rejected, with an explicit wildcard exception only for the packaged loopback-mapped Docker proxy. [@claim:clm_c1e12176466c486a3e5c9a2eb3838b4deaca4620f87dc347a35c8bd96bcf508d]
<!-- rcw:end owner=source:src_4613dabcb13457d2add7c7d457d6203c block=evidence -->

## Researcher notes

