---
access: public
aliases: []
claim_ids:
- clm_32ef382ea12467e64979669c4b49e9d3923e03704b47ddfd7f2c12e82ad608c3
- clm_4db274464bd36c34f3faa27a3f21083ae8508ada708359789f4c62244b442338
- clm_69566f5e26c42329412adf5da2bee2455861ae1a111f0c3a1c3789802db73670
- clm_7911bd8adf73c81b8e0a95864815a9047316ecf757607bcfe0ab936e4fb17937
- clm_907db88c7eb34dcb1278b0d9d49cd32cc541aac3cc2424fbae1dbda54ada8a86
- clm_cd7a1bf6231d79a4a7d502245a606370cbfde2e93d85bfa5efe5f906f364050c
- clm_ef944e2c12e0e9d22011b892636f1b17fc6f493a5f9bafcd7fe1474ba70090c6
- clm_f4d0ec550119d8f1b82a56bcf0230b312989bb4051a35651252247dc329247af
maturity: draft
page_id: pg_b082c59ad722538a868eb1ddc14f27a2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_57bd6ea6268855678328178e8da46cb9
title: alibaba/open-code-review/README.md @ 494bf1c8d7a1
updated_at: '2026-09-14T01:59:22Z'
---

# alibaba/open-code-review/README.md @ 494bf1c8d7a1

<!-- rcw:begin owner=source:src_57bd6ea6268855678328178e8da46cb9 block=evidence -->
- Related files are grouped into bundles, and each bundle runs as a sub-agent with isolated context, described as a divide-and-conquer strategy that stays stable on large changesets and supports concurrent review. [@claim:clm_32ef382ea12467e64979669c4b49e9d3923e03704b47ddfd7f2c12e82ad608c3]
- The product exposes an `ocr` CLI with commands including `ocr review` (workspace, --from/--to branch range, --commit), `ocr scan`, `ocr config provider/model`, `ocr session list`, and `ocr delegate`. [@claim:clm_4db274464bd36c34f3faa27a3f21083ae8508ada708359789f4c62244b442338]
- The README acknowledges lower recall than general-purpose agents, framed as a deliberate trade-off favoring precision over noise. [@claim:clm_69566f5e26c42329412adf5da2bee2455861ae1a111f0c3a1c3789802db73670]
- The core design pairs deterministic engineering (file selection, file bundling, template-based rule matching, positioning/reflection modules) with an agent for dynamic decisions and context retrieval. [@claim:clm_7911bd8adf73c81b8e0a95864815a9047316ecf757607bcfe0ab936e4fb17937]
- The README reports a benchmark built from 50 open-source repositories, 200 real PRs, and 10 languages with 1,505 annotated issues, measuring F1, precision, recall, average time, and tokens; it claims higher precision/F1 than Claude Code at ~1/9 the tokens but lower recall by design. [@claim:clm_907db88c7eb34dcb1278b0d9d49cd32cc541aac3cc2424fbae1dbda54ada8a86]
- Each review session writes to its own JSONL file with no shared state between sessions, and interrupted reviews can be resumed via `--resume <session-id>`. [@claim:clm_cd7a1bf6231d79a4a7d502245a606370cbfde2e93d85bfa5efe5f906f364050c]
- The agent has tool-use capabilities: it can read full file contents, search the codebase, and inspect other changed files for context; built-in tools include file_read and code_search. [@claim:clm_ef944e2c12e0e9d22011b892636f1b17fc6f493a5f9bafcd7fe1474ba70090c6]
- The tool requires Git >= 2.41 for diff generation, code search, and repository operations, and is distributed as an npm package `@alibaba-group/open-code-review`. [@claim:clm_f4d0ec550119d8f1b82a56bcf0230b312989bb4051a35651252247dc329247af]
<!-- rcw:end owner=source:src_57bd6ea6268855678328178e8da46cb9 block=evidence -->

## Researcher notes

