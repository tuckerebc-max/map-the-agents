---
access: public
aliases: []
claim_ids:
- clm_34c3bc6abd899a6c14329edbc25af68353be686c6b0b49df0a9c775fe72b2686
- clm_6bebbfd61415de1e5ffd3c2b8c85679817ce5c32aa9a46770d4ed7966a45bcf7
maturity: draft
page_id: pg_55e391198e7556e09b84c2341414c673
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e280ebeb38dc51a09be10278604c3c79
title: minmaxflow/mini-kode/docs/llm-tool-integration.md @ 4e7f9767e5ca
updated_at: '2026-09-14T02:19:14Z'
---

# minmaxflow/mini-kode/docs/llm-tool-integration.md @ 4e7f9767e5ca

<!-- rcw:begin owner=source:src_e280ebeb38dc51a09be10278604c3c79 block=evidence -->
- The agent executor runs a loop: build context, send the request with tool descriptions to the LLM, parse text or tool calls, execute tools, feed results back, and repeat until a final response; conversation length is managed via auto-compaction. [@claim:clm_34c3bc6abd899a6c14329edbc25af68353be686c6b0b49df0a9c775fe72b2686]
- The system reads an AGENTS.md file from the project root and includes it in system prompts, providing persistent project context across sessions that users can edit. [@claim:clm_6bebbfd61415de1e5ffd3c2b8c85679817ce5c32aa9a46770d4ed7966a45bcf7]
<!-- rcw:end owner=source:src_e280ebeb38dc51a09be10278604c3c79 block=evidence -->

## Researcher notes

