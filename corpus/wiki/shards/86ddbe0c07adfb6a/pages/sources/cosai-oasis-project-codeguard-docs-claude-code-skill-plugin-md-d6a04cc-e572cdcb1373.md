---
access: public
aliases: []
claim_ids:
- clm_10dc9805950b6b976da0fc3073627c06e84f07733e027a97ede1df3cea651541
- clm_159bc845ff0e7b1800ed47f647043e4874ff29f6202a0e0b80ab97140f75a83e
- clm_30c717e7b61016c2b6eaa07eb77151d38f5bfe984572972ab9a7a96873ac2987
- clm_4cd559c4d37f7b31d55bc60a124f4be607ba8d2d61d3660365123c91cf0b72ff
- clm_d125e13a79a4a6a65cc83d3a8653f051bcce74966508293abae3f563a98204cf
- clm_d6cd8e0597c3d2854cc1d0ae62042830afb1ddbc9c5047b4c9757796e3eb3622
- clm_f23a1d16b1d66a36951885b38e2adb4ae72d8d149ac22c9feefece6d9fabc6e9
maturity: draft
page_id: pg_ecf87921a80b58ba9d8ae572cdcb1373
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_09e4f5423c46575bbb5f1fe99a695f43
title: cosai-oasis/project-codeguard/docs/claude-code-skill-plugin.md @ d6a04cc5bfee
updated_at: '2026-09-14T03:43:13Z'
---

# cosai-oasis/project-codeguard/docs/claude-code-skill-plugin.md @ d6a04cc5bfee

<!-- rcw:begin owner=source:src_09e4f5423c46575bbb5f1fe99a695f43 block=evidence -->
- Repository development practice: contributors regenerate the plugin with 'uv run python src/convert_to_ide_formats.py', which converts sources/ rules into skills/ (core rules only) and dist/ formats. [@claim:clm_10dc9805950b6b976da0fc3073627c06e84f07733e027a97ede1df3cea651541]
- The skill follows a 3-step workflow: initial security check to identify applicable rules, code generation with secure-by-default patterns, and a security review against rule checklists. [@claim:clm_159bc845ff0e7b1800ed47f647043e4874ff29f6202a0e0b80ab97140f75a83e]
- CodeGuard ships 23 security rule files: 3 always-apply rules (hardcoded credentials, crypto algorithms, digital certificates) and 20 context-specific rules selected by language, framework, or feature. [@claim:clm_30c717e7b61016c2b6eaa07eb77151d38f5bfe984572972ab9a7a96873ac2987]
- Rules are authored in a unified markdown format under sources/ and converted into formats for popular coding agents, with release automation packaging them into downloadable ZIP files. [@claim:clm_4cd559c4d37f7b31d55bc60a124f4be607ba8d2d61d3660365123c91cf0b72ff]
- Licensing is split: rules are CC BY 4.0 and tools are Apache License 2.0. [@claim:clm_d125e13a79a4a6a65cc83d3a8653f051bcce74966508293abae3f563a98204cf]
- The Claude Code skill activates automatically when writing or reviewing code, implementing security-sensitive features, handling user input or credentials, or configuring cloud infrastructure. [@claim:clm_d6cd8e0597c3d2854cc1d0ae62042830afb1ddbc9c5047b4c9757796e3eb3622]
- Repository development practice: local plugin testing is done via 'claude --plugin-dir .' after regeneration, with /reload-plugins to pick up regenerated files in a running session. [@claim:clm_f23a1d16b1d66a36951885b38e2adb4ae72d8d149ac22c9feefece6d9fabc6e9]
<!-- rcw:end owner=source:src_09e4f5423c46575bbb5f1fe99a695f43 block=evidence -->

## Researcher notes

