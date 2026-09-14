# microsoft/typechat -- full detail

[Back to orientation](typechat.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/microsoft/typechat/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/607b40318815028b.json](../../../wiki/dossiers/microsoft/typechat/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/607b40318815028b.json)

## specifications (1 claim(s))

- [observation/documented] TypeChat is a library for building natural language interfaces using types, replacing prompt engineering with schema engineering. -- evidence: [README.md#L3-L3](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L3-L3), [README.md#L7-L7](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L7-L7) (`clm_532b10bde929022cee04542b26cdb8863958e14e4f4147c9deb75815d8c8a783`)

## components (1 claim(s))

- [observation/documented] After validation, TypeChat summarizes the resulting instance succinctly without using an LLM to confirm alignment with user intent. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L13-L15) (`clm_3b39565381a90c73d1973b5d86ba82d4504246e11cbc9f91e7da9121b5824cdc`)

## design-choices (2 claim(s))

- [observation/documented] Developers define types representing supported intents, from simple sentiment classification to complex schemas like shopping carts or music apps. -- evidence: [README.md#L9-L9](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L9-L9) (`clm_3f97560752a84efde2f19f2f57b465a5a28565a0cd5af09a7c7fbc3754326c52`)
- [observation/documented] Schemas can be extended by adding types to a discriminated union, and made hierarchical via a meta-schema that selects sub-schemas from user input. -- evidence: [README.md#L9-L9](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L9-L9) (`clm_e110ca5bc9af171f6664a5f13c876e8ff70e185056b53c30c00ec9d6f873b2bb`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributions require agreeing to a Contributor License Agreement, with a CLA bot decorating pull requests to determine status. -- evidence: [README.md#L55-L57](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L55-L57), [README.md#L51-L53](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L51-L53) (`clm_1e965e0095096478658bda15e03ee67bae21f69fe50f67ebd798df3e44983e30`)
- [observation/documented] Repository development practice: the project adopts the Microsoft Open Source Code of Conduct, with questions directed to opencode@microsoft.com. -- evidence: [CODE_OF_CONDUCT.md#L3-L3](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/CODE_OF_CONDUCT.md#L3-L3), [README.md#L59-L61](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L59-L61) (`clm_05c69a67ddc6f59acf6925fecd08da692e8e4509a1e112e765fd4df62a0289be`)
- [observation/documented] Repository development practice: security vulnerabilities must not be filed as public GitHub issues; they go to MSRC via its report form or secure@microsoft.com, preferably encrypted with Microsoft's PGP key. -- evidence: [SECURITY.md#L13-L13](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SECURITY.md#L13-L13), [SECURITY.md#L11-L11](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SECURITY.md#L11-L11), [SECURITY.md#L15-L15](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SECURITY.md#L15-L15) (`clm_633fc8f798ebd83452a9e608fb486c1bb293190a57d1ca935f7d4efda0751b99`)
- [observation/documented] Repository development practice: bugs and feature requests are tracked via GitHub Issues (search first for duplicates), while usage questions go to GitHub Discussions or Stack Overflow. -- evidence: [SUPPORT.md#L5-L7](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SUPPORT.md#L5-L7), [SUPPORT.md#L9-L9](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SUPPORT.md#L9-L9) (`clm_a9010f0c190ff7f4944ef91b666c6708cf6fda6be5ea4d01b0618b78ff206f08`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Example projects live under typescript/examples and can be run locally or in a GitHub Codespace; documentation is hosted at microsoft.github.io/TypeChat. -- evidence: [README.md#L47-L47](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L47-L47), [README.md#L45-L45](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L45-L45) (`clm_a1ab767e14284b8f7931aaf04f85dc87163584baa15c8e8bf2c3a3fa599e97b6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] TypeChat's pipeline: builds an LLM prompt from the types, validates the response against the schema, and repairs invalid output through further model interaction. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L13-L15) (`clm_833b73fc6fcb8c19819e08dd75a0cea1cff58094a461d768b704cb27450210ba`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The TypeScript/JavaScript package is installed via npm install typechat; Python and C#/.NET variants exist, with .NET hosted in a separate TypeChat.net repository. -- evidence: [README.md#L41-L43](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L41-L43), [README.md#L23-L25](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L23-L25), [README.md#L21-L21](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/README.md#L21-L21) (`clm_95141e5104f1d5ceb2589152e36b25d1a42396038a93da37f965079cb19d7f0e`)

## limitations (1 claim(s))

- [observation/documented] Support for the project is limited to the listed community resources; Microsoft does not provide additional support channels for it. -- evidence: [SUPPORT.md#L13-L13](https://github.com/microsoft/TypeChat/blob/83caa1242d9a9a707a4a66bfbc5fe6174cbcb8dc/SUPPORT.md#L13-L13) (`clm_82ce99fd8b0d3c37efd0f0c08a57b835102217be22c10a70e75874913fab79e2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

