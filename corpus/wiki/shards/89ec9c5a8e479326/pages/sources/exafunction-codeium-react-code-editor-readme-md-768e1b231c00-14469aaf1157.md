---
access: public
aliases: []
claim_ids:
- clm_1dff493b154e1b0f10365d9d6637fef908afbff69064452a09a4221f5f6f241c
- clm_3d68b89eeb7ca0ace8dfef8cda1d47cf28e26b400c0d0e66d3185f15cb4791a8
- clm_4049cac0bdc1963a70ec2ce62d8790bc46fb30ea2dcc39bc09ec246761f0fcba
- clm_7078b08d2eecbc6ebb64a8f6bf79d7d5be3660991be9c2df9290a9ab02217491
- clm_79cf43d90310a80bec6fe2b810d5b19168ea07c5bb26992abb41b85ff37c55fd
- clm_7b0963b3ee92a82a5145002cb4b0a75357a582b649e2797fcc49851f70600bad
- clm_cd8c74774b504c476931c54742491eb4892ec8a6567132dead80ca772bbda81b
- clm_ce9667cb1c1234cb2e304e420d4888f2f317b35e5b437558f1628ad04b388bc2
- clm_d4eca92fca61122171a847f89c98738e560f8ea41ecbadd49f984533525fa2de
- clm_ea171323ba5f63fe8db72aba3aa6721b15a0f564c7a5f6ed385f46bf1a4058da
maturity: draft
page_id: pg_231b8572c03055a8a78a14469aaf1157
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ae54be1300cf559284ca51de5d4fa645
title: Exafunction/codeium-react-code-editor/readme.md @ 768e1b231c00
updated_at: '2026-09-14T03:50:02Z'
---

# Exafunction/codeium-react-code-editor/readme.md @ 768e1b231c00

<!-- rcw:begin owner=source:src_ae54be1300cf559284ca51de5d4fa645 block=evidence -->
- The core editor API matches that of the wrapped Monaco React project, and the component is imported as CodeiumEditor from @codeium/react-code-editor. [@claim:clm_1dff493b154e1b0f10365d9d6637fef908afbff69064452a09a4221f5f6f241c]
- The otherDocuments prop accepts at most 10 documents, and a reranker runs behind the scenes to optimize what fits within the token limit. [@claim:clm_3d68b89eeb7ca0ace8dfef8cda1d47cf28e26b400c0d0e66d3185f15cb4791a8]
- Installation is supported via npm, yarn, or pnpm using the package name @codeium/react-code-editor. [@claim:clm_4049cac0bdc1963a70ec2ce62d8790bc46fb30ea2dcc39bc09ec246761f0fcba]
- The project depends on and extends Suren Atoyan's Monaco React project, which it credits as foundational. [@claim:clm_7078b08d2eecbc6ebb64a8f6bf79d7d5be3660991be9c2df9290a9ab02217491]
- CodeiumEditor accepts props including language, theme, and otherDocuments; the advanced example passes Document objects with absolutePath, relativePath, text, editorLanguage, and language fields. [@claim:clm_79cf43d90310a80bec6fe2b810d5b19168ea07c5bb26992abb41b85ff37c55fd]
- An ESM build is available via the subpath @codeium/react-code-editor/dist/esm; TypeScript users may need a module declaration workaround for missing types. [@claim:clm_7b0963b3ee92a82a5145002cb4b0a75357a582b649e2797fcc49851f70600bad]
- Autocomplete is context-aware: the editor analyzes its content (and neighboring documents) to predict suggestions, with multi-document context improving completion quality. [@claim:clm_cd8c74774b504c476931c54742491eb4892ec8a6567132dead80ca772bbda81b]
- Dual CommonJS/ESM support is described as an open issue, and pull requests fixing it are welcome. [@claim:clm_ce9667cb1c1234cb2e304e420d4888f2f317b35e5b437558f1628ad04b388bc2]
- The package is a React code-editor component providing AI autocomplete, built as a wrapper around Microsoft's Monaco editor (the editor powering VS Code). [@claim:clm_d4eca92fca61122171a847f89c98738e560f8ea41ecbadd49f984533525fa2de]
- The package is free and open-source with no account required, and a live demo is hosted at codeium.com/playground. [@claim:clm_ea171323ba5f63fe8db72aba3aa6721b15a0f564c7a5f6ed385f46bf1a4058da]
<!-- rcw:end owner=source:src_ae54be1300cf559284ca51de5d4fa645 block=evidence -->

## Researcher notes

