# stravu/crystal -- full detail

[Back to orientation](crystal.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stravu/crystal/1e18e0bc981225f75b5226f82a300fa741970c6f/2cfde189ea98353a.json](../../../wiki/dossiers/stravu/crystal/1e18e0bc981225f75b5226f82a300fa741970c6f/2cfde189ea98353a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The changelog indicates Crystal manages AI coding sessions, supporting both Claude Code and OpenAI Codex agents. -- evidence: [CHANGELOG.md#L22-L26](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L22-L26), [CHANGELOG.md#L102-L103](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L102-L103) (`clm_9dda593c68f1da416b7011e10cd9ea69d5487407cb208beea22f2283edce15f9`)
- [observation/documented] Crystal provides a panel-based workspace where multiple agent and terminal panels can exist inside a single session, with keyboard navigation between panels via Cmd+Option+Arrow. -- evidence: [CHANGELOG.md#L68-L73](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L68-L73), [CHANGELOG.md#L102-L103](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L102-L103), [CHANGELOG.md#L61-L65](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L61-L65) (`clm_46d6a8786daff376a8b77e568455af33829482df9335eb006577b37eddff08ff`)

## design-choices (1 claim(s))

- [observation/documented] The changelog records a change to a merge-to-main git strategy instead of rebase, described as safer operations. -- evidence: [CHANGELOG.md#L39-L40](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L39-L40) (`clm_fca61571e47a83f75d9bd95fdb21b0bdf197ecfed1f9b44824a30d5852183339`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md specifies a pnpm workspace (main, frontend, shared, tests packages) with commands like pnpm dev, pnpm build, pnpm lint, pnpm typecheck, and Playwright E2E tests via pnpm test. -- evidence: [AGENTS.md#L9-L14](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L9-L14), [AGENTS.md#L4-L6](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L4-L6) (`clm_1ed30322967d4329468a1c105881cad3218132d2e7533bcd647ef60ede5d5083`)
- [observation/documented] Repository development practice: contributors must use TypeScript with ESLint configs, 2-space indentation, camelCase/PascalCase/kebab-case naming, run lint and typecheck before PRs, and include descriptions, linked issues, and testing notes in PRs. -- evidence: [AGENTS.md#L17-L20](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L17-L20), [AGENTS.md#L28-L30](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L28-L30) (`clm_0eb800c631bb8da8a7928657e91b904d909cb79eedc055b8e81156e27d36c661`)
- [observation/documented] Repository development practice: AGENTS.md requires Node >= 22.14 and pnpm >= 8, secrets kept in .env and never committed, and instructs automation agents to review the root CLAUDE.md and every folder's CLAUDE.md before working there. -- evidence: [AGENTS.md#L33-L35](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L33-L35), [AGENTS.md#L38-L42](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/AGENTS.md#L38-L42) (`clm_13eac932e03bc0b4a45f76d866857f9b93f74dd2ec338d1c6a7506def136106d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product includes a diff viewer with Monaco-based editing, a commit dialog, file-path navigation within diffs, an auto-commit toggle, and @<file-path> file references. -- evidence: [CHANGELOG.md#L279-L282](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L279-L282), [CHANGELOG.md#L369-L371](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L369-L371), [CHANGELOG.md#L290-L290](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L290-L290) (`clm_022ce4afb6b97b9f6793c7c5103c946c15d4844d25e1fd5fd0f5538ff47a9f03`)
- [observation/documented] Sessions support per-session model selection, an automatic model choice option, slash commands such as /context in Claude Code panels, and AWS Bedrock model support. -- evidence: [CHANGELOG.md#L167-L172](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L167-L172), [CHANGELOG.md#L234-L236](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L234-L236), [CHANGELOG.md#L61-L65](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L61-L65), [CHANGELOG.md#L139-L143](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L139-L143) (`clm_8ae27134a31a4d3337274d71077ca77c40db1e5a47953f17e4c9f04780396e40`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The changelog records use of the Claude Code SDK (updated to 2.0.0), Electron (temporarily at 37.6.0), and dependency updates driven by Dependabot security warnings. -- evidence: [CHANGELOG.md#L76-L80](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L76-L80) (`clm_068f4e3c4e037a8f6eee41a5146916425f8dc048382c8cabf84b4ae6843a1e19`)
- [observation/documented] Crystal can be installed on macOS via Homebrew with 'brew install --cask stravu-crystal', and Linux AppImage builds were added to the release process. -- evidence: [CHANGELOG.md#L131-L131](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L131-L131), [CHANGELOG.md#L334-L336](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L334-L336) (`clm_8374eee84ff459b9433217c695226598f80d500cc78f784aaff21d88a984811e`)

## limitations (1 claim(s))

- [observation/documented] The changelog states Crystal will not be updated in the future, and that the application no longer fails to load if Codex or Claude Code are not installed. -- evidence: [CHANGELOG.md#L22-L26](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L22-L26), [CHANGELOG.md#L7-L8](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/CHANGELOG.md#L7-L8) (`clm_945c5fa7f18d862c63ebd1ef7eaa6991651213d72f3d11710f61d53f7b731972`)

## relevance (2 claim(s))

- [observation/documented] Crystal, formerly a multi-session AI code assistant manager, was deprecated in February 2026 and replaced by Nimbalyst, though users may continue using it. -- evidence: [README.md#L52-L54](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/README.md#L52-L54), [README.md#L12-L16](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/README.md#L12-L16) (`clm_620ba0ff36ca4ad144c15e1cbddee59938f61ec9ee59ec52bd7249b79444ebfd`)
- [observation/documented] The README directs users to nimbalyst.com for downloads, documentation, and updates, and recommends migrating to Nimbalyst for active updates. -- evidence: [README.md#L52-L54](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/README.md#L52-L54), [README.md#L26-L28](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/README.md#L26-L28), [README.md#L56-L56](https://github.com/stravu/crystal/blob/1e18e0bc981225f75b5226f82a300fa741970c6f/README.md#L56-L56) (`clm_32fc08eee628f3710f89b0b2fb0ad37b549fbc4490aa8ef36a1e9ed5b58adc65`)

