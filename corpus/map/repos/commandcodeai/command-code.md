# commandcodeai/command-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5c8f1b48c9d6 @ 5960e9e356d6db47

## Summary (orientation draft, not independently verified)

The snapshot contains only the README of command-code, an npm-distributed terminal coding agent that advertises a continuously learning 'taste' model (taste-1) and an interactive CLI session mode. No code, tests, or contributor guidance appear in the evidence.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The README describes a model called `taste-1` as the core of the product's taste architecture, which it says learns from the user and grows with them. -- evidence: [readme.md#L61-L61](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L61-L61), [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36)
- design-choices (2 claim(s)):
  - [observation/documented] The taste system is designed to treat every accept, reject, and edit as a signal that shapes a per-user taste profile. -- evidence: [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36)
  - [observation/documented] Taste rules are designed to be shareable across a team via `npx taste push/pull`, with the README stating that rules decay while taste compounds. -- evidence: [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [inference/documented] The docs site advertises workflow recipes pairing concrete scenarios with prompts and expected outcomes, suggesting a curated usage-pattern library, though only the link is in evidence. -- evidence: [readme.md#L75-L75](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L75-L75), [readme.md#L73-L73](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L73-L73)
- interfaces (3 claim(s)):
  - [observation/documented] The product runs as a CLI: it is installed globally via npm and started inside a project with the `cmd` command. -- evidence: [readme.md#L50-L53](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L50-L53), [readme.md#L44-L46](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L44-L46)
  - [observation/documented] Interactive sessions support typed prefixes: `/` opens a command menu, `!` enters Bash mode, and `@` triggers file-path mention autocomplete. -- evidence: [readme.md#L67-L67](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L67-L67)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The tool is distributed as the npm package `command-code`, installed with `npm i -g command-code`. -- evidence: [readme.md#L11-L15](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L11-L15), [readme.md#L44-L46](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L44-L46)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The project is a coding agent positioned as building full-stack projects, fixing bugs, writing tests, and refactoring while adapting to the user's coding style. -- evidence: [readme.md#L7-L9](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L7-L9)

(1 additional claim(s) omitted for length; see [full detail](command-code.detail.md) for every claim.)

Metadata and full claim list: [full detail](command-code.detail.md)
Human notes ([notes](command-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
