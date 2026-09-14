---
access: public
aliases: []
claim_ids:
- clm_85429c59af7c20ec475ff145d3a4b3d1507942d7120fa382cf5d5aeca9af38b7
- clm_bddcabe4e1e06c7aa3522a1051b41015d54d265af12f37239c4b6539661b75a0
- clm_e31ee75fc39008345d739c17892878e761989d34c69e1a7fcea72c8c6e33cbdf
- clm_f94f33ccd8cd547116554f21493e51889dbddd8d125e76d37f2cf78aba797c3c
maturity: draft
page_id: pg_f38db79ef6d55a7b8c5463e12717b2f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c4513fc2028d58c281f20900f262d2d0
title: codefox-lab/CodeFox-CLI/WIKI.md @ 7b5f855fb6b5
updated_at: '2026-09-14T03:41:04Z'
---

# codefox-lab/CodeFox-CLI/WIKI.md @ 7b5f855fb6b5

<!-- rcw:begin owner=source:src_c4513fc2028d58c281f20900f262d2d0 block=evidence -->
- Analysis rule categories cover security (vulnerabilities, secret leaks), performance, and style, toggleable in the ruler config section. [@claim:clm_85429c59af7c20ec475ff145d3a4b3d1507942d7120fa382cf5d5aeca9af38b7]
- Supported providers are Gemini (default), Ollama for local/remote servers, and OpenRouter; Ollama allows fully local reviews. [@claim:clm_bddcabe4e1e06c7aa3522a1051b41015d54d265af12f37239c4b6539661b75a0]
- The system prompt can be fully overridden via prompt.system, and prompt options include hard_mode, short_mode, and strict_facts. [@claim:clm_e31ee75fc39008345d739c17892878e761989d34c69e1a7fcea72c8c6e33cbdf]
- RAG-based context retrieval is configurable: chunk size, overlap, max RAG characters, embedding batch size, and lazy loading, with fastembed embedding defaulting to BAAI/bge-small-en-v1.5. [@claim:clm_f94f33ccd8cd547116554f21493e51889dbddd8d125e76d37f2cf78aba797c3c]
<!-- rcw:end owner=source:src_c4513fc2028d58c281f20900f262d2d0 block=evidence -->

## Researcher notes

