# cherryhq/cherry-studio -- full detail

[Back to orientation](cherry-studio.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cherryhq/cherry-studio/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/c0035cf5a75c4323.json](../../../wiki/dossiers/cherryhq/cherry-studio/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/c0035cf5a75c4323.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Cherry Studio is a desktop client supporting multiple LLM providers, available on Windows, Mac, and Linux. -- evidence: [README.md#L37-L37](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L37-L37) (`clm_1addc01ed1de188c9a5486ee8da1a86b9c1b34e1f10a591b0ea1ea958df19d2e`)
- [observation/documented] The app supports cloud LLM services such as OpenAI, Gemini, and Anthropic, plus local models via Ollama and LM Studio. -- evidence: [README.md#L55-L57](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L55-L57) (`clm_f93331f9ae0729dd80f02f9f61d371234b324d8f16bcf09c41354a19c70e6a07`)
- [observation/documented] Advertised features include 300+ pre-configured AI assistants, custom assistant creation, and multi-model simultaneous conversations. -- evidence: [README.md#L61-L63](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L61-L63) (`clm_1bb4920b8dac1198067ec84e63c2143a6c66bff14ce3987ffa4ea1e0a6286422`)

## design-choices (3 claim(s))

- [observation/documented] The architecture follows an Electron process model with main, renderer, shared, and utility-process layers, each with documented dependency rules. -- evidence: [docs/README.md#L55-L62](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L55-L62) (`clm_519228072d71e11a6d1af2e564551e841244e2986511f984572a8c8652ec2e71`)
- [observation/documented] The file domain splits into FileManager for persistent FileEntry records and DirectoryTreeManager for in-memory directory mirrors, which do not automatically join. -- evidence: [docs/references/file/architecture.md#L15-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/references/file/architecture.md#L15-L16), [docs/references/file/architecture.md#L18-L19](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/references/file/architecture.md#L18-L19) (`clm_a1bffa8cd353c467adf4de5aa7d48d143bbfd373426b497f06eca0d858c44f6f`)
- [observation/documented] The Community Edition is licensed under AGPL-3.0, with commercial licenses available by contact; an Enterprise Edition offers private deployment. -- evidence: [README.md#L197-L197](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L197-L197), [README.md#L262-L262](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L262-L262), [README.md#L266-L266](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L266-L266) (`clm_8bf9aee384633abf38130fc6a03076914b6cc302e4e63a1f5152eb57ced52731`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributions follow a documented branching strategy with pull request guidelines and version tag management targeting main. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16), [README.md#L148-L148](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L148-L148) (`clm_6e387bbe072c4af6297c39fab0daac4405f3cc4f5e7b00ccd952bf10873be285`)
- [observation/documented] Repository development practice: a maintainer runbook covers preparing, validating, hotfixing, publishing, and synchronizing release branches, and a Test Plan process governs beta and rc testing. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16) (`clm_58b46ca21d7990952f55e3c85d9baabb0e4d7262b7a02677bc237b946be196f0`)
- [observation/documented] Repository development practice: getting started steps are fork, create a branch, commit and push, then open a pull request describing the changes. -- evidence: [README.md#L152-L155](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/README.md#L152-L155) (`clm_7afe7c010a72c7cc99d1374a603dc4da2d04463c8717e3364ad2d578e4c695da`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A local HTTP API gateway exposes OpenAI, Anthropic, Gemini, Cherry REST, and MCP-compatible client endpoints. -- evidence: [docs/README.md#L49-L51](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L49-L51) (`clm_a439c3d6a3d2dc95045bbdddbeccb2b69dbf71c1f5aacb4f30cabc052bceae93`)
- [observation/documented] A LAN transfer protocol specification covers desktop-mobile sync using mDNS discovery, a TCP handshake, and file transfer. -- evidence: [docs/README.md#L179-L181](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L179-L181) (`clm_056f1035c4085b8b2c5fed7580284a7a29ce8227cc5167fd1e082b9582f395a3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Linux packaging uses pinned better-sqlite3 prebuilds, with documented build commands and prebuild update steps. -- evidence: [docs/README.md#L7-L16](https://github.com/CherryHQ/cherry-studio/blob/61cac30ece4dfae7eca8f08e441ad584e2ea8c59/docs/README.md#L7-L16) (`clm_73320509ca7623179a7b28be0571f88f4b96f0d93af40805c8264e99d82e17be`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

