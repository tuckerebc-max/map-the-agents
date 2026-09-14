# xeol-io/bumpgen

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e87754033875 @ 08ae1fc3ca5db8f4

## Summary (orientation draft, not independently verified)

bumpgen is a CLI/GitHub-action tool that upgrades TypeScript/TSX dependencies and uses build errors, a ts-morph AST, and a plan-graph DAG with GPT-4 Turbo to fix resulting breakages. Evidence covers its architecture, usage, limitations, and a benchmark against swe-bump-bench.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] bumpgen upgrades TypeScript/TSX dependencies and makes code changes automatically when the upgrade breaks things. -- evidence: [README.md#L22-L22](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L22-L22)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The tool builds the project to detect what broke after a dependency bump, then uses ts-morph to build an AST of the code and obtain type definitions for external methods. -- evidence: [README.md#L36-L39](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L36-L39), [README.md#L160-L160](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L160-L160)
  - [observation/documented] bumpgen creates a plan-graph DAG, based on Microsoft's codeplan paper, to execute changes in order and propagate fixes for second-order breakages across the codebase. -- evidence: [README.md#L164-L164](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L164-L164), [README.md#L36-L39](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L36-L39)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcome and setup for development is documented in .github/development.md. -- evidence: [README.md#L188-L188](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L188-L188)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI accepts a package name and target version (e.g. bumpgen @tanstack/react-query 5.28.14), can be run without arguments to pick a package from a menu, and offers --help for options. -- evidence: [README.md#L59-L59](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L59-L59), [README.md#L50-L55](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L50-L55), [README.md#L57-L57](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L57-L57)
  - [observation/documented] The example GitHub workflow grants pull-requests:read and contents:write permissions and passes path, llm_key, and github_token inputs to the bumpgen action. -- evidence: [README.md#L82-L97](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L82-L97), [README.md#L78-L80](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L78-L80)
- memory-state (1 claim(s)):
  - [observation/documented] The plan graph, the error, and the file containing the breaking change are passed to the LLM as context to maximize its ability to fix the issue. -- evidence: [README.md#L168-L168](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L168-L168)
- orchestration (1 claim(s)):
  - [observation/documented] A GitHub action runs bumpgen, intended to trigger on dependabot or renovatebot PRs, committing fixes to the PR branch when breaking changes are detected. -- evidence: [README.md#L63-L63](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L63-L63)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] bumpgen with GPT-4 Turbo scored 45% (67 tasks) on a benchmark suite of version bumps with breaking changes (swe-bump-bench), with evals published in that repo. -- evidence: [README.md#L184-L184](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L184-L184), [README.md#L180-L182](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L180-L182)
- dependencies (1 claim(s)):
  - [observation/documented] bumpgen requires an OpenAI API key and only supports the gpt-4-turbo-preview model at this time. -- evidence: [README.md#L46-L46](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L46-L46), [README.md#L172-L172](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L172-L172)
- limitations (2 claim(s)):
  - [observation/documented] bumpgen relies on build errors, so behavioral changes that don't produce build errors go undetected. -- evidence: [README.md#L106-L108](https://github.com/xeol-io/bumpgen/blob/e8775403387523b667916d35676c3e8fa1026e83/README.md#L106-L108)
More evidence: [full detail](bumpgen.detail.md)

Metadata and full claim list: [full detail](bumpgen.detail.md)
Human notes ([notes](bumpgen.notes.md), never overwritten by build)

[Back to map index](../../index.md)
