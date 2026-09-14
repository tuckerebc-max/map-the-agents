---
access: public
aliases: []
claim_ids:
- clm_20f2dcb8b073e39e03dfea3cd5967653eaeb5aaef156f94d2139a5fea584a27f
- clm_33f2d1659583ddf2381bc63fb576f774a8853987e03230f16968b1ae9a670e51
- clm_3d37ba67b7f4146dd98677d44f7ebdfffdc98277eab73f5a148d3723863acbdf
- clm_6fd95171d84cb28be7cff5efa13b7c50098d12f6142e3809cf72fb226bde7876
- clm_ac9b82cfa8f0e7c9e321440ad868bcf358d1acde8b87332207d98bff3a24385e
maturity: draft
page_id: pg_742bdb3913c250e88e22cb5c0017c988
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_035c9a49c9dc5f369e041896e498e515
title: cosmtrek/mindwalk/docs/dynamic-rubric-evaluation.md @ 77cd79596a1b
updated_at: '2026-09-14T03:42:57Z'
---

# cosmtrek/mindwalk/docs/dynamic-rubric-evaluation.md @ 77cd79596a1b

<!-- rcw:begin owner=source:src_035c9a49c9dc5f369e041896e498e515 block=evidence -->
- Verdicts are never decided by the model: Go mechanically rolls up dimension and criterion verdicts from finding severities and coverage grades, strips hallucinated citations, and retries once on invalid output. [@claim:clm_20f2dcb8b073e39e03dfea3cd5967653eaeb5aaef156f94d2139a5fea584a27f]
- The judge subprocess runs sealed: it gets no tools, no MCP servers, no user or project settings, and no session persistence, and it only receives the evaluated session's summary. [@claim:clm_33f2d1659583ddf2381bc63fb576f774a8853987e03230f16968b1ae9a670e51]
- Evaluation reports are cached one per session in ~/.mindwalk/reports, go stale without auto-rerun when session content changes, and reuse the drafted rubric when task wording is unchanged. [@claim:clm_3d37ba67b7f4146dd98677d44f7ebdfffdc98277eab73f5a148d3723863acbdf]
- Session evaluation uses up to two sealed judge calls via the user's own claude or codex CLI: one drafting task-specific criteria from user messages, one unified scoring pass over four fixed process dimensions plus those criteria. [@claim:clm_6fd95171d84cb28be7cff5efa13b7c50098d12f6142e3809cf72fb226bde7876]
- The fixed process dimensions (exploration, scope, wandering, verification) are tuned for code-editing work and can be systematically too harsh on research, debugging, or documentation sessions, per the project's own design doc. [@claim:clm_ac9b82cfa8f0e7c9e321440ad868bcf358d1acde8b87332207d98bff3a24385e]
<!-- rcw:end owner=source:src_035c9a49c9dc5f369e041896e498e515 block=evidence -->

## Researcher notes

