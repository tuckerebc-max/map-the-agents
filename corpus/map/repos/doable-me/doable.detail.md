# doable-me/doable -- full detail

[Back to orientation](doable.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/doable-me/doable/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/8579e6e121fc73e8.json](../../../wiki/dossiers/doable-me/doable/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/8579e6e121fc73e8.json)

## specifications (1 claim(s))

- [observation/documented] Doable is described as a self-hosted AI app builder for teams that builds, deploys, and hosts apps on the operator's own infrastructure. -- evidence: [README.md#L7-L9](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L7-L9), [README.md#L11-L14](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L11-L14) (`clm_8b143e460f7ef20a76818d91116aed8dbda2bb657cdc0bc40c0c82968a0f6983`)

## components (1 claim(s))

- [observation/documented] The monorepo uses pnpm workspaces plus Turborepo, with a Next.js web app (port 3000), Hono API (4000), Hono WebSocket service with Yjs (4001), and PostgreSQL 16 (5432). -- evidence: [README.md#L330-L335](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L330-L335), [README.md#L324-L324](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L324-L324) (`clm_7134b2c5333f4fcf94a98cdf89e4e6e2d5fd3e4320d4b052f24aecc3711de8bc`)

## design-choices (1 claim(s))

- [observation/documented] The product advertises multi-tenant workspaces, sandboxed code execution by default, audit logs, MFA, and RBAC, under an MIT license. -- evidence: [README.md#L210-L210](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L210-L210), [README.md#L16-L18](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L16-L18) (`clm_57e3703b5bf6b7c62413a51eb7535bd8f1539f98139d7fff2fdc9d3a43bd52b8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md, and local development runs via pnpm install and pnpm dev after forking and cloning. -- evidence: [README.md#L402-L403](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L402-L403), [README.md#L398-L398](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L398-L398) (`clm_cb4797e39a0e17fee273825fce068cce0adac02712334f487392e1bb29f0111d`)
- [observation/documented] Repository development practice: a Contributor Covenant 2.1-based Code of Conduct defines an escalation ladder from private written warning through temporary ban to permanent ban, with reports to conduct@doable.me. -- evidence: [CODE_OF_CONDUCT.md#L112-L113](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L112-L113), [CODE_OF_CONDUCT.md#L117-L118](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L117-L118), [CODE_OF_CONDUCT.md#L79-L81](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L79-L81), [CODE_OF_CONDUCT.md#L61-L64](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L61-L64), [CODE_OF_CONDUCT.md#L100-L104](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/CODE_OF_CONDUCT.md#L100-L104) (`clm_85cf400c6dec2900accdddee038d8feb342a21011385057b1ad8918a8d517dae`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A Rust TUI CLI named doable can provision a server over SSH and also serves as a platform-admin TUI for users, roles, feature flags, provider keys, credits, and sandbox rules. -- evidence: [README.md#L354-L354](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L354-L354), [README.md#L341-L341](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L341-L341) (`clm_78fa8c360733ed2d3e425962a2f47f1798c1c5f7280fbaedac8f2ed72895b619`)
- [observation/documented] Any OpenAI-compatible endpoint can be added as a custom provider from the admin panel by specifying a display name, base URL, wire protocol, auth header pattern, and model IDs. -- evidence: [docs/PROVIDERS.md#L9-L9](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L9-L9), [docs/PROVIDERS.md#L44-L48](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L44-L48), [docs/PROVIDERS.md#L42-L42](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L42-L42) (`clm_88f196027b89c5b431dd145a3d9d30d0313c296ee63edfa28124ec9d581d80ed`)

## memory-state (1 claim(s))

- [observation/documented] Tenant isolation is enforced at the PostgreSQL layer via row-level security using doable.current_user_id session variables for workspace-scoped queries. -- evidence: [README.md#L383-L385](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L383-L385) (`clm_6103a2e6e21683255d0c051a5422fafc72653bbaecbe7dfc4552be2edeb21fbc`)

## orchestration (1 claim(s))

- [observation/documented] Deployment is offered via one-click buttons for DigitalOcean, Render, Railway, Heroku, and GitHub Codespaces, plus Coolify, Fly.io, and Kubernetes manifests, all backed by prebuilt ghcr images. -- evidence: [README.md#L72-L76](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L72-L76), [README.md#L70-L70](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L70-L70), [README.md#L78-L78](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L78-L78) (`clm_57178c3f0daa9a446c86d34b3666dbf3d0e8c84a02c408d158fed4560ac6ec76`)

## tools-permissions (1 claim(s))

- [observation/documented] AI-generated code runs in per-project Linux UIDs with systemd hardening, seccomp filtering, and an egress firewall, enabled by default; dovault and docore packages provide the bubblewrap jail and process isolation. -- evidence: [README.md#L212-L221](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L212-L221), [README.md#L375-L379](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L375-L379) (`clm_69aed95c00cfa929d1d1c2456b202a3bae0d3f6a41424994d7a337d0446c822f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] NOTICE.md credits ActivePieces for the integrations registry (630+ pieces), Yjs for real-time collaborative editing, and the Model Context Protocol for agentic tool extensibility. -- evidence: [NOTICE.md#L20-L25](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/NOTICE.md#L20-L25), [NOTICE.md#L10-L14](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/NOTICE.md#L10-L14), [NOTICE.md#L31-L37](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/NOTICE.md#L31-L37) (`clm_56b57de6a40331a99a3cdbc05b25b9105f794c093ff62757c7ff2b17e6b69a75`)
- [observation/documented] The provider catalog supports 63 providers and 19+ local model engines via BYOK, with a universal bridge accepting openai, azure, and anthropic wire protocols and six auth methods. -- evidence: [docs/PROVIDERS.md#L3-L3](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L3-L3), [docs/PROVIDERS.md#L25-L25](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L25-L25), [docs/PROVIDERS.md#L39-L40](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/docs/PROVIDERS.md#L39-L40) (`clm_682cb12bee88ae9e62aa1a364f5cd61bc82c64d6ad251bad67c5fdedcc9c7837`)

## limitations (1 claim(s))

- [observation/documented] SSO/SAML and SCIM are stated as roadmap items; the current identity features are TOTP MFA, RBAC, and audit logs. -- evidence: [README.md#L223-L223](https://github.com/doable-me/Doable/blob/0be4ebf5df45120030732ae1e1f5db8b5e73a68d/README.md#L223-L223) (`clm_d2d307c03dce52fd550085c921d8bf4f761df7fbc6f094da60a3722ca84a3234`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

