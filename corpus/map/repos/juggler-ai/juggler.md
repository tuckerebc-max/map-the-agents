# juggler-ai/juggler

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9446fd2936f0 @ c554519a9ceb4f47

## Summary (orientation draft, not independently verified)

Evidence consists of README and contributor license agreements for Juggler, a visual workbench for AI coding agents with a Go backend, Yjs-synchronized session documents, and a JavaScript extension SDK. Product claims below are documentation-based; development/build/CLA content is confined to workflows. Evidence coverage: 143 of 199 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Most conversation capabilities are JavaScript extensions on a public SDK: context items defining tools like read/write/bash, strategies defining the LLM loop, slash commands, and UI cards or file viewers; MCP servers and skills enter through the same system. -- evidence: [README.md#L94-L94](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L94-L94), [README.md#L101-L101](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L101-L101), [README.md#L96-L99](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L96-L99)
- design-choices (4 claim(s)):
  - [observation/documented] Conversations are represented as persistent trees of typed items rather than scrolling transcripts, with Miller-column navigation and nested child threads that return results to their parent. -- evidence: [README.md#L7-L7](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L7-L7), [README.md#L13-L16](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L13-L16), [README.md#L82-L82](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L82-L82)
  - [observation/documented] Context is editable: history can be folded into a thread, items moved or copied between branches, branches expanded back, and structural changes undone. -- evidence: [README.md#L22-L27](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L22-L27), [README.md#L82-L82](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L82-L82)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: builds require Go 1.26+ with vendored submodules; `make go-build` compiles, `make test` runs tests (race detector on by default), and `make test-full` with linting is expected before a PR. -- evidence: [README.md#L142-L142](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L142-L142), [README.md#L233-L233](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L233-L233), [README.md#L217-L217](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L217-L217), [README.md#L159-L161](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L159-L161)
  - [observation/documented] Repository development practice: every commit must carry a DCO `Signed-off-by:` line, and corporate or employer-owned contributions require executing the CCLA/CLA privately, not in public PRs. -- evidence: [CCLA.md#L11-L16](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CCLA.md#L11-L16), [CCLA.md#L130-L133](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CCLA.md#L130-L133), [CLA.md#L11-L14](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/CLA.md#L11-L14)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Juggler ships a native desktop app plus a headless `juggler` CLI server that serves a web UI, prints its URL and QR code, and can open the browser on a keypress. -- evidence: [README.md#L37-L38](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L37-L38), [README.md#L56-L56](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L56-L56)
  - [observation/documented] The desktop app and browser tabs are synchronized clients of the same server, so multiple clients can share one live session across machines or a phone. -- evidence: [README.md#L40-L40](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L40-L40), [README.md#L66-L66](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L66-L66)
- memory-state (1 claim(s)):
  - [observation/documented] Session documents live on disk and persist across quit or reconnect, including pending approvals; synchronization uses Yjs. -- evidence: [README.md#L22-L27](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L22-L27), [README.md#L239-L239](https://github.com/juggler-ai/juggler/blob/9446fd2936f02740057442a0a16b51440f68e63b/README.md#L239-L239)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](juggler.detail.md)

Metadata and full claim list: [full detail](juggler.detail.md)
Human notes ([notes](juggler.notes.md), never overwritten by build)

[Back to map index](../../index.md)
