---
access: public
aliases: []
claim_ids:
- clm_7f6e10f32806a3784ce989681c7a0692bc83c198b2450f466e54d51a34369a72
- clm_956863e8798b597f03be73e3bd7b460f80139047798925c3b9fda64bab6c0558
- clm_a18b21d91126976578eb09bc6196cb0ed5b28be28d29c638830818e8b3ec78c2
- clm_b464f1fa2c3cfd05d47aa83b4ef7468398022a3f92de310aaf1fbf6ef944c089
- clm_b7aab3587b646437cde5f4be0b80fd71e435546d136c3a230d4cc0ce8a00f289
maturity: draft
page_id: pg_eb69201ab94d5e66a4458231ea2ff87a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b596055b6e555d60b12d4a14e30a0500
title: ZhuLinsen/MiniAgent/AGENTS.md @ 657909f0237b
updated_at: '2026-09-14T04:41:41Z'
---

# ZhuLinsen/MiniAgent/AGENTS.md @ 657909f0237b

<!-- rcw:begin owner=source:src_b596055b6e555d60b12d4a14e30a0500 block=evidence -->
- Repository development practice: tests are run with pytest (e.g. 'uv run pytest tests/ -v'), the suite reportedly covers 100+ cases, and code should follow PEP 8 with type annotations and docstrings. [@claim:clm_7f6e10f32806a3784ce989681c7a0692bc83c198b2450f466e54d51a34369a72]
- The product supports two tool-calling modes: a default text-parsing mode where the LLM emits structured text like 'TOOL: bash / ARGS: {...}', and a native OpenAI function-calling mode enabled via mode="native" that supports parallel tool calls. [@claim:clm_956863e8798b597f03be73e3bd7b460f80139047798925c3b9fda64bab6c0558]
- Repository development practice: contributors must not push directly to main; changes go through pull requests requiring at least one maintainer review, with Conventional Commits message format and tests required for core-logic changes. [@claim:clm_a18b21d91126976578eb09bc6196cb0ed5b28be28d29c638830818e8b3ec78c2]
- The product includes lightweight session memory stored at ~/.miniagent/memory.json (path configurable via MINIAGENT_HOME) and auto-compresses conversation history beyond a configurable message limit. [@claim:clm_b464f1fa2c3cfd05d47aa83b4ef7468398022a3f92de310aaf1fbf6ef944c089]
- The runtime includes a safety guard that auto-detects dangerous bash commands and requires confirmation before execution, controlled by a CONFIRM_DANGEROUS setting documented as defaulting to true. [@claim:clm_b7aab3587b646437cde5f4be0b80fd71e435546d136c3a230d4cc0ce8a00f289]
<!-- rcw:end owner=source:src_b596055b6e555d60b12d4a14e30a0500 block=evidence -->

## Researcher notes

