---
access: public
aliases: []
claim_ids:
- clm_7c5f892d169b977226e2500467871b71343df62d2d007f33437254d597d624be
- clm_b5f9b3c639ca7fe384065b7558a08b8ac24d2eb63eed2c6750b6b5f4771932e7
- clm_d32e1ab6efdbc6ca898ebed2bc6735352397d1f30806cbeba97599adfe1c2174
- clm_d82042df7cf48253c27f0a9a7220288d44c40d5603848b02cd3603158acb4cd7
maturity: draft
page_id: pg_5f0e95ae1dee554f95fae58f30de8d20
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_13e7842fe45a502a877ecf2c03133646
title: warpdotdev/warp/README.md @ 3959ea72141f
updated_at: '2026-09-14T03:22:42Z'
---

# warpdotdev/warp/README.md @ 3959ea72141f

<!-- rcw:begin owner=source:src_13e7842fe45a502a877ecf2c03133646 block=evidence -->
- The client app is licensed AGPL v3 to keep derivatives open, while the warpui_core and warpui UI framework crates are MIT-licensed to maximize reuse. [@claim:clm_7c5f892d169b977226e2500467871b71343df62d2d007f33437254d597d624be]
- Repository development practice: build and run locally via ./script/bootstrap and ./script/run (or cargo run), with ./script/presubmit running fmt, clippy, and tests; tests can also run via cargo nextest. [@claim:clm_b5f9b3c639ca7fe384065b7558a08b8ac24d2eb63eed2c6750b6b5f4771932e7]
- The README calls out open-source dependencies including Tokio, NuShell, Alacritty, Hyper, FontKit, Smol, Fig completion specs, and the warp server framework. [@claim:clm_d32e1ab6efdbc6ca898ebed2bc6735352397d1f30806cbeba97599adfe1c2174]
- Repository development practice: contributions start with a GitHub issue; maintainers apply readiness labels (ready-to-spec, ready-to-implement, needs-mocks), and feature work requires a spec PR adding product.md and tech.md under specs/GH<issue-number>/ before code. [@claim:clm_d82042df7cf48253c27f0a9a7220288d44c40d5603848b02cd3603158acb4cd7]
<!-- rcw:end owner=source:src_13e7842fe45a502a877ecf2c03133646 block=evidence -->

## Researcher notes

