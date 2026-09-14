---
access: public
aliases: []
claim_ids:
- clm_23e5e36be1bea4a5d315788e05af8ba3eb6e80a3dea2483e106ebe7081911aca
- clm_4592bb549b23f83420a8400a6ca4ce32f0fd9ec8acde3da26ae2be218a1d6006
maturity: draft
page_id: pg_0b63b126d76855249dc574ed9cd4b856
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eb9be3928d8e58ea85b5a009d3e6f303
title: devdanzin/fusil/doc/configuration.rst @ a7aa4e94bd84
updated_at: '2026-09-14T03:46:53Z'
---

# devdanzin/fusil/doc/configuration.rst @ a7aa4e94bd84

<!-- rcw:begin owner=source:src_eb9be3928d8e58ea85b5a009d3e6f303 block=evidence -->
- Fusil is configured entirely through command-line options, grouped into categories like Input, Running, Fuzzing, OOM Fuzzing, and Logging; a former fusil.conf file mechanism was removed, making CLI options the single source of truth. [@claim:clm_23e5e36be1bea4a5d315788e05af8ba3eb6e80a3dea2483e106ebe7081911aca]
- A few settings lack CLI flags — session scoring thresholds, the memory limit, and the dedicated fusil-user sandbox user/group — and live as constants in fusil/config.py's FusilConfig class. [@claim:clm_4592bb549b23f83420a8400a6ca4ce32f0fd9ec8acde3da26ae2be218a1d6006]
<!-- rcw:end owner=source:src_eb9be3928d8e58ea85b5a009d3e6f303 block=evidence -->

## Researcher notes

