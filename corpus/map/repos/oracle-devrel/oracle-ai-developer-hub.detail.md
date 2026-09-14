# oracle-devrel/oracle-ai-developer-hub -- full detail

[Back to orientation](oracle-ai-developer-hub.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oracle-devrel/oracle-ai-developer-hub/3317c535db76ed698fa92e32a65acd5e5f2769bc/6eaeb11cc5dd8d7d.json](../../../wiki/dossiers/oracle-devrel/oracle-ai-developer-hub/3317c535db76ed698fa92e32a65acd5e5f2769bc/6eaeb11cc5dd8d7d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The hub is organized into key areas: apps (reference implementations), notebooks, guides, workshops, and partner-contributed resources, each referenced under its own named path in the README. -- evidence: [README.md#L108-L108](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L108-L108), [README.md#L7-L7](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L7-L7), [README.md#L27-L27](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L27-L27), [README.md#L93-L93](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L93-L93), [README.md#L11-L11](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L11-L11), [README.md#L51-L51](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L51-L51) (`clm_aaaf6cb1d6eed2302279e07478328ad0da0a07530090937739a10c5ea840e29d`)
- [observation/documented] A dedicated agent-memory notebook collection covers the oracleagentmemory package, including a developer guide, benchmarks, and end-to-end examples for OpenAI Agents SDK, Claude Agent SDK, and LangGraph. -- evidence: [README.md#L66-L66](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L66-L66), [README.md#L64-L64](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L64-L64) (`clm_df824e4fcb035d99c72e0ce306cf2975f6a9fee57842279448256597ed53255b`)

## design-choices (1 claim(s))

- [observation/documented] A decision tree in oamp.md maps memory shapes to tools: OAMP for conversational per-user durable memory, OracleVS for fixed RAG corpora, OracleChatHistory for simple chat logs, and SQL tables for counters and audit trails. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L131-L138](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L131-L138) (`clm_1d3a4b64f90b85a9a4bc4e3900aae8c865176dfef1947ee754749160244d23a5`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are made by forking the repository and submitting pull requests, and contributors are asked to install pre-commit hooks that auto-format code with Ruff for Python and Prettier for JS/TS/JSON/YAML/Markdown. -- evidence: [README.md#L154-L154](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L154-L154), [README.md#L129-L129](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L129-L129), [README.md#L156-L157](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L156-L157), [README.md#L125-L125](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L125-L125) (`clm_98e77cb2e4a456b317efea44b38e08cfbbeaed830e00eb342e3cc9c635bc2aa0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A shared oamp_helpers module exposes make_oamp_client, make_oamp_thread, and add_turn convenience functions, with auto-extraction enabled only when OCI_GENAI_API_KEY is set, otherwise degrading to manual-add mode. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L8-L16](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L8-L16) (`clm_6a13e834ba965d6387609918821a8da9eb651bb27f74492ccb32ecd76ce247ec`)

## memory-state (1 claim(s))

- [observation/documented] The agent-memory notebooks present Oracle AI Database as a unified memory core serving conversation history, durable facts, and entity state instead of separate vector, key-value, and relational stores. -- evidence: [README.md#L64-L64](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L64-L64) (`clm_8e79f821f2fe2ef38b86c217bc68398fb8720655f7c288a849742f7729a99067`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] An OAMP Benchmarks notebook measures token cost, latency, and response quality of OAMP versus naive flat-history memory across 80 scripted turns with three agent variants. -- evidence: [README.md#L68-L74](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L68-L74) (`clm_90bf0805eb0ab95972e27216744c6ff5615b3d79f6ce1bf4d8594d847d2c2116`)
- [observation/documented] A v2 friction-pass re-walk of four scaffolds produced 10 new findings versus 54 in v1, a reported -81% reduction, with all four verify checks passing and memory persistence confirmed for the self-memory run. -- evidence: [docs/cyp-friction-pass/2026-05-05-v2-results.md#L12-L18](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-v2-results.md#L12-L18), [docs/cyp-friction-pass/2026-05-05-v2-results.md#L7-L8](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-v2-results.md#L7-L8) (`clm_475e5f1a3489510bac4f198320d82d3a15071aa0d03e265b5dff21ca9e0bf11b`)

## dependencies (1 claim(s))

- [observation/documented] The OAMP retrofit pass records the package version as oracleagentmemory==26.4.0, and a pre-flight step confirms 26.4.0 or newer is installed. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L3-L4](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L3-L4), [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L154-L155](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L154-L155) (`clm_05c3823377d183a77c704d3c247a32cb57cca1262f5ff7ca7c0c7e181c95261e`)

## limitations (2 claim(s))

- [observation/documented] A documented OAMP issue (V4-OAMP-1): batched add_messages calls count as one event, so memory-extraction frequency triggers never fire; the fix is per-turn writes via an add_turn helper. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L89-L89](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L89-L89), [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L87-L87](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L87-L87), [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L91-L94](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L91-L94) (`clm_886a8211b7a533146c206af3c9510d614e8f8d73179a58f690d7bdbade760d8d`)
- [observation/documented] Documented OAMP quirks include context_card.formatted_content being a byte-for-byte alias of content, batch-written messages sharing one timestamp, and RECORD_CHUNKS holding roughly 1.3 rows per message. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L102-L102](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L102-L102), [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L98-L98](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L98-L98), [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L106-L106](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L106-L106) (`clm_0e9b5754e76d7cd505e34f455794b1cc88a10f00ff9cb3e9b1e862c181fa263f`)

## relevance (1 claim(s))

- [observation/documented] The repository provides technical resources for AI developers and engineers building AI applications, agents, and systems using Oracle AI Database and OCI services. -- evidence: [README.md#L3-L3](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L3-L3) (`clm_a9c4fc7ac2aa92c162d7d6fe32d748d6d0e45380876a8633d16087e916c8caa0`)

