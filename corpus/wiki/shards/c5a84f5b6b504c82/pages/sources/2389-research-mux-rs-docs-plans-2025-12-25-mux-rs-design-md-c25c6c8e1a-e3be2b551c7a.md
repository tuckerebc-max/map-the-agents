---
access: public
aliases: []
claim_ids:
- clm_38c90e7fd5f690ddaa369fbddcc36a4eaf01f1ac52a4a715c60debcededc9466
- clm_6dfb632b798e53105c946cfc1ca7c8da04eb3373a557d80dafc78727f25c630f
- clm_b5c9a133cda55566609c70ef9b7cba45a22518933f3f6e2267cde60e812d27f7
- clm_b6f7d2b7c65052d89c6ae52db5792aa8d750fc1abd4288f25120448ecd383697
maturity: draft
page_id: pg_79edcbf128ba5049a9b3e3be2b551c7a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_33303493fc5f5f178642db7545656c50
title: 2389-research/mux-rs/docs/plans/2025-12-25-mux-rs-design.md @ c25c6c8e1acb
updated_at: '2026-09-14T01:28:13Z'
---

# 2389-research/mux-rs/docs/plans/2025-12-25-mux-rs-design.md @ c25c6c8e1acb

<!-- rcw:begin owner=source:src_33303493fc5f5f178642db7545656c50 block=evidence -->
- The planned LlmClient trait exposes async create_message returning a Response, and create_message_stream returning a pinned Stream of StreamEvent items (MessageStart, ContentBlockStart/Delta/Stop, MessageDelta, MessageStop). [@claim:clm_38c90e7fd5f690ddaa369fbddcc36a4eaf01f1ac52a4a715c60debcededc9466]
- The planned crate layout includes llm (types, client trait, anthropic, openai), tool (trait, registry, result), permission (policy, handler), mcp (types, client, proxy), an error module, and a mux-derive crate providing a #[derive(Tool)] proc macro. [@claim:clm_6dfb632b798e53105c946cfc1ca7c8da04eb3373a557d80dafc78727f25c630f]
- Planned core dependencies are tokio (full features), serde with derive, serde_json, thiserror 2, anyhow, async-trait, reqwest 0.12 with json and stream features, futures 0.3, and glob 0.3, with tokio-test as a dev dependency. [@claim:clm_b5c9a133cda55566609c70ef9b7cba45a22518933f3f6e2267cde60e812d27f7]
- The design doc records choices including a derive macro plus trait for tool definition, Tokio as async runtime, thiserror plus anyhow for errors, a policy engine for permissions, client-only MCP scope, and multi-provider LLM support (Anthropic and OpenAI). [@claim:clm_b6f7d2b7c65052d89c6ae52db5792aa8d750fc1abd4288f25120448ecd383697]
<!-- rcw:end owner=source:src_33303493fc5f5f178642db7545656c50 block=evidence -->

## Researcher notes

