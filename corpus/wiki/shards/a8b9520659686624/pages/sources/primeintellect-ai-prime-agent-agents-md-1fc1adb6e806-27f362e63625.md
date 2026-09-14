---
access: public
aliases: []
claim_ids:
- clm_10f22556452cb5352867155618ce28444e071b1faad62052e54f69164c3d7ce5
- clm_3a103463d5a6d4767b5c300625bdee71a25cc1fd7237eff4073f91752785ac62
- clm_70b43fb7575e858260bd5ffdfb710010c9ddc07fff55009392bf4f487892f316
- clm_a6c11274fc4d88ec8234e80fcb71a122220c0dd8ca6197b8fabcafdaa0ec57a8
- clm_eda536769e487f7f55ad542d0a4bdf6ef1f8dcfe1c9d0c0033febbfcb2069107
maturity: draft
page_id: pg_0b635f08581c5a7ca0f127f362e63625
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_790fb802493a5233be0f69b905c98090
title: PrimeIntellect-ai/prime-agent/AGENTS.md @ 1fc1adb6e806
updated_at: '2026-09-14T02:32:27Z'
---

# PrimeIntellect-ai/prime-agent/AGENTS.md @ 1fc1adb6e806

<!-- rcw:begin owner=source:src_790fb802493a5233be0f69b905c98090 block=evidence -->
- Repository development practice: daemon protocol changes must be classified as backward-compatible, capability-gated, or incompatible; incompatible changes require bumping DAEMON_PROTOCOL_VERSION and updating schema revision and compatibility tests. [@claim:clm_10f22556452cb5352867155618ce28444e071b1faad62052e54f69164c3d7ce5]
- Repository development practice: changelog entries are added as fragment files under packages/<pkg>/.changes/ rather than editing CHANGELOG.md directly, and PRs touching package src without a fragment fail CI unless labeled no-changelog. [@claim:clm_3a103463d5a6d4767b5c300625bdee71a25cc1fd7237eff4073f91752785ac62]
- Repository development practice: dependency updates are subject to a 7-day minimum release age enforced via .npmrc min-release-age=7 and a matching Dependabot cooldown, with an explicit override flag for urgent security patches. [@claim:clm_70b43fb7575e858260bd5ffdfb710010c9ddc07fff55009392bf4f487892f316]
- Repository development practice: parallel agents in one worktree must stage only their own files (never git add -A), and destructive operations like git reset --hard, git clean -fd, and commit --no-verify are forbidden. [@claim:clm_a6c11274fc4d88ec8234e80fcb71a122220c0dd8ca6197b8fabcafdaa0ec57a8]
- Repository development practice: AGENTS.md requires running 'npm run check' after code changes, forbids npm run dev/build/test, and mandates running any created or modified test file until it passes, using the faux provider harness for coding-agent suite tests. [@claim:clm_eda536769e487f7f55ad542d0a4bdf6ef1f8dcfe1c9d0c0033febbfcb2069107]
<!-- rcw:end owner=source:src_790fb802493a5233be0f69b905c98090 block=evidence -->

## Researcher notes

