---
access: public
aliases: []
claim_ids:
- clm_43e04a65e57fe98db28e142c59b407dfe49e3fa4eb704b861079c96124795628
- clm_4c36484d66c9001ef9c48d7ed1505cc9193e6632f1e0a53a49028da3fcf77a6a
- clm_b8313bf54a7739d54148bc81fcc6939fd4770d682ef263649a5ad94d6bbeec5c
- clm_c82bcc38c5d66716392763634a1e48caa3203ca3a2d272fc543266900f08a203
maturity: draft
page_id: pg_ca929ba58fca558383910d2236e1bc98
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_13d8ee4f54f95c4bacf29c91d3843b39
title: markshust/hcf/CHANGELOG.md @ 9cfca7de63c3
updated_at: '2026-09-14T04:08:07Z'
---

# markshust/hcf/CHANGELOG.md @ 9cfca7de63c3

<!-- rcw:begin owner=source:src_13d8ee4f54f95c4bacf29c91d3843b39 block=evidence -->
- Discovery failures are treated as hard errors (exit 3 for invalid phase/mode, exit 4 for mid-run enrollment change) rather than empty hooks, reflecting a design preference for failing loudly over silently running a different pipeline. [@claim:clm_43e04a65e57fe98db28e142c59b407dfe49e3fa4eb704b861079c96124795628]
- A malformed plansDir value (absolute path, .. segment, or empty string) stops the run rather than falling back to the default plans directory, and the resolver avoids a jq dependency. [@claim:clm_4c36484d66c9001ef9c48d7ed1505cc9193e6632f1e0a53a49028da3fcf77a6a]
- HCF does not migrate plan folders when the plans directory changes; the user must move them, and project-update warns if .claude/plans still holds plan folders after a move. [@claim:clm_b8313bf54a7739d54148bc81fcc6939fd4770d682ef263649a5ad94d6bbeec5c]
- Repository development practice: contributors fork, create a feature branch, test locally with --plugin-dir, add a CHANGELOG [Unreleased] entry for user-visible changes, and submit a pull request; the repo's own test suite runs via ./tests/run-tests.sh with no dependencies beyond bash/awk/sed/sort/grep. [@claim:clm_c82bcc38c5d66716392763634a1e48caa3203ca3a2d272fc543266900f08a203]
<!-- rcw:end owner=source:src_13d8ee4f54f95c4bacf29c91d3843b39 block=evidence -->

## Researcher notes

