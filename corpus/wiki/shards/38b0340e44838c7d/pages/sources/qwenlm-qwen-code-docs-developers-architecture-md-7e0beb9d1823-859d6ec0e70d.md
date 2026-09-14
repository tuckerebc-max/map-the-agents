---
access: public
aliases: []
claim_ids:
- clm_08d2e35bb045bb91e815fa67d94fae91be0691738d13f973553a59e88ddd6232
- clm_254bea1c00a829fc129a389f13de362f4c10ee854fbfdd18b64958c24034b408
- clm_39be8499f6049f7de9d74a1031bfb54c3919074de076ba21029a6c507251d9ff
- clm_ba678e712368f880bc4037da02af772d1e5c5aab114626cc48b30580e2e968fd
maturity: draft
page_id: pg_634748430d17599c8ec5859d6ec0e70d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d7eeff27735e54acaabd783ed77d565f
title: QwenLM/qwen-code/docs/developers/architecture.md @ 7e0beb9d1823
updated_at: '2026-09-14T02:34:00Z'
---

# QwenLM/qwen-code/docs/developers/architecture.md @ 7e0beb9d1823

<!-- rcw:begin owner=source:src_d7eeff27735e54acaabd783ed77d565f block=evidence -->
- In daemon mode with multi-workspace sessions, each live workspace runtime owns its own bridge and `qwen --acp` child, with filesystem access, environment overlays, MCP transports, and sessions scoped to that runtime. [@claim:clm_08d2e35bb045bb91e815fa67d94fae91be0691738d13f973553a59e88ddd6232]
- The product offers multiple invocation surfaces: an interactive `qwen` TUI started in a project directory, headless `qwen -p "..."` for scripts/CI, and an experimental `qwen serve` daemon exposing HTTP + SSE (ACP). [@claim:clm_254bea1c00a829fc129a389f13de362f4c10ee854fbfdd18b64958c24034b408]
- The core runtime owns the agent loop — model requests, conversation context, tool dispatch, permission policy — while display and transport decisions are deliberately kept in the CLI, bridge, SDK, and UI layers. [@claim:clm_39be8499f6049f7de9d74a1031bfb54c3919074de076ba21029a6c507251d9ff]
- Key monorepo packages: `packages/cli` (executable, arg parsing, Ink TUI, headless output, ACP entry, `qwen serve`), `packages/core` (agent orchestration, tools, permissions, sessions, memory), and `packages/acp-bridge` (ACP channel lifecycle, session multiplexing, permission mediation). [@claim:clm_ba678e712368f880bc4037da02af772d1e5c5aab114626cc48b30580e2e968fd]
<!-- rcw:end owner=source:src_d7eeff27735e54acaabd783ed77d565f block=evidence -->

## Researcher notes

