---
access: public
aliases: []
claim_ids:
- clm_a2b72fe6c9159f1cc7ca9e7411e9c792349829a39505fa5b21ecf28608fed28a
- clm_cc8cb60de48d7c35b4add6729d9b0720dcea386713ff74bc9e7a412dbef17bb5
- clm_ed683449e8d0df4a65abcc2b2db7d895e48f44cc2d280aca5d2a104cd53b22c6
maturity: draft
page_id: pg_7bb5ab579fe75369a3b4f5db2847fa0d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_69eb142128df5bf28646cfb47831aaa0
title: yusifeng/formax/CODEMAP.md @ 1b0c3f32eb20
updated_at: '2026-09-14T03:26:09Z'
---

# yusifeng/formax/CODEMAP.md @ 1b0c3f32eb20

<!-- rcw:begin owner=source:src_69eb142128df5bf28646cfb47831aaa0 block=evidence -->
- Permissions use a deny/ask/allow rule matcher, a policy engine with preflight enforcement before tool execution, and an approval service with user prompts and remember behavior. [@claim:clm_a2b72fe6c9159f1cc7ca9e7411e9c792349829a39505fa5b21ecf28608fed28a]
- Session save/replay is supported with writer/reader modules and durable transcript turn snapshots; session saving is enabled by default and can be disabled via `FORMAX_SESSION_SAVE`. [@claim:clm_cc8cb60de48d7c35b4add6729d9b0720dcea386713ff74bc9e7a412dbef17bb5]
- The codebase includes a hooks system (PreToolUse, PermissionRequest, PostToolUse) configured via `.formax/settings.local.json` with scripts under `.formax/hooks/*`, plus audit fields and a debug env flag. [@claim:clm_ed683449e8d0df4a65abcc2b2db7d895e48f44cc2d280aca5d2a104cd53b22c6]
<!-- rcw:end owner=source:src_69eb142128df5bf28646cfb47831aaa0 block=evidence -->

## Researcher notes

