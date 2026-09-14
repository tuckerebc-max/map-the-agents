---
access: public
aliases: []
claim_ids:
- clm_0cd68a7deeb0d5589eca6e9ef4c41a8e2a0198956fe916baf77a719274b74867
- clm_10c58a31819b721241fcc455430122a92831b302f6f55b8013bba0f8ecb9433e
- clm_3a44982f7830f0ddfd911d65ad3ee8c631bb4b12577bfd9a9ec30d95bf42a145
- clm_6ee99b1a49d13d324d18b0292ba5406d2d903686c0e73c9e10d61f23ac85d278
- clm_7777d76bbabddc6e65eb53320a473bee7ba741f52299d0e907174cbed290f855
- clm_868d5db5ede5f73973baeac3c2fe9c0c8e2f0710ef309b7606f0f58b6ae7e8ff
- clm_8ce0fb86a485d89e06007e71557f92699c8ad62d668c1ffa60ca24fbaf5ecc43
- clm_bb5b194cf2f2df691e327770bca86bd9eaa7e2c15fe808a947e6585cdbac2611
- clm_c1cb44e3925745ed552930bc70b4e219fd30ee62dabc58da7de0d9bf2bfb1b0a
maturity: draft
page_id: pg_d875c52a104d5eb3a6aaa2580ae7fb5f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5d9a5dc55ea55e04847a27bf7a0e0ba8
title: vercel-labs/deepsec/docs/architecture.md @ 23a69227e338
updated_at: '2026-09-14T04:30:26Z'
---

# vercel-labs/deepsec/docs/architecture.md @ 23a69227e338

<!-- rcw:begin owner=source:src_5d9a5dc55ea55e04847a27bf7a0e0ba8 block=evidence -->
- The scan stage globs the project root, applies regex matchers to every matched file, and writes candidate matches into per-file FileRecords without any AI usage. [@claim:clm_0cd68a7deeb0d5589eca6e9ef4c41a8e2a0198956fe916baf77a719274b74867]
- Three agent backends are supported for process: codex (default, via @openai/codex-sdk), claude (via @anthropic-ai/claude-agent-sdk), and pi (via @earendil-works/pi-coding-agent), each with a documented default model. [@claim:clm_10c58a31819b721241fcc455430122a92831b302f6f55b8013bba0f8ecb9433e]
- The processor claims files atomically via lockedByRunId so multiple workers can run in parallel; concurrency and batch size flags control how many files are in flight. [@claim:clm_3a44982f7830f0ddfd911d65ad3ee8c631bb4b12577bfd9a9ec30d95bf42a145]
- The setup coordinator uses a read-only agent to produce INFO.md and a structured surface inventory, evaluates scan coverage, generates data-only matcher specs validated for regex safety and slug collisions, and gates paid processing until coverage passes. [@claim:clm_6ee99b1a49d13d324d18b0292ba5406d2d903686c0e73c9e10d61f23ac85d278]
- The process stage batches pending files, sends each batch to a configured AI agent backend with the system prompt and INFO.md, and parses JSON responses into findings stored on FileRecords. [@claim:clm_7777d76bbabddc6e65eb53320a473bee7ba741f52299d0e907174cbed290f855]
- The architecture doc describes five plugin extension points in packages/core/src/plugin.ts: matchers, notifiers, and agents are additive, while ownership, people, and executor are single-slot with last-write-wins ordering. [@claim:clm_868d5db5ede5f73973baeac3c2fe9c0c8e2f0710ef309b7606f0f58b6ae7e8ff]
- The revalidate stage re-checks findings for false positives using git history and, per the docs, empirically reduces the false-positive rate by 50% or more on most repos. [@claim:clm_8ce0fb86a485d89e06007e71557f92699c8ad62d668c1ffa60ca24fbaf5ecc43]
- The unit of work is a source file rather than a finding, which the architecture doc says makes per-file atomic locking and idempotent merges natural. [@claim:clm_bb5b194cf2f2df691e327770bca86bd9eaa7e2c15fe808a947e6585cdbac2611]
- On-disk state is append-only: re-scans merge new candidates, re-processing appends to analysisHistory and merges findings, and revalidation annotates findings with verdicts without overwriting or deleting anything. [@claim:clm_c1cb44e3925745ed552930bc70b4e219fd30ee62dabc58da7de0d9bf2bfb1b0a]
<!-- rcw:end owner=source:src_5d9a5dc55ea55e04847a27bf7a0e0ba8 block=evidence -->

## Researcher notes

