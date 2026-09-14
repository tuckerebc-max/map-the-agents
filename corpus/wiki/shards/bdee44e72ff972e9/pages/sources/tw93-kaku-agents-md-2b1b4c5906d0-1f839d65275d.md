---
access: public
aliases: []
claim_ids:
- clm_3e6847cf3d6c9bbf4c649d944a9dc4192fd9af4415bf11f167bc31460c1fa388
- clm_56f97fe51cd609896e25dea16bf5190c5fff51ebec4bce81ed86c6783a039cce
- clm_e284be4e4a9c2796e8367470f9186e6c5cd36da6e34408798415e378a16771f7
maturity: draft
page_id: pg_9af8c311641a57a6875e1f839d65275d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eecb4a967e245b3aac3ff84e45e2a73f
title: tw93/Kaku/AGENTS.md @ 2b1b4c5906d0
updated_at: '2026-09-14T03:20:40Z'
---

# tw93/Kaku/AGENTS.md @ 2b1b4c5906d0

<!-- rcw:begin owner=source:src_eecb4a967e245b3aac3ff84e45e2a73f block=evidence -->
- Repository development practice: releases use `V0.x.x` tags with `scripts/release.sh` as source of truth, release notes titled from `.github/RELEASE_NOTES.md`, and a manual pre-release smoke checklist in `.agents/skills/release/SKILL.md` run on the built app before tagging. [@claim:clm_3e6847cf3d6c9bbf4c649d944a9dc4192fd9af4415bf11f167bc31460c1fa388]
- Repository development practice: CI runs fmt, check, tests, and log/prompt guards on pushes to main and pull requests, with paths-ignore for markdown and assets so docs-only changes skip CI; clippy and a relay-check job gate separately. [@claim:clm_56f97fe51cd609896e25dea16bf5190c5fff51ebec4bce81ed86c6783a039cce]
- Repository development practice: contributors verify changes with make targets (fmt, fmt-check, check, test, app) and release scripts; `make fmt` requires the nightly toolchain, and `make check` does not run clippy, which CI checks separately. [@claim:clm_e284be4e4a9c2796e8367470f9186e6c5cd36da6e34408798415e378a16771f7]
<!-- rcw:end owner=source:src_eecb4a967e245b3aac3ff84e45e2a73f block=evidence -->

## Researcher notes

