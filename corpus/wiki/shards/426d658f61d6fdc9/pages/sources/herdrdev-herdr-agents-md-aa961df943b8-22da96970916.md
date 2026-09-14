---
access: public
aliases: []
claim_ids:
- clm_07d91a02c0212240ca632a315bd896d598d6371a9ba62240d76cc263ab99dcac
- clm_27cc1c66b0c94d350798b0b90d4cbff4a96aac4b94225cb1ad9352383475f5e4
- clm_584cd59b8e63da898eb5112c9645d734e79c1b296fbd04cd4287325507988c84
- clm_8bed0e196ed063659d069e5d55b2b8ce0e31b499268d5caece88418d34c4fe4b
maturity: draft
page_id: pg_f672b08de046591f825e22da96970916
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6e8a3dd2bc7c57fc89760bda9b266d82
title: herdrdev/herdr/AGENTS.md @ aa961df943b8
updated_at: '2026-09-14T03:08:56Z'
---

# herdrdev/herdr/AGENTS.md @ aa961df943b8

<!-- rcw:begin owner=source:src_6e8a3dd2bc7c57fc89760bda9b266d82 block=evidence -->
- Repository development practice: Rust production code must avoid unwrap(), use tracing for logging, and gate platform-specific code via cfg attributes in src/platform/. [@claim:clm_07d91a02c0212240ca632a315bd896d598d6371a9ba62240d76cc263ab99dcac]
- Repository development practice: contributors should use just recipes (just test, just check) rather than invoking cargo directly, and run just check before committing. [@claim:clm_27cc1c66b0c94d350798b0b90d4cbff4a96aac4b94225cb1ad9352383475f5e4]
- Repository development practice: commits use lowercase conventional-commit style with no emojis or AI co-author lines, and reference issues with 'refs #<n>' rather than closing keywords. [@claim:clm_584cd59b8e63da898eb5112c9645d734e79c1b296fbd04cd4287325507988c84]
- Repository development practice: external contributors' unsolicited implementation PRs are closed automatically unless the human is listed in .github/APPROVED_CONTRIBUTORS; agents may only file verified, reproducible bug reports. [@claim:clm_8bed0e196ed063659d069e5d55b2b8ce0e31b499268d5caece88418d34c4fe4b]
<!-- rcw:end owner=source:src_6e8a3dd2bc7c57fc89760bda9b266d82 block=evidence -->

## Researcher notes

