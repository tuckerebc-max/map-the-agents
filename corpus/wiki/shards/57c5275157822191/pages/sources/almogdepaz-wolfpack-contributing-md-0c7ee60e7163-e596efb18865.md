---
access: public
aliases: []
claim_ids:
- clm_ab7a08ce2dce81b49d82b4737793755b3a55f6a6f232f4e74ac83685c3058514
- clm_e23b9376c60c35e5917ae0b6e257860391cac79f320c98fc7b3e350e12c6fe8e
- clm_ed3869a6e44fde4fddcaa6526ccddb963a3d73868141f9c4d5ccfda3a57348c6
maturity: draft
page_id: pg_e86c2398f53f589ca9dde596efb18865
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1c15434b9c51557dab591f21f6daa54c
title: almogdepaz/wolfpack/CONTRIBUTING.md @ 0c7ee60e7163
updated_at: '2026-09-14T01:32:37Z'
---

# almogdepaz/wolfpack/CONTRIBUTING.md @ 0c7ee60e7163

<!-- rcw:begin owner=source:src_1c15434b9c51557dab591f21f6daa54c block=evidence -->
- Repository development practice: contributors need Bun (v1.4.2+ pinned in CI) and a Rust toolchain, plus a pinned Zig toolchain and Ghostty VT build only for source builds of the broker; release-install users need neither Zig nor Ghostty. [@claim:clm_ab7a08ce2dce81b49d82b4737793755b3a55f6a6f232f4e74ac83685c3058514]
- Repository development practice: tests run via bun test (unit/integration/snapshot under tests/), Playwright for e2e, and cargo test for the Rust broker; PRs must branch off main, pass bun test, and stay focused. [@claim:clm_e23b9376c60c35e5917ae0b6e257860391cac79f320c98fc7b3e350e12c6fe8e]
- Repository development practice: frontend assets in public/ are embedded into the binary via scripts/gen-assets.ts, and src/public-assets.ts must not be edited manually. [@claim:clm_ed3869a6e44fde4fddcaa6526ccddb963a3d73868141f9c4d5ccfda3a57348c6]
<!-- rcw:end owner=source:src_1c15434b9c51557dab591f21f6daa54c block=evidence -->

## Researcher notes

