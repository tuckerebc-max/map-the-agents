---
access: public
aliases: []
claim_ids:
- clm_2408e8f33183dcd90e2ff8396d9e8056f0117cf12876ef72c30161a837da3c89
- clm_3dc4bafe7ae41a81772fe7063e68430f8163578031ae6c0113ad264770e6a7a0
- clm_4d9e084e52aebd01a63ef21deb59a10ecda8e047199fe5d28a37469d293e15a1
- clm_660a173d9b27c35f74bfa43ba91ce0d633d206d9c26673ab15560e4832570687
- clm_7a763f6f905b4edb71d175b28021efd7ec78915dcb8c4aa4593b542ead89a167
- clm_8a908aa0db557dcadaacbe630929da67d1b031907ca55d3d8243a7d9fed71b82
- clm_e22c83a7df8d3c7a5bcc5094a8841d3d99472d82df2767efffb365d120c2d8c7
maturity: draft
page_id: pg_24b761189bad5b31827932e931928054
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9d9cac9282ba5e158b3ae8128df8efa3
title: irgolic/AutoPR/USAGE.md @ a95671a20d8d
updated_at: '2026-09-14T02:05:59Z'
---

# irgolic/AutoPR/USAGE.md @ a95671a20d8d

<!-- rcw:begin owner=source:src_9d9cac9282ba5e158b3ae8128df8efa3 block=evidence -->
- The plan_and_code agent accepts agent_config options: planning_actions, codegen_actions, and max_codegen_iterations (default 5). [@claim:clm_2408e8f33183dcd90e2ff8396d9e8056f0117cf12876ef72c30161a837da3c89]
- AutoPR is a GitHub Action that automatically writes pull requests in response to issues, per its usage guide. [@claim:clm_3dc4bafe7ae41a81772fe7063e68430f8163578031ae6c0113ad264770e6a7a0]
- The action requires an OpenAI API key with ChatGPT access, supplied via the OPENAI_API_KEY secret. [@claim:clm_4d9e084e52aebd01a63ef21deb59a10ecda8e047199fe5d28a37469d293e15a1]
- AutoPR is documented as not optimized for gpt-3.5-turbo; users with gpt-4 API access are advised to use that instead. [@claim:clm_660a173d9b27c35f74bfa43ba91ce0d633d206d9c26673ab15560e4832570687]
- Documented inputs include github_token (required), base_branch (default main), model (default gpt-4), context_limit (8192), min/max_tokens, num_reasks, temperature, agent_id (default plan_and_code), and overwrite_existing. [@claim:clm_7a763f6f905b4edb71d175b28021efd7ec78915dcb8c4aa4593b542ead89a167]
- The action is invoked as docker://ghcr.io/irgolic/autopr:latest and configured through workflow 'with:' parameters such as github_token and model. [@claim:clm_8a908aa0db557dcadaacbe630929da67d1b031907ca55d3d8243a7d9fed71b82]
- Triggered runs create a branch named autopr/issue-# and open a PR to the base branch; an existing branch is overwritten by default behavior described in the usage steps. [@claim:clm_e22c83a7df8d3c7a5bcc5094a8841d3d99472d82df2767efffb365d120c2d8c7]
<!-- rcw:end owner=source:src_9d9cac9282ba5e158b3ae8128df8efa3 block=evidence -->

## Researcher notes

