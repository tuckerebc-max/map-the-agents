---
access: public
aliases: []
claim_ids:
- clm_0bbb77d9d7e0ffb4fe9b82c8b6ca2db0c7917474edaf49515512fc9f30136d0e
- clm_6e3a2f73c2820e75141dfc39fda3392c9751034145bfdc213f750c8029c80070
maturity: draft
page_id: pg_acebead3cd0250029d4fe22298926aca
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6c7ec9d78aa35426add8b3acf69bfe32
title: blaine/fantastty/doc/GITHUB_ACTIONS_SETUP.md @ 60d248d0d20a
updated_at: '2026-09-14T03:38:52Z'
---

# blaine/fantastty/doc/GITHUB_ACTIONS_SETUP.md @ 60d248d0d20a

<!-- rcw:begin owner=source:src_6c7ec9d78aa35426add8b3acf69bfe32 block=evidence -->
- Repository development practice: the Build and Release workflow creates a GitHub Release only for pushed v* tags, builds, signs, notarizes, and publishes the DMG and Sparkle appcast, and tags must never be force-pushed. [@claim:clm_0bbb77d9d7e0ffb4fe9b82c8b6ca2db0c7917474edaf49515512fc9f30136d0e]
- Repository development practice: CI requires seven GitHub secrets, including a Sparkle EdDSA private key whose matching public key is committed in Info.plist as SUPublicEDKey. [@claim:clm_6e3a2f73c2820e75141dfc39fda3392c9751034145bfdc213f750c8029c80070]
<!-- rcw:end owner=source:src_6c7ec9d78aa35426add8b3acf69bfe32 block=evidence -->

## Researcher notes

