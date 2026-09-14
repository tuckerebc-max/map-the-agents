---
access: public
aliases: []
claim_ids:
- clm_1dc02c761fb27b1f9cf25cf98583245da083a264f75094a5098d366ad0639370
- clm_7d3d616153d516b94b296965b77a93cbffe59221e9335da9ea9a87b7b44cba53
- clm_a241a7349355eab240fed9c52f2afba35b3691f8234d21b90a63385b8c21266f
- clm_ddfe9fe340fa8a4f32c36dca959c401e7a4d2c2dbee9f6302cf6ba582533f56e
maturity: draft
page_id: pg_d60e42fbe6b95af285bc7d031af80783
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_12a388105eba50fbb183a1ef3b39ec2d
title: quack-ai/companion-vscode/CONTRIBUTING.md @ 3b4d567ae047
updated_at: '2026-09-14T04:17:32Z'
---

# quack-ai/companion-vscode/CONTRIBUTING.md @ 3b4d567ae047

<!-- rcw:begin owner=source:src_12a388105eba50fbb183a1ef3b39ec2d block=evidence -->
- Repository development practice: CI uses GitHub Actions workflows for package build and coverage plus Codacy for code-quality analysis; contributors are expected to add unit tests covering their code, and precommit hooks plus an automated PR label/title check were added. [@claim:clm_1dc02c761fb27b1f9cf25cf98583245da083a264f75094a5098d366ad0639370]
- Repository development practice: local configuration is optional via a root .env file with POSTHOG_KEY and POSTHOG_HOST keys; bug reports and feature requests go through GitHub issues and questions through GitHub discussions. [@claim:clm_7d3d616153d516b94b296965b77a93cbffe59221e9335da9ea9a87b7b44cba53]
- Repository development practice: contributors fork the repo, work on a non-main branch, follow the Angular commit format, and open a pull request from their fork's branch using the PR template. [@claim:clm_a241a7349355eab240fed9c52f2afba35b3691f8234d21b90a63385b8c21266f]
- Repository development practice: quality checks run via 'make quality' (non-mutating) and auto-fixes via 'make style'; changes are tested locally with 'make run' and F5 to load the extension in a new window. [@claim:clm_ddfe9fe340fa8a4f32c36dca959c401e7a4d2c2dbee9f6302cf6ba582533f56e]
<!-- rcw:end owner=source:src_12a388105eba50fbb183a1ef3b39ec2d block=evidence -->

## Researcher notes

