# exafunction/codeium-react-code-editor

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 768e1b231c00 @ 8df5fe65efa0abcb

## Summary (orientation draft, not independently verified)

README-only evidence for @codeium/react-code-editor, a free React code-editor component wrapping Monaco React with AI autocomplete, installable via npm/yarn/pnpm and configurable via props like language, theme, and otherDocuments.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The package is a React code-editor component providing AI autocomplete, built as a wrapper around Microsoft's Monaco editor (the editor powering VS Code). -- evidence: [readme.md#L7-L7](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L7-L7), [readme.md#L99-L99](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L99-L99)
- design-choices (2 claim(s)):
  - [observation/documented] The otherDocuments prop accepts at most 10 documents, and a reranker runs behind the scenes to optimize what fits within the token limit. -- evidence: [readme.md#L89-L89](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L89-L89)
  - [observation/documented] Autocomplete is context-aware: the editor analyzes its content (and neighboring documents) to predict suggestions, with multi-document context improving completion quality. -- evidence: [readme.md#L50-L50](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L50-L50), [readme.md#L68-L87](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L68-L87), [readme.md#L101-L101](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L101-L101)
- workflows (1 claim(s)):
  - [observation/documented] Installation is supported via npm, yarn, or pnpm using the package name @codeium/react-code-editor. -- evidence: [readme.md#L29-L29](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L29-L29), [readme.md#L32-L33](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L32-L33), [readme.md#L26-L26](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L26-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The core editor API matches that of the wrapped Monaco React project, and the component is imported as CodeiumEditor from @codeium/react-code-editor. -- evidence: [readme.md#L109-L109](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L109-L109), [readme.md#L37-L38](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L37-L38)
  - [observation/documented] CodeiumEditor accepts props including language, theme, and otherDocuments; the advanced example passes Document objects with absolutePath, relativePath, text, editorLanguage, and language fields. -- evidence: [readme.md#L68-L87](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L68-L87), [readme.md#L40-L48](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L40-L48)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project depends on and extends Suren Atoyan's Monaco React project, which it credits as foundational. -- evidence: [readme.md#L13-L14](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L13-L14), [readme.md#L109-L109](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L109-L109), [readme.md#L125-L125](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L125-L125)
- limitations (1 claim(s)):
  - [observation/documented] Dual CommonJS/ESM support is described as an open issue, and pull requests fixing it are welcome. -- evidence: [readme.md#L121-L121](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L121-L121)
- relevance (1 claim(s)):
  - [observation/documented] The package is free and open-source with no account required, and a live demo is hosted at codeium.com/playground. -- evidence: [readme.md#L13-L14](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L13-L14), [readme.md#L7-L7](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L7-L7), [readme.md#L18-L18](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L18-L18)

(1 additional claim(s) omitted for length; see [full detail](codeium-react-code-editor.detail.md) for every claim.)

Metadata and full claim list: [full detail](codeium-react-code-editor.detail.md)
Human notes ([notes](codeium-react-code-editor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
