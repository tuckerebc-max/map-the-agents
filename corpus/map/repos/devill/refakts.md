# devill/refakts

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2ff430870b04 @ 2276e7161e5c276e

## Summary (orientation draft, not independently verified)

Selected evidence records: RefakTS is a command-line tool exposing commands including extract-variable, inline-variable, rename, select, sort-methods, find-usages, and move-file. The select command supports regex, range, structural, and boundary modes, e.g. --range with start/end regexes and --boundaries "function".

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] move-file updates import references across the codebase, and find-usages locates symbol usages across files. -- evidence: [README.md#L31-L40](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L31-L40)
- design-choices (1 claim(s)):
  - [observation/documented] The design goal is surgical edits: instead of regenerating whole files, operations change only the targeted code and its references, saving tokens and preserving agent cognitive capacity. -- evidence: [README.md#L20-L24](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L20-L24), [README.md#L11-L16](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L11-L16), [README.md#L26-L26](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L26-L26)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: the repo is optimized for Claude Code; contributors are told to have Claude set up pre/post commit hooks, pick a 'good first issue', assign it to themselves, and can direct work by issue number. -- evidence: [README.md#L135-L140](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L135-L140)
  - [observation/documented] Repository development practice: tests are fixture-based under tests/fixtures with .input.ts, .expected.ts, and .expected.txt files per command, and npm run test:coverage checks for uncovered use cases. -- evidence: [README.md#L147-L156](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L147-L156)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] RefakTS is a command-line tool exposing commands including extract-variable, inline-variable, rename, select, sort-methods, find-usages, and move-file. -- evidence: [README.md#L31-L40](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L31-L40), [README.md#L20-L24](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L20-L24)
  - [observation/documented] The select command supports regex, range, structural, and boundary modes, e.g. --range with start/end regexes and --boundaries "function". -- evidence: [README.md#L66-L70](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L66-L70)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool uses ts-morph for AST manipulation and @phenomnomnominal/tsquery for node selection, and is built with TypeScript. -- evidence: [README.md#L76-L76](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L76-L76), [README.md#L74-L74](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L74-L74)
  - [observation/documented] The package is installed globally via npm as 'refakts'. -- evidence: [README.md#L44-L46](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L44-L46)
- limitations (2 claim(s)):
  - [observation/documented] The project is explicitly labeled a proof of concept demonstrating the core concept with basic refactoring operations, with more commands in development. -- evidence: [README.md#L80-L80](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L80-L80)
  - [observation/documented] Licensing is PolyForm Noncommercial 1.0.0: free for non-commercial use while businesses require a license, with fees distributed among contributors at project leads' discretion. -- evidence: [README.md#L162-L162](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L162-L162), [LICENSE.md#L56-L56](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/LICENSE.md#L56-L56), [README.md#L129-L131](https://github.com/devill/refakts/blob/2ff430870b0428326a771aeb0e320271c61c3c24/README.md#L129-L131)
- relevance (1 claim(s)):
More evidence: [full detail](refakts.detail.md)

Metadata and full claim list: [full detail](refakts.detail.md)
Human notes ([notes](refakts.notes.md), never overwritten by build)

[Back to map index](../../index.md)
