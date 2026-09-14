# exafunction/codeium-react-code-editor -- full detail

[Back to orientation](codeium-react-code-editor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/exafunction/codeium-react-code-editor/768e1b231c00e078c86bc19c8ede697a1e37ec75/8df5fe65efa0abcb.json](../../../wiki/dossiers/exafunction/codeium-react-code-editor/768e1b231c00e078c86bc19c8ede697a1e37ec75/8df5fe65efa0abcb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The package is a React code-editor component providing AI autocomplete, built as a wrapper around Microsoft's Monaco editor (the editor powering VS Code). -- evidence: [readme.md#L7-L7](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L7-L7), [readme.md#L99-L99](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L99-L99) (`clm_d4eca92fca61122171a847f89c98738e560f8ea41ecbadd49f984533525fa2de`)

## design-choices (2 claim(s))

- [observation/documented] The otherDocuments prop accepts at most 10 documents, and a reranker runs behind the scenes to optimize what fits within the token limit. -- evidence: [readme.md#L89-L89](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L89-L89) (`clm_3d68b89eeb7ca0ace8dfef8cda1d47cf28e26b400c0d0e66d3185f15cb4791a8`)
- [observation/documented] Autocomplete is context-aware: the editor analyzes its content (and neighboring documents) to predict suggestions, with multi-document context improving completion quality. -- evidence: [readme.md#L50-L50](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L50-L50), [readme.md#L68-L87](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L68-L87), [readme.md#L101-L101](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L101-L101) (`clm_cd8c74774b504c476931c54742491eb4892ec8a6567132dead80ca772bbda81b`)

## workflows (1 claim(s))

- [observation/documented] Installation is supported via npm, yarn, or pnpm using the package name @codeium/react-code-editor. -- evidence: [readme.md#L29-L29](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L29-L29), [readme.md#L32-L33](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L32-L33), [readme.md#L26-L26](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L26-L26) (`clm_4049cac0bdc1963a70ec2ce62d8790bc46fb30ea2dcc39bc09ec246761f0fcba`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The core editor API matches that of the wrapped Monaco React project, and the component is imported as CodeiumEditor from @codeium/react-code-editor. -- evidence: [readme.md#L109-L109](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L109-L109), [readme.md#L37-L38](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L37-L38) (`clm_1dff493b154e1b0f10365d9d6637fef908afbff69064452a09a4221f5f6f241c`)
- [observation/documented] CodeiumEditor accepts props including language, theme, and otherDocuments; the advanced example passes Document objects with absolutePath, relativePath, text, editorLanguage, and language fields. -- evidence: [readme.md#L68-L87](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L68-L87), [readme.md#L40-L48](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L40-L48) (`clm_79cf43d90310a80bec6fe2b810d5b19168ea07c5bb26992abb41b85ff37c55fd`)
- [observation/documented] An ESM build is available via the subpath @codeium/react-code-editor/dist/esm; TypeScript users may need a module declaration workaround for missing types. -- evidence: [readme.md#L115-L115](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L115-L115), [readme.md#L117-L119](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L117-L119) (`clm_7b0963b3ee92a82a5145002cb4b0a75357a582b649e2797fcc49851f70600bad`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project depends on and extends Suren Atoyan's Monaco React project, which it credits as foundational. -- evidence: [readme.md#L13-L14](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L13-L14), [readme.md#L109-L109](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L109-L109), [readme.md#L125-L125](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L125-L125) (`clm_7078b08d2eecbc6ebb64a8f6bf79d7d5be3660991be9c2df9290a9ab02217491`)

## limitations (1 claim(s))

- [observation/documented] Dual CommonJS/ESM support is described as an open issue, and pull requests fixing it are welcome. -- evidence: [readme.md#L121-L121](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L121-L121) (`clm_ce9667cb1c1234cb2e304e420d4888f2f317b35e5b437558f1628ad04b388bc2`)

## relevance (1 claim(s))

- [observation/documented] The package is free and open-source with no account required, and a live demo is hosted at codeium.com/playground. -- evidence: [readme.md#L13-L14](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L13-L14), [readme.md#L7-L7](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L7-L7), [readme.md#L18-L18](https://github.com/Exafunction/codeium-react-code-editor/blob/768e1b231c00e078c86bc19c8ede697a1e37ec75/readme.md#L18-L18) (`clm_ea171323ba5f63fe8db72aba3aa6721b15a0f564c7a5f6ed385f46bf1a4058da`)

