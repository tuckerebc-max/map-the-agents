# project-codeguard/rules -- full detail

[Back to orientation](rules.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/project-codeguard/rules/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/4f540a0612c5e2b3.json](../../../wiki/dossiers/project-codeguard/rules/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/4f540a0612c5e2b3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (11 claim(s))

- [observation/documented] Repository development practice: contributors should first discuss changes via a GitHub issue; small fixes may go straight to a PR, while larger changes or new features require an issue first to align on scope. -- evidence: [CONTRIBUTING.md#L16-L16](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L16-L16) (`clm_6712f39e8411b32f17d25bac24a0c1548f9107e64f49e4873ac82ab3e9387684`)
- [observation/documented] Repository development practice: content updates to rules, controls, and structured content follow a two-stage process — technical PR review into 'develop', then a typically bi-weekly community review before release to 'main'. -- evidence: [CONTRIBUTING.md#L24-L24](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L24-L24), [CONTRIBUTING.md#L36-L36](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L36-L36), [CONTRIBUTING.md#L38-L38](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L38-L38), [CONTRIBUTING.md#L98-L98](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L98-L98) (`clm_1f5ac16b1b6fd2c17c0dcd95445e1fa518b790194e73ffc5632683838337f9b9`)
- [observation/documented] Repository development practice: non-content changes such as bug fixes, infrastructure updates, and dependency updates follow a standard process targeting 'main' directly, per maintainer policy. -- evidence: [CONTRIBUTING.md#L57-L57](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L57-L57), [CONTRIBUTING.md#L49-L55](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L49-L55), [CONTRIBUTING.md#L104-L107](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L104-L107) (`clm_8178143b6eabf88fef5bcef1ba0404242b7b85c45b55bb26904966c5fe0dee06`)
- [observation/documented] Repository development practice: content-update PRs are reviewed for correctness, formatting and schema validation, code hygiene, and commit message quality; reviewer responses are typically due within three business days. -- evidence: [CONTRIBUTING.md#L96-L96](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L96-L96), [CONTRIBUTING.md#L115-L115](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L115-L115), [CONTRIBUTING.md#L110-L111](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L110-L111) (`clm_50d02fdf149b4266df7cd9550234b799ab84148421af2841de3cf889e90e3f7a`)
- [observation/documented] Repository development practice: the project practices lazy consensus, and major platform or document changes require an issue or discussion with a comment period of at least seven business days. -- evidence: [CONTRIBUTING.md#L117-L117](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L117-L117) (`clm_c3911214d4a57ba3cfaaa2373ceadc4b99bd07ac52c9925679843856d7ef9cf3`)
- [observation/documented] Repository development practice: commit messages should continue the sentence 'This commit …', and branch naming conventions specify feature, codebugfix, languagefix, docs, and release prefixes with defined target branches. -- evidence: [CONTRIBUTING.md#L123-L129](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L123-L129), [CONTRIBUTING.md#L135-L137](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L135-L137), [CONTRIBUTING.md#L133-L133](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L133-L133) (`clm_0bc7cdb45d7c36697a4eb53097842e708bd29aa40bf94553df227166732c1f1b`)
- [observation/documented] Repository development practice: contributors modifying rules must run src/validate_unified_rules.py for validation and regenerate the version-controlled skills/ directory via src/convert_to_ide_formats.py. -- evidence: [CONTRIBUTING.md#L187-L188](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L187-L188), [CONTRIBUTING.md#L184-L184](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L184-L184) (`clm_9f818ba29ae7c1157efb9e56900e9cbd130680f1f799ff889f696c658b95e6e7`)
- [observation/documented] Repository development practice: releases involve bumping the version in pyproject.toml, running the conversion script to sync versions into plugin metadata and IDE rule files, then creating a GitHub release whose tag must match the pyproject version. -- evidence: [CONTRIBUTING.md#L161-L163](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L161-L163), [CONTRIBUTING.md#L148-L148](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L148-L148), [CONTRIBUTING.md#L169-L173](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L169-L173), [CONTRIBUTING.md#L145-L145](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L145-L145) (`clm_6e9abc41b243fc4754c018f83a05a92135ef7dfafb36aa36d411daccf0d13680`)
- [observation/documented] Repository development practice: on publishing a release, GitHub Actions automatically validate the version-tag match, build IDE bundles for Cursor, Windsurf, Copilot, and Antigravity, and upload ZIP artifacts. -- evidence: [CONTRIBUTING.md#L175-L178](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L175-L178) (`clm_93315d414cce9a69b4788ab7516a90ad8d5757b1455383c3283ce3f123a1ba43`)
- [observation/documented] Repository development practice: security bugs must not be reported through GitHub issues; contributors are directed to the procedures in SECURITY.md instead. -- evidence: [CONTRIBUTING.md#L79-L79](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L79-L79) (`clm_233b089b0304d8a1b2de0bb19254e921b789689c0fa002ac3194e60afa821092`)
- [observation/documented] Repository development practice: the repository layout includes sources/ (core with 22 files, owasp with 88), src/ conversion and validation tools, a committed generated skills/ Claude Code plugin, and uncommitted generated dist/ IDE bundles. -- evidence: [CONTRIBUTING.md#L61-L64](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/CONTRIBUTING.md#L61-L64) (`clm_41b26cbb2067fce1d4ae5f04cfb71d53c55712da534ab8b01c03eb0d0952823b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Project CodeGuard has been donated to the Coalition for Secure AI (CoSAI), and this repository directs readers to github.com/cosai-oasis/project-codeguard for the latest updates and contribution guidance. -- evidence: [README.md#L3-L3](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/README.md#L3-L3), [README.md#L5-L5](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/README.md#L5-L5), [README.md#L8-L8](https://github.com/project-codeguard/rules/blob/036b66c1554f36a65d6f7a0bf3c8ff9804e0f998/README.md#L8-L8) (`clm_9775ac953c642e500c4afc1613990cdc514b75dd2964ab642b15110f7e687909`)

