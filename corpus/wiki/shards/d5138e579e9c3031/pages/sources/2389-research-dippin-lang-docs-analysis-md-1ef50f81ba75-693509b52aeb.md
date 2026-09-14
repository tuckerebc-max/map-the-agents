---
access: public
aliases: []
claim_ids:
- clm_4274e78171743da678b3d32640846ea07df07c051046342ff395ddcfcd5c66bd
- clm_e86cc8898161ba8baa81915ac9ea64c2167326920c745401a0c4603f641eb977
maturity: draft
page_id: pg_491fd15e447d54d69f54693509b52aeb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2c853a7f62e95b2d812d91a82f1b7742
title: 2389-research/dippin-lang/docs/analysis.md @ 1ef50f81ba75
updated_at: '2026-09-14T01:26:01Z'
---

# 2389-research/dippin-lang/docs/analysis.md @ 1ef50f81ba75

<!-- rcw:begin owner=source:src_2c853a7f62e95b2d812d91a82f1b7742 block=evidence -->
- Core packages claim zero external dependencies; the LSP server uses go.lsp.dev libraries, watch uses fsnotify, and coverage's shell parsing uses mvdan.cc/sh/v3/syntax. Go 1.21+ is required to build. [@claim:clm_4274e78171743da678b3d32640846ea07df07c051046342ff395ddcfcd5c66bd]
- The cost command does not cross-reference parsed budget ceilings such as max_cost_cents, so no warning is emitted when estimated cost exceeds the budget. [@claim:clm_e86cc8898161ba8baa81915ac9ea64c2167326920c745401a0c4603f641eb977]
<!-- rcw:end owner=source:src_2c853a7f62e95b2d812d91a82f1b7742 block=evidence -->

## Researcher notes

