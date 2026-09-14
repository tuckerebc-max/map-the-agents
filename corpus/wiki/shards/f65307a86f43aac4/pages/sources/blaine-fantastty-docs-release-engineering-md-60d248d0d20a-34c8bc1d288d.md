---
access: public
aliases: []
claim_ids:
- clm_0bbb77d9d7e0ffb4fe9b82c8b6ca2db0c7917474edaf49515512fc9f30136d0e
- clm_5cadf8a669d9d042218472e985822f843be6decf505fc803ca33df70faa51cd4
maturity: draft
page_id: pg_1635d9389e445276963a34c8bc1d288d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_167770e863c95f56ad85a684e5f7aded
title: blaine/fantastty/docs/release-engineering.md @ 60d248d0d20a
updated_at: '2026-09-14T03:38:52Z'
---

# blaine/fantastty/docs/release-engineering.md @ 60d248d0d20a

<!-- rcw:begin owner=source:src_167770e863c95f56ad85a684e5f7aded block=evidence -->
- Repository development practice: the Build and Release workflow creates a GitHub Release only for pushed v* tags, builds, signs, notarizes, and publishes the DMG and Sparkle appcast, and tags must never be force-pushed. [@claim:clm_0bbb77d9d7e0ffb4fe9b82c8b6ca2db0c7917474edaf49515512fc9f30136d0e]
- Repository development practice: the release gate before merging to main runs xcodebuild tests, go test ./..., a Python unittest module, and git diff --check, with fast-forward merges preferred. [@claim:clm_5cadf8a669d9d042218472e985822f843be6decf505fc803ca33df70faa51cd4]
<!-- rcw:end owner=source:src_167770e863c95f56ad85a684e5f7aded block=evidence -->

## Researcher notes

