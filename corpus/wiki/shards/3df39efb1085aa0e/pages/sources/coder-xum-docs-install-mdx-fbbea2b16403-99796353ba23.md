---
access: public
aliases: []
claim_ids:
- clm_3e69f344286be336ffe7f8c428e1cda6aa1beee7adcc15aa88992ad6ef6ac4c1
- clm_e1015f08e7883bc2517b0f2d8b775ac0aeeba453268062488b79d5fc275a1817
- clm_ede2b000b3899b1ef050a5e4526d80d4c18de1bc3ee4549498eb6d257d0ccfbc
maturity: draft
page_id: pg_e213c21eb4b7589092f199796353ba23
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a0fbf653b13452be8a1581109ea7d98a
title: coder/xum/docs/install.mdx @ fbbea2b16403
updated_at: '2026-09-14T03:41:45Z'
---

# coder/xum/docs/install.mdx @ fbbea2b16403

<!-- rcw:begin owner=source:src_a0fbf653b13452be8a1581109ea7d98a block=evidence -->
- A CLI is available via npm: `npx @coder/xum run "..."` runs agent tasks and `npx @coder/xum server --port 3000` starts a server for remote/mobile access; the legacy `mux` package forwards to Xum during the rename transition. [@claim:clm_3e69f344286be336ffe7f8c428e1cda6aa1beee7adcc15aa88992ad6ef6ac4c1]
- Release distribution includes signed/notarized macOS DMGs (separate Intel and Apple Silicon builds), a Linux AppImage, and a Windows installer exe; only main-branch builds are signed, so PR builds need Gatekeeper bypass on macOS. [@claim:clm_e1015f08e7883bc2517b0f2d8b775ac0aeeba453268062488b79d5fc275a1817]
- Windows support is in alpha, requires Git for Windows (WSL is explicitly not supported), and tool hooks are documented as experimental with expected breaking changes. [@claim:clm_ede2b000b3899b1ef050a5e4526d80d4c18de1bc3ee4549498eb6d257d0ccfbc]
<!-- rcw:end owner=source:src_a0fbf653b13452be8a1581109ea7d98a block=evidence -->

## Researcher notes

