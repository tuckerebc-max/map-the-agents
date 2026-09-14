# xeol-io/bumpgen -- full detail

[Back to orientation](bumpgen.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xeol-io/bumpgen/e8775403387523b667916d35676c3e8fa1026e83/08ae1fc3ca5db8f4.json](../../../wiki/dossiers/xeol-io/bumpgen/e8775403387523b667916d35676c3e8fa1026e83/08ae1fc3ca5db8f4.json)

## specifications (1 claim(s))

- [observation/documented] bumpgen upgrades TypeScript/TSX dependencies and makes code changes automatically when the upgrade breaks things. -- evidence: [README.md#L22-L22](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L22-L22) (`clm_85cdd73eaaa0530f55fc31a2eb585b3ee0300af95e1d7666da8bcbd777284885`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The tool builds the project to detect what broke after a dependency bump, then uses ts-morph to build an AST of the code and obtain type definitions for external methods. -- evidence: [README.md#L36-L39](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L36-L39), [README.md#L160-L160](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L160-L160) (`clm_067cbf8536c1bb049b1ef5affd32f37cc54f39af436b1cf3d3dab38b70fff627`)
- [observation/documented] bumpgen creates a plan-graph DAG, based on Microsoft's codeplan paper, to execute changes in order and propagate fixes for second-order breakages across the codebase. -- evidence: [README.md#L164-L164](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L164-L164), [README.md#L36-L39](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L36-L39) (`clm_801a07e51f0af58a4857e24a99b6f6372bd7cad91779bc1304c0e6ce2b78ff50`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcome and setup for development is documented in .github/development.md. -- evidence: [README.md#L188-L188](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L188-L188) (`clm_0671b268d93ea651a0a351e525bc4695b9a04cc12412b557fc0d66af3e12757a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI accepts a package name and target version (e.g. bumpgen @tanstack/react-query 5.28.14), can be run without arguments to pick a package from a menu, and offers --help for options. -- evidence: [README.md#L59-L59](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L59-L59), [README.md#L50-L55](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L50-L55), [README.md#L57-L57](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L57-L57) (`clm_a10ec0d61ea6394c831623a41ed8424b1491431675edc570712caae38325f4a0`)
- [observation/documented] The example GitHub workflow grants pull-requests:read and contents:write permissions and passes path, llm_key, and github_token inputs to the bumpgen action. -- evidence: [README.md#L82-L97](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L82-L97), [README.md#L78-L80](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L78-L80) (`clm_ccd43d9f1943141113d18c83d92287cad6bb0477e372f2d419de896beb673ec3`)

## memory-state (1 claim(s))

- [observation/documented] The plan graph, the error, and the file containing the breaking change are passed to the LLM as context to maximize its ability to fix the issue. -- evidence: [README.md#L168-L168](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L168-L168) (`clm_500ceac0eecbdb80ead5f18294a98f8e11d857a8a07d5858732f03a2c22f8cfc`)

## orchestration (1 claim(s))

- [observation/documented] A GitHub action runs bumpgen, intended to trigger on dependabot or renovatebot PRs, committing fixes to the PR branch when breaking changes are detected. -- evidence: [README.md#L63-L63](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L63-L63) (`clm_d93adaef855c9fe4ac22f3e91846228d9666f035ec05f1c1bc0040f410905235`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] bumpgen with GPT-4 Turbo scored 45% (67 tasks) on a benchmark suite of version bumps with breaking changes (swe-bump-bench), with evals published in that repo. -- evidence: [README.md#L184-L184](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L184-L184), [README.md#L180-L182](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L180-L182) (`clm_dcdd4b5e64d3c0f445f526367a3ebde2bb42740cbd6965f90c16eddfd3ee6eba`)

## dependencies (1 claim(s))

- [observation/documented] bumpgen requires an OpenAI API key and only supports the gpt-4-turbo-preview model at this time. -- evidence: [README.md#L46-L46](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L46-L46), [README.md#L172-L172](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L172-L172) (`clm_7b28559f3a71e2ab0fee914ae754d3ca73f2453c56933e9b029a720f1c82631a`)

## limitations (2 claim(s))

- [observation/documented] bumpgen relies on build errors, so behavioral changes that don't produce build errors go undetected. -- evidence: [README.md#L106-L108](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L106-L108) (`clm_24adb78441e4d943d442e45b9ee6d41cfd161b2e80cc65dbf5325f1b679411cc`)
- [observation/documented] bumpgen cannot handle multiple packages at once, failing on upgrades needing simultaneous peer-dependency updates, and struggles with very large framework upgrades like vue 2 to 3. -- evidence: [README.md#L106-L108](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L106-L108) (`clm_bdb5b21184d1a2b4e1c5ffe4819fd0ea82a70716ed3144b885d8470837a864ec`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

