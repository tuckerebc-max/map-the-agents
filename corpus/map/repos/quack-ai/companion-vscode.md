# quack-ai/companion-vscode

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3b4d567ae047 @ 2d00dad695fdcd9e

## Summary (orientation draft, not independently verified)

Quack Companion is a VSCode extension offering guideline curation, code chat, and telemetry via PostHog, with smart linting temporarily disabled and code completion pending. Contributor-facing guidance covers CI, make targets, commit format, and PR flow.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is Quack Companion, an IDE extension for VSCode described as providing smart linting and code chat powered by team insights. -- evidence: [README.md#L1-L6](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L1-L6), [README.md#L56-L56](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L56-L56)
- components (1 claim(s)):
  - [observation/documented] After installation, opening a project gives a new extension tab with guideline curation and code chat; smart linting is temporarily disabled and code completion is coming soon. -- evidence: [README.md#L70-L70](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L70-L70), [README.md#L72-L75](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L72-L75)
- design-choices (1 claim(s)):
  - [observation/documented] The stated roadmap is to turn contribution guidelines into a live pair-coding experience, help developers find starter contribution opportunities, and align contributions with project priorities. -- evidence: [README.md#L101-L103](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L101-L103)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors fork the repo, work on a non-main branch, follow the Angular commit format, and open a pull request from their fork's branch using the PR template. -- evidence: [CONTRIBUTING.md#L65-L65](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L65-L65), [CONTRIBUTING.md#L85-L86](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L85-L86), [CONTRIBUTING.md#L75-L75](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L75-L75), [CONTRIBUTING.md#L114-L114](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L114-L114), [CONTRIBUTING.md#L127-L127](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L127-L127)
  - [observation/documented] Repository development practice: quality checks run via 'make quality' (non-mutating) and auto-fixes via 'make style'; changes are tested locally with 'make run' and F5 to load the extension in a new window. -- evidence: [CONTRIBUTING.md#L96-L96](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L96-L96), [CONTRIBUTING.md#L106-L108](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L106-L108), [CONTRIBUTING.md#L110-L110](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L110-L110), [CONTRIBUTING.md#L92-L94](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L92-L94), [CONTRIBUTING.md#L98-L100](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CONTRIBUTING.md#L98-L100)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The changelog records commands to fetch guidelines, retrieve diagnostics, run code analysis via the Quack API, and authenticate, plus a multi-turn chat view and revamped guideline view. -- evidence: [CHANGELOG.md#L54-L56](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L54-L56), [CHANGELOG.md#L14-L22](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L14-L22), [CHANGELOG.md#L78-L79](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L78-L79)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The extension collects event identifiers (event type and possibly repository scope) and user identification defaulting to the GitHub username, with an anonymized-UUID option and the ability to disable telemetry entirely. -- evidence: [README.md#L117-L118](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L117-L118), [README.md#L126-L127](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L126-L127)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Telemetry is sent through PostHog; a changelog entry notes axios was replaced with native fetch, and an earlier entry mentions bumping posthog to fix an axios security issue. -- evidence: [CHANGELOG.md#L14-L22](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L14-L22), [README.md#L124-L124](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L124-L124), [CHANGELOG.md#L48-L48](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/CHANGELOG.md#L48-L48)
  - [observation/documented] README badges indicate the extension targets Node 20 and is published on both the VS Marketplace and the Open VSX Registry. -- evidence: [README.md#L32-L45](https://github.com/quack-ai/companion-vscode/blob/3b4d567ae0472ff18f5f4c2795ab21a27f1a6a4d/README.md#L32-L45)
More evidence: [full detail](companion-vscode.detail.md)

Metadata and full claim list: [full detail](companion-vscode.detail.md)
Human notes ([notes](companion-vscode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
