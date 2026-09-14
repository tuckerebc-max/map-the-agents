# 2389-research/2389-agent-rust -- full detail

[Back to orientation](2389-agent-rust.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/2389-agent-rust/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/e524e8d668e3072d.json](../../../wiki/dossiers/2389-research/2389-agent-rust/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/e524e8d668e3072d.json)

## specifications (1 claim(s))

- [observation/documented] The architecture doc describes this project as a Rust implementation of the 2389 Agent Protocol, with agents interoperating over MQTT and an emphasis on reliability and strict protocol compliance. -- evidence: [docs/ARCHITECTURE.md#L18-L20](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L18-L20) (`clm_1fb3cce3856d8599171fd91df82c91b29b7b646623c9e4896d45842692066fd9`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] An accepted architecture decision record states Rust was chosen for the core implementation, citing memory safety without garbage-collection overhead and strong async support as rationale. -- evidence: [docs/ARCHITECTURE.md#L862-L862](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L862-L862), [docs/ARCHITECTURE.md#L866-L870](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L866-L870) (`clm_a4c2a78039fc7ff988af0410b5cebc648537754390b8a637bc4b363bcdab023b`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Documentation describes an explicit agent lifecycle moving through Uninitialized, Initializing, Running, Stopping and Stopped, with any state able to transition to an Error state on failure. -- evidence: [docs/ARCHITECTURE.md#L69-L72](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L69-L72), [docs/ARCHITECTURE.md#L556-L560](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L556-L560) (`clm_40000d59be14b8c76d56b55f1beca7e77d0b0dfa088e8096c42f202ddd1cf026`)

## tools-permissions (2 claim(s))

- [observation/documented] Listed tool-execution security controls include JSON-schema validation of parameters, per-tool process isolation with timeouts, and restricting available tools to an allow-list. -- evidence: [docs/ARCHITECTURE.md#L279-L282](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L279-L282) (`clm_c6ce283c6a9311c402be2b9cb45ac246f41dd74cdc812a280afec3a3379c0e1d`)
- [observation/documented] The threat model names four trust boundaries: the MQTT network perimeter, process isolation around tool execution, the LLM provider API boundary, and input validation at the data boundary. -- evidence: [docs/ARCHITECTURE.md#L626-L629](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L626-L629) (`clm_08094b898032f30087693c9da28d6e638d9bf0c3792e2890bfbcce87657dcba4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The LLM integration layer is documented as provider-agnostic behind a shared trait, with Anthropic Claude and OpenAI GPT listed as the currently supported providers. -- evidence: [docs/ARCHITECTURE.md#L318-L320](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L318-L320), [docs/ARCHITECTURE.md#L294-L294](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L294-L294) (`clm_fd4cc04f0f0c6bb196ea2241262581ce69d2ab73c38155a2b3c5358e65a098cc`)
- [observation/documented] A second accepted decision record names rumqttc as the MQTT client library, noting it avoids external C dependencies since it is a pure-Rust implementation. -- evidence: [docs/ARCHITECTURE.md#L885-L885](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L885-L885), [docs/ARCHITECTURE.md#L896-L899](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L896-L899) (`clm_3b5d917c455185f35669ddd1720db8f4053dd56edb676bc092c72b28dd78233c`)

## limitations (1 claim(s))

- [observation/documented] The Rust-language decision record acknowledges two consequences: a steeper learning curve for contributors unfamiliar with Rust, and longer compile times than an interpreted language would have. -- evidence: [docs/ARCHITECTURE.md#L874-L877](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L874-L877) (`clm_0e8319ee1c7a4658b65ec1218313a80514e3998cfe89b389333076ef4236cc57`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

