# vectorize-io/hindsight -- full detail

[Back to orientation](hindsight.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vectorize-io/hindsight/e3efe5dd8b070d00129c5186d111c0bc5f992363/9ffa132ee2d3ec22.json](../../../wiki/dossiers/vectorize-io/hindsight/e3efe5dd8b070d00129c5186d111c0bc5f992363/9ffa132ee2d3ec22.json)

## specifications (1 claim(s))

- [observation/documented] Hindsight is described as an agent memory system aimed at agents that learn over time, not merely recall conversation history. -- evidence: [README.md#L24-L24](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L24-L24) (`clm_54fd7d6a0a9e0a4a96eb6cdc9e2a6626bc9bd5c82d3cb50bdc942b66f828f9bd`)

## components (1 claim(s))

- [observation/documented] A coding-agents package builds a per-repo memory bank from git history and past sessions, injected into supported CLI coding agents with automatic ingestion. -- evidence: [README.md#L252-L252](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L252-L252), [README.md#L259-L259](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L259-L259) (`clm_3e4cbb355de874596d82c4ee30bd04d4d005fce008658155d2c281e715401fe4`)

## design-choices (2 claim(s))

- [observation/documented] Recall runs four retrieval strategies in parallel (semantic vector, BM25 keyword, graph, temporal) and merges results with reciprocal rank fusion plus cross-encoder reranking. -- evidence: [README.md#L326-L326](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L326-L326), [README.md#L318-L322](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L318-L322) (`clm_36dadd9593f754dc35d89903a42ebdca38233f6403be6623675f8a78b3733a9f`)
- [observation/documented] Banks carry disposition traits such as skepticism, literalism and empathy that shape how reflect reasons, and strict isolation prevents cross-bank leakage. -- evidence: [README.md#L364-L364](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L364-L364) (`clm_a179d096f2edb1040ba27f1b79370b451801209b47d5063606c74270db1984c2`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes three core operations: retain (store), recall (search), and reflect (deeper analysis), callable via Python, Node.js, Go, CLI, and REST clients. -- evidence: [README.md#L123-L128](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L123-L128), [README.md#L164-L164](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L164-L164), [README.md#L141-L141](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L141-L141), [README.md#L138-L138](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L138-L138), [README.md#L144-L145](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L144-L145) (`clm_cc9483d8ef4e10025356da709297133ee8d402e71569d0abd6cc43a78f4cc2bd`)
- [observation/documented] Every server ships a built-in MCP endpoint, one per bank, at /mcp/{bank_id}/, exposing retain, recall and reflect as tools to any MCP client. -- evidence: [README.md#L263-L263](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L263-L263), [README.md#L269-L269](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L269-L269), [README.md#L265-L267](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L265-L267) (`clm_9241421a8ecd39b18cccf70671b5bf207ba19ef11c9e632d7b6f8d81b0bc11cc`)

## memory-state (3 claim(s))

- [observation/documented] Memories are organized into four types: world facts, experiences, observations, and mental models, stored in isolated banks. -- evidence: [README.md#L364-L364](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L364-L364), [README.md#L281-L284](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L281-L284) (`clm_fd3d04ced8ef569369beb4a7b7ab4a76ec289c92df2bc034036633c23f4911a5`)
- [observation/documented] Background consolidation builds observations that keep supporting evidence with exact quotes and a proof count, and are refined rather than overwritten as new evidence arrives. -- evidence: [README.md#L350-L350](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L350-L350) (`clm_b4f175733345b07bb0447e33cb7be1251d7d8d68fdb30f6abe0106a7fb5f6fbf`)
- [observation/documented] Mental models are standing answers to defined questions that are rewritten in the background and readable as a plain database read without retrieval or an LLM call. -- evidence: [README.md#L356-L356](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L356-L356) (`clm_42688d4ec4e4156ef475f01f6d4a1056b5c8d4b1d7eb03f9115afba11122d178`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] An opt-in per-bank Memory Defense policy scans retains against 45 secret/PII patterns, redacting or blocking matches before storage. -- evidence: [README.md#L368-L369](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L368-L369) (`clm_21ed2cba4593d075dddb8757589e83cf5472d4450719b58abe6a52ffb5469cbc`)

## evaluation (1 claim(s))

- [observation/documented] The README reports state-of-the-art LongMemEval benchmark results, with live per-model accuracy, latency and cost published on a benchmarks site and independent reproduction claimed by Virginia Tech and The Washington Post. -- evidence: [README.md#L44-L44](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L44-L44), [README.md#L50-L50](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L50-L50), [README.md#L48-L48](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L48-L48) (`clm_e153d7f87219fcd4417011ce448c344ff1ae314dc8f0d528b554c214eaa88847`)

## dependencies (2 claim(s))

- [observation/documented] The server supports 25+ LLM providers via HINDSIGHT_API_LLM_PROVIDER, including hosted, local (ollama, lmstudio, llamacpp), OpenAI-compatible endpoints, and subscription-based options. -- evidence: [README.md#L82-L82](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L82-L82) (`clm_c3bec46a6430ab1fa6e0f1d320271f4f4f89a78f6fcaeced58161fdb402717e0`)
- [observation/documented] Storage uses PostgreSQL with pgvector, or Oracle AI Database 23ai with claimed full feature parity for enterprise deployments. -- evidence: [README.md#L397-L405](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L397-L405), [README.md#L93-L93](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L93-L93) (`clm_6ce50761c934b014f7de1da4bd3a3a4a0fdadf31cdd8b8014f266b6b8b755142`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Hindsight targets conversational and autonomous agents needing personalization and learning, and may be overkill for simple n8n-style workflows. -- evidence: [README.md#L375-L375](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L375-L375), [README.md#L379-L379](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L379-L379) (`clm_956dc963185b967a803a9338a04721e0cf3db04aa0cb56634804fd7112d23a71`)

