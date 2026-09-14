# quack-ai/companion-vscode -- full detail

[Back to orientation](companion-vscode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/quack-ai/companion-vscode/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/2d00dad695fdcd9e.json](../../../wiki/dossiers/quack-ai/companion-vscode/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/2d00dad695fdcd9e.json)

## specifications (1 claim(s))

- [observation/documented] The project is Quack Companion, an IDE extension for VSCode described as providing smart linting and code chat powered by team insights. -- evidence: [README.md#L1-L6](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L1-L6), [README.md#L56-L56](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L56-L56) (`clm_6e036370a302fa3a2351ee3bd15d8c272c04c2389007531d1eb27a61db010668`)

## components (1 claim(s))

- [observation/documented] After installation, opening a project gives a new extension tab with guideline curation and code chat; smart linting is temporarily disabled and code completion is coming soon. -- evidence: [README.md#L70-L70](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L70-L70), [README.md#L72-L75](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L72-L75) (`clm_6b02b93803eb2194a7809bd1ab274130286c5208cddc7cc32df99400049c9766`)

## design-choices (1 claim(s))

- [observation/documented] The stated roadmap is to turn contribution guidelines into a live pair-coding experience, help developers find starter contribution opportunities, and align contributions with project priorities. -- evidence: [README.md#L101-L103](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L101-L103) (`clm_47bb316469de632c0be5fe6a11f5e4547e5c0b941154d7f799abf74fa8899ea0`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors fork the repo, work on a non-main branch, follow the Angular commit format, and open a pull request from their fork's branch using the PR template. -- evidence: [CONTRIBUTING.md#L65-L65](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L65-L65), [CONTRIBUTING.md#L85-L86](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L85-L86), [CONTRIBUTING.md#L75-L75](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L75-L75), [CONTRIBUTING.md#L114-L114](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L114-L114), [CONTRIBUTING.md#L127-L127](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L127-L127) (`clm_a241a7349355eab240fed9c52f2afba35b3691f8234d21b90a63385b8c21266f`)
- [observation/documented] Repository development practice: quality checks run via 'make quality' (non-mutating) and auto-fixes via 'make style'; changes are tested locally with 'make run' and F5 to load the extension in a new window. -- evidence: [CONTRIBUTING.md#L96-L96](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L96-L96), [CONTRIBUTING.md#L106-L108](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L106-L108), [CONTRIBUTING.md#L110-L110](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L110-L110), [CONTRIBUTING.md#L92-L94](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L92-L94), [CONTRIBUTING.md#L98-L100](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L98-L100) (`clm_ddfe9fe340fa8a4f32c36dca959c401e7a4d2c2dbee9f6302cf6ba582533f56e`)
- [observation/documented] Repository development practice: CI uses GitHub Actions workflows for package build and coverage plus Codacy for code-quality analysis; contributors are expected to add unit tests covering their code, and precommit hooks plus an automated PR label/title check were added. -- evidence: [CONTRIBUTING.md#L21-L21](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L21-L21), [CHANGELOG.md#L14-L22](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L14-L22), [CONTRIBUTING.md#L18-L19](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L18-L19) (`clm_1dc02c761fb27b1f9cf25cf98583245da083a264f75094a5098d366ad0639370`)
- [observation/documented] Repository development practice: local configuration is optional via a root .env file with POSTHOG_KEY and POSTHOG_HOST keys; bug reports and feature requests go through GitHub issues and questions through GitHub discussions. -- evidence: [CONTRIBUTING.md#L34-L35](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L34-L35), [CONTRIBUTING.md#L37-L38](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L37-L38), [CONTRIBUTING.md#L53-L53](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L53-L53), [CONTRIBUTING.md#L59-L59](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L59-L59), [CONTRIBUTING.md#L47-L47](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L47-L47) (`clm_7d3d616153d516b94b296965b77a93cbffe59221e9335da9ea9a87b7b44cba53`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The changelog records commands to fetch guidelines, retrieve diagnostics, run code analysis via the Quack API, and authenticate, plus a multi-turn chat view and revamped guideline view. -- evidence: [CHANGELOG.md#L54-L56](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L54-L56), [CHANGELOG.md#L14-L22](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L14-L22), [CHANGELOG.md#L78-L79](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L78-L79) (`clm_b548ea9ffb1f3a0a22527af8b25f6c9b3632f9b732a3b8d63efa46d34a5bf699`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The extension collects event identifiers (event type and possibly repository scope) and user identification defaulting to the GitHub username, with an anonymized-UUID option and the ability to disable telemetry entirely. -- evidence: [README.md#L117-L118](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L117-L118), [README.md#L126-L127](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L126-L127) (`clm_52b0f7fc5a5785c6b1592bcc5f9749e13e70bc6c299ba749ed481141554fe1e5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Telemetry is sent through PostHog; a changelog entry notes axios was replaced with native fetch, and an earlier entry mentions bumping posthog to fix an axios security issue. -- evidence: [CHANGELOG.md#L14-L22](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L14-L22), [README.md#L124-L124](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L124-L124), [CHANGELOG.md#L48-L48](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L48-L48) (`clm_0e0dbf51817a0f26d2aa32d95c5641699e2b65f863582edc265251c3f30b541b`)
- [observation/documented] README badges indicate the extension targets Node 20 and is published on both the VS Marketplace and the Open VSX Registry. -- evidence: [README.md#L32-L45](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L32-L45) (`clm_3e0c3e604ea0df8e2add9454b337521fd20a9281656144abfd258c843e2eedb5`)

## limitations (1 claim(s))

- [observation/documented] Per the README, smart linting is temporarily disabled and code completion is listed as coming soon. -- evidence: [README.md#L72-L75](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L72-L75) (`clm_3eba535fff6578617bade12de7aecfd313695e96a38673932d39dcacf2dbd867`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

