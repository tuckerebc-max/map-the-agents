---
access: public
aliases: []
claim_ids:
- clm_093f811e18a7a7f0a85629e6a9f7dfe7f85aea0d18e7165abdfff6ff2958ce65
- clm_78f9d7a12d59986c836ec66817d65ddd1827c03778fd1fc146ce118a18081657
- clm_e1b36f0681d3738e57f4fdf5ea5d6447d7685f1cadb715be60e239d409a24dbb
maturity: draft
page_id: pg_143a1e65681a5f7282e9795b522f5458
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7703344396ae5857bf335a317b167f5e
title: truefoundry/trueforge/RELEASING.md @ 4bf9ce063019
updated_at: '2026-09-14T03:19:56Z'
---

# truefoundry/trueforge/RELEASING.md @ 4bf9ce063019

<!-- rcw:begin owner=source:src_7703344396ae5857bf335a317b167f5e block=evidence -->
- Repository development practice: fork PRs should change source only while maintainers regenerate the SDK after merge; releases use Changesets on main, npm trusted publishing via OIDC (no NPM_TOKEN), and a chart-release pipeline triggered after the trueforge npm publish. [@claim:clm_093f811e18a7a7f0a85629e6a9f7dfe7f85aea0d18e7165abdfff6ff2958ce65]
- The project requires Node.js >= 22.14, is MIT-licensed, and its Helm chart bundles optional Bitnami Postgres and Redis subcharts that can be disabled via postgresql.enabled=false / redis.enabled=false. [@claim:clm_78f9d7a12d59986c836ec66817d65ddd1827c03778fd1fc146ce118a18081657]
- The repo ships four npm packages: trueforge-core (library), trueforge (app + CLI, tarball includes dist/_frontend/), trueforge-sdk (Fern-generated, not hand-edited), and trueforge-ui (embeddable chat UI); packages/frontend is unpublished and its build is copied into the trueforge tarball. [@claim:clm_e1b36f0681d3738e57f4fdf5ea5d6447d7685f1cadb715be60e239d409a24dbb]
<!-- rcw:end owner=source:src_7703344396ae5857bf335a317b167f5e block=evidence -->

## Researcher notes

