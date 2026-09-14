---
access: public
aliases: []
claim_ids:
- clm_03542652bab2197f1e2d62c324e18afe732a4f8ce64d9835c99b5823382ebc25
- clm_df20135ae712835550d9c75edf542d45694f3d026f677929c3f55ff9c23d8595
- clm_f937581a41e9eb47c8de8c28b35dfff381421fc8c6943ce9e2ba755a1aa382a9
maturity: draft
page_id: pg_8e67da4999e954a8b85af677f60faf4f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3b7da76d300e559a84a8a7db1fa022a4
title: Gitlawb/zero/docs/AGENT_EVALS.md @ c1937dfac72e
updated_at: '2026-09-14T01:52:26Z'
---

# Gitlawb/zero/docs/AGENT_EVALS.md @ c1937dfac72e

<!-- rcw:begin owner=source:src_3b7da76d300e559a84a8a7db1fa022a4 block=evidence -->
- The eval bench changed-file scoring uses `git status --porcelain` against a baseline, so an agent that commits its own changes defeats the expectedChangedFiles check. [@claim:clm_03542652bab2197f1e2d62c324e18afe732a4f8ce64d9835c99b5823382ebc25]
- Zero ships an agent-eval harness (`zero eval`) with validate, run, and bench modes that score agent runs against fixture suites using verification commands, changed-file expectations, context checks, and required trace events. [@claim:clm_df20135ae712835550d9c75edf542d45694f3d026f677929c3f55ff9c23d8595]
- Repository development practice: contributors run `go test ./...`, and the internal/agenteval tests validate every suite JSON file, rejecting missing task IDs, empty verification commands, and malformed changed-file expectations. [@claim:clm_f937581a41e9eb47c8de8c28b35dfff381421fc8c6943ce9e2ba755a1aa382a9]
<!-- rcw:end owner=source:src_3b7da76d300e559a84a8a7db1fa022a4 block=evidence -->

## Researcher notes

