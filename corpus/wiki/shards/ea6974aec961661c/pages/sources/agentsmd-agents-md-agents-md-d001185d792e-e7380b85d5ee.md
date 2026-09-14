---
access: public
aliases: []
claim_ids:
- clm_07941e7283cc5537c6664a9cbdb6684e709b6e6aca73079c00798d04cbb1765c
- clm_ba16adfc89c4da687f508b447d50949b9d96f4cc2da11559c22e69b4827c2d98
- clm_cb56b6111324b0ad739d38686ac925308a7137bf519cc73c8616df03a045bd49
- clm_f2ec269f2e3f2ff7c61c91bd871c5a30fc0efc097aabfd62e96531345f02a6be
maturity: draft
page_id: pg_b98f34a4be1f537d9171e7380b85d5ee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1f0820e2d76c5238ae71dedc5571fcc8
title: agentsmd/agents.md/AGENTS.md @ d001185d792e
updated_at: '2026-09-14T03:31:48Z'
---

# agentsmd/agents.md/AGENTS.md @ d001185d792e

<!-- rcw:begin owner=source:src_1f0820e2d76c5238ae71dedc5571fcc8 block=evidence -->
- Repository development practice: when adding or updating dependencies, update the relevant lockfile and restart the dev server so Next.js picks up the changes. [@claim:clm_07941e7283cc5537c6664a9cbdb6684e709b6e6aca73079c00798d04cbb1765c]
- Repository development practice: contributors are told to use the dev server (npm/pnpm/yarn run dev) and never run the production build inside an agent session, since it disables hot reload and can leave the dev server inconsistent. [@claim:clm_ba16adfc89c4da687f508b447d50949b9d96f4cc2da11559c22e69b4827c2d98]
- Repository development practice: new components and utilities should preferably be TypeScript (.ts/.tsx), with component-specific styles co-located in the component's folder. [@claim:clm_cb56b6111324b0ad739d38686ac925308a7137bf519cc73c8616df03a045bd49]
- Repository development practice: a commands recap lists npm run dev, lint, test, and build, marking the production build as not to be run during agent sessions. [@claim:clm_f2ec269f2e3f2ff7c61c91bd871c5a30fc0efc097aabfd62e96531345f02a6be]
<!-- rcw:end owner=source:src_1f0820e2d76c5238ae71dedc5571fcc8 block=evidence -->

## Researcher notes

