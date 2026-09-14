---
access: public
aliases: []
claim_ids:
- clm_66a13df9cd4a483f69646b172d92ae151b9cac8398b47c67c273da04d44e7669
- clm_6a7ee3f54121c1a2f058a35b05b3d797fe691568dc74221b65388832be43bf0a
- clm_950caac5142aeebb46830f211e4cb125520b8c743b587497c4e2ecb340a01b83
maturity: draft
page_id: pg_55cb60e33d645ff0a0fbaa1e673295d3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_92e7cd4adc1358159089d775f558b57d
title: gastownhall/gastown/docs/agent-provider-integration.md @ 649b832b7672
updated_at: '2026-09-14T03:52:52Z'
---

# gastownhall/gastown/docs/agent-provider-integration.md @ 649b832b7672

<!-- rcw:begin owner=source:src_92e7cd4adc1358159089d775f558b57d block=evidence -->
- A stated key design principle is loose coupling: Gas Town orchestrates agents through tmux and environment variables, without importing or linking agent libraries — integration is configuration, not compilation. [@claim:clm_66a13df9cd4a483f69646b172d92ae151b9cac8398b47c67c273da04d44e7669]
- Agent provider integration is tiered: Tier 0 is zero-change tmux orchestration via send-keys and capture-pane, Tier 1 is a JSON preset in agents.json, Tier 2 adds hooks, and Tier 3 is deep native API integration. [@claim:clm_6a7ee3f54121c1a2f058a35b05b3d797fe691568dc74221b65388832be43bf0a]
- The Tier 0 tmux shim layer is described as timing-sensitive with no delivery confirmation, lacking session resume, automatic context injection, and process-name detection compared to higher integration tiers. [@claim:clm_950caac5142aeebb46830f211e4cb125520b8c743b587497c4e2ecb340a01b83]
<!-- rcw:end owner=source:src_92e7cd4adc1358159089d775f558b57d block=evidence -->

## Researcher notes

