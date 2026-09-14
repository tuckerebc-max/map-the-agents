# algonorhythm/flare

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5adc94b0616c @ f5b26167e3c40f3e

## Summary (orientation draft, not independently verified)

Flare is a graph-first IDE for agentic coding, shipped as an Electron desktop app and a browser-served variant sharing one backend core, with an MCP server exposing graph, board, and coordination tools to agents. Evidence is README documentation only.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Architecture separates a pure shared/ engine (import parser, resolver, incremental graph builder, scanner), an Electron-free core in electron/core.ts, desktop and browser adapters, and a React renderer with the three graph views, Monaco, and xterm terminals. -- evidence: [README.md#L438-L459](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L438-L459)
- design-choices (2 claim(s)):
  - [observation/documented] One implementation serves two transports: electron/core.ts holds all behavior as channel handlers, with desktop and browser adapters only translating; a test reportedly enforces that neither adapter names a channel. -- evidence: [README.md#L430-L436](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L430-L436)
  - [observation/documented] Flare deliberately does not lock files, arguing a lock would be an ignorable request that can silently fail open; instead agents announce intentions in a Channel and contention is surfaced on the graph and in review. -- evidence: [README.md#L151-L155](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L151-L155), [README.md#L172-L179](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L172-L179)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: testing is via npm test (633 vitest unit tests), npm run e2e (80 Playwright tests), and npm run verify (build + unit + e2e); releases build one runner per platform via a GitHub Actions matrix. -- evidence: [README.md#L512-L517](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L512-L517), [README.md#L422-L426](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L422-L426)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Flare exposes an MCP endpoint at /mcp/<slug> with tools including graph_overview, impact_of, tasks_list, task_get, task_update, task_create, decision_record, question_ask, working_agreement, chat_post, chat_read, and agents_list. -- evidence: [README.md#L597-L605](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L597-L605), [README.md#L379-L418](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L379-L418), [README.md#L356-L358](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L356-L358)
  - [observation/documented] The UI offers three graph views — Canvas (default), Wheel, and Districts treemap — switchable from the toolbar or command palette, each honoring the active lens, selection, collapsed directories, and search filter. -- evidence: [README.md#L37-L38](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L37-L38), [README.md#L40-L57](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L40-L57)
- memory-state (2 claim(s)):
  - [observation/documented] Every change burst is snapshotted into a local shadow history that can be diffed and reverted per file or whole tree; review supports reverting a file, a burst, or jumping to the last state whose checks passed. -- evidence: [README.md#L256-L285](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L256-L285), [README.md#L8-L12](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L8-L12)
  - [observation/documented] Agent identity is minted from the MCP session, which is established on initialize and echoed on every request, letting Flare name agents like 'Claude 2' and attribute writes where process lists cannot distinguish sessions. -- evidence: [README.md#L196-L214](https://github.com/AlgoNoRhythm/Flare/blob/5adc94b0616c6eae8c1f86aa97df264968fc52ab/README.md#L196-L214)
- orchestration (2 claim(s)):
More evidence: [full detail](flare.detail.md)

Metadata and full claim list: [full detail](flare.detail.md)
Human notes ([notes](flare.notes.md), never overwritten by build)

[Back to map index](../../index.md)
