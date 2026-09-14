---
access: public
aliases: []
claim_ids:
- clm_3fe9aa7c7a429b28933df118f007705dfb45c4fb3fe4fdcdc24ebb10fbdcd8ee
- clm_948c6ce38f18d2fea7adb5a071c641abd7ea65fcce0475c4b0f1de3d5d1adddd
maturity: draft
page_id: pg_92f8217e2bdc512cb59179b744e5d3e0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0f8c86d4a754592bbe99689e7b7ffda7
title: juyterman1000/entroly/docs/architecture.md @ 9bab5850955c
updated_at: '2026-09-14T04:02:43Z'
---

# juyterman1000/entroly/docs/architecture.md @ 9bab5850955c

<!-- rcw:begin owner=source:src_0f8c86d4a754592bbe99689e7b7ffda7 block=evidence -->
- The design preserves provider protocol, headers, tools, parameters, ordering, and cache semantics, transforming only injected context and output; model/params/tools are never mutated unless transparent routing is explicitly enabled, and then recorded in the receipt. [@claim:clm_3fe9aa7c7a429b28933df118f007705dfb45c4fb3fe4fdcdc24ebb10fbdcd8ee]
- Architecture invariants specify fail-closed behavior only for the security/compliance gate and provider gateway; all other stages fail open by passing the exact original context through unchanged with a receipt warning. [@claim:clm_948c6ce38f18d2fea7adb5a071c641abd7ea65fcce0475c4b0f1de3d5d1adddd]
<!-- rcw:end owner=source:src_0f8c86d4a754592bbe99689e7b7ffda7 block=evidence -->

## Researcher notes

