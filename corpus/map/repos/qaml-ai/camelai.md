# qaml-ai/camelai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5f3c295d66fd @ ceee23502cd9df82

## Summary (orientation draft, not independently verified)

camelAI is an AI coding-assistant platform on Cloudflare: per-thread coding agents in Durable Objects, sandboxed JavaScript execution, file storage, publishing, enterprise OIDC SSO, and a Docker Compose self-host target. Evidence supports product architecture, SSO behavior, self-hosting capabilities, and contributor workflows. Evidence coverage: 141 of 249 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Each chat thread runs its own coding agent inside a Cloudflare Durable Object (ChatThreadDO), which owns the agent loop and persistent chat state. -- evidence: [README.md#L22-L25](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L22-L25), [README.md#L108-L111](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L108-L111)
- design-choices (1 claim(s)):
  - [observation/documented] The agent harness is camelAI's own, built from pi's lower-level agent-loop and state-management libraries; Anthropic, OpenAI, OpenRouter, Bedrock, and custom endpoints supply only the model, not the harness. -- evidence: [README.md#L103-L106](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L103-L106)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors should run bun run typecheck, lint, and test:all before opening a pull request, add focused tests for behavior changes, and follow the architecture and code conventions in AGENTS.md. -- evidence: [README.md#L218-L218](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L218-L218), [README.md#L226-L229](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L226-L229), [README.md#L220-L224](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L220-L224)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Enterprise SSO uses OIDC and is configured per organization at Settings → Organization → Single sign-on, with fields for issuer URL, client ID/secret, token auth method, email claim, allowed domains, and an uninvited-users toggle. -- evidence: [CUSTOMER_SSO_SETUP_GUIDE.md#L78-L86](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L78-L86), [CUSTOMER_SSO_SETUP_GUIDE.md#L3-L5](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L3-L5), [CUSTOMER_SSO_SETUP_GUIDE.md#L76-L76](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/CUSTOMER_SSO_SETUP_GUIDE.md#L76-L76)
  - [observation/documented] Self-hosted deployments expose GET /api/selfhost/health as both the readiness endpoint and a versioned machine-readable capability contract; failed runtime checks return HTTP 503 with status fail. -- evidence: [SELF_HOSTING.md#L164-L166](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L164-L166), [SELF_HOSTING.md#L243-L250](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/SELF_HOSTING.md#L243-L250)
- memory-state (1 claim(s)):
  - [observation/documented] Project files live in WorkspaceFilesystemDO: small files in Durable Object SQLite, larger ones in R2, with git history provided by Cloudflare Artifacts. -- evidence: [README.md#L113-L117](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L113-L117)
- orchestration (1 claim(s)):
  - [observation/documented] Linux sandbox containers are reserved for short-lived jobs (app builds, notebook analysis, SQL queries); project deploys flow through a build sandbox to Workers for Platforms, and a dispatcher Worker routes requests to published apps. -- evidence: [README.md#L113-L117](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L113-L117), [README.md#L97-L101](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L97-L101)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent writes JavaScript instead of bash; Code Mode runs it in fresh V8 isolates with explicit platform and connection methods, and credentials remain outside the execution sandbox. -- evidence: [README.md#L108-L111](https://github.com/qaml-ai/camelAI/blob/5f3c295d66fd3fe3d70069aa56a394faf75814d5/README.md#L108-L111)
- evaluation (1 claim(s)):
More evidence: [full detail](camelai.detail.md)

Metadata and full claim list: [full detail](camelai.detail.md)
Human notes ([notes](camelai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
