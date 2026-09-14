---
access: public
aliases: []
claim_ids:
- clm_4eb4f4f0e76508af22b9aaa7e34e3254c8c9eb3aae69a2f908f27aa336195e19
- clm_69210465d4e48c55c184d3b0ee9154dca80b249543ef129e81d26fe77bdbce7e
- clm_9a6af3e7ea044000ddd3793fdb33078ae900a109006e3725494cf3f174b4383b
- clm_de65a34c4bf86ee8b14d771c02e1eccc7f541c8e99f9fe10cdb225c6eaf9cbc4
- clm_e058d91f5fab7be25fda81680cd62504d2b0ecfd1865625e730bb3c471daf567
maturity: draft
page_id: pg_c1009397a4e65b8ba54ebc9fd1728be5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_90f471204588504a843d111df6f10efc
title: fivetaku/kkirikkiri/CHANGELOG.md @ 99df0f40feb6
updated_at: '2026-09-14T01:49:09Z'
---

# fivetaku/kkirikkiri/CHANGELOG.md @ 99df0f40feb6

<!-- rcw:begin owner=source:src_90f471204588504a843d111df6f10efc block=evidence -->
- Multi-model support appears to work by shelling out to installed external CLIs (Codex, agy, grok, gjc) with per-provider flags and model-override env vars like KKIRIKKIRI_GROK_MODEL. [@claim:clm_4eb4f4f0e76508af22b9aaa7e34e3254c8c9eb3aae69a2f908f27aa336195e19]
- The opt-in preparation pilot generates cards and Agent requests from one approved plan but is explicitly not a runtime permission sandbox, and no OS sandbox or write serialization for concurrent sessions is newly guaranteed. [@claim:clm_69210465d4e48c55c184d3b0ee9154dca80b249543ef129e81d26fe77bdbce7e]
- Two execution substrates are offered: a live collaborating Agent Teams mode or a deterministic Workflow pipeline for high-volume fan-out work; the user picks between them. [@claim:clm_9a6af3e7ea044000ddd3793fdb33078ae900a109006e3725494cf3f174b4383b]
- The changelog explicitly notes a known limit: gates verify that write_scope declarations exist but cannot judge actual compliance without per-member output isolation, deferred to a v0.25 backlog. [@claim:clm_de65a34c4bf86ee8b14d771c02e1eccc7f541c8e99f9fe10cdb225c6eaf9cbc4]
- Hook-based gates enforce write boundaries at runtime: gate-spawn blocks spawning a member whose write_scope overlaps another member's declared scope, and blocks spawns lacking tool/read-only/write_scope/stop declarations. [@claim:clm_e058d91f5fab7be25fda81680cd62504d2b0ecfd1865625e730bb3c471daf567]
<!-- rcw:end owner=source:src_90f471204588504a843d111df6f10efc block=evidence -->

## Researcher notes

