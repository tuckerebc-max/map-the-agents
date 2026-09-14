---
access: public
aliases: []
claim_ids:
- clm_6d8f5f2a1c2e1548468efaadf8a5075be93afe19f1149fcf7ffebabcda387a0c
- clm_c66a49b9f4185d8862fb7d4b737c35563621dfbcf120ee9f387837ccb801fdb4
maturity: draft
page_id: pg_d7435372795e5417b357c32fcf1a07d7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_12ea332d5fa55ffea280f61060eba534
title: AizenvoltPrime/damocles/docs/hooks.md @ b8787a5e9b69
updated_at: '2026-09-14T01:30:55Z'
---

# AizenvoltPrime/damocles/docs/hooks.md @ b8787a5e9b69

<!-- rcw:begin owner=source:src_12ea332d5fa55ffea280f61060eba534 block=evidence -->
- Hook safety is bounded by workspace trust: the global ~/.damocles/hooks.json is always honored while the project-level file is honored only in a trusted workspace, and both files hot-reload on change with global running before project. [@claim:clm_6d8f5f2a1c2e1548468efaadf8a5075be93afe19f1149fcf7ffebabcda387a0c]
- Hooks let users run their own commands at session events via hooks.json; the child process receives one JSON object on stdin and replies with one on stdout, and a tool_call hook can block, force-allow, or rewrite a tool call. [@claim:clm_c66a49b9f4185d8862fb7d4b737c35563621dfbcf120ee9f387837ccb801fdb4]
<!-- rcw:end owner=source:src_12ea332d5fa55ffea280f61060eba534 block=evidence -->

## Researcher notes

