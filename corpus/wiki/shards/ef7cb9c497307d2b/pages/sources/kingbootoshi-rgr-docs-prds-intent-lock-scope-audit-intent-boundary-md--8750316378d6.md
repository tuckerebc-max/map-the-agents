---
access: public
aliases: []
claim_ids:
- clm_5eb3e72825e6d10306645adce4fe2a85f1652ff8629bac52644c047ab29854c1
- clm_9fe03ac6c24a79c2eb41f18ca165e2426c5558925e9a4b520f1ded755b3eb655
- clm_a3013de4a7d0fb3024bd1409eaf0ad792e71886313a4c78780bbaceb97627f58
maturity: draft
page_id: pg_092837e4623350b9af678750316378d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f643615a30725a0a9f54396e31684599
title: kingbootoshi/rgr/docs/prds/intent-lock-scope-audit.intent-boundary.md @ 45ffc907a54b
updated_at: '2026-09-14T04:03:28Z'
---

# kingbootoshi/rgr/docs/prds/intent-lock-scope-audit.intent-boundary.md @ 45ffc907a54b

<!-- rcw:begin owner=source:src_f643615a30725a0a9f54396e31684599 block=evidence -->
- The intent-lock feature adds core files intent.ts, scope-audit.ts, glob.ts, and stable-json.ts, with the scope audit composed inside verifyCommand rather than as a standalone authoritative command. [@claim:clm_5eb3e72825e6d10306645adce4fe2a85f1652ff8629bac52644c047ab29854c1]
- The project is intended to stay zero-dependency, using only Bun and node: builtins; the boundary forbids adding npm packages for glob matching, signature verification, or JSON canonicalization. [@claim:clm_9fe03ac6c24a79c2eb41f18ca165e2426c5558925e9a4b520f1ded755b3eb655]
- The CLI exposes subcommands including init, red, green, refactor, verify, revise-test, status, doctor, inspect-test, prompt, and lock-intent, invoked via Bun with flags like --goal-id, --test, --protect, --ci, --replay. [@claim:clm_a3013de4a7d0fb3024bd1409eaf0ad792e71886313a4c78780bbaceb97627f58]
<!-- rcw:end owner=source:src_f643615a30725a0a9f54396e31684599 block=evidence -->

## Researcher notes

