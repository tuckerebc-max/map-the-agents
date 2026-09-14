# fareedkhan-dev/multi-agent-training-grpo

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 48758c5e67e7 @ 57f32112a4bb2240

## Summary (orientation draft, not independently verified)

Selected evidence records: The project trains a multi-agent system with the GRPO reinforcement learning algorithm to improve planning and reduce hallucination and off-track results in long-horizon agentic tasks. GRPO is described as group-based: the agent attempts the same query multiple times, and strategies are reinforced relative to the group average rather than graded in isolation.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The preprocessing pipeline normalizes both datasets to a shared schema (id, question, chain, result, source, extra_info), concatenates them, shuffles with seed 42, re-indexes, and saves as Parquet; the combined training set totals 182,190 samples. -- evidence: [README.md#L438-L442](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L438-L442), [README.md#L432-L432](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L432-L432), [README.md#L182-L187](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L182-L187), [README.md#L218-L229](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L218-L229), [README.md#L364-L376](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L364-L376), [README.md#L466-L466](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L466-L466), [README.md#L416-L417](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L416-L417), [README.md#L451-L452](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L451-L452)
  - [observation/documented] The multi-agent architecture comprises stages including planning, tool use, execution, observation and reflection, iteration until a verifier agent determines the query is answered, and final synthesis. -- evidence: [README.md#L477-L482](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L477-L482)
- design-choices (3 claim(s)):
  - [observation/documented] The project trains a multi-agent system with the GRPO reinforcement learning algorithm to improve planning and reduce hallucination and off-track results in long-horizon agentic tasks. -- evidence: [README.md#L5-L5](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L5-L5), [README.md#L62-L62](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L62-L62), [README.md#L20-L20](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L20-L20)
  - [observation/documented] GRPO is described as group-based: the agent attempts the same query multiple times, and strategies are reinforced relative to the group average rather than graded in isolation. -- evidence: [README.md#L52-L52](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L52-L52), [README.md#L12-L16](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L12-L16), [README.md#L56-L60](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L56-L60)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The planning model is served through a vLLM server with an OpenAI-compatible API; the example serves Qwen/Qwen2.5-7B-Instruct on port 8000 with an API key and 8192 max context length. -- evidence: [README.md#L541-L541](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L541-L541), [README.md#L538-L538](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L538-L538), [README.md#L493-L497](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L493-L497), [README.md#L544-L544](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L544-L544)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Tool API keys are configured as placeholders: an OpenAI key is noted as needed for embeddings in the web search tool and a Google key for the Google search tool. -- evidence: [README.md#L549-L551](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L549-L551)
- evaluation (1 claim(s)):
  - [observation/documented] During GRPO training, an external judge scores each trajectory's final answer against ground truth with binary rewards (1.0 correct, 0.0 failed or hallucinated), and relative advantages are computed against the group mean. -- evidence: [README.md#L56-L60](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L56-L60)
- dependencies (1 claim(s)):
More evidence: [full detail](multi-agent-training-grpo.detail.md)

Metadata and full claim list: [full detail](multi-agent-training-grpo.detail.md)
Human notes ([notes](multi-agent-training-grpo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
