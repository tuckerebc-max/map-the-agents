---
access: public
aliases: []
claim_ids:
- clm_12c5c4229190e5f94a6a6c4c22a3841cfc4f3c8ace3ee99e1a065d0199f9e961
- clm_4594211eef566e525b89c7fe4560ec6c21a9052567f49a20c1ef8211caec6d1b
maturity: draft
page_id: pg_1c0e1bc0b66553d6aebe305bf355de36
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_780362ef2015543c9569170ae5c9bee0
title: jcz2020/par/docs/sdk/skills.md @ 4b593db4465d
updated_at: '2026-09-14T02:07:13Z'
---

# jcz2020/par/docs/sdk/skills.md @ 4b593db4465d

<!-- rcw:begin owner=source:src_780362ef2015543c9569170ae5c9bee0 block=evidence -->
- Skills are markdown files under ~/.par/skills/<id>/skill.md with YAML frontmatter (schema_version, id, trigger, tool_filter, system_prompt_override), auto-discovered and activated by Auto, Manual, or Keyword triggers. [@claim:clm_12c5c4229190e5f94a6a6c4c22a3841cfc4f3c8ace3ee99e1a065d0199f9e961]
- Skill markdown bodies are lazy-loaded only on activation, and total skill description tokens are capped at 2048 by default via skill_token_budget, dropping lowest-priority descriptions with a warning. [@claim:clm_4594211eef566e525b89c7fe4560ec6c21a9052567f49a20c1ef8211caec6d1b]
<!-- rcw:end owner=source:src_780362ef2015543c9569170ae5c9bee0 block=evidence -->

## Researcher notes

