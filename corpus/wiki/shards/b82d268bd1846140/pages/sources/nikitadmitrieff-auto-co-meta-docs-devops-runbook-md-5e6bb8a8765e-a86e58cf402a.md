---
access: public
aliases: []
claim_ids:
- clm_0a74b819a7480753aa876342746598bdfe2258d89b2a31763bae36761d981001
- clm_1798dfaec9bdee2883e3cd53b17f79eda74d5d6fc76f12dd61ff9effdf1f3568
- clm_8bac5388a7862c739ce4f150b191cfc5d1c1a50cfc84e7ea8a45ba7fb7a3b3a3
- clm_c9fe278c0bbdac0610debda0408f1dc1b15947791c49d293626a6b4be2007ad5
maturity: draft
page_id: pg_1d59985cf9445ced9afda86e58cf402a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_19e7da2c9bc25b5fb8b4da92a7dc3b6f
title: NikitaDmitrieff/auto-co-meta/docs/devops/runbook.md @ 5e6bb8a8765e
updated_at: '2026-09-14T04:12:54Z'
---

# NikitaDmitrieff/auto-co-meta/docs/devops/runbook.md @ 5e6bb8a8765e

<!-- rcw:begin owner=source:src_19e7da2c9bc25b5fb8b4da92a7dc3b6f block=evidence -->
- The Makefile exposes operational commands such as make start, monitor, status, health, history, export, stop, pause, and resume, plus a Next.js dashboard runnable on port 3000. [@claim:clm_0a74b819a7480753aa876342746598bdfe2258d89b2a31763bae36761d981001]
- Consensus.md acts as the relay baton carrying state between cycles, written atomically via a .consensus.tmp temp file and rename, with a .bak backup restored automatically on cycle failure. [@claim:clm_1798dfaec9bdee2883e3cd53b17f79eda74d5d6fc76f12dd61ff9effdf1f3568]
- Configuration is environment-based via .env, with documented variables including MODEL (default sonnet), LOOP_INTERVAL (120s), CYCLE_TIMEOUT_SECONDS (1800s), MAX_CONSECUTIVE_ERRORS (3), and COOLDOWN_SECONDS (300). [@claim:clm_8bac5388a7862c739ce4f150b191cfc5d1c1a50cfc84e7ea8a45ba7fb7a3b3a3]
- The loop includes resilience mechanisms: a circuit breaker after MAX_CONSECUTIVE_ERRORS failures with a cooldown, and automatic sleep of LIMIT_WAIT_SECONDS (default one hour) on API usage-limit errors. [@claim:clm_c9fe278c0bbdac0610debda0408f1dc1b15947791c49d293626a6b4be2007ad5]
<!-- rcw:end owner=source:src_19e7da2c9bc25b5fb8b4da92a7dc3b6f block=evidence -->

## Researcher notes

