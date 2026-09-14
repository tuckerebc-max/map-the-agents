# luangjokaj/wordpressify

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit df91d7e2d2ef @ b1048ee00b385110

## Summary (orientation draft, not independently verified)

WordPressify is a Docker-based WordPress block-theme development workflow with a Gulp build pipeline, an npm-published CLI installer, and a five-service Docker stack. Evidence is mostly README/CHANGELOG documentation plus contributor-facing CLAUDE.md and CONTRIBUTING.md guidance. Evidence coverage: 228 of 243 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] WordPressify is described as a tool to automate the WordPress development workflow. -- evidence: [README.md#L5-L5](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The default theme was rewritten as a modern block-based theme using HTML markup instead of PHP templates (v0.5.0). -- evidence: [CHANGELOG.md#L49-L55](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L49-L55)
- design-choices (1 claim(s)):
  - [observation/documented] v0.6.0 replaced chalk and prompts with native ANSI codes and Node's readline, cutting installer dependencies from over 100 to 18 packages. -- evidence: [CHANGELOG.md#L31-L43](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L31-L43)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md provides guidance to Claude Code when working with code in this repository. -- evidence: [CLAUDE.md#L3-L3](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CLAUDE.md#L3-L3)
  - [observation/documented] Repository development practice: contributors fork and clone, install Docker and Node.js v16+, scaffold with npx wordpressify, then run npm start and npm run dev inside the container. -- evidence: [CONTRIBUTING.md#L7-L10](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CONTRIBUTING.md#L7-L10)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] v0.4.0 replaced older npm tasks with commands such as npm run start, npm run export, npm run export:backup, npm run lintcss, and docker compose equivalents. -- evidence: [CHANGELOG.md#L61-L69](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L61-L69)
  - [observation/documented] The v0.6.3 installer adds an update subcommand that upgrades existing projects without overwriting theme source files. -- evidence: [CHANGELOG.md#L5-L12](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L5-L12)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Export and export:backup scripts auto-stop Docker containers when the stack was not already running, and a healthcheck was added to the WordPress service to fix a chmod race condition. -- evidence: [CHANGELOG.md#L31-L43](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L31-L43)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project requires Docker and is stated to be compatible with macOS, Windows, and Linux. -- evidence: [README.md#L7-L8](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/README.md#L7-L8)
  - [observation/documented] Since v0.4.0, NodeJS is no longer a global dependency; Docker is the only main dependency, enabling cross-platform runs. -- evidence: [CHANGELOG.md#L59-L59](https://github.com/luangjokaj/wordpressify/blob/df91d7e2d2ef991d6818c3ea8ce3d5572b500a56/CHANGELOG.md#L59-L59)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](wordpressify.detail.md) for every claim.)

Metadata and full claim list: [full detail](wordpressify.detail.md)
Human notes ([notes](wordpressify.notes.md), never overwritten by build)

[Back to map index](../../index.md)
