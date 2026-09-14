# doable-me/doable

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0be4ebf5df45 @ 8579e6e121fc73e8

## Summary (orientation draft, not independently verified)

Doable is a self-hosted, MIT-licensed, multi-tenant AI app builder with sandboxed code execution, RBAC/MFA/audit logging, a pnpm/Turborepo monorepo (Next.js web, Hono API/WS, PostgreSQL 16), BYOK provider support, and one-click deployment paths. Evidence is documentation-based; the community Code of Conduct defines an escalation ladder from private warning to permanent ban. Evidence coverage: 151 of 293 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Doable is described as a self-hosted AI app builder for teams that builds, deploys, and hosts apps on the operator's own infrastructure. -- evidence: [README.md#L7-L9](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L7-L9), [README.md#L11-L14](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L11-L14)
- components (1 claim(s)):
  - [observation/documented] The monorepo uses pnpm workspaces plus Turborepo, with a Next.js web app (port 3000), Hono API (4000), Hono WebSocket service with Yjs (4001), and PostgreSQL 16 (5432). -- evidence: [README.md#L330-L335](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L330-L335), [README.md#L324-L324](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L324-L324)
- design-choices (1 claim(s)):
  - [observation/documented] The product advertises multi-tenant workspaces, sandboxed code execution by default, audit logs, MFA, and RBAC, under an MIT license. -- evidence: [README.md#L210-L210](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L210-L210), [README.md#L16-L18](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L16-L18)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md, and local development runs via pnpm install and pnpm dev after forking and cloning. -- evidence: [README.md#L402-L403](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L402-L403), [README.md#L398-L398](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L398-L398)
  - [observation/documented] Repository development practice: a Contributor Covenant 2.1-based Code of Conduct defines an escalation ladder from private written warning through temporary ban to permanent ban, with reports to conduct@doable.me. -- evidence: [CODE_OF_CONDUCT.md#L112-L113](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L112-L113), [CODE_OF_CONDUCT.md#L117-L118](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L117-L118), [CODE_OF_CONDUCT.md#L79-L81](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L79-L81), [CODE_OF_CONDUCT.md#L61-L64](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L61-L64), [CODE_OF_CONDUCT.md#L100-L104](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L100-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A Rust TUI CLI named doable can provision a server over SSH and also serves as a platform-admin TUI for users, roles, feature flags, provider keys, credits, and sandbox rules. -- evidence: [README.md#L354-L354](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L354-L354), [README.md#L341-L341](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L341-L341)
  - [observation/documented] Any OpenAI-compatible endpoint can be added as a custom provider from the admin panel by specifying a display name, base URL, wire protocol, auth header pattern, and model IDs. -- evidence: [docs/PROVIDERS.md#L9-L9](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L9-L9), [docs/PROVIDERS.md#L44-L48](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L44-L48), [docs/PROVIDERS.md#L42-L42](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L42-L42)
- memory-state (1 claim(s)):
  - [observation/documented] Tenant isolation is enforced at the PostgreSQL layer via row-level security using doable.current_user_id session variables for workspace-scoped queries. -- evidence: [README.md#L383-L385](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L383-L385)
- orchestration (1 claim(s)):
  - [observation/documented] Deployment is offered via one-click buttons for DigitalOcean, Render, Railway, Heroku, and GitHub Codespaces, plus Coolify, Fly.io, and Kubernetes manifests, all backed by prebuilt ghcr images. -- evidence: [README.md#L72-L76](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L72-L76), [README.md#L70-L70](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L70-L70), [README.md#L78-L78](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L78-L78)
- tools-permissions (1 claim(s)):
More evidence: [full detail](doable.detail.md)

Metadata and full claim list: [full detail](doable.detail.md)
Human notes ([notes](doable.notes.md), never overwritten by build)

[Back to map index](../../index.md)
