---
access: public
aliases: []
claim_ids:
- clm_0819eb7020fb14be456ce1284b0ccb9b6f9305f7e4593a98c855f8df64fdadbf
- clm_59e6a2953b2025f067819b07959a163447c9c670c2aaefceb97e88044a9f4860
- clm_87d6f46280444c64c484e474c34a3cafde30b29dc8cadc3e1c7e355f7642348f
- clm_b89cb351da0d7fd4344434d8b81ada1f14a922c4efa1822d6399c8a92d93788c
- clm_d1115bd2a6c72aca659cafa27940cbf4cacacc2ceadff376c4017b34b79f7d6b
- clm_d97216d1dd68b61fa06a0d1d5ee7ecbfd8d2909a479c2f0e1e100bf92a09bc68
maturity: draft
page_id: pg_ae31a0675df559fc89a3b7b4ca5fce78
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3d8c6ddb76ab57ea9dbe985900dd1d7c
title: sweepai/sweep/docs/pages/usage/config.mdx @ a8b8b67bda4f
updated_at: '2026-09-14T03:16:50Z'
---

# sweepai/sweep/docs/pages/usage/config.mdx @ a8b8b67bda4f

<!-- rcw:begin owner=source:src_3d8c6ddb76ab57ea9dbe985900dd1d7c block=evidence -->
- By default Sweep reads logs and outputs from the repository's existing GitHub Actions runs; gha_enabled: False disables this. [@claim:clm_0819eb7020fb14be456ce1284b0ccb9b6f9305f7e4593a98c855f8df64fdadbf]
- The blocked_dirs setting lists directories Sweep will not edit, e.g. .github/, restricting its write access within a repository. [@claim:clm_59e6a2953b2025f067819b07959a163447c9c670c2aaefceb97e88044a9f4860]
- Sweep is configured through a sweep.yaml file placed in the repository root, and Sweep can open a PR adding that config file after the first issue. [@claim:clm_87d6f46280444c64c484e474c34a3cafde30b29dc8cadc3e1c7e355f7642348f]
- When draft mode is enabled, all pull requests are created as drafts and GitHub Actions are not triggered for them. [@claim:clm_b89cb351da0d7fd4344434d8b81ada1f14a922c4efa1822d6399c8a92d93788c]
- Repository development practice: the project's own sweep.yaml description instructs that sweepai/sweep is a Python 3.10 project with main API endpoints in sweepai/api.py and that code should adhere to PEP8. [@claim:clm_d1115bd2a6c72aca659cafa27940cbf4cacacc2ceadff376c4017b34b79f7d6b]
- The sweep.yaml config supports keys gha_enabled, branch, blocked_dirs, draft, and description, controlling GitHub Actions reading, target branch, excluded directories, draft PRs, and repo context. [@claim:clm_d97216d1dd68b61fa06a0d1d5ee7ecbfd8d2909a479c2f0e1e100bf92a09bc68]
<!-- rcw:end owner=source:src_3d8c6ddb76ab57ea9dbe985900dd1d7c block=evidence -->

## Researcher notes

