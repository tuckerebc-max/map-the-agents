---
access: public
aliases: []
claim_ids:
- clm_32790b7ead9a4948841858e4a3aa090513de616cf7c825c12f7e994a99e8dde0
- clm_4b77d48813e64244206c481d888475847d7b5130b866fd7c5fa9ba36891006f1
- clm_5a540c3290e1bd6954b0a094e070993e17536264b22f78f2b71e9b3608ef4c9d
- clm_8d04121bcac26cde224365e9233ca72c37ffa60e7e9ebdac20347af6a2c36cc5
maturity: draft
page_id: pg_2a6a27579af857f3ac24548ddb0450ee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a4fec1600b3e5d8ead39153aea525649
title: limecloud/lime/FEATURE-MAP.md @ 580022b574cb
updated_at: '2026-09-14T02:12:36Z'
---

# limecloud/lime/FEATURE-MAP.md @ 580022b574cb

<!-- rcw:begin owner=source:src_a4fec1600b3e5d8ead39153aea525649 block=evidence -->
- Desktop GUI business capabilities enter the Rust runtime only through App Server JSON-RPC; Electron IPC is limited to windows, file selection, system permissions, notifications, updates, native views, and sidecar lifecycle. [@claim:clm_32790b7ead9a4948841858e4a3aa090513de616cf7c825c12f7e994a99e8dde0]
- Repository development practice: minimal documentation checks are `npm run docs:boundary`, relative-link validation, and `git diff --check`, with `npm run governance:legacy-report` added when governance categories change. [@claim:clm_4b77d48813e64244206c481d888475847d7b5130b866fd7c5fa9ba36891006f1]
- FEATURE-MAP assigns ownership across crates: agent-runtime/agent for turn lifecycle and orchestration, model-provider for catalog/routing/retry, and tool-runtime for tool definitions, permissions, sandbox, dispatch, processes and MCP; the main-chain diagram lists thread-store/repository for persistence and projection. [@claim:clm_5a540c3290e1bd6954b0a094e070993e17536264b22f78f2b71e9b3608ef4c9d]
- Repository development practice: FEATURE-MAP maintenance rules require updating code and the architecture doc first, then syncing the map after owner confirmation, and readiness is judged by code, protocol, and corresponding evidence levels rather than roadmap claims or single test results. [@claim:clm_8d04121bcac26cde224365e9233ca72c37ffa60e7e9ebdac20347af6a2c36cc5]
<!-- rcw:end owner=source:src_a4fec1600b3e5d8ead39153aea525649 block=evidence -->

## Researcher notes

