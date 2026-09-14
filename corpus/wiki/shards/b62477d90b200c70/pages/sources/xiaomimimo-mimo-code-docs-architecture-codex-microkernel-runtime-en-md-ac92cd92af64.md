---
access: public
aliases: []
claim_ids:
- clm_2990f3cc22d78682a10f6967c7ffc961156bfc83574fed19cc0fb69812d369c9
- clm_5f7e36ab93631df2b87a88ce376a949ffe84becb0522f1b166b26b0caff321cb
maturity: draft
page_id: pg_a36ec0092726553fbacfac92cd92af64
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6b019d2dcaa65e8b94675c5a2066b0e4
title: XiaomiMiMo/MiMo-Code/docs/architecture/codex-microkernel-runtime.en.md @ 6fbb1732232c
updated_at: '2026-09-14T03:25:17Z'
---

# XiaomiMiMo/MiMo-Code/docs/architecture/codex-microkernel-runtime.en.md @ 6fbb1732232c

<!-- rcw:begin owner=source:src_6b019d2dcaa65e8b94675c5a2066b0e4 block=evidence -->
- For GPT/Codex models, a smaller tool ABI (bash, apply_patch, view_image, exec) is exposed; exec composes host tools inside QuickJS while permissions and side effects remain under host control. [@claim:clm_2990f3cc22d78682a10f6967c7ffc961156bfc83574fed19cc0fb69812d369c9]
- The GPT profile is enabled when the model ID contains 'gpt-' (excluding 'oss' and 'gpt-4') and hides overlapping read/write/edit/grep/glob tools; prompt routing and tool profiles use separate string rules not yet unified. [@claim:clm_5f7e36ab93631df2b87a88ce376a949ffe84becb0522f1b166b26b0caff321cb]
<!-- rcw:end owner=source:src_6b019d2dcaa65e8b94675c5a2066b0e4 block=evidence -->

## Researcher notes

