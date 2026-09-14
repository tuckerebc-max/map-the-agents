# microsoft/typechat

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 83caa1242d9a @ 607b40318815028b

## Summary (orientation draft, not independently verified)

Evidence is limited to the top-level README and community/support files of microsoft/typechat. It documents TypeChat as a library for building natural-language interfaces from types, its schema-engineering approach and pipeline, plus contribution, security, and support policies; no code internals are shown.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] TypeChat is a library for building natural language interfaces using types, replacing prompt engineering with schema engineering. -- evidence: [README.md#L3-L3](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L3-L3), [README.md#L7-L7](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] After validation, TypeChat summarizes the resulting instance succinctly without using an LLM to confirm alignment with user intent. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L13-L15)
- design-choices (2 claim(s)):
  - [observation/documented] Developers define types representing supported intents, from simple sentiment classification to complex schemas like shopping carts or music apps. -- evidence: [README.md#L9-L9](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L9-L9)
  - [observation/documented] Schemas can be extended by adding types to a discriminated union, and made hierarchical via a meta-schema that selects sub-schemas from user input. -- evidence: [README.md#L9-L9](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L9-L9)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributions require agreeing to a Contributor License Agreement, with a CLA bot decorating pull requests to determine status. -- evidence: [README.md#L55-L57](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L55-L57), [README.md#L51-L53](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L51-L53)
  - [observation/documented] Repository development practice: the project adopts the Microsoft Open Source Code of Conduct, with questions directed to opencode@microsoft.com. -- evidence: [CODE_OF_CONDUCT.md#L3-L3](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/CODE_OF_CONDUCT.md#L3-L3), [README.md#L59-L61](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L59-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Example projects live under typescript/examples and can be run locally or in a GitHub Codespace; documentation is hosted at microsoft.github.io/TypeChat. -- evidence: [README.md#L47-L47](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L47-L47), [README.md#L45-L45](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L45-L45)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] TypeChat's pipeline: builds an LLM prompt from the types, validates the response against the schema, and repairs invalid output through further model interaction. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L13-L15)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The TypeScript/JavaScript package is installed via npm install typechat; Python and C#/.NET variants exist, with .NET hosted in a separate TypeChat.net repository. -- evidence: [README.md#L41-L43](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L41-L43), [README.md#L23-L25](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L23-L25), [README.md#L21-L21](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L21-L21)
- limitations (1 claim(s)):
  - [observation/documented] Support for the project is limited to the listed community resources; Microsoft does not provide additional support channels for it. -- evidence: [SUPPORT.md#L13-L13](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SUPPORT.md#L13-L13)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](typechat.detail.md) for every claim.)

Metadata and full claim list: [full detail](typechat.detail.md)
Human notes ([notes](typechat.notes.md), never overwritten by build)

[Back to map index](../../index.md)
