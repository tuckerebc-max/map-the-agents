---
access: public
aliases: []
claim_ids:
- clm_1e9b4a1f8073d7f2ea1b51736a8a23674daacae454333973dc5e4ea907efed5d
- clm_688557c894870f0a0af1d0b7298c49ddf2b214c57287e5eacd675ecb1a47a8b6
- clm_b6afab1e67a0dbdef4bb09a92a7b3dad69c815b14b93c8d8e84b2fe246e4f4a2
- clm_d3915434ca37350a01dd12891fc7cf3cc2da35a40846decc6a922a366962f851
maturity: draft
page_id: pg_4724b15bded252b79c7256f3146ea6d8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_df0dc25607b7544aa3ee6644fc12c916
title: echoVic/blade-code/docs/en/configuration/permissions.md @ 8917e4e0ef61
updated_at: '2026-09-14T02:00:47Z'
---

# echoVic/blade-code/docs/en/configuration/permissions.md @ 8917e4e0ef61

<!-- rcw:begin owner=source:src_df0dc25607b7544aa3ee6644fc12c916 block=evidence -->
- The runtime offers four permission modes (default, autoEdit, plan, yolo); Shift+Tab cycles the first three in the TUI, while yolo requires an explicit command, launch argument, or setting. [@claim:clm_1e9b4a1f8073d7f2ea1b51736a8a23674daacae454333973dc5e4ea907efed5d]
- A maxTurns setting caps model rounds (0 disables, -1 unlimited, N>0 limits); recovery paths such as output-length correction, Stop hooks, and mid-turn input cannot bypass it, and non-interactive callers without a continuation callback receive max_turns_exceeded. [@claim:clm_688557c894870f0a0af1d0b7298c49ddf2b214c57287e5eacd675ecb1a47a8b6]
- Permission rules use Tool(param:value) syntax with picomatch * and ** wildcards, evaluated in order deny > allow > ask > default (ask), covering file paths, Bash commands, and WebFetch/WebSearch URL patterns. [@claim:clm_b6afab1e67a0dbdef4bb09a92a7b3dad69c815b14b93c8d8e84b2fe246e4f4a2]
- When a rule resolves to ask, a confirmation dialog offers Once/Session/Project/Deny; Session authorizations live only in runtime memory and expire with the session, while Project writes the rule to .blade/settings.local.json. [@claim:clm_d3915434ca37350a01dd12891fc7cf3cc2da35a40846decc6a922a366962f851]
<!-- rcw:end owner=source:src_df0dc25607b7544aa3ee6644fc12c916 block=evidence -->

## Researcher notes

