# fireproof-storage/fireproof

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 404e6c5c7f28 @ 11291582979dda34

## Summary (orientation draft, not independently verified)

README and CHANGELOG evidence describes Fireproof as an embedded JavaScript document database with encrypted sync, React hooks, and a core API, plus debugging/logging configuration and repository testing instructions. No source code slices are present, so claims are documentation-based.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Fireproof is described as a lightweight embedded document database with encrypted live sync, usable in any JavaScript environment via a unified API for React hooks and a standalone core API. -- evidence: [README.md#L10-L10](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L10-L10)
  - [observation/documented] From version 0.19 onward the database format is stated to be stable with no backward-compatibility breaks, though internal APIs changed between the 0.19 and 0.20 series. -- evidence: [CHANGELOG.md#L5-L7](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/CHANGELOG.md#L5-L7)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The ledger enforces cryptographic causal consistency and integrity using a hash history, storing and replicating data as content-addressed encrypted blobs suitable for syncing via object storage. -- evidence: [README.md#L21-L21](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L21-L21)
  - [observation/documented] The project claims multi-writer safety, CRDT-based real-time collaboration, encryption, and a small package size with no wasm, targeting browser, cloud, and edge environments. -- evidence: [README.md#L147-L147](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L147-L147), [README.md#L142-L145](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L142-L145)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the test suite runs with pnpm run test across projects, with pattern-based filtering, per-file React component tests, and FP_DEBUG env presets for vitest. -- evidence: [README.md#L210-L212](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L210-L212), [README.md#L204-L206](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L204-L206), [README.md#L181-L186](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L181-L186), [README.md#L190-L190](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L190-L190), [README.md#L198-L200](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L198-L200), [README.md#L192-L194](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L192-L194)
  - [observation/documented] Repository development practice: a CI workflow badge links to ci.yaml on GitHub Actions, and docs are generated with pnpm run build:docs, which the README cautions pushes directly. -- evidence: [README.md#L251-L253](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L251-L253), [README.md#L3-L8](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L3-L8), [README.md#L249-L249](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L249-L249)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] React hooks useLiveQuery and useDocument are exposed through useFireproof, with useLiveQuery supporting options like descending order and a result limit. -- evidence: [README.md#L64-L65](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L64-L65), [README.md#L58-L59](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L58-L59), [README.md#L16-L19](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L16-L19)
  - [observation/documented] The core API exposes a document-database style interface (fireproof(name)) with put, get, subscribe, and query methods including range queries. -- evidence: [README.md#L126-L126](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L126-L126), [README.md#L133-L136](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L133-L136), [README.md#L121-L122](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L121-L122), [README.md#L128-L131](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L128-L131), [README.md#L124-L124](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L124-L124)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Distribution is via npm packages use-fireproof (core plus React hooks) and @fireproof/core, also loadable from ESM.sh or a jsDelivr browser script tag exposing a global Fireproof. -- evidence: [README.md#L45-L47](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L45-L47), [README.md#L25-L25](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L25-L25), [README.md#L39-L41](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L39-L41), [README.md#L27-L29](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L27-L29), [README.md#L33-L35](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L33-L35)
More evidence: [full detail](fireproof.detail.md)

Metadata and full claim list: [full detail](fireproof.detail.md)
Human notes ([notes](fireproof.notes.md), never overwritten by build)

[Back to map index](../../index.md)
