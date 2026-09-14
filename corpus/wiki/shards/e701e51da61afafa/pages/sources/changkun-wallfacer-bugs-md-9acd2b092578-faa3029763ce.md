---
access: public
aliases: []
claim_ids:
- clm_9fda7d3639d1533a8f88743c2143f09e309c3d3365026758a6a294cdc8297dd6
maturity: draft
page_id: pg_92dac420f0ac5248af36faa3029763ce
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_96638da841b95551a3041d18fccf181d
title: changkun/wallfacer/BUGS.md @ 9acd2b092578
updated_at: '2026-09-14T01:40:39Z'
---

# changkun/wallfacer/BUGS.md @ 9acd2b092578

<!-- rcw:begin owner=source:src_96638da841b95551a3041d18fccf181d block=evidence -->
- A known bug: the OAuth redirect_uri is derived from the requested address before a port fallback, so when the configured port is taken the redirect points at a port the server is not listening on. [@claim:clm_9fda7d3639d1533a8f88743c2143f09e309c3d3365026758a6a294cdc8297dd6]
<!-- rcw:end owner=source:src_96638da841b95551a3041d18fccf181d block=evidence -->

## Researcher notes

