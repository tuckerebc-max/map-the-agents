---
access: public
aliases: []
claim_ids:
- clm_097d52dc731c2067688fce6326641425aee963780a6113d91f017f50460fc29b
- clm_54af29809cd6886c86c2654963fe36ffaa75e34b4d862fbcb7bdf9d231fc959c
- clm_94b1a84daf77ef3fbb376bb8c700084eb42cd3f20287f81060ee0ad603def074
- clm_976351d3841cf1ad125995382e27520cf79dcf3f83d8ece9dde30b8470177012
- clm_c0566dab291991e25532c6b552c071fd876eb1e22ab3a9b3fa70101d7287e1c1
maturity: draft
page_id: pg_ad42589d2dd657f4929b35882f6bbb9f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_367e908a67f15cbf9b8c3462e4d9ac24
title: echoVic/blade-code/docs/en/guides/memory.md @ 8917e4e0ef61
updated_at: '2026-09-14T02:00:47Z'
---

# echoVic/blade-code/docs/en/guides/memory.md @ 8917e4e0ef61

<!-- rcw:begin owner=source:src_367e908a67f15cbf9b8c3462e4d9ac24 block=evidence -->
- Auto Memory persists project knowledge across sessions: the first 200 lines of MEMORY.md are injected into the system prompt at session start, knowledge is saved via MemoryWrite, and read on demand via MemoryRead. [@claim:clm_097d52dc731c2067688fce6326641425aee963780a6113d91f017f50460fc29b]
- Full compaction extracts explicitly marked entries (remember:, convention:, lesson:, fixed:) into topic files, capped at 20 entries, 500 code points each, 8,000 total, with deduplication, in-process and file locks, atomic replacement, and 0600 permissions. [@claim:clm_54af29809cd6886c86c2654963fe36ffaa75e34b4d862fbcb7bdf9d231fc959c]
- Memory safety mechanisms include rejecting credential-like content (password, token, sk-*, AWS key IDs, PEM headers), forbidding '..' or '/' in topic names, and content-free projections so TUI/Web/ACP/Headless receive only outcome, entry count, and topic names. [@claim:clm_94b1a84daf77ef3fbb376bb8c700084eb42cd3f20287f81060ee0ad603def074]
- Memory files live under ~/.blade/projects/{escaped-path}/memory/ with per-project isolation, containing a MEMORY.md index plus topic files such as patterns.md, debugging.md, and architecture.md. [@claim:clm_976351d3841cf1ad125995382e27520cf79dcf3f83d8ece9dde30b8470177012]
- Auto Memory can be disabled with BLADE_AUTO_MEMORY=0; the documented default is enabled (BLADE_AUTO_MEMORY=1). [@claim:clm_c0566dab291991e25532c6b552c071fd876eb1e22ab3a9b3fa70101d7287e1c1]
<!-- rcw:end owner=source:src_367e908a67f15cbf9b8c3462e4d9ac24 block=evidence -->

## Researcher notes

