---
access: public
aliases: []
claim_ids:
- clm_0ee652287001d4ae33177d0b3def495535969f804b700a099122d4820b1cb305
- clm_90d4ae62b6f68a2efcf473f9a331a7a481ffd9adafe7c428d8d37bc2274ac33c
- clm_d0137f85e3295818a0c7cb73a24b1869f1ff54f424ef2c9b638fd419f2146987
- clm_ea459120c95ef373dc95284b07d23d0ea39ff717f607af8c2648befd82f69f66
maturity: draft
page_id: pg_7af27ee27d33575c8d63dfb4f7984352
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8994ddca19a95bc5984d678a5a61dc61
title: Dicklesworthstone/frankenterm/AGENTS.md @ 9416f404da44
updated_at: '2026-09-14T03:07:04Z'
---

# Dicklesworthstone/frankenterm/AGENTS.md @ 9416f404da44

<!-- rcw:begin owner=source:src_8994ddca19a95bc5984d678a5a61dc61 block=evidence -->
- Repository development practice: direct tokio usage is forbidden; all async must go through the project's `runtime_async` asupersync wrapper, enforced by compile-time sealed traits, source grep guards, cargo-deny bans, and test-time checks. [@claim:clm_0ee652287001d4ae33177d0b3def495535969f804b700a099122d4820b1cb305]
- Repository development practice: releases must go exclusively through Doodlestein Self-Releaser (dsr) — doctor/health, quality, build, release, and verify commands — and GitHub Actions must never be inspected, triggered, or relied on for any claim. [@claim:clm_90d4ae62b6f68a2efcf473f9a331a7a481ffd9adafe7c428d8d37bc2274ac33c]
- Repository development practice: upstream WezTerm fixes are backported weekly via a read-only tracking ref with manual per-commit ports tagged `Upstream-WezTerm: <sha>`; blind pulls, merges, or bulk directory copies from upstream are prohibited. [@claim:clm_d0137f85e3295818a0c7cb73a24b1869f1ff54f424ef2c9b638fd419f2146987]
- Repository development practice: agents may never delete files without explicit written permission, must not use git worktrees, must work on `main` (never `master`), and must avoid destructive commands like `git reset --hard` or `rm -rf` without explicit user authorization. [@claim:clm_ea459120c95ef373dc95284b07d23d0ea39ff717f607af8c2648befd82f69f66]
<!-- rcw:end owner=source:src_8994ddca19a95bc5984d678a5a61dc61 block=evidence -->

## Researcher notes

