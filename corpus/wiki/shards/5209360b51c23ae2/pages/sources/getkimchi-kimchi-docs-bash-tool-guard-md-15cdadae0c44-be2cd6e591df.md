---
access: public
aliases: []
claim_ids:
- clm_26bb09ef3ecde25545d76e7adf143a9caae8b79be747cf7e9593e886638f22b2
maturity: draft
page_id: pg_f7649fe7161356509f74be2cd6e591df
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_48a83400c6ac5d4da1ad4576b21a4817
title: getkimchi/kimchi/docs/bash-tool-guard.md @ 15cdadae0c44
updated_at: '2026-09-14T01:51:06Z'
---

# getkimchi/kimchi/docs/bash-tool-guard.md @ 15cdadae0c44

<!-- rcw:begin owner=source:src_48a83400c6ac5d4da1ad4576b21a4817 block=evidence -->
- A bash-tool guard steers the model away from shell commands that duplicate dedicated tools, flagging patterns like `cat`, `sed -i`, and output redirection, and suggesting read/edit/write instead; stream targets like /dev/null are exempt. [@claim:clm_26bb09ef3ecde25545d76e7adf143a9caae8b79be747cf7e9593e886638f22b2]
<!-- rcw:end owner=source:src_48a83400c6ac5d4da1ad4576b21a4817 block=evidence -->

## Researcher notes

