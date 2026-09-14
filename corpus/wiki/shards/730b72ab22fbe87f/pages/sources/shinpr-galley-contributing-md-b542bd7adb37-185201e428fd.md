---
access: public
aliases: []
claim_ids:
- clm_0739514d0879c50424af8232723805bfe4da1d24d9a8a5269823f298f38fd0b0
- clm_7436ed74d467404be417b19607c82aeceb6b27b5da18d045eb28d24ce24c2796
- clm_97737edea9274ad95e9d132e02609a4c4d8eb87448532aa810b5fcb6f33cde16
maturity: draft
page_id: pg_05a5dd10d50b5e078f89185201e428fd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aed7fe39c4d85fb39e33d52bf96f507d
title: shinpr/galley/CONTRIBUTING.md @ b542bd7adb37
updated_at: '2026-09-14T02:39:53Z'
---

# shinpr/galley/CONTRIBUTING.md @ b542bd7adb37

<!-- rcw:begin owner=source:src_aed7fe39c4d85fb39e33d52bf96f507d block=evidence -->
- Repository development practice: contributors run gofmt, go test ./..., go build ./cmd/galley, and scripts/smoke-local.sh before opening a PR, and validate examples and plugin metadata when changing schemas or plugin files. [@claim:clm_0739514d0879c50424af8232723805bfe4da1d24d9a8a5269823f298f38fd0b0]
- Repository development practice: releases are created from the GitHub UI, triggering a GoReleaser workflow that attaches macOS, Linux, and Windows archives; contributors add CHANGELOG.md entries for user-visible changes. [@claim:clm_7436ed74d467404be417b19607c82aeceb6b27b5da18d045eb28d24ce24c2796]
- The CLI exposes commands including daemon config init, daemon start, daemon status --output json, daemon run --once, task validate, profile validate, and schema generate/check. [@claim:clm_97737edea9274ad95e9d132e02609a4c4d8eb87448532aa810b5fcb6f33cde16]
<!-- rcw:end owner=source:src_aed7fe39c4d85fb39e33d52bf96f507d block=evidence -->

## Researcher notes

