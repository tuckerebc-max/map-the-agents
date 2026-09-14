---
access: public
aliases: []
claim_ids:
- clm_1c7f0af6ae4b2123933e56ea49dacca108233d152a64b8d14229a275dbb443b6
- clm_4e2eca492102310199b71e3bedb3655e5a502eef81f51c34cbf0aeb59c959348
maturity: draft
page_id: pg_7bcae1dbcc7c54fab462f64809049a34
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2cecbf6e140055deaf2b3ee06da213e7
title: superloglabs/superlog/docs/github-app-setup.md @ feffc9fd542a
updated_at: '2026-09-14T03:17:02Z'
---

# superloglabs/superlog/docs/github-app-setup.md @ feffc9fd542a

<!-- rcw:begin owner=source:src_2cecbf6e140055deaf2b3ee06da213e7 block=evidence -->
- The GitHub App is configured with minimum repository permissions: Contents read/write to read files and push fix branches, Pull requests read/write to open/update/merge PRs, Issues read/write for comments, and read-only Metadata; no account or organization permissions are required. [@claim:clm_1c7f0af6ae4b2123933e56ea49dacca108233d152a64b8d14229a275dbb443b6]
- The agent integrates with GitHub via a GitHub App using two OAuth callback URLs on the API: /github/install/callback for the connect/install flow and /github/author/callback for a commit-author OAuth flow. [@claim:clm_4e2eca492102310199b71e3bedb3655e5a502eef81f51c34cbf0aeb59c959348]
<!-- rcw:end owner=source:src_2cecbf6e140055deaf2b3ee06da213e7 block=evidence -->

## Researcher notes

