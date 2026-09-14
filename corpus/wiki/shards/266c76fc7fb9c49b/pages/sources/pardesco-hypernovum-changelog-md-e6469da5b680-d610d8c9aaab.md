---
access: public
aliases: []
claim_ids:
- clm_505d8f63fec9079e5484f9bfa60ce49193e1f3c6df85502174c7c56977f80bc3
- clm_98b4bf59fe92ee7111c8c22afeff2b9e362d39a71c879635b0aac74fce151282
- clm_ba216a48a59ed43f4c54b99667f3b94b94dc87032a86a988ee362ba5b09b3ea7
- clm_ff6067f92da0b04d90126e2cbaf7c510913d9e7f3005d2af7efbba900a6b2383
maturity: draft
page_id: pg_ff1b215d5a3353bf963ed610d8c9aaab
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e95dbe2419565169aa952334f24398ed
title: Pardesco/hypernovum/CHANGELOG.md @ e6469da5b680
updated_at: '2026-09-14T02:29:03Z'
---

# Pardesco/hypernovum/CHANGELOG.md @ e6469da5b680

<!-- rcw:begin owner=source:src_e95dbe2419565169aa952334f24398ed block=evidence -->
- An untagged vault renders as a whole-vault fallback (folders as districts, notes as buildings, height from incoming links); tagging one note switches the city to project mode, and the fallback only applies at zero projects. [@claim:clm_505d8f63fec9079e5484f9bfa60ce49193e1f3c6df85502174c7c56977f80bc3]
- The plugin is built with Three.js, Zustand, and the Obsidian Plugin API, and requires Obsidian minAppVersion 1.6.0. [@claim:clm_98b4bf59fe92ee7111c8c22afeff2b9e362d39a71c879635b0aac74fce151282]
- Repository development practice: development uses npm scripts (dev, build, typecheck, vitest tests), releases are cut from the root manifest.json with check-versions.mjs mirroring versions, and CI typechecks and tests before building. [@claim:clm_ba216a48a59ed43f4c54b99667f3b94b94dc87032a86a988ee362ba5b09b3ea7]
- A vault mode turns the entire agent layer off — no process execution and no reads outside the vault — while the city, lenses, filters and backlink graph keep working; first run asks whether to enable the agent layer. [@claim:clm_ff6067f92da0b04d90126e2cbaf7c510913d9e7f3005d2af7efbba900a6b2383]
<!-- rcw:end owner=source:src_e95dbe2419565169aa952334f24398ed block=evidence -->

## Researcher notes

