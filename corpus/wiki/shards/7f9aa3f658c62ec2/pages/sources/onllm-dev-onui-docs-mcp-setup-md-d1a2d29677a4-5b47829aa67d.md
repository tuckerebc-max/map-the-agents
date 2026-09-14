---
access: public
aliases: []
claim_ids:
- clm_0a6cdbcd4247e87899182199c11af1f69428675c9f61a12bcd6317259577f95a
- clm_225e4bbd78c8649ca64eed9b8a3d919b76d49cd7fc23ad50541212e38c6c4baf
- clm_7417f873c6180d1cb2ed9b5b5e9a0c9146fb0d0338b442f30a70cef61ab41dd6
- clm_b078dcab1d17214f58df8e8bf2fd5b882b441175fa19dabb4f67a830194f54a2
maturity: draft
page_id: pg_b859f8d9307e57248c5c5b47829aa67d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a3e1d54b23c2580ab58d61d65e2b1889
title: onllm-dev/onUI/docs/mcp-setup.md @ d1a2d29677a4
updated_at: '2026-09-14T04:14:12Z'
---

# onllm-dev/onUI/docs/mcp-setup.md @ d1a2d29677a4

<!-- rcw:begin owner=source:src_a3e1d54b23c2580ab58d61d65e2b1889 block=evidence -->
- The extension offers two capture flows: Annotate mode for element-level targeting (with Shift multi-select) and Draw mode for rectangle/ellipse region annotations. [@claim:clm_0a6cdbcd4247e87899182199c11af1f69428675c9f61a12bcd6317259577f95a]
- The local MCP server exposes eight tools: onui_list_pages, onui_get_annotations, onui_get_report, onui_search_annotations, onui_update_annotation_metadata, onui_bulk_update_annotation_metadata, onui_delete_annotation, and onui_clear_page_annotations. [@claim:clm_225e4bbd78c8649ca64eed9b8a3d919b76d49cd7fc23ad50541212e38c6c4baf]
- Exports come in four output levels (compact, standard, detailed, forensic); region annotations include shape and geometry fields in report output at detailed and forensic levels. [@claim:clm_7417f873c6180d1cb2ed9b5b5e9a0c9146fb0d0338b442f30a70cef61ab41dd6]
- The MCP server is registered as 'onui-local' and runs via node on the onui-cli.js entrypoint; setup auto-registers it for Claude Code and Codex when those CLIs are installed. [@claim:clm_b078dcab1d17214f58df8e8bf2fd5b882b441175fa19dabb4f67a830194f54a2]
<!-- rcw:end owner=source:src_a3e1d54b23c2580ab58d61d65e2b1889 block=evidence -->

## Researcher notes

