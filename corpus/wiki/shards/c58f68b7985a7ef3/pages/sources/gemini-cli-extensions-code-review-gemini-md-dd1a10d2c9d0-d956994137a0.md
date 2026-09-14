---
access: public
aliases: []
claim_ids:
- clm_3108043ff185cbb892cf1948165b98cd3702bd758ac2df0f53c3b884ab849047
- clm_496444317e55db264bc44bb8c08df7b6958a2c55bba59d844439472fe7cdadcb
maturity: draft
page_id: pg_0e615ea916555ea58a11d956994137a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b1d40a1458b25358bf924f9e65318e6e
title: gemini-cli-extensions/code-review/GEMINI.md @ dd1a10d2c9d0
updated_at: '2026-09-14T03:52:39Z'
---

# gemini-cli-extensions/code-review/GEMINI.md @ dd1a10d2c9d0

<!-- rcw:begin owner=source:src_b1d40a1458b25358bf924f9e65318e6e block=evidence -->
- GEMINI.md names the pull-request command /pr-review while the README calls it /pr-code-review, suggesting a possible naming inconsistency between the two files. [@claim:clm_3108043ff185cbb892cf1948165b98cd3702bd758ac2df0f53c3b884ab849047]
- The bundled GEMINI.md instructs the CLI agent to prefer /code-review when users request change reviews, and for PR review to check $REPOSITORY, $PULL_REQUEST_NUMBER, and $ADDITIONAL_CONTEXT, asking for clarification if missing or ambiguous. [@claim:clm_496444317e55db264bc44bb8c08df7b6958a2c55bba59d844439472fe7cdadcb]
<!-- rcw:end owner=source:src_b1d40a1458b25358bf924f9e65318e6e block=evidence -->

## Researcher notes

