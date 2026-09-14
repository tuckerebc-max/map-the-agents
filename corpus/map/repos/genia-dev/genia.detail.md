# genia-dev/genia -- full detail

[Back to orientation](genia.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/genia-dev/genia/39a206b85d84d72c8bab3ff1e724f821443e52ad/b0f34378113763be.json](../../../wiki/dossiers/genia-dev/genia/39a206b85d84d72c8bab3ff1e724f821443e52ad/b0f34378113763be.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The project positions the agent as a production-grade team member operating inside a team's Slack channel and executing tasks in the production environment on users' behalf. -- evidence: [README.md#L4-L15](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L4-L15), [README.md#L44-L44](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L44-L44) (`clm_ec6b6b950f91f55283257136855766529f9cd264873a0e6ac041a2059fb129c9`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork the repo and submit pull requests, run tests with 'poetry run pytest tests', and can build/run the project via Docker or Poetry commands documented in the developer guide. -- evidence: [docs/developer-guide.md#L17-L19](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L17-L19), [docs/developer-guide.md#L5-L9](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L5-L9), [docs/developer-guide.md#L57-L59](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L57-L59), [README.md#L124-L126](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L124-L126), [docs/developer-guide.md#L37-L39](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L37-L39) (`clm_cf971297c59910ae04981a6640df33ecea79e77260013296795cd0e867fbdfdb`)
- [observation/documented] Repository development practice: local setup requires copying .env.template to .env with OPENAI_API_KEY as the minimal secret, and the repo displays a CI workflow badge. -- evidence: [docs/developer-guide.md#L13-L13](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L13-L13), [README.md#L1-L2](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L1-L2) (`clm_516ae2f346bbba598d3b77550c48365730fa40880d5e142ffa80166c16197f4c`)

## skills-patterns (3 claim(s))

- [observation/documented] New tools are added via YAML specs following OpenAI JSON function-configuration standards, with usage guidance kept in a separate tools.yaml file. -- evidence: [docs/add-new-tool.md#L5-L6](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L5-L6) (`clm_460cb09ad9855a9dc0e1addaa7ad98f73d459ba693df51e9496cd738ea5e4c1f`)
- [observation/documented] Tool specs support Python code tools (naming a class and method), URL tools performing GET requests via templated URLs, and OpenAPI Swagger-based integrations, the latter noted as still under development. -- evidence: [docs/add-new-tool.md#L22-L27](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L22-L27), [docs/add-new-tool.md#L12-L16](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L12-L16), [docs/add-new-tool.md#L29-L30](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L29-L30) (`clm_11d97d31b18f60a9732beb06b05921fd121caf1fac55c40d384de6d0e90b59f5`)
- [observation/documented] An experimental feature lets the agent learn new skills from natural language by storing accomplished task steps in long-term memory, categorizing them as a skill, and reloading them for future use. -- evidence: [docs/add-new-tool.md#L29-L30](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L29-L30) (`clm_09ebb0b675199ec4db496ec19c24e02b213ddf038ccd52313c2df0c0953102f5`)

## interfaces (1 claim(s))

- [observation/documented] The product can run in three modes: a local terminal mode, a Slack app bot mode, and a Streamlit web app mode, per the developer guide and README. -- evidence: [docs/developer-guide.md#L17-L19](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L17-L19), [docs/developer-guide.md#L45-L47](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L45-L47), [README.md#L115-L117](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L115-L117), [README.md#L109-L111](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L109-L111), [docs/developer-guide.md#L51-L53](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L51-L53), [docs/developer-guide.md#L23-L25](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L23-L25) (`clm_a4b48ffe496d036d367a1448088dbc70aef76308b5b9e29099ee3e946f201ae9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] GeniA is built on OpenAI's function-calling capability (OpenAI or Azure) and requires an OpenAI API key to run. -- evidence: [README.md#L32-L32](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L32-L32), [docs/faq.md#L3-L4](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/faq.md#L3-L4) (`clm_1fefc086b206a3fd1cd7890e856a1eb1f5fd38dce413d7f5822a4585ca64bb21`)
- [observation/documented] By default the product uses the gpt-3.5-turbo-0613 model; the FAQ notes gpt-4-0613 often gives better results but 3.5 was chosen as more cost-effective. -- evidence: [docs/faq.md#L10-L11](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/faq.md#L10-L11) (`clm_687cda6c8c462c92ca5377c3eb1c8c55e73494a0b76034184b8dec2e21adde83`)

## limitations (1 claim(s))

- [observation/documented] The roadmap lists capabilities not yet present: OKTA SSO integration, RBAC support, and extension with thousands of new tools are future plans. -- evidence: [README.md#L145-L147](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L145-L147) (`clm_6d752c104e78ff18d1ee57e82d104bac0e7bc2e109f7fefef4cddb16d30b73ff`)

## relevance (1 claim(s))

- [observation/documented] Documented use cases target platform-engineering teams: k8s/Argo deployments and troubleshooting, FinOps cloud-cost reporting, SecOps vulnerability checks, SRE outage troubleshooting, and DevOps cluster upgrades. -- evidence: [README.md#L73-L75](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L73-L75), [README.md#L89-L91](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L89-L91), [README.md#L65-L67](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L65-L67), [README.md#L97-L99](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L97-L99), [README.md#L81-L83](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L81-L83) (`clm_0e64851e42b7e152ae742a8caeeb9a96d20b26febc82801004a7795aa2f31c6e`)

