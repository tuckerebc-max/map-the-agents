---
access: public
aliases: []
claim_ids:
- clm_2eb72eefc16934145c90cddb080826eda4ac296740027a65579b04217429a2bf
- clm_3b4c72cc7897c909e5d2de95ef1897a3e48a6df68ed2038bb988fce84a6930bb
- clm_545e98b621d6a95adbeaecf4c734894274b6252dd19073d51192a6375b91db83
- clm_ad3546ece26e1932c52133eee57202d707c9d4d887d9d9a320ffc5792f83c6eb
maturity: draft
page_id: pg_bf4d5f89a2d25082bda5f3f45a63f9a1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f65d8c557cc0541390a3cca8564853e3
title: sshh12/coding-agents-workshop/race.md @ f89984463925
updated_at: '2026-09-14T04:23:31Z'
---

# sshh12/coding-agents-workshop/race.md @ f89984463925

<!-- rcw:begin owner=source:src_f65d8c557cc0541390a3cca8564853e3 block=evidence -->
- Headless scripts automate the race: race.sh launches claude -p in both dirs with stream-json output, race-reset.sh resets git state and deletes SQLite files, and race-analyze.sh parses timing, tool usage, tokens, and test results. [@claim:clm_2eb72eefc16934145c90cddb080826eda4ac296740027a65579b04217429a2bf]
- The race narrative notes Pydantic 2.9.0 is listed in Version A's requirements but never imported, and alembic and redis are installed but unconfigured. [@claim:clm_3b4c72cc7897c909e5d2de95ef1897a3e48a6df68ed2038bb988fce84a6930bb]
- The race demo has a documented fallback if the live demo fails: play a pre-recorded side-by-side video or walk through the codebases manually. [@claim:clm_545e98b621d6a95adbeaecf4c734894274b6252dd19073d51192a6375b91db83]
- The race demo measures agent performance by giving identical prompts to two agents on the two codebases, comparing files changed, test integrity, timing, and tool usage. [@claim:clm_ad3546ece26e1932c52133eee57202d707c9d4d887d9d9a320ffc5792f83c6eb]
<!-- rcw:end owner=source:src_f65d8c557cc0541390a3cca8564853e3 block=evidence -->

## Researcher notes

