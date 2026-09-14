# 2389-research/2389-agent-rust

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 9ebe8438dbdb @ e524e8d668e3072d

## Summary (orientation draft, not independently verified)

2389-agent-rust documents a Rust implementation of the 2389 Agent Protocol whose agents communicate over MQTT, with an explicit lifecycle state machine, tool-execution security controls, provider-agnostic LLM integration, and two accepted architecture decisions covering the choice of Rust and the MQTT client library.

## Source coverage

Source coverage (partial): 6 of 38 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The architecture doc describes this project as a Rust implementation of the 2389 Agent Protocol, with agents interoperating over MQTT and an emphasis on reliability and strict protocol compliance. -- evidence: [docs/ARCHITECTURE.md#L18-L20](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L18-L20)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] An accepted architecture decision record states Rust was chosen for the core implementation, citing memory safety without garbage-collection overhead and strong async support as rationale. -- evidence: [docs/ARCHITECTURE.md#L862-L862](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L862-L862), [docs/ARCHITECTURE.md#L866-L870](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L866-L870)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Documentation describes an explicit agent lifecycle moving through Uninitialized, Initializing, Running, Stopping and Stopped, with any state able to transition to an Error state on failure. -- evidence: [docs/ARCHITECTURE.md#L69-L72](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L69-L72), [docs/ARCHITECTURE.md#L556-L560](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L556-L560)
- tools-permissions (2 claim(s)):
  - [observation/documented] Listed tool-execution security controls include JSON-schema validation of parameters, per-tool process isolation with timeouts, and restricting available tools to an allow-list. -- evidence: [docs/ARCHITECTURE.md#L279-L282](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L279-L282)
  - [observation/documented] The threat model names four trust boundaries: the MQTT network perimeter, process isolation around tool execution, the LLM provider API boundary, and input validation at the data boundary. -- evidence: [docs/ARCHITECTURE.md#L626-L629](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L626-L629)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The LLM integration layer is documented as provider-agnostic behind a shared trait, with Anthropic Claude and OpenAI GPT listed as the currently supported providers. -- evidence: [docs/ARCHITECTURE.md#L318-L320](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L318-L320), [docs/ARCHITECTURE.md#L294-L294](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L294-L294)
  - [observation/documented] A second accepted decision record names rumqttc as the MQTT client library, noting it avoids external C dependencies since it is a pure-Rust implementation. -- evidence: [docs/ARCHITECTURE.md#L885-L885](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L885-L885), [docs/ARCHITECTURE.md#L896-L899](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L896-L899)
- limitations (1 claim(s)):
  - [observation/documented] The Rust-language decision record acknowledges two consequences: a steeper learning curve for contributors unfamiliar with Rust, and longer compile times than an interpreted language would have. -- evidence: [docs/ARCHITECTURE.md#L874-L877](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L874-L877)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](2389-agent-rust.detail.md).

Metadata and full claim list: [full detail](2389-agent-rust.detail.md)
Human notes ([notes](2389-agent-rust.notes.md), never overwritten by build)

[Back to map index](../../index.md)
