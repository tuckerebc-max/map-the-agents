---
access: public
aliases: []
claim_ids:
- clm_1bf8957122c5db5db52bd23a0d3416154f87ae22df82df1bd95d938759b3c41b
- clm_3b102fe8eeff36f54ad5676bb23d1a70c2d64747b8c9e6786e5bbd5a96fa8295
- clm_89f6e0da0c6cdbf76dd21284ed73c7529549a2c1467d25bdc56724c0812de97d
- clm_9021b31f6a2716e56028a92d3444c4426037dd3a5439242180b3ea43fd5aa884
- clm_ac3eff7f44cd12487c2e51b7b902e8c857b0e7d4b2ffc51be50b7659668fdf32
- clm_f5a8dd5955c8625c98428866b0f3c363cd47a414d854ac7ab96d1a89ed61445d
- clm_f8d18be7088dd821d582f6aee9e3a54df42f184f13ce6f9d36272c5aa065f051
maturity: draft
page_id: pg_8fc8b49368195d18a6ca5cd582a2f894
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d08230c9a04658cabe5a4047f45c353b
title: mufeedvh/code2prompt/README.md @ 66585136062c
updated_at: '2026-09-14T04:10:23Z'
---

# mufeedvh/code2prompt/README.md @ 66585136062c

<!-- rcw:begin owner=source:src_d08230c9a04658cabe5a4047f45c353b block=evidence -->
- An installable agent skill (skills/code2prompt/SKILL.md) teaches coding agents to use code2prompt for repository navigation and scoped context gathering, installable via the Skills CLI (npx skills add mufeedvh/code2prompt). [@claim:clm_1bf8957122c5db5db52bd23a0d3416154f87ae22df82df1bd95d938759b3c41b]
- Prompt generation respects .gitignore rules, supports glob-based include/exclude filtering, and uses Handlebars templates that users can customize. [@claim:clm_3b102fe8eeff36f54ad5676bb23d1a70c2d64747b8c9e6786e5bbd5a96fa8295]
- The token estimate is approximate by design: it relies on per-file counts and estimated template overhead rather than tokenizing the fully rendered prompt. [@claim:clm_89f6e0da0c6cdbf76dd21284ed73c7529549a2c1467d25bdc56724c0812de97d]
- The ecosystem comprises a Rust core library for file traversal, gitignore handling, and Git metadata; a CLI/TUI; a Python SDK with bindings to the Rust core published on PyPI; and an MCP server. [@claim:clm_9021b31f6a2716e56028a92d3444c4426037dd3a5439242180b3ea43fd5aa884]
- The skill installer adds only the skill folder and its template, possibly cloning the repository temporarily; the rest of the repository is not installed. [@claim:clm_ac3eff7f44cd12487c2e51b7b902e8c857b0e7d4b2ffc51be50b7659668fdf32]
- The tool targets LLM context preparation: generating prompts from codebases for chat models, AI agents, RAG pipelines, and MCP-based agentic workflows. [@claim:clm_f5a8dd5955c8625c98428866b0f3c363cd47a414d854ac7ab96d1a89ed61445d]
- Token counts are estimated via parallel per-file counts plus estimated template overhead; the full rendered prompt is not re-tokenized and the JSON envelope is excluded from the estimate. [@claim:clm_f8d18be7088dd821d582f6aee9e3a54df42f184f13ce6f9d36272c5aa065f051]
<!-- rcw:end owner=source:src_d08230c9a04658cabe5a4047f45c353b block=evidence -->

## Researcher notes

