---
access: public
aliases: []
claim_ids:
- clm_1e1a0befdb0e4fd8a217f904ef8da3fbd1c6b7f562c9b0386e78ed353b39c0b0
- clm_880295c9cad60a9094632fa898cf13ae9400a6b5606405bcf54542f11b930f5f
- clm_f44e363f3102d4abd8d5b5753aee83f7259d20a01a79197f19b4b3226bd390ca
maturity: draft
page_id: pg_fda0a2075c0b5f5caf1f2b06e2c7a93e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4a5cdb83f286518c8a05425bcbd808ff
title: penso/arbor/CLAUDE.md @ d8d82b7eec6c
updated_at: '2026-09-14T02:30:09Z'
---

# penso/arbor/CLAUDE.md @ d8d82b7eec6c

<!-- rcw:begin owner=source:src_4a5cdb83f286518c8a05425bcbd808ff block=evidence -->
- Repository development practice: CLAUDE.md requires just format, just lint (zero warnings), and just test before committing, and forbids Co-Authored-By trailers in conventional commits. [@claim:clm_1e1a0befdb0e4fd8a217f904ef8da3fbd1c6b7f562c9b0386e78ed353b39c0b0]
- Repository development practice: UI changes are implemented in the native GPUI app first, then ported to the web UI to keep the two surfaces in parity, with screenshot-based verification via screencapture. [@claim:clm_880295c9cad60a9094632fa898cf13ae9400a6b5606405bcf54542f11b930f5f]
- Repository development practice: Rust rules forbid unwrap()/expect() outside tests, require SessionId/WorkspaceId newtypes, and prohibit shelling out to CLIs like gh or git for GitHub API calls in favor of Rust crates. [@claim:clm_f44e363f3102d4abd8d5b5753aee83f7259d20a01a79197f19b4b3226bd390ca]
<!-- rcw:end owner=source:src_4a5cdb83f286518c8a05425bcbd808ff block=evidence -->

## Researcher notes

