---
access: public
aliases: []
claim_ids:
- clm_691fd690eead13be218f2520a2f8cde945841369f65328d62667bf1c83d45754
- clm_6b6235502d377abfb7244e922251b87dd7379f7f136f3e694c2665c997add103
- clm_b16214a73cf65b452dcaea65c42921655f7e9ffbe1710bfcbb0c9d4972bb1a7c
maturity: draft
page_id: pg_a99e1a645d92549fb8a6c61f7a640a5c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f89d513d9ad25ceabffd953b28a30c91
title: SWE-agent/SWE-agent/docs/background/architecture.md @ 3ea751c087f3
updated_at: '2026-09-14T03:16:49Z'
---

# SWE-agent/SWE-agent/docs/background/architecture.md @ 3ea751c087f3

<!-- rcw:begin owner=source:src_f89d513d9ad25ceabffd953b28a30c91 block=evidence -->
- A HistoryProcessor compresses the conversation history to make best use of the model's context window, and a parser extracts the action from the model output before it is executed in the shell session via SWEEnv. [@claim:clm_691fd690eead13be218f2520a2f8cde945841369f65328d62667bf1c83d45754]
- The central entry point is the sweagent CLI, which initializes a SWEEnv environment wrapper (a thin wrapper around SWE-ReX since 1.0) and an Agent class whose forward() method prompts the model and executes its action. [@claim:clm_6b6235502d377abfb7244e922251b87dd7379f7f136f3e694c2665c997add103]
- SWEEnv relies on the SWE-ReX package: its Deployment starts a local Docker container or a remote container (e.g. modal or aws) and starts a shell session inside it that executes commands. [@claim:clm_b16214a73cf65b452dcaea65c42921655f7e9ffbe1710bfcbb0c9d4972bb1a7c]
<!-- rcw:end owner=source:src_f89d513d9ad25ceabffd953b28a30c91 block=evidence -->

## Researcher notes

