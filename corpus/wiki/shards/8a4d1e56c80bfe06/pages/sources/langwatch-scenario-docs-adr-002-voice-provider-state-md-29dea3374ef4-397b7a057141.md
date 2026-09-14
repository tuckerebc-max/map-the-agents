---
access: public
aliases: []
claim_ids:
- clm_c70d919d7bd61b458207f87e2c464837cc45b4884c07431f2f7ea130ec6da592
maturity: draft
page_id: pg_a0989c86058e5dadb12f397b7a057141
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_145e81dac7af546485786655633054d8
title: langwatch/scenario/docs/adr/002-voice-provider-state.md @ 29dea3374ef4
updated_at: '2026-09-14T04:04:57Z'
---

# langwatch/scenario/docs/adr/002-voice-provider-state.md @ 29dea3374ef4

<!-- rcw:begin owner=source:src_145e81dac7af546485786655633054d8 block=evidence -->
- A proposed ADR moves voice STT/TTS provider state from module-global singletons to per-run ScenarioConfig.voice, because global provider state is unsafe under concurrent runs; Python still carries the global-state design. [@claim:clm_c70d919d7bd61b458207f87e2c464837cc45b4884c07431f2f7ea130ec6da592]
<!-- rcw:end owner=source:src_145e81dac7af546485786655633054d8 block=evidence -->

## Researcher notes

