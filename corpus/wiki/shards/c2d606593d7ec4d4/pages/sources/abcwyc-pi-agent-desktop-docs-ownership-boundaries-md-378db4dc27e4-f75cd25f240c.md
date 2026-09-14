---
access: public
aliases: []
claim_ids:
- clm_4eb915dd780f40054391d925df0c9cb362363e3758242172a87a8113c12c9d45
- clm_fda93dedc2fe9dc44c65e97d701d8b60eb075c4e637b7c5a3679bcde06471f56
maturity: draft
page_id: pg_2e39e0efae155397ae2cf75cd25f240c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_71deb2f6a5ec5cdbb551448ada5f5869
title: abcwyc/pi-agent-desktop/docs/ownership-boundaries.md @ 378db4dc27e4
updated_at: '2026-09-14T01:59:03Z'
---

# abcwyc/pi-agent-desktop/docs/ownership-boundaries.md @ 378db4dc27e4

<!-- rcw:begin owner=source:src_71deb2f6a5ec5cdbb551448ada5f5869 block=evidence -->
- Repository development practice: a nightly component-updates workflow syncs upstream pi and pi-web releases, intersecting changes with fork-ownership.json and running the full gate before pushing to main or opening a PR. [@claim:clm_4eb915dd780f40054391d925df0c9cb362363e3758242172a87a8113c12c9d45]
- The app bundles three components: the desktop shell authored in this fork, the pi agent runtime as an npm dependency, and the pi-web UI merged from an upstream release tag. [@claim:clm_fda93dedc2fe9dc44c65e97d701d8b60eb075c4e637b7c5a3679bcde06471f56]
<!-- rcw:end owner=source:src_71deb2f6a5ec5cdbb551448ada5f5869 block=evidence -->

## Researcher notes

