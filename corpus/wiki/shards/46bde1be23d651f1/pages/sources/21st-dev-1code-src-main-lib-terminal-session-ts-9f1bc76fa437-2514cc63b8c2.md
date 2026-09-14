---
access: public
aliases: []
claim_ids:
- clm_564579a9f71ccada4484d242508daab0129317e508cbb1891f4323eff056298c
- clm_c40781fb933966ef803589514c83dce6dbfe827b64c85f0fd24f227e27051828
maturity: draft
page_id: pg_5e8bfb28ca79510895092514cc63b8c2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6a0f6069381c58d099cefe29ee26b121
title: 21st-dev/1code/src/main/lib/terminal/session.ts @ 9f1bc76fa437
updated_at: '2026-09-14T01:58:36Z'
---

# 21st-dev/1code/src/main/lib/terminal/session.ts @ 9f1bc76fa437

<!-- rcw:begin owner=source:src_6a0f6069381c58d099cefe29ee26b121 block=evidence -->
- The terminal session code falls back to the user's home directory when the requested working directory does not exist or is not a directory. [@claim:clm_564579a9f71ccada4484d242508daab0129317e508cbb1891f4323eff056298c]
- The terminal session module's spawnPty function catches a failed PTY spawn and retries once using a fallback shell constant. [@claim:clm_c40781fb933966ef803589514c83dce6dbfe827b64c85f0fd24f227e27051828]
<!-- rcw:end owner=source:src_6a0f6069381c58d099cefe29ee26b121 block=evidence -->

## Researcher notes

