---
access: public
aliases: []
claim_ids:
- clm_2a37f5bbc9ec7a5de37a77de719d276b15e81f79e00e41d47f8ec971053c6474
maturity: draft
page_id: pg_47fc53c519915d00bef446bde3d577de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5b257e03a2d05950b72d6df8041406b1
title: DeadWaveWave/demo2apk/docs/ARM64_BUILD_ISSUES.md @ 1405c4405c96
updated_at: '2026-09-14T03:45:12Z'
---

# DeadWaveWave/demo2apk/docs/ARM64_BUILD_ISSUES.md @ 1405c4405c96

<!-- rcw:begin owner=source:src_5b257e03a2d05950b72d6df8041406b1 block=evidence -->
- Google does not publish Linux ARM64 Android build-tools (notably aapt2), so ARM64 Docker builds rely on a temporary Rosetta x86_64 emulation workaround that is slower than native. [@claim:clm_2a37f5bbc9ec7a5de37a77de719d276b15e81f79e00e41d47f8ec971053c6474]
<!-- rcw:end owner=source:src_5b257e03a2d05950b72d6df8041406b1 block=evidence -->

## Researcher notes

