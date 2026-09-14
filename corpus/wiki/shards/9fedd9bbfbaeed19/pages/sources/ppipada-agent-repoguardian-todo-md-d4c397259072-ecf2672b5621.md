---
access: public
aliases: []
claim_ids:
- clm_32904783195847554eea3af0bdce96cfcef4cdf6259f1e3d763eb76c300f1c24
- clm_427d60857dea3563f3a955f520ce8cd0ad678dba27169295a1f08123fb162e53
- clm_767123d6e0e486100e5a43431fb753f4a0c062d86455a5e551cad3dc41da1fee
- clm_a8df54aa49f5fc4ab443aebda1fa028ee6fe31206680a9181a9062f97d80b4a2
- clm_ad78299240d3b41bc7d447f7abb3cafbcbf0b692b926a7a75f996ded47ef1a19
- clm_db05f9ab590d2a02a6b0f4b65bfa5374a130fea799336797bd7a19d00cbf4cd4
- clm_e366f805ded7cb5d716e63316d2187da09a8c584a0b42e7846581307f4bb3d1b
maturity: draft
page_id: pg_26aae728316f50839a03ecf2672b5621
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07ab7e07fba25956a452dacd0f2ae696
title: ppipada/agent-repoguardian/todo.md @ d4c397259072
updated_at: '2026-09-14T04:16:18Z'
---

# ppipada/agent-repoguardian/todo.md @ d4c397259072

<!-- rcw:begin owner=source:src_07ab7e07fba25956a452dacd0f2ae696 block=evidence -->
- A code scanner component takes a scan item as input and performs an LLM-based scan, with OpenAI and Anthropic provider capability and batching marked as done. [@claim:clm_32904783195847554eea3af0bdce96cfcef4cdf6259f1e3d763eb76c300f1c24]
- The pipeline includes an LLM categorization step that assigns code to broad functional areas mapped to CWE vulnerability buckets, with unique CWE categories labeled. [@claim:clm_427d60857dea3563f3a955f520ce8cd0ad678dba27169295a1f08123fb162e53]
- The detection prompt is designed to work in a chain-of-thought manner to detect, verify, and score issues. [@claim:clm_767123d6e0e486100e5a43431fb753f4a0c062d86455a5e551cad3dc41da1fee]
- The todo records metric collection from eval runs including token metrics, while accuracy metrics and an eval report script remain unchecked. [@claim:clm_a8df54aa49f5fc4ab443aebda1fa028ee6fe31206680a9181a9062f97d80b4a2]
- A completed todo item records an eval processor that takes a view JSON as input, converts eval items into scan-specific items, and runs them across multiple eval items. [@claim:clm_ad78299240d3b41bc7d447f7abb3cafbcbf0b692b926a7a75f996ded47ef1a19]
- Completed pipeline items cover multiple eval types (simple query, batching with code-item segregation, tagged plus query, categorization) and running evals across multiple eval sets. [@claim:clm_db05f9ab590d2a02a6b0f4b65bfa5374a130fea799336797bd7a19d00cbf4cd4]
- The todo suggests an earlier 'solver' scaffolding for orchestration, prompts, and results was planned for evaluation with the OpenAI eval framework, though these items are struck through and unchecked. [@claim:clm_e366f805ded7cb5d716e63316d2187da09a8c584a0b42e7846581307f4bb3d1b]
<!-- rcw:end owner=source:src_07ab7e07fba25956a452dacd0f2ae696 block=evidence -->

## Researcher notes

