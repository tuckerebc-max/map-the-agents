# azure/gpt-rag-orchestrator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b64a5b96206 @ 6d6e1636c9e5b9d8

## Summary (orientation draft, not independently verified)

The evidence is a README (plus PR/release notes and a PR template) for the GPT-RAG Orchestrator, an agentic RAG orchestration service on Azure AI Foundry Agent Service with multiple selectable strategies, MCP/Toolbox identity passthrough, audit events, and an optional admin dashboard. No code is shown, so claims are documentation-based. Evidence coverage: 116 of 128 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 30 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

30 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The orchestrator is an agentic orchestration layer built on Azure AI Foundry Agent Service and the Microsoft Agent Framework, coordinating multiple specialized agents for agent-based RAG workflows. -- evidence: [README.md#L20-L20](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L20-L20)
  - [observation/documented] The repository snapshot carries image tag v2.8.11-c840851, while PR and release notes describe a v2.8.12 set of five operator-dashboard fixes. -- evidence: [.image-tag.txt#L1-L1](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/.image-tag.txt#L1-L1), [.release-notes.md#L3-L3](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/.release-notes.md#L3-L3), [.pr-body.md#L3-L3](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/.pr-body.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The rag and multimodal_rag strategies use Foundry IQ's Knowledge Base retrieve API, with optional opt-in Work IQ knowledge source over Outlook, Teams, and SharePoint/OneDrive data. -- evidence: [README.md#L321-L321](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L321-L321), [README.md#L323-L323](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L323-L323)
- design-choices (9 claim(s)):
  - [observation/documented] Five selectable strategies are documented: single_agent_rag, maf_agent_service, maf_lite, mcp, and nl2sql, each keyed by an AGENT_STRATEGY value. -- evidence: [README.md#L24-L30](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L24-L30)
  - [observation/documented] A non-null previous_response_id is rejected with HTTP 422 so callers must send complete ordered history as input; store is unconditionally overridden to False because the hosted container lacks managed-Conversations data-plane RBAC. -- evidence: [README.md#L90-L124](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L90-L124)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the PR template requires all pull requests to target the develop branch, with PRs targeting main automatically blocked, and asks for at least two reviewers plus local verification and CHANGELOG updates. -- evidence: [docs/pull_request_template.md#L5-L5](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/docs/pull_request_template.md#L5-L5), [docs/pull_request_template.md#L57-L61](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/docs/pull_request_template.md#L57-L61)
  - [observation/documented] Repository development practice: the v2.8.12 PR reports pytest tests/test_dashboard.py with 25 passed, npm run lint with zero warnings, and a clean vite production build. -- evidence: [.pr-body.md#L21-L22](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/.pr-body.md#L21-L22), [.pr-body.md#L15-L19](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/.pr-body.md#L15-L19)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The hosted entrypoint exposes POST /responses (Foundry Responses v2 protocol), GET /readiness for readiness probes, and a compatibility GET /health route returning image version and hosted-eligible strategies. -- evidence: [README.md#L135-L137](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L135-L137), [README.md#L82-L88](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L82-L88)
  - [observation/documented] The /responses adapter accepts a plain string input or ordered text-only role/content messages, streaming or synchronous execution, metadata, and platform-injected agent_reference; all other top-level fields are logged and dropped. -- evidence: [README.md#L90-L124](https://github.com/Azure/gpt-rag-orchestrator/blob/9b64a5b962067161cb55252c6e0917a2738ba984/README.md#L90-L124)
- memory-state (1 claim(s)):
More evidence: [full detail](gpt-rag-orchestrator.detail.md)

Metadata and full claim list: [full detail](gpt-rag-orchestrator.detail.md)
Human notes ([notes](gpt-rag-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
