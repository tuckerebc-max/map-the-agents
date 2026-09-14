---
access: public
aliases: []
claim_ids:
- clm_0c12ac598840de1d240853f7894df7c1af5156a02b57b7dc602dc169e4ad271c
- clm_2a2353bea03c8280a40b04662eb0a4d0823fb74a0e0d1cda4460d532d3c3faff
- clm_351188e71d23d66b0f6244052fa9c8a7e615a26f9a71c7801bdce4688162ab51
- clm_bcab83a0d9115abec8ffdc6c784f16baca14f9faa4ad507429688007dac9c093
maturity: draft
page_id: pg_fc492f4becfe5d82a31b42800f92d1a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e80b8b4502255bf190c104fc44e271dd
title: JuliusBrussee/cavemem/CLAUDE.md @ 166078dd7c46
updated_at: '2026-09-14T04:02:15Z'
---

# JuliusBrussee/cavemem/CLAUDE.md @ 166078dd7c46

<!-- rcw:begin owner=source:src_e80b8b4502255bf190c104fc44e271dd block=evidence -->
- Repository development practice: an end-to-end publish script (scripts/e2e-publish.sh) must pass in CI before changeset publish, driving real hook events, FTS search, and the MCP server in an isolated install prefix. [@claim:clm_0c12ac598840de1d240853f7894df7c1af5156a02b57b7dc602dc169e4ad271c]
- Repository development practice: contributors must pass four gates (pnpm typecheck, lint, test, build) before merging, add changesets for package changes, use Conventional Commits, and get one review on PRs. [@claim:clm_2a2353bea03c8280a40b04662eb0a4d0823fb74a0e0d1cda4460d532d3c3faff]
- The npm package cavemem installs globally via npm; the default embedding provider is local (Transformers.js per CLAUDE.md), with ollama and openai as opt-in remote providers. [@claim:clm_351188e71d23d66b0f6244052fa9c8a7e615a26f9a71c7801bdce4688162ab51]
- An evals/ harness measures compression performance: fixtures verify determinism and technical-token round-trip, and the benchmark corpus requires at least 30% average token reduction (targets of 40% at full and 55% at ultra intensity). [@claim:clm_bcab83a0d9115abec8ffdc6c784f16baca14f9faa4ad507429688007dac9c093]
<!-- rcw:end owner=source:src_e80b8b4502255bf190c104fc44e271dd block=evidence -->

## Researcher notes

