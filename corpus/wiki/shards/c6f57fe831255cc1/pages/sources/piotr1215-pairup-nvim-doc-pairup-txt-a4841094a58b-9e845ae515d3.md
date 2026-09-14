---
access: public
aliases: []
claim_ids:
- clm_485f8162b1d4bbf33922f75f040d078a009aa660a28d3e27b7bb233ca1f5d25d
- clm_6832875b98dc3c7f7f56ee631750232b967d5c37b96ff8a9d8124b70548a6afc
- clm_71ec5053dd23050507e718d1c26dacf251aed7c7b425238b301936167a162d3d
- clm_94a436377e36420e43635f534ad3acaf4bf3b00a09a1adfcbe17a72c5dd64a86
- clm_bb6f79e4d9c91f8289f2a9648c2d5116fad29b48756e508ff1de25d2ba470cc9
- clm_e9622db9799ced98da710a8fbecb7914d1a52a287723dfad1feff114b7b2ff2f
maturity: draft
page_id: pg_10dc851381ec5b7889ac9e845ae515d3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ecf9e0917857550883b157361a815f36
title: Piotr1215/pairup.nvim/doc/pairup.txt @ a4841094a58b
updated_at: '2026-09-14T04:16:14Z'
---

# Piotr1215/pairup.nvim/doc/pairup.txt @ a4841094a58b

<!-- rcw:begin owner=source:src_ecf9e0917857550883b157361a815f36 block=evidence -->
- The plugin exposes :Pairup subcommands including start, stop, toggle, say, markers, inline, diff, lsp, suspend, accept, and peripheral variants. [@claim:clm_485f8162b1d4bbf33922f75f040d078a009aa660a28d3e27b7bb233ca1f5d25d]
- v4.0 removed the overlay system, sessions, RPC, and marker-based suggestions to focus on simple inline editing, citing less complexity and more reliability; legacy features remain on the legacy-v3 branch. [@claim:clm_6832875b98dc3c7f7f56ee631750232b967d5c37b96ff8a9d8124b70548a6afc]
- ccp: (plan) makes Claude wrap changes in CURRENT/PROPOSED conflict markers so the user reviews and accepts or rejects before anything changes. [@claim:clm_71ec5053dd23050507e718d1c26dacf251aed7c7b425238b301936167a162d3d]
- Users write cc:, cc!:, or ccp: markers in code and save; Claude then edits the file directly, per the README's how-it-works section. [@claim:clm_94a436377e36420e43635f534ad3acaf4bf3b00a09a1adfcbe17a72c5dd64a86]
- uu: is Claude's reply marker for clarification questions; the user answers by appending a cc: line below it. [@claim:clm_bb6f79e4d9c91f8289f2a9648c2d5116fad29b48756e508ff1de25d2ba470cc9]
- cc!: (constitution) executes the instruction and additionally extracts the underlying rule into the project's CLAUDE.md for future work. [@claim:clm_e9622db9799ced98da710a8fbecb7914d1a52a287723dfad1feff114b7b2ff2f]
<!-- rcw:end owner=source:src_ecf9e0917857550883b157361a815f36 block=evidence -->

## Researcher notes

