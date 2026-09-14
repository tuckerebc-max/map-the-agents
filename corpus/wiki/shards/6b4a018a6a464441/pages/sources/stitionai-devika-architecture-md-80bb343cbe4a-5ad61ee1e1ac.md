---
access: public
aliases: []
claim_ids:
- clm_14bdfab44509b1b44797209d949e2219ac69d15dfa2219608fb568681b4235c9
- clm_3c9ab9f86d4953be3311393b64c74883d9e292d0b0a6f77c785a66283b291de8
maturity: draft
page_id: pg_114bcaae6a935e2290825ad61ee1e1ac
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6db95606c41d5a9ba641a3d0bd4d9ed0
title: stitionai/devika/ARCHITECTURE.md @ 80bb343cbe4a
updated_at: '2026-09-14T02:43:27Z'
---

# stitionai/devika/ARCHITECTURE.md @ 80bb343cbe4a

<!-- rcw:begin owner=source:src_6db95606c41d5a9ba641a3d0bd4d9ed0 block=evidence -->
- Devika supports multiple LLM providers including Claude, GPT-4/GPT-3, Gemini, Mistral, Groq, and self-hosted models via Ollama, with a unified LLM class abstracting provider APIs; the README recommends the Claude 3 family for optimal performance. [@claim:clm_14bdfab44509b1b44797209d949e2219ac69d15dfa2219608fb568681b4235c9]
- The Agent Core runs a loop where a user prompt goes to the Planner for a step plan, the Researcher extracts search queries, web results are formatted, and the Coder generates code saved to disk; follow-up prompts route through an Action agent to Runner, Feature, Patcher, or Reporter agents. [@claim:clm_3c9ab9f86d4953be3311393b64c74883d9e292d0b0a6f77c785a66283b291de8]
<!-- rcw:end owner=source:src_6db95606c41d5a9ba641a3d0bd4d9ed0 block=evidence -->

## Researcher notes

