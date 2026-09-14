---
access: public
aliases: []
claim_ids:
- clm_0fdf1a0da26b64c9ec94532109788a9e343319079875e27d7592a8169e781b48
- clm_1e8864d4bbd86577feffb3445a16134bf099a794f3e50df25b84e14cdb9ec3ee
- clm_880295c9cad60a9094632fa898cf13ae9400a6b5606405bcf54542f11b930f5f
- clm_f44e363f3102d4abd8d5b5753aee83f7259d20a01a79197f19b4b3226bd390ca
maturity: draft
page_id: pg_5cd6b43c1fc15cbd8300548990e5829f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6ce8c53ca6ac5bcdbdaaeceb67441cb2
title: penso/arbor/AGENTS.md @ d8d82b7eec6c
updated_at: '2026-09-14T02:30:09Z'
---

# penso/arbor/AGENTS.md @ d8d82b7eec6c

<!-- rcw:begin owner=source:src_6ce8c53ca6ac5bcdbdaaeceb67441cb2 block=evidence -->
- Repository development practice: the project uses bd (beads) for all issue tracking, with bd ready/claim/close commands and discovered-from dependency links instead of markdown TODOs. [@claim:clm_0fdf1a0da26b64c9ec94532109788a9e343319079875e27d7592a8169e781b48]
- Repository development practice: AGENTS.md instructs coding agents to run just format and just lint before committing, prefer just recipes, and run relevant checks for touched code before handoff. [@claim:clm_1e8864d4bbd86577feffb3445a16134bf099a794f3e50df25b84e14cdb9ec3ee]
- Repository development practice: UI changes are implemented in the native GPUI app first, then ported to the web UI to keep the two surfaces in parity, with screenshot-based verification via screencapture. [@claim:clm_880295c9cad60a9094632fa898cf13ae9400a6b5606405bcf54542f11b930f5f]
- Repository development practice: Rust rules forbid unwrap()/expect() outside tests, require SessionId/WorkspaceId newtypes, and prohibit shelling out to CLIs like gh or git for GitHub API calls in favor of Rust crates. [@claim:clm_f44e363f3102d4abd8d5b5753aee83f7259d20a01a79197f19b4b3226bd390ca]
<!-- rcw:end owner=source:src_6ce8c53ca6ac5bcdbdaaeceb67441cb2 block=evidence -->

## Researcher notes

