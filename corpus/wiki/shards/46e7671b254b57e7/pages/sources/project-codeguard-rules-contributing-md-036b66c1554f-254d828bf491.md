---
access: public
aliases: []
claim_ids:
- clm_0bc7cdb45d7c36697a4eb53097842e708bd29aa40bf94553df227166732c1f1b
- clm_1f5ac16b1b6fd2c17c0dcd95445e1fa518b790194e73ffc5632683838337f9b9
- clm_233b089b0304d8a1b2de0bb19254e921b789689c0fa002ac3194e60afa821092
- clm_41b26cbb2067fce1d4ae5f04cfb71d53c55712da534ab8b01c03eb0d0952823b
- clm_50d02fdf149b4266df7cd9550234b799ab84148421af2841de3cf889e90e3f7a
- clm_6712f39e8411b32f17d25bac24a0c1548f9107e64f49e4873ac82ab3e9387684
- clm_6e9abc41b243fc4754c018f83a05a92135ef7dfafb36aa36d411daccf0d13680
- clm_8178143b6eabf88fef5bcef1ba0404242b7b85c45b55bb26904966c5fe0dee06
- clm_93315d414cce9a69b4788ab7516a90ad8d5757b1455383c3283ce3f123a1ba43
- clm_9f818ba29ae7c1157efb9e56900e9cbd130680f1f799ff889f696c658b95e6e7
- clm_c3911214d4a57ba3cfaaa2373ceadc4b99bd07ac52c9925679843856d7ef9cf3
maturity: draft
page_id: pg_6dd4de2bd00153828628254d828bf491
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_224b24ff382158199d20d209d297c048
title: project-codeguard/rules/CONTRIBUTING.md @ 036b66c1554f
updated_at: '2026-09-14T04:16:19Z'
---

# project-codeguard/rules/CONTRIBUTING.md @ 036b66c1554f

<!-- rcw:begin owner=source:src_224b24ff382158199d20d209d297c048 block=evidence -->
- Repository development practice: commit messages should continue the sentence 'This commit …', and branch naming conventions specify feature, codebugfix, languagefix, docs, and release prefixes with defined target branches. [@claim:clm_0bc7cdb45d7c36697a4eb53097842e708bd29aa40bf94553df227166732c1f1b]
- Repository development practice: content updates to rules, controls, and structured content follow a two-stage process — technical PR review into 'develop', then a typically bi-weekly community review before release to 'main'. [@claim:clm_1f5ac16b1b6fd2c17c0dcd95445e1fa518b790194e73ffc5632683838337f9b9]
- Repository development practice: security bugs must not be reported through GitHub issues; contributors are directed to the procedures in SECURITY.md instead. [@claim:clm_233b089b0304d8a1b2de0bb19254e921b789689c0fa002ac3194e60afa821092]
- Repository development practice: the repository layout includes sources/ (core with 22 files, owasp with 88), src/ conversion and validation tools, a committed generated skills/ Claude Code plugin, and uncommitted generated dist/ IDE bundles. [@claim:clm_41b26cbb2067fce1d4ae5f04cfb71d53c55712da534ab8b01c03eb0d0952823b]
- Repository development practice: content-update PRs are reviewed for correctness, formatting and schema validation, code hygiene, and commit message quality; reviewer responses are typically due within three business days. [@claim:clm_50d02fdf149b4266df7cd9550234b799ab84148421af2841de3cf889e90e3f7a]
- Repository development practice: contributors should first discuss changes via a GitHub issue; small fixes may go straight to a PR, while larger changes or new features require an issue first to align on scope. [@claim:clm_6712f39e8411b32f17d25bac24a0c1548f9107e64f49e4873ac82ab3e9387684]
- Repository development practice: releases involve bumping the version in pyproject.toml, running the conversion script to sync versions into plugin metadata and IDE rule files, then creating a GitHub release whose tag must match the pyproject version. [@claim:clm_6e9abc41b243fc4754c018f83a05a92135ef7dfafb36aa36d411daccf0d13680]
- Repository development practice: non-content changes such as bug fixes, infrastructure updates, and dependency updates follow a standard process targeting 'main' directly, per maintainer policy. [@claim:clm_8178143b6eabf88fef5bcef1ba0404242b7b85c45b55bb26904966c5fe0dee06]
- Repository development practice: on publishing a release, GitHub Actions automatically validate the version-tag match, build IDE bundles for Cursor, Windsurf, Copilot, and Antigravity, and upload ZIP artifacts. [@claim:clm_93315d414cce9a69b4788ab7516a90ad8d5757b1455383c3283ce3f123a1ba43]
- Repository development practice: contributors modifying rules must run src/validate_unified_rules.py for validation and regenerate the version-controlled skills/ directory via src/convert_to_ide_formats.py. [@claim:clm_9f818ba29ae7c1157efb9e56900e9cbd130680f1f799ff889f696c658b95e6e7]
- Repository development practice: the project practices lazy consensus, and major platform or document changes require an issue or discussion with a comment period of at least seven business days. [@claim:clm_c3911214d4a57ba3cfaaa2373ceadc4b99bd07ac52c9925679843856d7ef9cf3]
<!-- rcw:end owner=source:src_224b24ff382158199d20d209d297c048 block=evidence -->

## Researcher notes

