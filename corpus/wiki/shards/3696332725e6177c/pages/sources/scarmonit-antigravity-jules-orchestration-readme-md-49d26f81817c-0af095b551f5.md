---
access: public
aliases: []
claim_ids:
- clm_1cdd45190120cbf2a3ff4d6309cc88e94372128423b30d05ce24329b933e7494
- clm_6c4e7be1ee8e97ba0af7c29c1c2940c46b423b5c77ed5ea5eea071e22859f435
- clm_715fb9ad1edf43c0d8d28ba845fe2676524fcbc65931064e40126a78e9c65d0d
- clm_8c4a55ec3784cc54dfbeffbe00509a7eec07496e51edf292bb24146706644b2d
- clm_948d25bbf066c790401bab2314a18f1ef8ca0c4488128638ee4b6fe11ad434fc
- clm_b54e50506debdcb18c1dae410d1869b561d8e59c1e0041118036df519d8cd68c
- clm_cad9bdc38464d4a52476acba06a3749b5f3d27181985d551193ddf7dd3decc67
- clm_cdb9af4fa01d31bb345f4744741db083dd0c425c4ffc9bc8e19ce5e499cc8b5e
- clm_dd0472d4309cc1e5e4b0aba939fff98be6dd546e615c6353daf88b0c6a886693
- clm_e62a5af5978ddf0dee8470c975f6519c6e21452182242f05cf52bbc2e2e72261
- clm_ffe6810f4f16b959c6fc8727d30c44136ba5c18fe70b18c44016c41353b03b30
maturity: draft
page_id: pg_14a5b22d72f356be95150af095b551f5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f72edac13db859ef8317f3395ac52102
title: Scarmonit/antigravity-jules-orchestration/README.md @ 49d26f81817c
updated_at: '2026-09-14T04:19:55Z'
---

# Scarmonit/antigravity-jules-orchestration/README.md @ 49d26f81817c

<!-- rcw:begin owner=source:src_f72edac13db859ef8317f3395ac52102 block=evidence -->
- A suggested-tasks scanner scans codebases for TODO/FIXME/HACK comments, ranks tasks by priority, and can create Jules sessions to fix the suggested tasks. [@claim:clm_1cdd45190120cbf2a3ff4d6309cc88e94372128423b30d05ce24329b933e7494]
- The system is a Node.js-based custom MCP server using Streamable HTTP transport, with Joi schemas for runtime input validation and a stateless architecture for compatibility with multiple MCP clients. [@claim:clm_6c4e7be1ee8e97ba0af7c29c1c2940c46b423b5c77ed5ea5eea071e22859f435]
- Repository development practice: contributors run tests with npm test or node --test tests/unit/health.test.js, and health response format changes must update the health-check workflow and unit tests. [@claim:clm_715fb9ad1edf43c0d8d28ba845fe2676524fcbc65931064e40126a78e9c65d0d]
- The Render auto-fix integration detects and fixes build failures on Jules PRs via a Render webhook receiver, build-log error pattern recognition, and AES-256-GCM encrypted credential storage. [@claim:clm_8c4a55ec3784cc54dfbeffbe00509a7eec07496e51edf292bb24146706644b2d]
- A semantic memory integration provides 8 MCP tools for persistent AI memory, with SSRF protection via a domain whitelist and error message sanitization. [@claim:clm_948d25bbf066c790401bab2314a18f1ef8ca0c4488128638ee4b6fe11ad434fc]
- Documentation appears internally inconsistent on tool count: the README states 65 MCP tools while the slash-commands doc says the commands leverage 30 MCP tools available. [@claim:clm_b54e50506debdcb18c1dae410d1869b561d8e59c1e0041118036df519d8cd68c]
- The README catalogs 65 MCP tools across groups including Jules core (7), session management (5), batch processing (7), semantic memory (8), Render integration (12), Ollama LLM (4), and RAG (4). [@claim:clm_cad9bdc38464d4a52476acba06a3749b5f3d27181985d551193ddf7dd3decc67]
- The documented autonomous loop runs: user task initiation, Antigravity planning, Jules session creation via MCP, parallel execution, progress monitoring, approval gates, then merge/test completion. [@claim:clm_cdb9af4fa01d31bb345f4744741db083dd0c425c4ffc9bc8e19ce5e499cc8b5e]
- Configuration variables include PORT (default 3323), required JULES_API_KEY, GITHUB_TOKEN, DATABASE_URL, SLACK_WEBHOOK_URL, LOG_LEVEL, ALLOWED_ORIGINS, and SEMANTIC_MEMORY_URL. [@claim:clm_dd0472d4309cc1e5e4b0aba939fff98be6dd546e615c6353daf88b0c6a886693]
- Performance features include an LRU cache (100 items, 10s default TTL), a circuit breaker tripping after 5 consecutive failures with 60s reset, and retry logic with 3 exponential-backoff retries plus jitter. [@claim:clm_e62a5af5978ddf0dee8470c975f6519c6e21452182242f05cf52bbc2e2e72261]
- Prerequisites are Node.js v18+, Google Antigravity installed, a Jules API account with key, and a GitHub account with connected repositories; setup uses npm install and npm run dev. [@claim:clm_ffe6810f4f16b959c6fc8727d30c44136ba5c18fe70b18c44016c41353b03b30]
<!-- rcw:end owner=source:src_f72edac13db859ef8317f3395ac52102 block=evidence -->

## Researcher notes

