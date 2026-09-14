---
access: public
aliases: []
claim_ids:
- clm_1b34a7debc1311954e67f6d350aa3217f5b96375723b93cfe74a8f3516d92fa1
- clm_24df3fd603b4e4051167965eea00be03f2d866c6725924ce96854268bffb6d79
- clm_44433d7a980c1e24c96eff57ece50b171a39671aceae7ac5290c69099536242e
- clm_6ca9db23a40886b306ffcb0c64a36667da03806f4990a6f5a7d7dd9dfa96eb26
- clm_b7ca3efcea9d777902b74df8b5c7e0ce56435235d244deacd8b9eb72189eddd2
- clm_bcaae0760238d545f6457ef2dcbd0ea9967782595481669884629ec568cf9b16
- clm_e3e9ce81b66270048c886d8b46679c1d102e1292668bf76c906b2a06877121af
maturity: draft
page_id: pg_e14046f319e358d6b2846d031c47e402
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f36a4df46f757ec8941ce6a660fd238
title: 2389-research/ourocodus/docs/prd/api.md @ 00bfe36ef930
updated_at: '2026-09-14T01:28:48Z'
---

# 2389-research/ourocodus/docs/prd/api.md @ 00bfe36ef930

<!-- rcw:begin owner=source:src_2f36a4df46f757ec8941ce6a660fd238 block=evidence -->
- The API spec defines structured error responses with codes such as SESSION_NOT_FOUND, and the demo documentation distinguishes recoverable from non-recoverable errors. [@claim:clm_1b34a7debc1311954e67f6d350aa3217f5b96375723b93cfe74a8f3516d92fa1]
- The PRD specifies an HTTP control plane providing REST endpoints for session management, agent lifecycle, event log access, health checks, and serving static web UI files. [@claim:clm_24df3fd603b4e4051167965eea00be03f2d866c6725924ce96854268bffb6d79]
- The documented REST API includes POST/GET/DELETE /api/sessions, GET /api/agents, event tailing and SSE streaming at /api/events, plus /health and /api/info endpoints. [@claim:clm_44433d7a980c1e24c96eff57ece50b171a39671aceae7ac5290c69099536242e]
- Documented dependencies include the Docker SDK for Go (Apache 2.0) for container lifecycle management and the NATS Go client, with the API built on Go's net/http stdlib. [@claim:clm_6ca9db23a40886b306ffcb0c64a36667da03806f4990a6f5a7d7dd9dfa96eb26]
- The API server uses in-memory state with reconstruction from an event log at startup, reconnecting to NATS and Docker and querying running agent containers. [@claim:clm_b7ca3efcea9d777902b74df8b5c7e0ce56435235d244deacd8b9eb72189eddd2]
- The PRD specifies Session, Agent, and Event data models with JSON fields including status, container_id, chunks_completed, and payload. [@claim:clm_bcaae0760238d545f6457ef2dcbd0ea9967782595481669884629ec568cf9b16]
- The API spec states the POC has no authentication, is localhost-only, and allows all CORS origins, with API keys, CORS config, and rate limiting deferred to post-POC. [@claim:clm_e3e9ce81b66270048c886d8b46679c1d102e1292668bf76c906b2a06877121af]
<!-- rcw:end owner=source:src_2f36a4df46f757ec8941ce6a660fd238 block=evidence -->

## Researcher notes

