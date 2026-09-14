---
access: public
aliases: []
claim_ids:
- clm_012fc4f7c4358bb86baffaa6b8f41684c2192a294d503728854f43555a4575e1
- clm_6bbcbe2232fc08a532ad3efc1fa8801fb598de1dd55862feb0c927439a7e1c4f
maturity: draft
page_id: pg_84b39112c4325b0480996f56fa40cb7d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_625193df09b65913974bbb4b68a35ef1
title: ramarlina/agx/docs/superpowers/plans/2026-04-17-github-integration-phase1.md
  @ e674cec11088
updated_at: '2026-09-14T02:34:58Z'
---

# ramarlina/agx/docs/superpowers/plans/2026-04-17-github-integration-phase1.md @ e674cec11088

<!-- rcw:begin owner=source:src_625193df09b65913974bbb4b68a35ef1 block=evidence -->
- The planned GitHub integration would store PRs, comments, links, and sync state in a dedicated SQLite database at ~/.agx/github/prs.sqlite (env-overridable), mirroring the existing Linear adapter pattern; this is planned, not verified as shipped. [@claim:clm_012fc4f7c4358bb86baffaa6b8f41684c2192a294d503728854f43555a4575e1]
- Repository development practice: a GitHub-integration Phase 1 plan instructs agentic workers to use superpowers subagent-driven-development or executing-plans, building schema, stores, OAuth stubs, a link resolver, and sync orchestrator behind an AGX_GITHUB_ENABLED feature flag, TDD-style with Jest and mocked HTTP. [@claim:clm_6bbcbe2232fc08a532ad3efc1fa8801fb598de1dd55862feb0c927439a7e1c4f]
<!-- rcw:end owner=source:src_625193df09b65913974bbb4b68a35ef1 block=evidence -->

## Researcher notes

