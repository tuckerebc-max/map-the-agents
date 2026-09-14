---
access: public
aliases: []
claim_ids:
- clm_1ef29b0721e24c4eee120122512fe24a90917bc06f83c3ad641258f8d8ab9232
- clm_6ca490113567e120064980146f89d49054a87981caa05a987ed0fc0db32d3dcc
- clm_95ea37020f92407860938d24ec99da935c1134eb7fee751a3d5d241a4c41579a
maturity: draft
page_id: pg_910ab8e36ad75166bbfcd794d880efe2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3ef3c660141857748042e27e883ba4a6
title: superset-sh/superset/AGENTS.md @ ed42524ed1d4
updated_at: '2026-09-14T03:16:41Z'
---

# superset-sh/superset/AGENTS.md @ ed42524ed1d4

<!-- rcw:begin owner=source:src_3ef3c660141857748042e27e883ba4a6 block=evidence -->
- Repository development practice: AGENTS.md prescribes a component folder layout (one folder per component, co-located tests, barrel exports), Lingui-based i18n with `bun run check:i18n` enforced in CI, and a rule against hand-editing generated Drizzle migration files. [@claim:clm_1ef29b0721e24c4eee120122512fe24a90917bc06f83c3ad641258f8d8ab9232]
- The tech stack is described as Electron, React, Tailwind, Bun, Turborepo, Vite, Biome, Drizzle ORM, Neon, and tRPC. [@claim:clm_6ca490113567e120064980146f89d49054a87981caa05a987ed0fc0db32d3dcc]
- Repository development practice: plugin releases are git tags `<name>@<version>`; publishing rewrites `.agent-marketplace.json` and generated manifests, and `bun run check:plugins` runs in CI to catch skipped publish steps. [@claim:clm_95ea37020f92407860938d24ec99da935c1134eb7fee751a3d5d241a4c41579a]
<!-- rcw:end owner=source:src_3ef3c660141857748042e27e883ba4a6 block=evidence -->

## Researcher notes

