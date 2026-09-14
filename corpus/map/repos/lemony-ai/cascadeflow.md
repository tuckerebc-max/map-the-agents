# lemony-ai/cascadeflow

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d8251001a51c @ 75606ca846a6a60c

## Summary (orientation draft, not independently verified)

cascadeflow is an in-process model-cascading library (Python and TypeScript) that speculatively runs a cheap drafter model, validates quality, and escalates to a verifier only when needed, with harness APIs, n8n and Hermes integrations, and optional ML-based semantic validation. Evidence coverage: 162 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 50 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The core mechanism is speculative execution with quality validation: run a cheap drafter first, validate responses against configurable thresholds, and escalate to a larger model only when validation fails. -- evidence: [docs/ARCHITECTURE.md#L23-L25](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L23-L25), [README.md#L94-L94](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L94-L94), [README.md#L96-L99](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L96-L99)
  - [observation/documented] CascadeAgent (agent.py) is the main orchestrator and entry point for all queries, exposing run, run_streaming, and stream_events and coordinating routing, cost calculation, metrics, and callbacks. -- evidence: [docs/ARCHITECTURE.md#L193-L196](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L193-L196), [docs/ARCHITECTURE.md#L191-L191](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L191-L191), [docs/ARCHITECTURE.md#L198-L203](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/docs/ARCHITECTURE.md#L198-L203)
- design-choices (1 claim(s)):
  - [observation/documented] cascadeflow is positioned as an in-process intelligence layer operating inside the agent execution loop rather than at the HTTP request boundary like external proxies. -- evidence: [README.md#L38-L38](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L38-L38), [README.md#L61-L68](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L61-L68)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The harness API offers three tiers: cascadeflow.init(mode="observe") for zero-change tracking, cascadeflow.run(budget=..., max_tool_calls=...) sessions with summary() and trace(), and a @cascadeflow.agent decorator accepting budget, compliance, and KPI weights. -- evidence: [README.md#L168-L171](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L168-L171), [README.md#L175-L181](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L175-L181), [README.md#L183-L188](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L183-L188)
  - [observation/documented] A drop-in gateway for existing OpenAI/Anthropic clients can be started with 'python -m cascadeflow.server --mode auto --port 8084'. -- evidence: [README.md#L392-L392](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L392-L392), [README.md#L394-L396](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L394-L396)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] At runtime the harness can enforce decisions with four actions: allow, switch_model, deny_tool, and stop, based on current context and policy state. -- evidence: [README.md#L75-L84](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L75-L84)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports benchmark-based cost savings of 69% on MT-Bench, 93% on GSM8K, 52% on MMLU, and 80% on TruthfulQA while retaining 96% GPT-5 quality. -- evidence: [README.md#L28-L28](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L28-L28)
- dependencies (1 claim(s)):
  - [observation/documented] ML-based semantic quality validation is optional: Python via cascadeflow[semantic] (FastEmbed, ~80MB model) and TypeScript via @cascadeflow/ml with @huggingface/transformers (BGE-small-en-v1.5 embeddings, auto-downloaded). -- evidence: [README.md#L340-L346](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L340-L346), [README.md#L296-L298](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L296-L298), [README.md#L224-L226](https://github.com/lemony-ai/cascadeflow/blob/d8251001a51c22dc3d3ea596d89f89c4a5d74f8b/README.md#L224-L226)
- limitations (1 claim(s)):
More evidence: [full detail](cascadeflow.detail.md)

Metadata and full claim list: [full detail](cascadeflow.detail.md)
Human notes ([notes](cascadeflow.notes.md), never overwritten by build)

[Back to map index](../../index.md)
