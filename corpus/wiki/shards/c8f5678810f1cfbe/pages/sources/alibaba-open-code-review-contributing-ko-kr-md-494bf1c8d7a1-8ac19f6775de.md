---
access: public
aliases: []
claim_ids:
- clm_afe52be53242a691c9958a7c95729c1cc094e4ea2ff2b8a45e2b42147c40f3e8
- clm_b4cca94010c68f4a00f99b87b5a5728f695746469b1192ce87afe3d94729b8f9
- clm_ef944e2c12e0e9d22011b892636f1b17fc6f493a5f9bafcd7fe1474ba70090c6
maturity: draft
page_id: pg_b051cbee70bb59e8a70f8ac19f6775de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_61dab23f00e656758dd0ba176e7f9969
title: alibaba/open-code-review/CONTRIBUTING.ko-KR.md @ 494bf1c8d7a1
updated_at: '2026-09-14T01:59:22Z'
---

# alibaba/open-code-review/CONTRIBUTING.ko-KR.md @ 494bf1c8d7a1

<!-- rcw:begin owner=source:src_61dab23f00e656758dd0ba176e7f9969 block=evidence -->
- Repository development practice: AI-assisted contributions must be disclosed early, contributors must understand and be able to explain all AI-generated code, AI/LLM may only be used for translation or prose polishing of replies, and 'Assisted-by'/'Co-developed-by' trailers are prohibited. [@claim:clm_afe52be53242a691c9958a7c95729c1cc094e4ea2ff2b8a45e2b42147c40f3e8]
- The repository layout includes cmd/opencodereview (CLI entry), internal packages for agent, config, diff parsing, LLM clients (Anthropic & OpenAI), session, tool, telemetry (OpenTelemetry), and viewer, plus a pages/ WebUI frontend. [@claim:clm_b4cca94010c68f4a00f99b87b5a5728f695746469b1192ce87afe3d94729b8f9]
- The agent has tool-use capabilities: it can read full file contents, search the codebase, and inspect other changed files for context; built-in tools include file_read and code_search. [@claim:clm_ef944e2c12e0e9d22011b892636f1b17fc6f493a5f9bafcd7fe1474ba70090c6]
<!-- rcw:end owner=source:src_61dab23f00e656758dd0ba176e7f9969 block=evidence -->

## Researcher notes

