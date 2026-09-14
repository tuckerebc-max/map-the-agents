---
access: public
aliases: []
claim_ids:
- clm_00b44735bc9abe1890598303bb860b865aa2187eef4cab15792c7de6d9e0b590
- clm_0994213b41b7dba63840e64dd46b1e4dbd79d5eaf011c8024931990ea27ec53b
- clm_1aa85b22e5c45226ac39b000f72a70fd49d1a933565f5976bae2ffad923ce819
- clm_1cf55f909357250400eff80514d53ebfa65a2229aa6736b05fe2a8935317f421
- clm_270ad78e50e6265e233e1ba54492678f00f01b63b41b330ae31355538be3975d
- clm_2b0302ed285102ccf972a43e98ea37cd87129db280da9a95980c68d5772871bf
- clm_2b4dbbd6de5c0a1589cc4dfdb0cd0206cd67768881058b93217b48d449b1e673
- clm_362bdb9afc37add0023c6fa42c325a9de18ce6a3c10cb605cb8c888a7ebb0c63
- clm_3b7aa4da8591d41fe9c13fe7b12acfe1f05518041dab3731d64488179ffe036b
- clm_4117f77d4ae6db652890eaa850ccadc8072a9b90acfcebda6f0c9c9aedec0fde
- clm_57f20265f7bc0ba09258bfc19d117057075299e74cd36ad817deb4b6e1b4f75d
- clm_71b3a4ded200df754e32e518f924045edfd17321215a6bf77404a666edbe43b8
- clm_80a805f59573fb2411919fc956a519e5058d22659062f9bc3676b031b03ce0f2
- clm_88df3552dae7dc4ae3f3023b129fd35c0dac57c33dec62723d4bf68fb68dc54b
- clm_891a64b0f6a918b1f2a97d5f31cc2a237a5f8f3c2e2e92edf196500be0811f08
- clm_8d8a530d5a2deb8a71030e37889b1b0d11f521aa5a0fc33b15f3a639167b072a
- clm_9b47d98d3cfbf5efe10d58c08df2b2a1af5de7ba203350858cdd0d421ad7c4ce
- clm_b2a4f0e492707592457823473ed7628fbed12a06ab03e136f69840a111f4701b
- clm_b5b7c7e8bf844ab2af15582959168659e9150f4a2d04da46d8ffc3a70c95d84c
- clm_ba3d506916aa10d2bf1aadab9ce50b25f98c25f74eead59ab70bcceb54d6b35f
- clm_de3f31d44e8fd1eb7549087575ab0bb8d9e27c8074aef8d663edfb8c910d810d
- clm_e02f2391364eadb58276d037a4194ba59403ed8aa5e05a0404e77166952589f4
- clm_e7b9a74abade31900b167f629277d8e8cb917bf65d8b73b45950cb87be7d6fdc
- clm_ed3873f9a5ffeed773b685826a5e5d3968db0d7fc3c0d6fb22dcdf202ffef098
- clm_f563beb5627f7e337cb490181da0f0a04a31eac660edbccd3f444d696b5ffe8a
- clm_f68b92502c990245a0c898d6a849ee62dcb94c19a027dbd41508e4b1aeff88b1
- clm_f934d32b92f56adc7e8ff70148f3d80e3269d740a3cfceb09b2348bb3229d4b1
maturity: draft
page_id: pg_3faeffa1895b5351a90002b6aa324d24
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8d19410fbabb5087922c4dda16a4d488
title: Azure/gpt-rag-orchestrator/README.md @ 9b64a5b96206
updated_at: '2026-09-14T03:37:10Z'
---

# Azure/gpt-rag-orchestrator/README.md @ 9b64a5b96206

<!-- rcw:begin owner=source:src_8d19410fbabb5087922c4dda16a4d488 block=evidence -->
- Generic MCP Server knowledge sources are a preview feature on API 2026-05-01-preview, disabled by default; when disabled the existing minimal-reasoning intents request is kept unchanged. [@claim:clm_00b44735bc9abe1890598303bb860b865aa2187eef4cab15792c7de6d9e0b590]
- Successful orchestrator and feedback responses return a server-generated X-Correlation-ID (inbound values ignored), which is explicitly not an authentication, authorization, idempotency, or immutability mechanism. [@claim:clm_0994213b41b7dba63840e64dd46b1e4dbd79d5eaf011c8024931990ea27ec53b]
- MCP knowledge-source query headers support managedIdentity, obo, keyVaultSecret, or none value kinds; literal header values and secrets are rejected, and trusted hosts require exact HTTPS matches. [@claim:clm_1aa85b22e5c45226ac39b000f72a70fd49d1a933565f5976bae2ffad923ce819]
- The /responses adapter accepts a plain string input or ordered text-only role/content messages, streaming or synchronous execution, metadata, and platform-injected agent_reference; all other top-level fields are logged and dropped. [@claim:clm_1cf55f909357250400eff80514d53ebfa65a2229aa6736b05fe2a8935317f421]
- MCP transport endpoints are resolved from MCP_APP_ENDPOINT by appending /sse for sse or /mcp for streamable_http; a conflicting suffix fails strategy initialization. [@claim:clm_270ad78e50e6265e233e1ba54492678f00f01b63b41b330ae31355538be3975d]
- The optional admin dashboard reads from the orchestrator's conversation/history Cosmos DB container (CONVERSATIONS_DATABASE_CONTAINER in DATABASE_NAME) and is read-only. [@claim:clm_2b0302ed285102ccf972a43e98ea37cd87129db280da9a95980c68d5772871bf]
- Ingestion audit event names (ingestion.run.* and ingestion.document.*) are part of the shared v1 schemas but are not emitted by this repository. [@claim:clm_2b4dbbd6de5c0a1589cc4dfdb0cd0206cd67768881058b93217b48d449b1e673]
- Work IQ is a gated preview requiring admin consent and a provisioned knowledge source; when the per-user OBO token is missing the source is skipped with a warning and managed-identity fallback is never used for remote kinds. [@claim:clm_362bdb9afc37add0023c6fa42c325a9de18ce6a3c10cb605cb8c888a7ebb0c63]
- Audit budgets are fixed rather than configurable: 64 events per request, 16 complete tool invocation pairs, and up to 25 grounding-source events per request. [@claim:clm_3b7aa4da8591d41fe9c13fe7b12acfe1f05518041dab3731d64488179ffe036b]
- For nl2sql, datasources must use a least-privilege read-only principal with only needed SELECT grants; the orchestrator validates generated SQL before execution but database permissions remain the primary security boundary. [@claim:clm_4117f77d4ae6db652890eaa850ccadc8072a9b90acfcebda6f0c9c9aedec0fde]
- The reusable v1 audit event JSON schema lives at contracts/audit-event-v1.schema.json, with an Application Insights wire schema and SHA-256 digests recorded in contracts/audit-event-v1.sha256. [@claim:clm_57f20265f7bc0ba09258bfc19d117057075299e74cd36ad817deb4b6e1b4f75d]
- Audit events are disabled by default, emitted under the gptrag.audit namespace, and enabling them requires a valid 256-bit HMAC key or startup fails. [@claim:clm_71b3a4ded200df754e32e518f924045edfd17321215a6bf77404a666edbe43b8]
- The mcp strategy runs on Microsoft Agent Framework rather than Semantic Kernel, keeping AGENT_STRATEGY=mcp and existing MCP configuration keys compatible, with sse as the default transport. [@claim:clm_80a805f59573fb2411919fc956a519e5058d22659062f9bc3676b031b03ce0f2]
- The dashboard is disabled by default; ENABLE_DASHBOARD=true mounts /dashboard, and when false neither the HTML page nor any /api/dashboard/* route is registered. [@claim:clm_88df3552dae7dc4ae3f3023b129fd35c0dac57c33dec62723d4bf68fb68dc54b]
- Audit events are best-effort operational telemetry, not an immutable ledger and not a compliance mechanism; disabling auditing stops new events without deleting already-exported telemetry. [@claim:clm_891a64b0f6a918b1f2a97d5f31cc2a237a5f8f3c2e2e92edf196500be0811f08]
- The runtime image pre-caches its tokenizer during build so hosted requests need no public Blob Storage egress in network-isolated environments. [@claim:clm_8d8a530d5a2deb8a71030e37889b1b0d11f521aa5a0fc33b15f3a639167b072a]
- For Toolbox-backed strategies (currently only mcp), x-agent-foundry-call-id is strictly validated (printable ASCII, max 256 chars) and missing or malformed values are rejected with HTTP 401 before any strategy or Toolbox client runs. [@claim:clm_9b47d98d3cfbf5efe10d58c08df2b2a1af5de7ba203350858cdd0d421ad7c4ce]
- A non-null previous_response_id is rejected with HTTP 422 so callers must send complete ordered history as input; store is unconditionally overridden to False because the hosted container lacks managed-Conversations data-plane RBAC. [@claim:clm_b2a4f0e492707592457823473ed7628fbed12a06ab03e136f69840a111f4701b]
- Deployment prerequisites include Azure CLI, Git, Python 3.12, and Docker CLI, with Azure Developer CLI optional and VS Code recommended; infrastructure must be provisioned from the GPT-RAG repo first. [@claim:clm_b5b7c7e8bf844ab2af15582959168659e9150f4a2d04da46d8ffc3a70c95d84c]
- The hosted entrypoint exposes POST /responses (Foundry Responses v2 protocol), GET /readiness for readiness probes, and a compatibility GET /health route returning image version and hosted-eligible strategies. [@claim:clm_ba3d506916aa10d2bf1aadab9ce50b25f98c25f74eead59ab70bcceb54d6b35f]
- With authentication configured, /api/dashboard/* routes require a bearer token whose roles claim contains the exact case-sensitive value Admin, except the version and auth-config bootstrap endpoints. [@claim:clm_de3f31d44e8fd1eb7549087575ab0bb8d9e27c8074aef8d663edfb8c910d810d]
- Five selectable strategies are documented: single_agent_rag, maf_agent_service, maf_lite, mcp, and nl2sql, each keyed by an AGENT_STRATEGY value. [@claim:clm_e02f2391364eadb58276d037a4194ba59403ed8aa5e05a0404e77166952589f4]
- The rag and multimodal_rag strategies use Foundry IQ's Knowledge Base retrieve API, with optional opt-in Work IQ knowledge source over Outlook, Teams, and SharePoint/OneDrive data. [@claim:clm_e7b9a74abade31900b167f629277d8e8cb917bf65d8b73b45950cb87be7d6fdc]
- The orchestrator is an agentic orchestration layer built on Azure AI Foundry Agent Service and the Microsoft Agent Framework, coordinating multiple specialized agents for agent-based RAG workflows. [@claim:clm_ed3873f9a5ffeed773b685826a5e5d3968db0d7fc3c0d6fb22dcdf202ffef098]
- The hosted Responses server disables generative-AI prompt and completion capture in OpenTelemetry by default; OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true should be set only when data policy permits. [@claim:clm_f563beb5627f7e337cb490181da0f0a04a31eac660edbccd3f444d696b5ffe8a]
- The container never reads or forwards the Authorization header (stripped by the platform gateway), never trusts caller- or model-supplied identity fields for retrieval security, and never logs call ids or authorization material. [@claim:clm_f68b92502c990245a0c898d6a849ee62dcb94c19a027dbd41508e4b1aeff88b1]
- Foundry IQ exposes MCP activity only after completion with no pre-invocation callback, so started-event timestamps for foundry_iq.mcp_tool are reconstructed and approximate, not proof of actual execution start. [@claim:clm_f934d32b92f56adc7e8ff70148f3d80e3269d740a3cfceb09b2348bb3229d4b1]
<!-- rcw:end owner=source:src_8d19410fbabb5087922c4dda16a4d488 block=evidence -->

## Researcher notes

