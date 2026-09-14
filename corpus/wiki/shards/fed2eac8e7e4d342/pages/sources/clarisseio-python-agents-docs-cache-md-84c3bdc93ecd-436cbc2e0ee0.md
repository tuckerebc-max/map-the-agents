---
access: public
aliases: []
claim_ids:
- clm_66b7a4cfb127b60833caf7c04e8539168c4f11e21546b810314e7ddcf9469ead
- clm_913dc7f704cc758ef9f4483e202bf62f82d35cb37c2e3ad7dfc780f94e846dd7
maturity: draft
page_id: pg_f0288b7921045339a8d8436cbc2e0ee0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4e01e6e7cf245ddf92cb578eb0846fc4
title: clarisseIO/python-agents/docs/cache.md @ 84c3bdc93ecd
updated_at: '2026-09-14T02:00:10Z'
---

# clarisseIO/python-agents/docs/cache.md @ 84c3bdc93ecd

<!-- rcw:begin owner=source:src_4e01e6e7cf245ddf92cb578eb0846fc4 block=evidence -->
- Caches expose async set/get/has/delete/clear/size operations, and custom caches are created by extending BaseCache, whose example also includes createSnapshot and loadSnapshot methods. [@claim:clm_66b7a4cfb127b60833caf7c04e8539168c4f11e21546b810314e7ddcf9469ead]
- Cache keys are produced by serializing function parameters with key order irrelevant; the default decorator key function is ObjectHashKeyFn, and SingletonCacheKeyFn yields a single shared key regardless of arguments. [@claim:clm_913dc7f704cc758ef9f4483e202bf62f82d35cb37c2e3ad7dfc780f94e846dd7]
<!-- rcw:end owner=source:src_4e01e6e7cf245ddf92cb578eb0846fc4 block=evidence -->

## Researcher notes

