---
access: public
aliases: []
claim_ids:
- clm_485f8162b1d4bbf33922f75f040d078a009aa660a28d3e27b7bb233ca1f5d25d
- clm_60960c24b6ca95fceb55ce8f5363c1a5d0b246ab3d32b92282057805bc4544ef
- clm_6832875b98dc3c7f7f56ee631750232b967d5c37b96ff8a9d8124b70548a6afc
- clm_7115563d46b64ac1443a5a285560fdb533c7a7bfdb7bb44c8d70f57bb3b684ac
- clm_71ec5053dd23050507e718d1c26dacf251aed7c7b425238b301936167a162d3d
- clm_90a57af4dd3d91a9c6d4a47333443478ed58a9e4f0f6d924aa8427562b10b9c5
- clm_94a436377e36420e43635f534ad3acaf4bf3b00a09a1adfcbe17a72c5dd64a86
- clm_a19f9d1e0f8877e2b2b09093a6b3658886f964ca086b0ef1add158d713dedfbb
- clm_bb6f79e4d9c91f8289f2a9648c2d5116fad29b48756e508ff1de25d2ba470cc9
- clm_c820833c60e3d0c0850000850886d1892e002915456c0d27c551ec5ff3e2aaef
- clm_da34287dd0cbc9f238109efd5f0493a44f6b577f0422070364c92302a3f888f8
- clm_e9622db9799ced98da710a8fbecb7914d1a52a287723dfad1feff114b7b2ff2f
maturity: draft
page_id: pg_e778ffe133b657fb8cc25eb388fc64b6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8033a2e78503599eaf7633a31702ceee
title: Piotr1215/pairup.nvim/README.md @ a4841094a58b
updated_at: '2026-09-14T04:16:14Z'
---

# Piotr1215/pairup.nvim/README.md @ a4841094a58b

<!-- rcw:begin owner=source:src_8033a2e78503599eaf7633a31702ceee block=evidence -->
- The plugin exposes :Pairup subcommands including start, stop, toggle, say, markers, inline, diff, lsp, suspend, accept, and peripheral variants. [@claim:clm_485f8162b1d4bbf33922f75f040d078a009aa660a28d3e27b7bb233ca1f5d25d]
- A peripheral Claude feature runs a second autonomous Claude instance in a sibling git worktree that receives diffs of spec files and implements changes independently. [@claim:clm_60960c24b6ca95fceb55ce8f5363c1a5d0b246ab3d32b92282057805bc4544ef]
- v4.0 removed the overlay system, sessions, RPC, and marker-based suggestions to focus on simple inline editing, citing less complexity and more reliability; legacy features remain on the legacy-v3 branch. [@claim:clm_6832875b98dc3c7f7f56ee631750232b967d5c37b96ff8a9d8124b70548a6afc]
- Operators gC{motion}, g!{motion}, and g?{motion} insert cc:, cc!:, and ccp: markers respectively, working with motions and text-objects; keybindings are active only when the plugin is loaded. [@claim:clm_7115563d46b64ac1443a5a285560fdb533c7a7bfdb7bb44c8d70f57bb3b684ac]
- ccp: (plan) makes Claude wrap changes in CURRENT/PROPOSED conflict markers so the user reviews and accepts or rejects before anything changes. [@claim:clm_71ec5053dd23050507e718d1c26dacf251aed7c7b425238b301936167a162d3d]
- Statusline indicators are auto-injected into lualine or the native statusline, showing states like [CL:pending], [CL:2/5], [CL:ready], and peripheral [CP] states. [@claim:clm_90a57af4dd3d91a9c6d4a47333443478ed58a9e4f0f6d924aa8427562b10b9c5]
- Users write cc:, cc!:, or ccp: markers in code and save; Claude then edits the file directly, per the README's how-it-works section. [@claim:clm_94a436377e36420e43635f534ad3acaf4bf3b00a09a1adfcbe17a72c5dd64a86]
- Todo progress is tracked via a Claude Code PostToolUse hook script that the user must copy into ~/.claude/scripts and register in settings.json. [@claim:clm_a19f9d1e0f8877e2b2b09093a6b3658886f964ca086b0ef1add158d713dedfbb]
- uu: is Claude's reply marker for clarification questions; the user answers by appending a cc: line below it. [@claim:clm_bb6f79e4d9c91f8289f2a9648c2d5116fad29b48756e508ff1de25d2ba470cc9]
- The default provider command includes Claude's --permission-mode acceptEdits flag so Claude edits files without per-change confirmation, which the docs say the inline workflow requires. [@claim:clm_c820833c60e3d0c0850000850886d1892e002915456c0d27c551ec5ff3e2aaef]
- Requirements are Neovim 0.11+ and the Claude Code CLI. [@claim:clm_da34287dd0cbc9f238109efd5f0493a44f6b577f0422070364c92302a3f888f8]
- cc!: (constitution) executes the instruction and additionally extracts the underlying rule into the project's CLAUDE.md for future work. [@claim:clm_e9622db9799ced98da710a8fbecb7914d1a52a287723dfad1feff114b7b2ff2f]
<!-- rcw:end owner=source:src_8033a2e78503599eaf7633a31702ceee block=evidence -->

## Researcher notes

