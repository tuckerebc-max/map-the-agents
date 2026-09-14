# 2389-research/mux-rs -- full detail

[Back to orientation](mux-rs.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/mux-rs/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/cac42de95f8bbe12.json](../../../wiki/dossiers/2389-research/mux-rs/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/cac42de95f8bbe12.json)

## specifications (1 claim(s))

- [observation/documented] A plan document specifies implementing an AnthropicClient that connects to the Claude API and implements the LlmClient trait. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L5-L5](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L5-L5) (`clm_4d2913f676115c63175d7420003298bf0c2f4c4dcaf567f6aaaf7450faecf41b`)

## components (2 claim(s))

- [observation/documented] The planned crate layout includes llm (types, client trait, anthropic, openai), tool (trait, registry, result), permission (policy, handler), mcp (types, client, proxy), an error module, and a mux-derive crate providing a #[derive(Tool)] proc macro. -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L19-L48](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L19-L48) (`clm_6dfb632b798e53105c946cfc1ca7c8da04eb3373a557d80dafc78727f25c630f`)
- [observation/documented] The plan adds streaming support via an AnthropicStreamEvent enum (message start/stop, content block events, ping, error) and an async-stream based SSE parser that buffers chunks and splits on blank lines. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L588-L594](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L588-L594), [docs/plans/2025-12-25-anthropic-client.md#L625-L628](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L625-L628), [docs/plans/2025-12-25-anthropic-client.md#L698-L698](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L698-L698), [docs/plans/2025-12-25-anthropic-client.md#L539-L563](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L539-L563), [docs/plans/2025-12-25-anthropic-client.md#L618-L619](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L618-L619) (`clm_6aa1c21faed7920792b2c1ec542a9cb66faba035de8b4ece1d73f24f1660f6aa`)

## design-choices (2 claim(s))

- [observation/documented] The planned Anthropic client architecture uses reqwest for HTTP with SSE streaming support, serializing the crate's Request type to Anthropic's format and deserializing responses back. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L7-L7](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L7-L7) (`clm_a8a9f481a361e4db352e7be4578bbebd30f65180a428589d20b62cbd20b394a1`)
- [observation/documented] The design doc records choices including a derive macro plus trait for tool definition, Tokio as async runtime, thiserror plus anyhow for errors, a policy engine for permissions, client-only MCP scope, and multi-provider LLM support (Anthropic and OpenAI). -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L7-L15](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L7-L15) (`clm_b6f7d2b7c65052d89c6ae52db5792aa8d750fc1abd4288f25120448ecd383697`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the plan's header instructs the implementing Claude agent to use the superpowers:executing-plans skill to implement the plan task-by-task. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L3-L3](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L3-L3) (`clm_e347956f0a35de2f4c6ee0019230d1b3ac57e0caa4d8c39a259bee4c959289af`)
- [observation/documented] Repository development practice: each plan task prescribes verification via cargo check or cargo test, final clippy and cargo fmt runs, and a git commit per task with conventional-commit style messages. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L110-L111](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L110-L111), [docs/plans/2025-12-25-anthropic-client.md#L728-L729](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L728-L729), [docs/plans/2025-12-25-anthropic-client.md#L738-L738](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L738-L738), [docs/plans/2025-12-25-anthropic-client.md#L733-L734](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L733-L734), [docs/plans/2025-12-25-anthropic-client.md#L115-L118](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L115-L118), [docs/plans/2025-12-25-anthropic-client.md#L514-L515](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L514-L515) (`clm_7dc00bede7df14b813e9673b2e68a8f05319076c6345221e4fa13bb536363452`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The planned LlmClient trait exposes async create_message returning a Response, and create_message_stream returning a pinned Stream of StreamEvent items (MessageStart, ContentBlockStart/Delta/Stop, MessageDelta, MessageStop). -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L145-L153](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L145-L153), [docs/plans/2025-12-25-mux-rs-design.md#L141-L143](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L141-L143), [docs/plans/2025-12-25-mux-rs-design.md#L138-L139](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L138-L139) (`clm_38c90e7fd5f690ddaa369fbddcc36a4eaf01f1ac52a4a715c60debcededc9466`)
- [observation/documented] The planned AnthropicRequest type carries model, messages, max_tokens, optional system and temperature, a tools list, and an optional stream flag, with optional fields skipped during serialization. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L29-L41](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L29-L41) (`clm_c5656c8867753e79d23267572efe2c7a826684f20a3351adeb58efef548705d4`)
- [observation/documented] The plan defines AnthropicClient::from_env, which reads the ANTHROPIC_API_KEY environment variable and returns an LlmError::Api error when it is unset. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L272-L281](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L272-L281) (`clm_e7945a56905129521cee3b8cb1d35fb791c135df55b6e20731cb0a8040c3ab4b`)
- [observation/documented] The planned client posts to https://api.anthropic.com/v1/messages with x-api-key, anthropic-version (2023-06-01), and JSON content-type headers, mapping non-success statuses to LlmError::Api. -- evidence: [docs/plans/2025-12-25-anthropic-client.md#L320-L328](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L320-L328), [docs/plans/2025-12-25-anthropic-client.md#L330-L337](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L330-L337), [docs/plans/2025-12-25-anthropic-client.md#L253-L254](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-anthropic-client.md#L253-L254) (`clm_49d2698042b1f93fbf7983eec6f760d9b373456068bafe1748fbb0aaf2d9ab22`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Planned core dependencies are tokio (full features), serde with derive, serde_json, thiserror 2, anyhow, async-trait, reqwest 0.12 with json and stream features, futures 0.3, and glob 0.3, with tokio-test as a dev dependency. -- evidence: [docs/plans/2025-12-25-mux-rs-design.md#L52-L62](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L52-L62), [docs/plans/2025-12-25-mux-rs-design.md#L64-L66](https://github.com/2389-research/mux-rs/blob/c25c6c8e1acbf05d62386c6ea4d5cc5212acb49b/docs/plans/2025-12-25-mux-rs-design.md#L64-L66) (`clm_b5c9a133cda55566609c70ef9b7cba45a22518933f3f6e2267cde60e812d27f7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

