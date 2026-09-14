---
access: public
aliases: []
claim_ids:
- clm_2ac694dd1225b98b7de4066deb3646ade386177223b8f1bf0999ead17eee5f24
- clm_c30fdd179c9eb3b6e3c1257e8627f61bc88df0fe751e13b8b0329a8a0bcc53a2
maturity: draft
page_id: pg_d8d6d3c9d582565e836e40a0f8c36566
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cb6813ff4b9d550f837ba7720eaa4b95
title: zellij-org/zellij/docs/ERROR_HANDLING.md @ a162323384df
updated_at: '2026-09-14T04:33:58Z'
---

# zellij-org/zellij/docs/ERROR_HANDLING.md @ a162323384df

<!-- rcw:begin owner=source:src_cb6813ff4b9d550f837ba7720eaa4b95 block=evidence -->
- Repository development practice: contributors are asked to eliminate unwrap() where possible in favor of Result-returning functions, using fatal()/non_fatal() helpers and the zellij_utils::errors prelude. [@claim:clm_2ac694dd1225b98b7de4066deb3646ade386177223b8f1bf0999ead17eee5f24]
- The error-handling approach uses the anyhow crate to propagate errors with context, the miette crate for panic-message formatting, and thiserror to build the ZellijError type. [@claim:clm_c30fdd179c9eb3b6e3c1257e8627f61bc88df0fe751e13b8b0329a8a0bcc53a2]
<!-- rcw:end owner=source:src_cb6813ff4b9d550f837ba7720eaa4b95 block=evidence -->

## Researcher notes

