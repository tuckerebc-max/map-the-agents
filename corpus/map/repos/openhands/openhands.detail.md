# openhands/openhands -- full detail

[Back to orientation](openhands.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openhands/openhands/28464621d879e3e9b3ceeae9d70a71d96da6212d/f5c20f1428089f35.json](../../../wiki/dossiers/openhands/openhands/28464621d879e3e9b3ceeae9d70a71d96da6212d/f5c20f1428089f35.json)

## specifications (1 claim(s))

- [observation/documented] Agent Canvas is described as a self-hosted developer control center for coding agents and automations, currently in beta status. -- evidence: [README.md#L3-L31](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L3-L31), [README.md#L33-L33](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L33-L33) (`clm_3eb5905676aaa9b01f870acc7cba1c41ecaa6ebe95979991b3cdde6d7184b29b`)

## components (1 claim(s))

- [observation/documented] Agent Canvas is powered by the OpenHands Agent Server, a REST API for running multiple agents on one machine; the frontend can connect to and switch between multiple Agent Servers. -- evidence: [README.md#L126-L126](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L126-L126) (`clm_ab89b3e6f087705482b6c66f6b7487d2acc55f07efc9bd120e7e31a254b1fd25`)

## design-choices (1 claim(s))

- [observation/documented] The project is split across repositories: this repo owns the frontend, backend selection, and local-stack orchestration, while the SDK owns the Agent Server API and the automation repo owns scheduling and dispatching. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150), [README.md#L143-L148](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L143-L148) (`clm_b102b6fbf0dd73b87495b80b328e6fd09ac258d037bc803aa0c14527fd5e220d`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are directed to AGENTS.md for contributor-specific repository boundaries and a required custom code-review guide. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150) (`clm_c4e24fcc04fef0d130e6b37aaa2389bbdbb1304395e66cd59b6820e67fe33d80`)
- [observation/documented] Repository development practice: the changelog follows Keep a Changelog format and the project adheres to Semantic Versioning; npm publishing is automated via a GitHub Actions workflow with OIDC trusted publishing. -- evidence: [CHANGELOG.md#L5-L6](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/CHANGELOG.md#L5-L6), [CHANGELOG.md#L14-L26](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/CHANGELOG.md#L14-L26) (`clm_9612de43cf60e1e4ca02f455466c104378c7b336246d5bc60f3b93508005784b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] It can run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. -- evidence: [README.md#L3-L31](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L3-L31) (`clm_fc6129a93846711e98cfe1c967e72301cac361acb4a3e2253bf8319653df7d71`)
- [observation/documented] The agent-canvas CLI starts the full local stack by default and supports --frontend-only and --backend-only flags to run pieces separately. -- evidence: [README.md#L75-L75](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L75-L75), [README.md#L77-L80](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L77-L80) (`clm_b5778ec096c8aedf70bda1d8e9768c89805135737f4f2341627da89487741738`)
- [observation/documented] The UI is served at localhost:8000 for npm/source launches and at /canvas for the Docker image, with backends addable from the UI. -- evidence: [README.md#L122-L122](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L122-L122) (`clm_49c25e9e4c714aa8c5ff0386c2b77d3f42de2833fc38028ce18331f7420d7917`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] An Automation Server can be paired with the Agent Server to run agents on a schedule or in response to events, dispatching conversations to the Agent Server/SDK. -- evidence: [README.md#L150-L150](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L150-L150), [README.md#L135-L135](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L135-L135) (`clm_f1c91aec83a0e9718c944ae4ea5faa2012761c4654b0ee3e5d2bc82d01b4a720`)

## tools-permissions (1 claim(s))

- [observation/documented] Running without a sandbox executes the agent-server directly on the host, where the agent has full filesystem access; the Docker option restricts agent access to projects under PROJECTS_PATH. -- evidence: [README.md#L65-L66](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L65-L66), [README.md#L104-L104](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L104-L104) (`clm_08c1442c8ba39b44ad195fc4f799f82db630b67adde1d4462d9faa7388cc4a99`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Non-sandboxed installs require Node.js 22.12.x or later and uv; the Docker option requires Docker Desktop or Engine and a PROJECTS_PATH host directory. -- evidence: [README.md#L68-L68](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L68-L68), [README.md#L86-L87](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/README.md#L86-L87) (`clm_117813620b870bc6441ccc1278877749b78300ab93e19feb74cb46c736d9a13f`)
- [observation/documented] The npm package @openhands/agent-canvas exposes subpath exports (browser, conversation, files, settings, sidebar, terminal, i18n) and TypeScript type declarations. -- evidence: [CHANGELOG.md#L14-L26](https://github.com/OpenHands/OpenHands/blob/28464621d879e3e9b3ceeae9d70a71d96da6212d/CHANGELOG.md#L14-L26) (`clm_fae76b886e09b271c63e2a5b69d39679cc5aee3afac8147115dae5d39437917b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

