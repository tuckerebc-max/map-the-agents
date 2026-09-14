# stravu/crystal

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1e18e0bc9812 @ 2cfde189ea98353a

## Summary (orientation draft, not independently verified)

The snapshot documents that Crystal, a multi-session AI code assistant manager, was deprecated in February 2026 and replaced by Nimbalyst, with a changelog describing its session/panel/git features and AGENTS.md providing contributor instructions. Evidence is documentation-only (README and CHANGELOG); no runtime source code is present in the slices.

## Source coverage

Source coverage (partial): 3 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The changelog indicates Crystal manages AI coding sessions, supporting both Claude Code and OpenAI Codex agents. -- evidence: [CHANGELOG.md#L22-L26](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L22-L26), [CHANGELOG.md#L102-L103](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L102-L103)
  - [observation/documented] Crystal provides a panel-based workspace where multiple agent and terminal panels can exist inside a single session, with keyboard navigation between panels via Cmd+Option+Arrow. -- evidence: [CHANGELOG.md#L68-L73](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L68-L73), [CHANGELOG.md#L102-L103](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L102-L103), [CHANGELOG.md#L61-L65](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L61-L65)
- design-choices (1 claim(s)):
  - [observation/documented] The changelog records a change to a merge-to-main git strategy instead of rebase, described as safer operations. -- evidence: [CHANGELOG.md#L39-L40](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L39-L40)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md specifies a pnpm workspace (main, frontend, shared, tests packages) with commands like pnpm dev, pnpm build, pnpm lint, pnpm typecheck, and Playwright E2E tests via pnpm test. -- evidence: [AGENTS.md#L9-L14](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L9-L14), [AGENTS.md#L4-L6](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L4-L6)
  - [observation/documented] Repository development practice: contributors must use TypeScript with ESLint configs, 2-space indentation, camelCase/PascalCase/kebab-case naming, run lint and typecheck before PRs, and include descriptions, linked issues, and testing notes in PRs. -- evidence: [AGENTS.md#L17-L20](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L17-L20), [AGENTS.md#L28-L30](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L28-L30)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product includes a diff viewer with Monaco-based editing, a commit dialog, file-path navigation within diffs, an auto-commit toggle, and @<file-path> file references. -- evidence: [CHANGELOG.md#L279-L282](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L279-L282), [CHANGELOG.md#L369-L371](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L369-L371), [CHANGELOG.md#L290-L290](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L290-L290)
  - [observation/documented] Sessions support per-session model selection, an automatic model choice option, slash commands such as /context in Claude Code panels, and AWS Bedrock model support. -- evidence: [CHANGELOG.md#L167-L172](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L167-L172), [CHANGELOG.md#L234-L236](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L234-L236), [CHANGELOG.md#L61-L65](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L61-L65), [CHANGELOG.md#L139-L143](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L139-L143)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The changelog records use of the Claude Code SDK (updated to 2.0.0), Electron (temporarily at 37.6.0), and dependency updates driven by Dependabot security warnings. -- evidence: [CHANGELOG.md#L76-L80](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L76-L80)
  - [observation/documented] Crystal can be installed on macOS via Homebrew with 'brew install --cask stravu-crystal', and Linux AppImage builds were added to the release process. -- evidence: [CHANGELOG.md#L131-L131](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L131-L131), [CHANGELOG.md#L334-L336](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L334-L336)
- limitations (1 claim(s)):
More evidence: [full detail](crystal.detail.md)

Metadata and full claim list: [full detail](crystal.detail.md)
Human notes ([notes](crystal.notes.md), never overwritten by build)

[Back to map index](../../index.md)
