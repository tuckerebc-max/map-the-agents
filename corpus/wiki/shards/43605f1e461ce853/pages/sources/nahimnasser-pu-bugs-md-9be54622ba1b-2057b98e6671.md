---
access: public
aliases: []
claim_ids:
- clm_0e8569c145933e4a051bdbecfc26e541704088fb667eb05bdb166e28387b44bd
- clm_55fa73644f0427cc7e9f3d1013ffed740becadadaa2e6414557abb4cc9b8194c
- clm_5b332f4c08569f771d957d3dbc900d04c5c9628cd47bf9bbbccb67c255028760
- clm_cde53d810c2aee4e4130e9f9859d932b517c2b6fce9859b2e8ab05da4765df5a
maturity: draft
page_id: pg_c6204dd7ed3b53f5bebb2057b98e6671
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_75d58b30c7d85d68ba4744aa11b9691b
title: NahimNasser/pu/bugs.md @ 9be54622ba1b
updated_at: '2026-09-14T02:22:10Z'
---

# NahimNasser/pu/bugs.md @ 9be54622ba1b

<!-- rcw:begin owner=source:src_75d58b30c7d85d68ba4744aa11b9691b block=evidence -->
- File writes and edits use mktemp temp files, preserve trailing newlines via sentinel capture, keep executable mode on edits, and edit requires a unique oldText match. [@claim:clm_0e8569c145933e4a051bdbecfc26e541704088fb667eb05bdb166e28387b44bd]
- Context budgeting is approximate bytes/chars rather than tokens, and compaction boundaries are heuristic, so transcripts can still be malformed or exceed budget after compaction. [@claim:clm_55fa73644f0427cc7e9f3d1013ffed740becadadaa2e6414557abb4cc9b8194c]
- The bash tool executes model-provided commands unsandboxed via a temp script; AGENT_CONFIRM=1 can be set to ask before each tool call. [@claim:clm_5b332f4c08569f771d957d3dbc900d04c5c9628cd47bf9bbbccb67c255028760]
- API keys are passed as curl header arguments, so on systems where process arguments are visible they can be exposed to other users during requests. [@claim:clm_cde53d810c2aee4e4130e9f9859d932b517c2b6fce9859b2e8ab05da4765df5a]
<!-- rcw:end owner=source:src_75d58b30c7d85d68ba4744aa11b9691b block=evidence -->

## Researcher notes

