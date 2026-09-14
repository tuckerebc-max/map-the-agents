---
access: public
aliases: []
claim_ids:
- clm_27c081171bad06164eb93a426a4566c05ca9d3c6223a164dd499a368d6236e0f
- clm_be3265a7dcc14ed8a7573a171401d3b9d450c535f19de110ca5c163967454220
- clm_f40285223b5560d9e448ea6dc191593959ffc864c6f687d4383bbfac80190330
maturity: draft
page_id: pg_fd91b2d75f7a5b50b827032c4a3dc381
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bede5d17f0a65650a67cfb0522ae3c39
title: Lore-Hex/QuillCode/docs/CUA_COMPUTER_USE_TEST_PLAN.md @ 9f412834f0d6
updated_at: '2026-09-14T02:14:03Z'
---

# Lore-Hex/QuillCode/docs/CUA_COMPUTER_USE_TEST_PLAN.md @ 9f412834f0d6

<!-- rcw:begin owner=source:src_bede5d17f0a65650a67cfb0522ae3c39 block=evidence -->
- A documented safety limitation: background desktop clicks via the opt-in cua-driver backend can actuate unapproved background apps because the Approved-Apps gate checks only the frontmost app. [@claim:clm_27c081171bad06164eb93a426a4566c05ca9d3c6223a164dd499a368d6236e0f]
- The computer-use backend adopts TryCua's MIT-licensed cua-driver behind the existing ComputerUseBackend seam, verified live against cua-driver 0.8.3. [@claim:clm_be3265a7dcc14ed8a7573a171401d3b9d450c535f19de110ca5c163967454220]
- The cua-driver computer-use backend is off by default and enabled via QUILLCODE_USE_CUA_DRIVER=1, with an optional path override; the agent-facing tools and approval gate are unchanged. [@claim:clm_f40285223b5560d9e448ea6dc191593959ffc864c6f687d4383bbfac80190330]
<!-- rcw:end owner=source:src_bede5d17f0a65650a67cfb0522ae3c39 block=evidence -->

## Researcher notes

