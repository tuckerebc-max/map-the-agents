# omnara-ai/omnara -- full detail

[Back to orientation](omnara.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/omnara-ai/omnara/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/c77612c90a9bb620.json](../../../wiki/dossiers/omnara-ai/omnara/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/c77612c90a9bb620.json)

## specifications (1 claim(s))

- [observation/documented] Agents are defined in an agent.yaml profile containing an instruction and a model section with provider_config and model name. -- evidence: [README.md#L26-L33](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L26-L33) (`clm_dae648e1fc1c91a4ae29edac5cb7afd913e049f52fa30b233d767cdc10b40202`)

## components (2 claim(s))

- [observation/documented] Agent state is committed atomically to Postgres, and agents recover automatically from crashes, restarts, and machine disconnects. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77) (`clm_4be89e5603cecca9a2c4879c99754cf8ed4e7e9e24820518a2ae7c6cf5181168`)
- [observation/documented] Agents can run on sandboxes from Blaxel, Daytona, Modal, or Unikraft, on user machines, or a mix, and machines can be added or removed while an agent runs. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77) (`clm_7d546220dc7b7da41cf5bd1779f0cc7c4af72f63c315906bd695e7f53db69d9f`)

## design-choices (2 claim(s))

- [observation/documented] Users bring their own API keys and models via compatible endpoints (OpenRouter, LiteLLM, Ollama), with OpenAI Responses, Chat Completions, and Anthropic Messages formats supported. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77) (`clm_10738a84ae8a5c40333dae4b7d234da071e60f149fb3450f0c371add05df5c03`)
- [observation/documented] The platform includes role-based access control with organization and project roles for users and API keys, separating management, configuration, operation, and viewing. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77) (`clm_2574fcc0d7192f0e518aa333e120723f9c1a8689d6402651d23061a52fabb610`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: source development needs the Go version in go.mod, Node.js 24+ with Corepack, and Docker Compose; verification runs via make verify, with integration, service e2e, and credential-gated live test targets. -- evidence: [README.md#L155-L156](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L155-L156), [README.md#L149-L149](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L149-L149), [README.md#L136-L138](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L136-L138), [README.md#L143-L143](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L143-L143), [README.md#L145-L147](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L145-L147), [README.md#L151-L153](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L151-L153), [README.md#L131-L132](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L131-L132) (`clm_9200b6d65b1efc5773ad8c317b4870892c38bedd8cb33647f6315960b3616376`)
- [observation/documented] Repository development practice: pull requests should be preceded by an issue for substantial changes, stay focused, use conventional titles, and run README checks; generated files must be regenerated via make targets after OpenAPI or SQL changes and committed with the source change. -- evidence: [CONTRIBUTING.md#L11-L18](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L11-L18), [CONTRIBUTING.md#L36-L36](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L36-L36), [CONTRIBUTING.md#L32-L34](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L32-L34), [CONTRIBUTING.md#L22-L22](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L22-L22), [CONTRIBUTING.md#L24-L28](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L24-L28) (`clm_be4e618150896860bf140534fa3b6ea49cc46a89c6cad853577e839a34bb1ebd`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The REST API is defined in api/openapi/openapi.yaml and served under /api/v1. -- evidence: [README.md#L125-L127](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L125-L127) (`clm_d09ed34ba44adb907c7d58ba2c0a449fe82e5c13fc10a377b34794a33ee20c27`)
- [observation/documented] The product is usable programmatically via a CLI, a TypeScript CLI, and a REST API; profiles are created and agents launched with npx omnara commands. -- evidence: [README.md#L49-L52](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L49-L52), [README.md#L38-L45](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L38-L45), [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77) (`clm_6a619053d3c8c33b4adc284171e8b6f5c6f605d5a0e7cc31264cc1d85a56445a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Self-hosting requires Docker with Compose; published images can be run or the stack built from source via docker compose with the app profile. -- evidence: [README.md#L96-L100](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L96-L100), [README.md#L92-L92](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L92-L92), [README.md#L104-L108](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L104-L108) (`clm_53489c4dc7e5318f25427c5258596f1dae9d64effd323d4f3e81bf4db0bc71f1`)

## limitations (1 claim(s))

- [observation/documented] Local development defaults are intentionally insecure and the README warns against using them in deployed environments, pointing to the self-hosting guide for production setup. -- evidence: [README.md#L117-L121](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L117-L121) (`clm_2bcce282001139f87d0a575e4774cc413c81d91cdaecc4310a7eb97d5162b2ca`)

## relevance (1 claim(s))

- [observation/documented] Omnara targets developers building agents for internal or customer-facing products and teams interacting with agents through the dashboard or a first-party Slack connector. -- evidence: [README.md#L17-L22](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L17-L22) (`clm_5a72d87d8b89691b749df72ffeb0b5aa3602ad41667d4b164f00e6bf50d47e59`)

