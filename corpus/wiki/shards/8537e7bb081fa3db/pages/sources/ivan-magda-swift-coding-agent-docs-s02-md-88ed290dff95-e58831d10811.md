---
access: public
aliases: []
claim_ids:
- clm_0e977347b396a584775b1845f3bdd2f7bf5e5a3c6a5f7c39262396efd8a83e6f
- clm_15612b25f88a32f89245cdbcc3f944aff628a6f7662223c8638da6631f2ca647
maturity: draft
page_id: pg_7cf2423c5d8652988615e58831d10811
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dc57c4eef518526f9c95b45cf7b3132c
title: ivan-magda/swift-coding-agent/docs/s02.md @ 88ed290dff95
updated_at: '2026-09-14T02:06:02Z'
---

# ivan-magda/swift-coding-agent/docs/s02.md @ 88ed290dff95

<!-- rcw:begin owner=source:src_dc57c4eef518526f9c95b45cf7b3132c block=evidence -->
- Tool dispatch is a dictionary mapping tool names to handlers (bash, read_file, write_file, edit_file), returning an unknownTool failure for unregistered names, chosen over a protocol registry for its simplicity. [@claim:clm_0e977347b396a584775b1845f3bdd2f7bf5e5a3c6a5f7c39262396efd8a83e6f]
- File tools enforce path sandboxing: paths are resolved against the working directory and any resolved location that escapes it is rejected with an executionFailed error. [@claim:clm_15612b25f88a32f89245cdbcc3f944aff628a6f7662223c8638da6631f2ca647]
<!-- rcw:end owner=source:src_dc57c4eef518526f9c95b45cf7b3132c block=evidence -->

## Researcher notes

