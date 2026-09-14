---
access: public
aliases: []
claim_ids:
- clm_06c3dbf08fd8321eb9d057ad62c53946e1075cb8a3790d96fa883330c0b04f77
- clm_1161a84c8f529c80732b7fbb8a9b5d9f9d9dd5b9ea72df9919e89c954a67fe44
- clm_8a9c8c329eec4604560aef3deec7c2bc32dc58eb39f61719ce48c3ae8b499577
maturity: draft
page_id: pg_fd6155eef91d5499827cc3d2d84995cf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b92e507f47555c9b955f451bd3af95ab
title: tempont/small-opencode-orchestrator/AGENTS.md @ 8f7702cef997
updated_at: '2026-09-14T04:25:44Z'
---

# tempont/small-opencode-orchestrator/AGENTS.md @ 8f7702cef997

<!-- rcw:begin owner=source:src_b92e507f47555c9b955f451bd3af95ab block=evidence -->
- Repository development practice: AGENTS.md prescribes strict role separation (code-explorer read-only, code-executor writes without exploring, code-reviewer neither writes nor explores) and a typical delegation order from exploration through review. [@claim:clm_06c3dbf08fd8321eb9d057ad62c53946e1075cb8a3790d96fa883330c0b04f77]
- The orchestrator agent has no write permissions by default to force subagent usage, and per AGENTS.md it must not use native read, glob, grep, list, lsp, or bash tools for repo discovery, delegating to code-explorer instead. [@claim:clm_1161a84c8f529c80732b7fbb8a9b5d9f9d9dd5b9ea72df9919e89c954a67fe44]
- Repository development practice: AGENTS.md instructs contributing agents to plan before non-trivial edits, keep diffs small and reversible, verify with the narrowest sufficient command and never claim success without output, and never push without explicit user intent. [@claim:clm_8a9c8c329eec4604560aef3deec7c2bc32dc58eb39f61719ce48c3ae8b499577]
<!-- rcw:end owner=source:src_b92e507f47555c9b955f451bd3af95ab block=evidence -->

## Researcher notes

