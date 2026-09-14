# 2389-research/mux-rs

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit c25c6c8e1acb @ cac42de95f8bbe12

## Summary (orientation draft, not independently verified)

The evidence consists of two planning documents: a design doc for mux-rs (a Rust agentic infrastructure library with LLM clients, tools, permissions, and MCP) and a task-by-task implementation plan for an Anthropic API client. All claims describe planned/documented design rather than inspected shipped code. Evidence coverage: 184 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 22 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] A plan document specifies implementing an AnthropicClient that connects to the Claude API and implements the LlmClient trait. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L5-L5](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The planned crate layout includes llm (types, client trait, anthropic, openai), tool (trait, registry, result), permission (policy, handler), mcp (types, client, proxy), an error module, and a mux-derive crate providing a #[derive(Tool)] proc macro. -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L19-L48](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L19-L48)
  - [observation/documented] The plan adds streaming support via an AnthropicStreamEvent enum (message start/stop, content block events, ping, error) and an async-stream based SSE parser that buffers chunks and splits on blank lines. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L588-L594](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L588-L594), [docs/plans/2025-12-25-anthropic-client.md#L625-L628](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L625-L628), [docs/plans/2025-12-25-anthropic-client.md#L698-L698](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L698-L698), [docs/plans/2025-12-25-anthropic-client.md#L539-L563](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L539-L563), [docs/plans/2025-12-25-anthropic-client.md#L618-L619](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L618-L619)
- design-choices (2 claim(s)):
  - [observation/documented] The planned Anthropic client architecture uses reqwest for HTTP with SSE streaming support, serializing the crate's Request type to Anthropic's format and deserializing responses back. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L7-L7](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L7-L7)
  - [observation/documented] The design doc records choices including a derive macro plus trait for tool definition, Tokio as async runtime, thiserror plus anyhow for errors, a policy engine for permissions, client-only MCP scope, and multi-provider LLM support (Anthropic and OpenAI). -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L7-L15](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L7-L15)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the plan's header instructs the implementing Claude agent to use the superpowers:executing-plans skill to implement the plan task-by-task. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L3-L3](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L3-L3)
  - [observation/documented] Repository development practice: each plan task prescribes verification via cargo check or cargo test, final clippy and cargo fmt runs, and a git commit per task with conventional-commit style messages. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L110-L111](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L110-L111), [docs/plans/2025-12-25-anthropic-client.md#L728-L729](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L728-L729), [docs/plans/2025-12-25-anthropic-client.md#L738-L738](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L738-L738), [docs/plans/2025-12-25-anthropic-client.md#L733-L734](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L733-L734), [docs/plans/2025-12-25-anthropic-client.md#L115-L118](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L115-L118), [docs/plans/2025-12-25-anthropic-client.md#L514-L515](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L514-L515)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The planned LlmClient trait exposes async create_message returning a Response, and create_message_stream returning a pinned Stream of StreamEvent items (MessageStart, ContentBlockStart/Delta/Stop, MessageDelta, MessageStop). -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L145-L153](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L145-L153), [docs/plans/2025-12-25-mux-rs-design.md#L141-L143](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L141-L143), [docs/plans/2025-12-25-mux-rs-design.md#L138-L139](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L138-L139)
  - [observation/documented] The planned AnthropicRequest type carries model, messages, max_tokens, optional system and temperature, a tools list, and an optional stream flag, with optional fields skipped during serialization. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L29-L41](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L29-L41)
- memory-state: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](mux-rs.detail.md)

Metadata and full claim list: [full detail](mux-rs.detail.md)
Human notes ([notes](mux-rs.notes.md), never overwritten by build)

[Back to map index](../../index.md)
