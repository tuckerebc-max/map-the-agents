---
access: public
aliases: []
claim_ids:
- clm_c99b008d74db552cc37541c39f16eb8bdd9f0c8aede342b037ae08b384a0292c
maturity: draft
page_id: pg_167fe1d30b4a5e78a0c87b882ffaec57
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07758cc2fa085f6b9fec02ce849bc834
title: hotovo/aider-desk/docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md
  @ cb7ee89bf213
updated_at: '2026-09-14T02:04:46Z'
---

# hotovo/aider-desk/docs/adr/agent-system/0007-agent-profiles-and-system-prompts.md @ cb7ee89bf213

<!-- rcw:begin owner=source:src_07758cc2fa085f6b9fec02ce849bc834 block=evidence -->
- Agent behavior is modeled as AgentProfile entities managed by agent-profile-manager.ts, with system prompts assembled via a prompts system supporting placeholder substitution; subagents are profiles invoked by a parent profile. [@claim:clm_c99b008d74db552cc37541c39f16eb8bdd9f0c8aede342b037ae08b384a0292c]
<!-- rcw:end owner=source:src_07758cc2fa085f6b9fec02ce849bc834 block=evidence -->

## Researcher notes

