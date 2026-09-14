---
access: public
aliases: []
claim_ids:
- clm_57178c3f0daa9a446c86d34b3666dbf3d0e8c84a02c408d158fed4560ac6ec76
- clm_57e3703b5bf6b7c62413a51eb7535bd8f1539f98139d7fff2fdc9d3a43bd52b8
- clm_6103a2e6e21683255d0c051a5422fafc72653bbaecbe7dfc4552be2edeb21fbc
- clm_69aed95c00cfa929d1d1c2456b202a3bae0d3f6a41424994d7a337d0446c822f
- clm_7134b2c5333f4fcf94a98cdf89e4e6e2d5fd3e4320d4b052f24aecc3711de8bc
- clm_78fa8c360733ed2d3e425962a2f47f1798c1c5f7280fbaedac8f2ed72895b619
- clm_8b143e460f7ef20a76818d91116aed8dbda2bb657cdc0bc40c0c82968a0f6983
- clm_cb4797e39a0e17fee273825fce068cce0adac02712334f487392e1bb29f0111d
- clm_d2d307c03dce52fd550085c921d8bf4f761df7fbc6f094da60a3722ca84a3234
maturity: draft
page_id: pg_e426f71abe96504584cf1c831522faf8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7f91853cd43c5347b87c1272fd5a8e7b
title: doable-me/Doable/README.md @ 0be4ebf5df45
updated_at: '2026-09-14T01:46:25Z'
---

# doable-me/Doable/README.md @ 0be4ebf5df45

<!-- rcw:begin owner=source:src_7f91853cd43c5347b87c1272fd5a8e7b block=evidence -->
- Deployment is offered via one-click buttons for DigitalOcean, Render, Railway, Heroku, and GitHub Codespaces, plus Coolify, Fly.io, and Kubernetes manifests, all backed by prebuilt ghcr images. [@claim:clm_57178c3f0daa9a446c86d34b3666dbf3d0e8c84a02c408d158fed4560ac6ec76]
- The product advertises multi-tenant workspaces, sandboxed code execution by default, audit logs, MFA, and RBAC, under an MIT license. [@claim:clm_57e3703b5bf6b7c62413a51eb7535bd8f1539f98139d7fff2fdc9d3a43bd52b8]
- Tenant isolation is enforced at the PostgreSQL layer via row-level security using doable.current_user_id session variables for workspace-scoped queries. [@claim:clm_6103a2e6e21683255d0c051a5422fafc72653bbaecbe7dfc4552be2edeb21fbc]
- AI-generated code runs in per-project Linux UIDs with systemd hardening, seccomp filtering, and an egress firewall, enabled by default; dovault and docore packages provide the bubblewrap jail and process isolation. [@claim:clm_69aed95c00cfa929d1d1c2456b202a3bae0d3f6a41424994d7a337d0446c822f]
- The monorepo uses pnpm workspaces plus Turborepo, with a Next.js web app (port 3000), Hono API (4000), Hono WebSocket service with Yjs (4001), and PostgreSQL 16 (5432). [@claim:clm_7134b2c5333f4fcf94a98cdf89e4e6e2d5fd3e4320d4b052f24aecc3711de8bc]
- A Rust TUI CLI named doable can provision a server over SSH and also serves as a platform-admin TUI for users, roles, feature flags, provider keys, credits, and sandbox rules. [@claim:clm_78fa8c360733ed2d3e425962a2f47f1798c1c5f7280fbaedac8f2ed72895b619]
- Doable is described as a self-hosted AI app builder for teams that builds, deploys, and hosts apps on the operator's own infrastructure. [@claim:clm_8b143e460f7ef20a76818d91116aed8dbda2bb657cdc0bc40c0c82968a0f6983]
- Repository development practice: contributors are directed to CONTRIBUTING.md, and local development runs via pnpm install and pnpm dev after forking and cloning. [@claim:clm_cb4797e39a0e17fee273825fce068cce0adac02712334f487392e1bb29f0111d]
- SSO/SAML and SCIM are stated as roadmap items; the current identity features are TOTP MFA, RBAC, and audit logs. [@claim:clm_d2d307c03dce52fd550085c921d8bf4f761df7fbc6f094da60a3722ca84a3234]
<!-- rcw:end owner=source:src_7f91853cd43c5347b87c1272fd5a8e7b block=evidence -->

## Researcher notes

