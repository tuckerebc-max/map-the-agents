---
access: public
aliases: []
claim_ids:
- clm_67ad10e89a7923ace210d22446d9c69172612e9134c448dc7edb3e470feee622
- clm_725048b93485263b33e8782ef66faa3d0c29a58d759f2a96f66ebf83751589c7
- clm_8d71fa897e9d0d658adea3b0dd229a2e0f56c543ca155465065327095becd55c
- clm_964871baad4c438d10f588df9ac25162e45c57e7ad330dbede75e17c51868bd3
- clm_c6a2d9d2b1788e90147936eebd885332bc0b7a292aa5d66e87d8dd8d5cecb631
maturity: draft
page_id: pg_14979b66cb795002a7ed0bb5991692f9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ccf55178811f5c3d983967135e21c3bd
title: marcusschiesser/edge-pi/architecture.md @ c4b694c4abb1
updated_at: '2026-09-14T02:16:18Z'
---

# marcusschiesser/edge-pi/architecture.md @ c4b694c4abb1

<!-- rcw:begin owner=source:src_ccf55178811f5c3d983967135e21c3bd block=evidence -->
- The edge-pi-cli package handles CLI args and modes, a model factory, auth storage/OAuth, and settings, skills, prompts, and context. [@claim:clm_67ad10e89a7923ace210d22446d9c69172612e9134c448dc7edb3e470feee622]
- The runtime abstraction connects tools to a local filesystem/shell environment, with optional WebContainer and Vercel Sandbox execution environments. [@claim:clm_725048b93485263b33e8782ef66faa3d0c29a58d759f2a96f66ebf83751589c7]
- The edge-pi core package contains CodingAgent, Tool Factory with tools, SessionManager, Compaction, and a runtime abstraction, per the architecture diagram. [@claim:clm_8d71fa897e9d0d658adea3b0dd229a2e0f56c543ca155465065327095becd55c]
- The architecture diagram lists external provider integrations: Anthropic SDK, OpenAI SDK, Google SDK, a GitHub Copilot endpoint, and the Vercel AI SDK ToolLoopAgent. [@claim:clm_964871baad4c438d10f588df9ac25162e45c57e7ad330dbede75e17c51868bd3]
- Sessions are persisted as JSONL files, and a changelog entry says SessionManager is integrated with CodingAgent so history is auto-restored and persisted during generate() and stream(). [@claim:clm_c6a2d9d2b1788e90147936eebd885332bc0b7a292aa5d66e87d8dd8d5cecb631]
<!-- rcw:end owner=source:src_ccf55178811f5c3d983967135e21c3bd block=evidence -->

## Researcher notes

