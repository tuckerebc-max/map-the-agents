# amrit110/oli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 18cf418cb0ee @ 9033f0017a5fdc22

## Summary (orientation draft, not independently verified)

oli is documented as a Rust-backend, React/Ink-frontend coding assistant supporting both cloud model providers and local Ollama models, exposing a JSON-RPC 2.0 server API over stdio. Its docs describe a documented tool benchmark methodology, explicit security caveats about the server being unauthenticated, and note the project is early-stage.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes oli as an open-source coding-assistant alternative to Claude Code with a hybrid architecture, supporting cloud APIs (Anthropic, OpenAI, Google) as well as local models served through Ollama. -- evidence: [README.md#L15-L20](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L15-L20), [README.md#L13-L13](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L13-L13)
- components (1 claim(s)):
  - [observation/documented] The server exposes a JSON-RPC 2.0 API over stdio, documented to include a cancel_task method for stopping the current or a named task and a clear_conversation method for resetting conversation history. -- evidence: [docs/src/api.md#L197-L197](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L197-L197), [docs/src/api.md#L10-L11](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L10-L11), [docs/src/api.md#L233-L233](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L233-L233)
- design-choices (1 claim(s)):
  - [observation/documented] The API docs state the server can be extended with additional JSON-RPC methods by editing main.rs and registering them, citing language-server-protocol integration or MCP support as example use cases. -- evidence: [docs/src/api.md#L602-L602](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L602-L602)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to comment on an existing issue or open a new one before starting work, and to fill out the pull-request template and link it to the relevant issue. -- evidence: [CONTRIBUTING.md#L11-L12](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/CONTRIBUTING.md#L11-L12), [CONTRIBUTING.md#L5-L9](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/CONTRIBUTING.md#L5-L9)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The documented get_tasks method returns each task's id, description, status, tool count, and separate input and output token counts. -- evidence: [docs/src/api.md#L155-L163](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L155-L163)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The API docs state the server has no built-in authentication and should be treated as a trusted component, recommending a sandboxed deployment and passing model API keys through environment variables. -- evidence: [docs/src/api.md#L595-L598](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/api.md#L595-L598)
- evaluation (1 claim(s)):
  - [observation/documented] A documented benchmark methodology measures how efficiently each tool performs against local Ollama models using simple test cases, with the results table automatically refreshed by the CI/CD pipeline on new pull requests. -- evidence: [docs/src/benchmark.md#L8-L9](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/benchmark.md#L8-L9), [docs/src/benchmark.md#L13-L13](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/docs/src/benchmark.md#L13-L13)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] The README carries an explicit warning that the project is at a very early stage and prone to bugs and issues, asking users to report problems as they hit them. -- evidence: [README.md#L22-L22](https://github.com/amrit110/oli/blob/18cf418cb0ee5812761c7de664c796dca6ddfabb/README.md#L22-L22)
More evidence: [full detail](oli.detail.md)

Metadata and full claim list: [full detail](oli.detail.md)
Human notes ([notes](oli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
