# omnara-ai/omnara

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1d62b055ebb4 @ c77612c90a9bb620

## Summary (orientation draft, not independently verified)

README and CONTRIBUTING describe Omnara as an open-source platform for running managed agents, with agent profiles defined in YAML, a REST API under /api/v1, Postgres-backed durable state, and self-hosting via Docker Compose. Contributor-facing instructions cover PR conventions, generated-code regeneration, and test targets.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Agents are defined in an agent.yaml profile containing an instruction and a model section with provider_config and model name. -- evidence: [README.md#L26-L33](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L26-L33)
- components (2 claim(s)):
  - [observation/documented] Agent state is committed atomically to Postgres, and agents recover automatically from crashes, restarts, and machine disconnects. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77)
  - [observation/documented] Agents can run on sandboxes from Blaxel, Daytona, Modal, or Unikraft, on user machines, or a mix, and machines can be added or removed while an agent runs. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77)
- design-choices (2 claim(s)):
  - [observation/documented] Users bring their own API keys and models via compatible endpoints (OpenRouter, LiteLLM, Ollama), with OpenAI Responses, Chat Completions, and Anthropic Messages formats supported. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77)
  - [observation/documented] The platform includes role-based access control with organization and project roles for users and API keys, separating management, configuration, operation, and viewing. -- evidence: [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: source development needs the Go version in go.mod, Node.js 24+ with Corepack, and Docker Compose; verification runs via make verify, with integration, service e2e, and credential-gated live test targets. -- evidence: [README.md#L155-L156](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L155-L156), [README.md#L149-L149](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L149-L149), [README.md#L136-L138](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L136-L138), [README.md#L143-L143](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L143-L143), [README.md#L145-L147](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L145-L147), [README.md#L151-L153](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L151-L153), [README.md#L131-L132](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L131-L132)
  - [observation/documented] Repository development practice: pull requests should be preceded by an issue for substantial changes, stay focused, use conventional titles, and run README checks; generated files must be regenerated via make targets after OpenAPI or SQL changes and committed with the source change. -- evidence: [CONTRIBUTING.md#L11-L18](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L11-L18), [CONTRIBUTING.md#L36-L36](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L36-L36), [CONTRIBUTING.md#L32-L34](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L32-L34), [CONTRIBUTING.md#L22-L22](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L22-L22), [CONTRIBUTING.md#L24-L28](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/CONTRIBUTING.md#L24-L28)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The REST API is defined in api/openapi/openapi.yaml and served under /api/v1. -- evidence: [README.md#L125-L127](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L125-L127)
  - [observation/documented] The product is usable programmatically via a CLI, a TypeScript CLI, and a REST API; profiles are created and agents launched with npx omnara commands. -- evidence: [README.md#L49-L52](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L49-L52), [README.md#L38-L45](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L38-L45), [README.md#L56-L77](https://github.com/omnara-ai/omnara/blob/1d62b055ebb48165bd4ec684f09dffbe510d5d3c/README.md#L56-L77)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](omnara.detail.md)

Metadata and full claim list: [full detail](omnara.detail.md)
Human notes ([notes](omnara.notes.md), never overwritten by build)

[Back to map index](../../index.md)
