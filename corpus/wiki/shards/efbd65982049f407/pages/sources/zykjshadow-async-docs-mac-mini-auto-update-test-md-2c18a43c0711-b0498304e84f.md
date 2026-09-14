---
access: public
aliases: []
claim_ids:
- clm_151fecd3080948373995600bdc6cb29b510fa7a749b800a779195f456ede6f6d
- clm_d6d93e4f6ef214281b5521151b52e4b76f813957151e99a791a8c7898c698ea6
maturity: draft
page_id: pg_71debf19ea285ff6a5f2b0498304e84f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d094b6d9b2e5055bf7786290f3aeff3
title: ZYKJShadow/Async/docs/mac-mini-auto-update-test.md @ 2c18a43c0711
updated_at: '2026-09-14T03:28:21Z'
---

# ZYKJShadow/Async/docs/mac-mini-auto-update-test.md @ 2c18a43c0711

<!-- rcw:begin owner=source:src_2d094b6d9b2e5055bf7786290f3aeff3 block=evidence -->
- Repository development practice: the repo can be run with npm install then npm run desktop, with dev, dev:debug, and icons scripts; the macOS test guide documents building unsigned packages via npm run release:mac:unsigned. [@claim:clm_151fecd3080948373995600bdc6cb29b510fa7a749b800a779195f456ede6f6d]
- The macOS build is unsigned, so electron-updater cannot auto-install updates; the app instead downloads the ZIP to ~/Downloads and prompts manual installation, while Windows builds auto-install. [@claim:clm_d6d93e4f6ef214281b5521151b52e4b76f813957151e99a791a8c7898c698ea6]
<!-- rcw:end owner=source:src_2d094b6d9b2e5055bf7786290f3aeff3 block=evidence -->

## Researcher notes

