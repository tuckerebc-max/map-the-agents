# juyterman1000/entroly

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9bab5850955c @ 123494e15847ef5e

## Summary (orientation draft, not independently verified)

Selected evidence records: Entroly is described as a local-first AI token-efficiency and context-assurance layer offering budgeted evidence selection, recoverable compression, content-addressed recovery, and auditable receipts. The product runs as a CLI, Python/TypeScript SDK, MCP server, HTTP proxy, or library import, per the README's product-surface description.

## Source coverage

Source coverage (partial): 6 of 149 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 12 facet(s); 1 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Entroly is described as a local-first AI token-efficiency and context-assurance layer offering budgeted evidence selection, recoverable compression, content-addressed recovery, and auditable receipts. -- evidence: [README.md#L14-L29](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L14-L29)
- components (2 claim(s)):
  - [observation/documented] The README lists six research algorithms with named implementation files, including a provenance tracer (Python), and nkbe, causal, cognitive_bus, and resonance modules in a Rust core (entroly-core). -- evidence: [README.md#L70-L77](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L70-L77)
  - [observation/documented] A Rust-accelerated engine is available via PyO3 and WASM, and a standalone Rust binary can be built from entroly-core with cargo using the proxy feature. -- evidence: [README.md#L135-L143](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L135-L143), [README.md#L522-L537](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L522-L537)
- design-choices (3 claim(s)):
  - [observation/documented] Architecture invariants specify fail-closed behavior only for the security/compliance gate and provider gateway; all other stages fail open by passing the exact original context through unchanged with a receipt warning. -- evidence: [docs/architecture.md#L22-L30](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/docs/architecture.md#L22-L30)
  - [observation/documented] The design preserves provider protocol, headers, tools, parameters, ordering, and cache semantics, transforming only injected context and output; model/params/tools are never mutated unless transparent routing is explicitly enabled, and then recorded in the receipt. -- evidence: [docs/architecture.md#L22-L30](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/docs/architecture.md#L22-L30)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to a reproducible development setup in CONTRIBUTING.md, and local installation plus the normal test suite need no API key. -- evidence: [README.md#L185-L188](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L185-L188)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product runs as a CLI, Python/TypeScript SDK, MCP server, HTTP proxy, or library import, per the README's product-surface description. -- evidence: [README.md#L308-L308](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L308-L308)
  - [observation/documented] The Python SDK exposes functions such as compress, compress_messages, optimize, shared_memory_write, and shared_memory_search, with budget and query parameters shown in examples. -- evidence: [README.md#L493-L497](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L493-L497), [README.md#L228-L233](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L228-L233)
- memory-state (1 claim(s)):
  - [observation/documented] Cross-agent shared memory is a content-addressed store with SimHash deduplication and BM25 search, letting multiple agents share a knowledge base with provenance tracking. -- evidence: [README.md#L491-L491](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L491-L491)
- orchestration (1 claim(s)):
  - [observation/documented] Output token reduction uses a three-layer pipeline: effort classification steers verbosity directives, max_tokens budgets cap generation, and post-generation distillation trims filler. -- evidence: [README.md#L501-L501](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L501-L501)
- tools-permissions (1 claim(s)):
More evidence: [full detail](entroly.detail.md)

Metadata and full claim list: [full detail](entroly.detail.md)
Human notes ([notes](entroly.notes.md), never overwritten by build)

[Back to map index](../../index.md)
