---
access: public
aliases: []
claim_ids:
- clm_699acd4ba97d5823bd8f1cabd51fefe13fb8f06327cffd3255dc264d1b2d93bc
maturity: draft
page_id: pg_dbe1aa9d9dc85a8bab7c30071948528b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0545ea67657053e89b075342eb81c6a1
title: shoyann/thrush-swe-agent/docs/adr/0001-default-auto-runs-to-docker.md @ daef0a6d6a6d
updated_at: '2026-09-14T02:40:06Z'
---

# shoyann/thrush-swe-agent/docs/adr/0001-default-auto-runs-to-docker.md @ daef0a6d6a6d

<!-- rcw:begin owner=source:src_0545ea67657053e89b075342eb81c6a1 block=evidence -->
- Auto Runs execute mini-swe-agent in a Docker environment by default because the agent runs autonomously; local shell execution is an explicit advanced opt-in that gives the agent unrestricted host command access. [@claim:clm_699acd4ba97d5823bd8f1cabd51fefe13fb8f06327cffd3255dc264d1b2d93bc]
<!-- rcw:end owner=source:src_0545ea67657053e89b075342eb81c6a1 block=evidence -->

## Researcher notes

