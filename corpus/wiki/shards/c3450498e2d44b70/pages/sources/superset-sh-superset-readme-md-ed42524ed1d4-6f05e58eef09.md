---
access: public
aliases: []
claim_ids:
- clm_412ef1f667382f3ef812c8498ab5b40ba4f85182f41f8b31298e14a44cd8eec4
- clm_4d48112cee747b6ee534dd7c5468f10c4887892f9163c2e1c1aa230789ffcc98
- clm_608904044747fbcba50a6a2aed5c8482f182a23dab479c18ed4a13708e305639
- clm_6ca490113567e120064980146f89d49054a87981caa05a987ed0fc0db32d3dcc
- clm_9e4d34f44a781e92dc045a706f7eca8409b2b1c61bdb3d22625e550b8b3916a4
- clm_ae6e5ee6b9906fa9329629d30e11d3b9ae9c9dd14665bc76aba7745ed47d102b
- clm_cdf7a99d30c1a333a06c24bfb3f0122d0d213cfd3946fe1f6b499d201b2988bf
- clm_ce8f3063791b3e38c027cd9d4087fa6f0e412debc4840830d93f4afa6c2b8bc1
- clm_fef957afcc1973e2e0465fccfd8a15789b7e043672202ba71ae9dd628253dae2
maturity: draft
page_id: pg_690d0d79b8205360ac9d6f05e58eef09
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2e00f5e8a11e5b39908f5cc1a72c2fc0
title: superset-sh/superset/README.md @ ed42524ed1d4
updated_at: '2026-09-14T03:16:41Z'
---

# superset-sh/superset/README.md @ ed42524ed1d4

<!-- rcw:begin owner=source:src_2e00f5e8a11e5b39908f5cc1a72c2fc0 block=evidence -->
- Per the README, Windows builds are not yet available; Linux x64 AppImage is experimental, with macOS the primary target. [@claim:clm_412ef1f667382f3ef812c8498ab5b40ba4f85182f41f8b31298e14a44cd8eec4]
- Agent sessions can be scheduled as automations, e.g. overnight issue triage, changelog drafting, or dependency freshness tasks. [@claim:clm_4d48112cee747b6ee534dd7c5468f10c4887892f9163c2e1c1aa230789ffcc98]
- Superset runs CLI-based coding agents in parallel, each isolated in its own git worktree with its own branch, terminal, and environment. [@claim:clm_608904044747fbcba50a6a2aed5c8482f182a23dab479c18ed4a13708e305639]
- The tech stack is described as Electron, React, Tailwind, Bun, Turborepo, Vite, Biome, Drizzle ORM, Neon, and tRPC. [@claim:clm_6ca490113567e120064980146f89d49054a87981caa05a987ed0fc0db32d3dcc]
- Repository development practice: contributors run `./.superset/setup.local.sh` then `bun run dev`; the setup script brings up local Postgres plus Electric via Docker and seeds a dev account, requiring Bun 1.3.14+, docker, jq, and caddy. [@claim:clm_9e4d34f44a781e92dc045a706f7eca8409b2b1c61bdb3d22625e550b8b3916a4]
- Agents come pre-loaded with `superset:*` skills (orchestrating parallel agents, scheduling automations, filing feedback, diagnosing issues) provisioned automatically at launch. [@claim:clm_ae6e5ee6b9906fa9329629d30e11d3b9ae9c9dd14665bc76aba7745ed47d102b]
- The desktop app includes a built-in terminal (splits, persistent sessions, rich prompt editor), a diff viewer for reviewing and committing agent changes, and an in-app browser with per-workspace port detection. [@claim:clm_cdf7a99d30c1a333a06c24bfb3f0122d0d213cfd3946fe1f6b499d201b2988bf]
- The only hard runtime prerequisite stated is Git; the GitHub CLI (gh) is optional and unlocks PR workflows, with Superset offering to install it. [@claim:clm_ce8f3063791b3e38c027cd9d4087fa6f0e412debc4840830d93f4afa6c2b8bc1]
- The product ships multiple surfaces: a desktop app, a single `superset` CLI binary, a TypeScript SDK (@superset_sh/sdk), and an MCP server that lets agents create and manage workspaces. [@claim:clm_fef957afcc1973e2e0465fccfd8a15789b7e043672202ba71ae9dd628253dae2]
<!-- rcw:end owner=source:src_2e00f5e8a11e5b39908f5cc1a72c2fc0 block=evidence -->

## Researcher notes

