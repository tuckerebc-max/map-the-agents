---
access: public
aliases: []
claim_ids:
- clm_186cf25acdbeb3437e66b2eafd1c73c71344e4eab4bc446e9c7fc923b19b1c21
- clm_38802e992c323b0c3772365c82c4d3c5228e8cd06ee342b87af5f840288c35e3
- clm_a3587c5c5ca174845d6e4cafea96026f314e4869f60627c583f8ac65ba34533d
maturity: draft
page_id: pg_eb69b1e5b12e5dbfbd5df6ddf8d66251
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4a6a47553b785f45bfc693b1bed74c49
title: samholt/L2MAC/docs/guide/api.md @ 105e74afdc67
updated_at: '2026-09-14T02:39:03Z'
---

# samholt/L2MAC/docs/guide/api.md @ 105e74afdc67

<!-- rcw:begin owner=source:src_4a6a47553b785f45bfc693b1bed74c49 block=evidence -->
- The main generation API accepts parameters including prompt_task, domain ('codebase' or 'book', default 'codebase'), run_tests (default False), steps (default 10), prompt_program, prompts_file_path, tools_enabled, debugging_level, and init_config. [@claim:clm_186cf25acdbeb3437e66b2eafd1c73c71344e4eab4bc446e9c7fc923b19b1c21]
- The tools_enabled parameter controls which functions agents can use, defaulting to all available tools; for codebase generation, tools include syntax-error checking and running unit tests. [@claim:clm_38802e992c323b0c3772365c82c4d3c5228e8cd06ee342b87af5f840288c35e3]
- L2MAC offers a CLI (e.g. `l2mac "..."` creating a codebase repo in ./workspace) and a Python library API including generate_codebase and run_l2mac, plus helper functions for book and custom domains. [@claim:clm_a3587c5c5ca174845d6e4cafea96026f314e4869f60627c583f8ac65ba34533d]
<!-- rcw:end owner=source:src_4a6a47553b785f45bfc693b1bed74c49 block=evidence -->

## Researcher notes

