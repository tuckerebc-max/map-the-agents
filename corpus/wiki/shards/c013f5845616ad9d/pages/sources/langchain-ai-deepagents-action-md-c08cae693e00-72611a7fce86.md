---
access: public
aliases: []
claim_ids:
- clm_34f4a5ebe5ed14fae7dc3a7447090b3c64d3944acbbb844011d8ee9b204b5ba5
- clm_aedaaa38be07471c52dcdf1792330f70e02144a092d146315056d4296228620e
- clm_e0d10f5857f8e11d9dfa4e38506e90c283187c0f5e18c995f0920290f54f9c26
maturity: draft
page_id: pg_dcc3b7a8dedf5c06a40f72611a7fce86
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e0cc30d53872579db1f72f8c99bd20de
title: langchain-ai/deepagents/ACTION.md @ c08cae693e00
updated_at: '2026-09-14T02:10:56Z'
---

# langchain-ai/deepagents/ACTION.md @ c08cae693e00

<!-- rcw:begin owner=source:src_e0cc30d53872579db1f72f8c99bd20de block=evidence -->
- The repository's root action.yml runs dcode non-interactively in GitHub Actions, with inputs for prompt, model, API keys, shell_allow_list, max_turns, task_timeout, quiet, and json output. [@claim:clm_34f4a5ebe5ed14fae7dc3a7447090b3c64d3944acbbb844011d8ee9b204b5ba5]
- In the GitHub Action, shell commands are permitted via a shell_allow_list input; interactive-only options like --auto-approve are intentionally not exposed. [@claim:clm_aedaaa38be07471c52dcdf1792330f70e02144a092d146315056d4296228620e]
- The GitHub Action enables persistent memory by default through actions/cache, with memory_scope (pr, branch, or repo) and agent_name inputs controlling cache sharing and separation. [@claim:clm_e0d10f5857f8e11d9dfa4e38506e90c283187c0f5e18c995f0920290f54f9c26]
<!-- rcw:end owner=source:src_e0cc30d53872579db1f72f8c99bd20de block=evidence -->

## Researcher notes

