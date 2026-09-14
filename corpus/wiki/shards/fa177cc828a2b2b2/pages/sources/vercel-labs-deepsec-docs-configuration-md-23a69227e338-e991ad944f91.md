---
access: public
aliases: []
claim_ids:
- clm_868d5db5ede5f73973baeac3c2fe9c0c8e2f0710ef309b7606f0f58b6ae7e8ff
- clm_9805870812e23e8c45bc01b85f098cb82d63934be157bd09d42560b814462a54
maturity: draft
page_id: pg_885a018dc9c65395a924e991ad944f91
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_39098c834c805138a3e18506b459dbf8
title: vercel-labs/deepsec/docs/configuration.md @ 23a69227e338
updated_at: '2026-09-14T04:30:26Z'
---

# vercel-labs/deepsec/docs/configuration.md @ 23a69227e338

<!-- rcw:begin owner=source:src_39098c834c805138a3e18506b459dbf8 block=evidence -->
- The architecture doc describes five plugin extension points in packages/core/src/plugin.ts: matchers, notifiers, and agents are additive, while ownership, people, and executor are single-slot with last-write-wins ordering. [@claim:clm_868d5db5ede5f73973baeac3c2fe9c0c8e2f0710ef309b7606f0f58b6ae7e8ff]
- Configuration lives in deepsec.config.ts (or .mjs/.js/.cjs) resolved from the current directory walking upward, declaring projects, plugins, matcher filters, default agent/model/thinking level, AI route, and dataDir. [@claim:clm_9805870812e23e8c45bc01b85f098cb82d63934be157bd09d42560b814462a54]
<!-- rcw:end owner=source:src_39098c834c805138a3e18506b459dbf8 block=evidence -->

## Researcher notes

