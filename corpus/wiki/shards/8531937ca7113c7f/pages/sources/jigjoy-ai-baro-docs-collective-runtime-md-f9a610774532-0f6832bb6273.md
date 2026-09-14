---
access: public
aliases: []
claim_ids:
- clm_3d6a7d0597e6ca15591c35cdbf4113cdb7106ddda2212e97034005af8fda2239
- clm_630a3eb1b0633aa3bc1604d67ebf3a855db38c1a79fa35bfc09e1a9b75b7e73c
- clm_bb94c90bc24882cf73f385ce667a79ed9663f7f19767f5a5e236628239cba494
maturity: draft
page_id: pg_62dc6fd10b5f5c6783560f6832bb6273
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3e20a7f65eef5c579ad41eddb06e0f40
title: jigjoy-ai/baro/docs/collective-runtime.md @ f9a610774532
updated_at: '2026-09-14T02:06:52Z'
---

# jigjoy-ai/baro/docs/collective-runtime.md @ f9a610774532

<!-- rcw:begin owner=source:src_3e20a7f65eef5c579ad41eddb06e0f40 block=evidence -->
- Codex, OpenCode, and Pi workers are one-shot CLI processes that cannot consume corrective messages after exit; failed verdicts for those backends require a separate recovery execution rather than in-process revision. [@claim:clm_3d6a7d0597e6ca15591c35cdbf4113cdb7106ddda2212e97034005af8fda2239]
- The runtime is distributed but not leaderless: the Board serializes scheduling and durable graph commits while separate participants own goal meaning, route selection, lease granting, quality evaluation, merging, and verification. [@claim:clm_630a3eb1b0633aa3bc1604d67ebf3a855db38c1a79fa35bfc09e1a9b75b7e73c]
- The docs state Baro lacks a trusted per-story CandidateVerifier that executes new deterministic commands in the active worktree, so genuinely missing or fully stale command evidence stays inconclusive after bounded rechecks. [@claim:clm_bb94c90bc24882cf73f385ce667a79ed9663f7f19767f5a5e236628239cba494]
<!-- rcw:end owner=source:src_3e20a7f65eef5c579ad41eddb06e0f40 block=evidence -->

## Researcher notes

