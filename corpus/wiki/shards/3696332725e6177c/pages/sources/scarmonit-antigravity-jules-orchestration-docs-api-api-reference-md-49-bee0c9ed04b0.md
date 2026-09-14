---
access: public
aliases: []
claim_ids:
- clm_715fb9ad1edf43c0d8d28ba845fe2676524fcbc65931064e40126a78e9c65d0d
- clm_77d63c1ab4b4aa645f961b401271c5a7bb070a15b626c36369ba9e8a2e382332
- clm_a4f6a455b967b13ab2252b5a677200b747a8824c9b26beeb9767d03ab8de7e78
- clm_efdb0b5dedcafb5eff54d38579420f5fc55fa29ee738a9ca84ef897c30323f91
maturity: draft
page_id: pg_061ece61ebc55daea6a1bee0c9ed04b0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f7f3db8b26a8591d8d4a0db9e093bc76
title: Scarmonit/antigravity-jules-orchestration/docs/api/API_REFERENCE.md @ 49d26f81817c
updated_at: '2026-09-14T04:19:55Z'
---

# Scarmonit/antigravity-jules-orchestration/docs/api/API_REFERENCE.md @ 49d26f81817c

<!-- rcw:begin owner=source:src_f7f3db8b26a8591d8d4a0db9e093bc76 block=evidence -->
- Repository development practice: contributors run tests with npm test or node --test tests/unit/health.test.js, and health response format changes must update the health-check workflow and unit tests. [@claim:clm_715fb9ad1edf43c0d8d28ba845fe2676524fcbc65931064e40126a78e9c65d0d]
- The health endpoint returns status, version, timestamp, uptime, memory usage, per-service configuration status (julesApi, database, github), and circuit breaker failure count and open state. [@claim:clm_77d63c1ab4b4aa645f961b401271c5a7bb070a15b626c36369ba9e8a2e382332]
- The server exposes HTTP endpoints including GET /health, GET /, GET /mcp/tools, POST /mcp/execute, GET /api/sessions/active, and GET /api/sessions/stats. [@claim:clm_a4f6a455b967b13ab2252b5a677200b747a8824c9b26beeb9767d03ab8de7e78]
- POST /mcp/execute accepts a JSON body containing a tool name and a params object, and returns a tool-specific response based on the executed tool. [@claim:clm_efdb0b5dedcafb5eff54d38579420f5fc55fa29ee738a9ca84ef897c30323f91]
<!-- rcw:end owner=source:src_f7f3db8b26a8591d8d4a0db9e093bc76 block=evidence -->

## Researcher notes

