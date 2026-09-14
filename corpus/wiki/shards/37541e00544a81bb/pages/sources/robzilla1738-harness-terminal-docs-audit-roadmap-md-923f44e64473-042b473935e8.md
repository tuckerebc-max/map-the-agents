---
access: public
aliases: []
claim_ids:
- clm_1634d253f6758eb84a9ec13893d3bc44540d0943bade947bf17ef5b7f8255ec0
- clm_27eaee531bfc71a17a05c10cf1ee4d54881000b8961357400e35f8b4b2bc3552
- clm_81d61ef732659003886a59996f86a6b7832915a08f68cf51a0e5a23cb08c3302
maturity: draft
page_id: pg_686d85b126255c329fd8042b473935e8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0028f77469c653dc80ecd2d75df26e43
title: robzilla1738/harness-terminal/docs/AUDIT_ROADMAP.md @ 923f44e64473
updated_at: '2026-09-14T02:36:11Z'
---

# robzilla1738/harness-terminal/docs/AUDIT_ROADMAP.md @ 923f44e64473

<!-- rcw:begin owner=source:src_0028f77469c653dc80ecd2d75df26e43 block=evidence -->
- A 42-agent audit workflow (parallel finders, adversarial verification, synthesis, completeness critic) produced 101 findings with 28 adversarially verified, and reported parity scores such as VT core 90%, input protocols 92%, and tmux commands 85% versus ghostty/tmux. [@claim:clm_1634d253f6758eb84a9ec13893d3bc44540d0943bade947bf17ef5b7f8255ec0]
- The audit roadmap states the daemon uses single-lock serialization as a documented correctness invariant, and the daemon control socket is secured with 0o600 permissions plus a peer-UID check; OSC 52 clipboard reads are silently refused. [@claim:clm_27eaee531bfc71a17a05c10cf1ee4d54881000b8961357400e35f8b4b2bc3552]
- The audit identified gaps later fixed via shipped PRs, including a paste escape-injection bug, missing DECSTR/REP/IRM/DECOM handlers, DCS misrouting into the Sixel decoder, and Kitty graphics being display-only; animation (a=a) and iTerm2 multipart upload remain deliberately deferred. [@claim:clm_81d61ef732659003886a59996f86a6b7832915a08f68cf51a0e5a23cb08c3302]
<!-- rcw:end owner=source:src_0028f77469c653dc80ecd2d75df26e43 block=evidence -->

## Researcher notes

