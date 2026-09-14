---
access: public
aliases: []
claim_ids:
- clm_1f0fac13c7f89852bf6109b57f39634dfd2ddb4b8adc113ccc7a0bfe87ef6a9d
- clm_a13609ffb8e96fe43912f5298ebef616c01b55b35ba7fb3a9e6667df47103a0b
- clm_e8db7a7c2c4bc2de2eddcb8c56946fbaea75725eb0228aeb8fdeb7ab85771980
- clm_f1d6bd894219c79a39c6f6aaef054f2bccbb9fb0a387112fa3d265ea7862a016
maturity: draft
page_id: pg_02013ac96cb950d4bb978c660cd9f184
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_de7da90b562656c7ac9b9ae790c251ba
title: jacopone/antigravity-nix/CLAUDE.md @ 0d6f9760ee4d
updated_at: '2026-09-14T04:00:19Z'
---

# jacopone/antigravity-nix/CLAUDE.md @ 0d6f9760ee4d

<!-- rcw:begin owner=source:src_de7da90b562656c7ac9b9ae790c251ba block=evidence -->
- The flake provides three packages: the Antigravity 2.0 Base App (default), the Antigravity IDE, and the `agy` CLI, with GUI binaries wrapped in an FHS environment. [@claim:clm_1f0fac13c7f89852bf6109b57f39634dfd2ddb4b8adc113ccc7a0bfe87ef6a9d]
- Repository development practice: hashes in `artifacts/versions.json` must be real SRI hashes obtained via `nix-prefetch-url` and `nix hash to-sri`; placeholder hashes fail CI before reaching users. [@claim:clm_a13609ffb8e96fe43912f5298ebef616c01b55b35ba7fb3a9e6667df47103a0b]
- A daily GitHub Actions workflow (07:00 UTC) checks Google Cloud Run endpoints for new versions, verifies hashes, builds, and opens auto-merge PRs; release and branch-cleanup workflows follow. [@claim:clm_e8db7a7c2c4bc2de2eddcb8c56946fbaea75725eb0228aeb8fdeb7ab85771980]
- Repository development practice: contributors fork, create a feature branch, test with `nix build` and `nix flake check`, and submit a PR; CLAUDE.md adds build, version-update, and workflow-testing checklists. [@claim:clm_f1d6bd894219c79a39c6f6aaef054f2bccbb9fb0a387112fa3d265ea7862a016]
<!-- rcw:end owner=source:src_de7da90b562656c7ac9b9ae790c251ba block=evidence -->

## Researcher notes

