---
access: public
aliases: []
claim_ids:
- clm_4ec3ec229c4844c6806718c17320ce8c41791919b2d519f37493de1b6409bc62
- clm_78f7ed147a13da0000b6a127a2f4815f6d09a2646b96f43e3bb711526ee39989
- clm_83a09b4e49e1aeb4047c4e5fb537b39ad886445f9d366d3349c185b671d90947
maturity: draft
page_id: pg_e72f27b332b0597297c2367ad054f04c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a50b9592033e5d49a45e0776f34a0570
title: onecli/onecli/docs/development.md @ 3e595ef04d1a
updated_at: '2026-09-14T02:25:50Z'
---

# onecli/onecli/docs/development.md @ 3e595ef04d1a

<!-- rcw:begin owner=source:src_a50b9592033e5d49a45e0776f34a0570 block=evidence -->
- The codebase is a pnpm/turbo monorepo with apps (web, api-server, gateway, runner, sandbox-supervisor, ssh-terminator, channel-adapter, e2e suites) and packages (api, agent-protocol, db, ui), plus Docker Compose files for self-hosting. [@claim:clm_4ec3ec229c4844c6806718c17320ce8c41791919b2d519f37493de1b6409bc62]
- Repository development practice: local setup is `mise install`, `pnpm install`, `pnpm dev`, which generates .env secrets, starts PostgreSQL, applies migrations, and runs web, api, gateway and runner; `pnpm check` is the pre-push and CI gate and `pnpm test` runs test suites. [@claim:clm_78f7ed147a13da0000b6a127a2f4815f6d09a2646b96f43e3bb711526ee39989]
- Development prerequisites are mise (provisioning Node.js and pnpm), Rust for the gateway, and Docker for PostgreSQL and agent sandboxes; the stack uses Prisma ORM with PostgreSQL. [@claim:clm_83a09b4e49e1aeb4047c4e5fb537b39ad886445f9d366d3349c185b671d90947]
<!-- rcw:end owner=source:src_a50b9592033e5d49a45e0776f34a0570 block=evidence -->

## Researcher notes

