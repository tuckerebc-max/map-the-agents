---
access: public
aliases: []
claim_ids:
- clm_2c82003ce49b23f6366e4681e44d956d4f7cb458fb3a42794ac4136cd4a5552e
- clm_57ead4dc81d871de9a1e2cf9dbcc24185bc051cb6e7e89c358afbba0cadde00c
- clm_6fb693d884be52eee3ce297bea6b3584daf52afd51e0b2d80cd3f5ca24f59a13
- clm_8106f3f7d1aa05bfe6eeb45687d4276555a62357f1c77e234446b7a7396af8bb
- clm_f1c311867b3ff7b31ba4ff761d3eab2c604fe495983e7f50d6bc652d458e2c8d
- clm_f30bb1b43f25a89c9ad640a215ea61b91bbc1d6f3bb3ae0a26fc687b207e219d
- clm_f3a927b48065f242a51d9df4aab26026dbc0865d513aef6fa60dca2b496f250c
maturity: draft
page_id: pg_05fe278f7c85526db7b49bb7a352f2f1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_88239ff17cc05d9e9f31136e54f74da6
title: XCodingLab/XCoding/docs/theme-packs.md @ 349a05eeb1e8
updated_at: '2026-09-14T03:23:46Z'
---

# XCodingLab/XCoding/docs/theme-packs.md @ 349a05eeb1e8

<!-- rcw:begin owner=source:src_88239ff17cc05d9e9f31136e54f74da6 block=evidence -->
- Deleting a theme folder causes the app to fall back to builtin-classic without a blank screen, suggesting built-in fallback handling for missing themes. [@claim:clm_2c82003ce49b23f6366e4681e44d956d4f7cb458fb3a42794ac4136cd4a5552e]
- Theme CSS is sandboxed: only relative paths inside the theme folder are allowed; remote/unsafe URLs are ignored and @import is stripped to block external resource loading. [@claim:clm_57ead4dc81d871de9a1e2cf9dbcc24185bc051cb6e7e89c358afbba0cadde00c]
- Settings supports importing .zip theme packs, prompting to replace existing themes with the same id; both single-top-level-directory and root-level theme.json zip layouts are accepted. [@claim:clm_6fb693d884be52eee3ce297bea6b3584daf52afd51e0b2d80cd3f5ca24f59a13]
- A theme pack must contain theme.json following VS Code Color Theme JSON structure (name/type/colors/tokenColors), with optional theme.css and assets/. [@claim:clm_8106f3f7d1aa05bfe6eeb45687d4276555a62357f1c77e234446b7a7396af8bb]
- Theme packs are folders placed in userData/themes/ that appear in Settings for selection; Settings offers an 'Open Themes Folder' action. [@claim:clm_f1c311867b3ff7b31ba4ff761d3eab2c604fe495983e7f50d6bc652d458e2c8d]
- Theme color keys map to --vscode-* CSS variables; a non-standard 'css' field can load extra CSS, and 'cssVars' supplies additional non-VSCode variables. [@claim:clm_f30bb1b43f25a89c9ad640a215ea61b91bbc1d6f3bb3ae0a26fc687b207e219d]
- XCoding ships a non-deletable default theme pack 'builtin-classic' (auto-recreated if missing) and writes an editable 'builtin-dark' (Aurora Dark) pack on first initialization. [@claim:clm_f3a927b48065f242a51d9df4aab26026dbc0865d513aef6fa60dca2b496f250c]
<!-- rcw:end owner=source:src_88239ff17cc05d9e9f31136e54f74da6 block=evidence -->

## Researcher notes

