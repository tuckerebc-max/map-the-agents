---
access: public
aliases: []
claim_ids:
- clm_2b3acfa713a425ff1c1d1d27ad16cff190ab5e9e5f67213a8a7d783831ff7c53
- clm_82f86f56c02c3003ff186abb3e7472b3e50f675c6341557a234cb632efe71f7a
- clm_eae6dd8cc17c310ec477b5c9cae1668f9131230091e2b4464c105443035951e7
maturity: draft
page_id: pg_2f5cd29011ba5e9db85affdbc2f17c58
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f9ba73776a315be7971d4f949e97603b
title: shrijayan/itwillsync/CONTRIBUTING.md @ f12b57bf7385
updated_at: '2026-09-14T02:39:54Z'
---

# shrijayan/itwillsync/CONTRIBUTING.md @ f12b57bf7385

<!-- rcw:begin owner=source:src_f9ba73776a315be7971d4f949e97603b block=evidence -->
- Repository development practice: code style is TypeScript with ESM modules, no linter is enforced yet (follow existing patterns), dependencies should stay minimal, and contributions are MIT-licensed. [@claim:clm_2b3acfa713a425ff1c1d1d27ad16cff190ab5e9e5f67213a8a7d783831ff7c53]
- The monorepo contains packages for the CLI (main npm package), a web-client browser terminal, a hub dashboard daemon, a landing page, and VitePress docs. [@claim:clm_82f86f56c02c3003ff186abb3e7472b3e50f675c6341557a234cb632efe71f7a]
- Repository development practice: contributors use Node 22+ via nvm and pnpm 10+, build packages in order (web-client, hub, CLI) with pnpm build, run pnpm test (optionally with --coverage), and open focused PRs against main with tests and passing CI. [@claim:clm_eae6dd8cc17c310ec477b5c9cae1668f9131230091e2b4464c105443035951e7]
<!-- rcw:end owner=source:src_f9ba73776a315be7971d4f949e97603b block=evidence -->

## Researcher notes

