---
access: public
aliases: []
claim_ids:
- clm_04dc357464cf162697013fdaac23860ac035b892e0c5c079b25089fe5126fd4c
- clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7
- clm_31f0c2abfe1a9546fda7f0ef6990a5a85e035ba5b7cf48a0a62e31d829b994e6
maturity: draft
page_id: pg_d1de764334935fda93cc47f04b80ae32
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5a22b9b3ced4527194dc27e753d9ef38
title: MagicCube/helixent/docs/foundation.md @ 5cc1fb3faf29
updated_at: '2026-09-14T02:15:19Z'
---

# MagicCube/helixent/docs/foundation.md @ 5cc1fb3faf29

<!-- rcw:begin owner=source:src_5a22b9b3ced4527194dc27e753d9ef38 block=evidence -->
- The foundation layer provides three core primitives: a Model abstraction over LLM providers, a single Message transcript type, and Tool definitions with execution plumbing. [@claim:clm_04dc357464cf162697013fdaac23860ac035b892e0c5c079b25089fe5126fd4c]
- The OpenAI provider defaults to temperature 0 and top_p 0, merges caller options last, and works with any OpenAI-compatible endpoint; thinking content is dropped when converting messages to OpenAI wire format. [@claim:clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7]
- The ModelProvider contract requires invoke(params) returning Promise<AssistantMessage> and stream(params) returning an AsyncGenerator of AssistantMessage; params bundle model, messages, optional tools, provider options, and an AbortSignal. [@claim:clm_31f0c2abfe1a9546fda7f0ef6990a5a85e035ba5b7cf48a0a62e31d829b994e6]
<!-- rcw:end owner=source:src_5a22b9b3ced4527194dc27e753d9ef38 block=evidence -->

## Researcher notes

