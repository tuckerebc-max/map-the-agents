# scarmonit/antigravity-jules-orchestration -- full detail

[Back to orientation](antigravity-jules-orchestration.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/scarmonit/antigravity-jules-orchestration/49d26f81817c123045ea0e23092c53f8f1f74174/9593a4b4c9beb21b.json](../../../wiki/dossiers/scarmonit/antigravity-jules-orchestration/49d26f81817c123045ea0e23092c53f8f1f74174/9593a4b4c9beb21b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The system is a Node.js-based custom MCP server using Streamable HTTP transport, with Joi schemas for runtime input validation and a stateless architecture for compatibility with multiple MCP clients. -- evidence: [README.md#L25-L42](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L25-L42) (`clm_6c4e7be1ee8e97ba0af7c29c1c2940c46b423b5c77ed5ea5eea071e22859f435`)
- [observation/documented] The README catalogs 65 MCP tools across groups including Jules core (7), session management (5), batch processing (7), semantic memory (8), Render integration (12), Ollama LLM (4), and RAG (4). -- evidence: [README.md#L25-L42](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L25-L42) (`clm_cad9bdc38464d4a52476acba06a3749b5f3d27181985d551193ddf7dd3decc67`)
- [observation/documented] The Render auto-fix integration detects and fixes build failures on Jules PRs via a Render webhook receiver, build-log error pattern recognition, and AES-256-GCM encrypted credential storage. -- evidence: [README.md#L47-L50](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L47-L50) (`clm_8c4a55ec3784cc54dfbeffbe00509a7eec07496e51edf292bb24146706644b2d`)
- [observation/documented] A suggested-tasks scanner scans codebases for TODO/FIXME/HACK comments, ranks tasks by priority, and can create Jules sessions to fix the suggested tasks. -- evidence: [README.md#L53-L55](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L53-L55) (`clm_1cdd45190120cbf2a3ff4d6309cc88e94372128423b30d05ce24329b933e7494`)

## design-choices (2 claim(s))

- [observation/documented] Safety design includes approval gates requiring a 'Plan Approved' state before code modification, stricter approval for high-risk infra/auth tasks, and all Jules output delivered via pull requests for human review. -- evidence: [docs/reference/ARCHITECTURE.md#L56-L60](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L56-L60) (`clm_d31a662b07743d128b3f4709ee535c3cc08d52fe44c3d8ea5b7a4d815125b4a2`)
- [observation/documented] Performance features include an LRU cache (100 items, 10s default TTL), a circuit breaker tripping after 5 consecutive failures with 60s reset, and retry logic with 3 exponential-backoff retries plus jitter. -- evidence: [README.md#L142-L144](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L142-L144) (`clm_e62a5af5978ddf0dee8470c975f6519c6e21452182242f05cf52bbc2e2e72261`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run tests with npm test or node --test tests/unit/health.test.js, and health response format changes must update the health-check workflow and unit tests. -- evidence: [docs/api/API_REFERENCE.md#L171-L171](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L171-L171), [README.md#L155-L157](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L155-L157), [docs/api/API_REFERENCE.md#L71-L71](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L71-L71), [docs/api/API_REFERENCE.md#L180-L182](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L180-L182) (`clm_715fb9ad1edf43c0d8d28ba845fe2676524fcbc65931064e40126a78e9c65d0d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The server exposes HTTP endpoints including GET /health, GET /, GET /mcp/tools, POST /mcp/execute, GET /api/sessions/active, and GET /api/sessions/stats. -- evidence: [docs/api/API_REFERENCE.md#L9-L12](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L9-L12), [docs/api/API_REFERENCE.md#L157-L159](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L157-L159), [docs/api/API_REFERENCE.md#L163-L165](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L163-L165), [docs/api/API_REFERENCE.md#L89-L91](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L89-L91), [docs/api/API_REFERENCE.md#L118-L120](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L118-L120), [docs/api/API_REFERENCE.md#L132-L134](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L132-L134) (`clm_a4f6a455b967b13ab2252b5a677200b747a8824c9b26beeb9767d03ab8de7e78`)
- [observation/documented] POST /mcp/execute accepts a JSON body containing a tool name and a params object, and returns a tool-specific response based on the executed tool. -- evidence: [docs/api/API_REFERENCE.md#L149-L149](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L149-L149), [docs/api/API_REFERENCE.md#L138-L145](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L138-L145) (`clm_efdb0b5dedcafb5eff54d38579420f5fc55fa29ee738a9ca84ef897c30323f91`)
- [observation/documented] The health endpoint returns status, version, timestamp, uptime, memory usage, per-service configuration status (julesApi, database, github), and circuit breaker failure count and open state. -- evidence: [docs/api/API_REFERENCE.md#L16-L36](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L16-L36), [docs/api/API_REFERENCE.md#L40-L52](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/api/API_REFERENCE.md#L40-L52) (`clm_77d63c1ab4b4aa645f961b401271c5a7bb070a15b626c36369ba9e8a2e382332`)
- [observation/documented] The system provides slash commands including /status, /quick-fix, /session, /batch, /audit, /deploy-check, /implement-feature, /fix-issues, /security, /test, /learn-pattern, and /generate-command. -- evidence: [docs/COMMANDS_REFERENCE.md#L197-L210](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/COMMANDS_REFERENCE.md#L197-L210) (`clm_bccb7e8966015d665fece5b03d7515622e655665b2bd4b04b95a63fd5ce85cdb`)
- [observation/documented] Configuration variables include PORT (default 3323), required JULES_API_KEY, GITHUB_TOKEN, DATABASE_URL, SLACK_WEBHOOK_URL, LOG_LEVEL, ALLOWED_ORIGINS, and SEMANTIC_MEMORY_URL. -- evidence: [README.md#L129-L138](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L129-L138) (`clm_dd0472d4309cc1e5e4b0aba939fff98be6dd546e615c6353daf88b0c6a886693`)
- [inference/documented] Documentation appears internally inconsistent on tool count: the README states 65 MCP tools while the slash-commands doc says the commands leverage 30 MCP tools available. -- evidence: [README.md#L25-L42](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L25-L42), [docs/COMMANDS_REFERENCE.md#L252-L252](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/COMMANDS_REFERENCE.md#L252-L252) (`clm_b54e50506debdcb18c1dae410d1869b561d8e59c1e0041118036df519d8cd68c`)

## memory-state (1 claim(s))

- [observation/documented] A semantic memory integration provides 8 MCP tools for persistent AI memory, with SSRF protection via a domain whitelist and error message sanitization. -- evidence: [README.md#L58-L60](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L58-L60) (`clm_948d25bbf066c790401bab2314a18f1ef8ca0c4488128638ee4b6fe11ad434fc`)

## orchestration (3 claim(s))

- [observation/documented] The documented autonomous loop runs: user task initiation, Antigravity planning, Jules session creation via MCP, parallel execution, progress monitoring, approval gates, then merge/test completion. -- evidence: [README.md#L104-L110](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L104-L110) (`clm_cdb9af4fa01d31bb345f4744741db083dd0c425c4ffc9bc8e19ce5e499cc8b5e`)
- [observation/documented] The architecture positions Jules API as the inner-loop coding executor (clone, plan, edit, create PRs) with agent.scarmonit.com as an orchestration layer translating events into tasks and managing approval flows. -- evidence: [docs/reference/ARCHITECTURE.md#L7-L20](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L7-L20), [docs/reference/ARCHITECTURE.md#L4-L4](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L4-L4) (`clm_08d8af258fbc47bf85888001c6f96ee1446098cf5d645570565aaab3617343a8`)
- [observation/documented] The system is event-driven, reacting to GitHub labels (jules-auto), comments (@jules plan this), PR review comments, monitoring webhooks, and CI build failures. -- evidence: [docs/reference/ARCHITECTURE.md#L26-L28](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L26-L28), [docs/reference/ARCHITECTURE.md#L31-L32](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L31-L32), [docs/reference/ARCHITECTURE.md#L23-L23](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/docs/reference/ARCHITECTURE.md#L23-L23) (`clm_7074de051b24963c255c3e73041ed8c2243e5ca0e879859df1bfb57daf50e46e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Node.js v18+, Google Antigravity installed, a Jules API account with key, and a GitHub account with connected repositories; setup uses npm install and npm run dev. -- evidence: [README.md#L122-L125](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L122-L125), [README.md#L115-L118](https://github.com/Scarmonit/antigravity-jules-orchestration/blob/49d26f81817c123045ea0e23092c53f8f1f74174/README.md#L115-L118) (`clm_ffe6810f4f16b959c6fc8727d30c44136ba5c18fe70b18c44016c41353b03b30`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

