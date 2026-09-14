---
access: public
aliases: []
claim_ids:
- clm_1c8b043b57ca5a887e56505d7952db69de53c1927c10b4a5e224c0946d12cd51
- clm_325c6474998977cfd0ee302e4824ee1ca1d7837b574e492a70e6b8ffed77c449
- clm_7534fb0d5e43f58e61709c4528f73172cb7da6bd32456dcbbbe0bb6e00ca247d
- clm_991f98a2b40e90c9654cb89e216e7022e85f6c567e396e913c27706fa929fe9a
maturity: draft
page_id: pg_0ddc8ef86a4b5095812391edc7dc48f0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e711b6d0fbb75022bf6121226508f73b
title: qcri/codebadger/docs/available-tools.md @ 857adcabe386
updated_at: '2026-09-14T04:17:42Z'
---

# qcri/codebadger/docs/available-tools.md @ 857adcabe386

<!-- rcw:begin owner=source:src_e711b6d0fbb75022bf6121226508f73b block=evidence -->
- The product analyzes only the CPG, not files on disk: source is discarded after the build, so there are no file-reading tools and users must grep their own checkout. [@claim:clm_1c8b043b57ca5a887e56505d7952db69de53c1927c10b4a5e224c0946d12cd51]
- Git-history reconnaissance is not a built-in tool because only the CPG is kept, not the source .git; such mining must be run in a separate checkout. [@claim:clm_325c6474998977cfd0ee302e4824ee1ca1d7837b574e492a70e6b8ffed77c449]
- Vulnerability detectors cover use-after-free, double free, null deref (CWE-476), heap/stack overflow, uninitialized reads, integer overflow, format strings, TOCTOU, and command injection. [@claim:clm_7534fb0d5e43f58e61709c4528f73172cb7da6bd32456dcbbbe0bb6e00ca247d]
- Documented tools include generate_cpg, get_cpg_status, remove_cpg, list_methods, get_call_graph, get_cfg, run_cpgql_query, find_taint_flows, get_program_slice, and get_variable_flow. [@claim:clm_991f98a2b40e90c9654cb89e216e7022e85f6c567e396e913c27706fa929fe9a]
<!-- rcw:end owner=source:src_e711b6d0fbb75022bf6121226508f73b block=evidence -->

## Researcher notes

