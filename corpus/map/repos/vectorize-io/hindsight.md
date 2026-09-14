# vectorize-io/hindsight

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e3efe5dd8b07 @ 9ffa132ee2d3ec22

## Summary (orientation draft, not independently verified)

Selected evidence records: Hindsight is described as an agent memory system aimed at agents that learn over time, not merely recall conversation history. The product exposes three core operations: retain (store), recall (search), and reflect (deeper analysis), callable via Python, Node.js, Go, CLI, and REST clients.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Hindsight is described as an agent memory system aimed at agents that learn over time, not merely recall conversation history. -- evidence: [README.md#L24-L24](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L24-L24)
- components (1 claim(s)):
  - [observation/documented] A coding-agents package builds a per-repo memory bank from git history and past sessions, injected into supported CLI coding agents with automatic ingestion. -- evidence: [README.md#L252-L252](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L252-L252), [README.md#L259-L259](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L259-L259)
- design-choices (2 claim(s)):
  - [observation/documented] Recall runs four retrieval strategies in parallel (semantic vector, BM25 keyword, graph, temporal) and merges results with reciprocal rank fusion plus cross-encoder reranking. -- evidence: [README.md#L326-L326](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L326-L326), [README.md#L318-L322](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L318-L322)
  - [observation/documented] Banks carry disposition traits such as skepticism, literalism and empathy that shape how reflect reasons, and strict isolation prevents cross-bank leakage. -- evidence: [README.md#L364-L364](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L364-L364)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes three core operations: retain (store), recall (search), and reflect (deeper analysis), callable via Python, Node.js, Go, CLI, and REST clients. -- evidence: [README.md#L123-L128](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L123-L128), [README.md#L164-L164](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L164-L164), [README.md#L141-L141](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L141-L141), [README.md#L138-L138](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L138-L138), [README.md#L144-L145](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L144-L145)
  - [observation/documented] Every server ships a built-in MCP endpoint, one per bank, at /mcp/{bank_id}/, exposing retain, recall and reflect as tools to any MCP client. -- evidence: [README.md#L263-L263](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L263-L263), [README.md#L269-L269](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L269-L269), [README.md#L265-L267](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L265-L267)
- memory-state (3 claim(s)):
  - [observation/documented] Memories are organized into four types: world facts, experiences, observations, and mental models, stored in isolated banks. -- evidence: [README.md#L364-L364](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L364-L364), [README.md#L281-L284](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L281-L284)
  - [observation/documented] Background consolidation builds observations that keep supporting evidence with exact quotes and a proof count, and are refined rather than overwritten as new evidence arrives. -- evidence: [README.md#L350-L350](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L350-L350)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] An opt-in per-bank Memory Defense policy scans retains against 45 secret/PII patterns, redacting or blocking matches before storage. -- evidence: [README.md#L368-L369](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L368-L369)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports state-of-the-art LongMemEval benchmark results, with live per-model accuracy, latency and cost published on a benchmarks site and independent reproduction claimed by Virginia Tech and The Washington Post. -- evidence: [README.md#L44-L44](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L44-L44), [README.md#L50-L50](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L50-L50), [README.md#L48-L48](https://github.com/vectorize-io/hindsight/blob/e3efe5dd8b070d00129c5186d111c0bc5f992363/README.md#L48-L48)
- dependencies (2 claim(s)):
More evidence: [full detail](hindsight.detail.md)

Metadata and full claim list: [full detail](hindsight.detail.md)
Human notes ([notes](hindsight.notes.md), never overwritten by build)

[Back to map index](../../index.md)
