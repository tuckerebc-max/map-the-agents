# juyterman1000/entroly -- full detail

[Back to orientation](entroly.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/juyterman1000/entroly/9bab5850955cff6f1e374fada7227d45c9f2f570/123494e15847ef5e.json](../../../wiki/dossiers/juyterman1000/entroly/9bab5850955cff6f1e374fada7227d45c9f2f570/123494e15847ef5e.json)

## specifications (1 claim(s))

- [observation/documented] Entroly is described as a local-first AI token-efficiency and context-assurance layer offering budgeted evidence selection, recoverable compression, content-addressed recovery, and auditable receipts. -- evidence: [README.md#L14-L29](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L14-L29) (`clm_cd71cf3373611f9938e2b1b7274e650c05672a270262bc71d954c9cecce32122`)

## components (2 claim(s))

- [observation/documented] The README lists six research algorithms with named implementation files, including a provenance tracer (Python), and nkbe, causal, cognitive_bus, and resonance modules in a Rust core (entroly-core). -- evidence: [README.md#L70-L77](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L70-L77) (`clm_6a5fea4bd8fa2828ee66c7536c3f72f1f1d98beb770e9abcc73f5ff48b1d8f54`)
- [observation/documented] A Rust-accelerated engine is available via PyO3 and WASM, and a standalone Rust binary can be built from entroly-core with cargo using the proxy feature. -- evidence: [README.md#L135-L143](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L135-L143), [README.md#L522-L537](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L522-L537) (`clm_109c939154c2848f0655334d8e7f4e02f92e7ba418b044de76fe53d1554f0f3a`)

## design-choices (3 claim(s))

- [observation/documented] Architecture invariants specify fail-closed behavior only for the security/compliance gate and provider gateway; all other stages fail open by passing the exact original context through unchanged with a receipt warning. -- evidence: [docs/architecture.md#L22-L30](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/docs/architecture.md#L22-L30) (`clm_948c6ce38f18d2fea7adb5a071c641abd7ea65fcce0475c4b0f1de3d5d1adddd`)
- [observation/documented] The design preserves provider protocol, headers, tools, parameters, ordering, and cache semantics, transforming only injected context and output; model/params/tools are never mutated unless transparent routing is explicitly enabled, and then recorded in the receipt. -- evidence: [docs/architecture.md#L22-L30](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/docs/architecture.md#L22-L30) (`clm_3fe9aa7c7a429b28933df118f007705dfb45c4fb3fe4fdcdc24ebb10fbdcd8ee`)
- [observation/documented] Authorization in the govern subsystem is deny-by-default, and every denial names the policy and reason; identity tokens are unsigned unless ENTROLY_IDENTITY_KEY is set. -- evidence: [README.md#L446-L446](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L446-L446) (`clm_f945930fdae2c8c9adc72bd9e504837dd99552fa1265daf776f39dd095db2385`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to a reproducible development setup in CONTRIBUTING.md, and local installation plus the normal test suite need no API key. -- evidence: [README.md#L185-L188](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L185-L188) (`clm_31d31f36e450ceef441b1ec570d3babe5aa2f155f073fd14119d813267ebf1d8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product runs as a CLI, Python/TypeScript SDK, MCP server, HTTP proxy, or library import, per the README's product-surface description. -- evidence: [README.md#L308-L308](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L308-L308) (`clm_b1f8534d1555b0ab876b5c01db645fd21d2d954cd029ca2046b45c75c24182ce`)
- [observation/documented] The Python SDK exposes functions such as compress, compress_messages, optimize, shared_memory_write, and shared_memory_search, with budget and query parameters shown in examples. -- evidence: [README.md#L493-L497](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L493-L497), [README.md#L228-L233](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L228-L233) (`clm_bc7ccbc0df959e45dc347edad8608ea63890a4a67fd8df124293ea2872d20db0`)

## memory-state (1 claim(s))

- [observation/documented] Cross-agent shared memory is a content-addressed store with SimHash deduplication and BM25 search, letting multiple agents share a knowledge base with provenance tracking. -- evidence: [README.md#L491-L491](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L491-L491) (`clm_acab2812b0ee0d6881c84aeb8ccc6062fc5252a31b1053ffef255cff5d0f61db`)

## orchestration (1 claim(s))

- [observation/documented] Output token reduction uses a three-layer pipeline: effort classification steers verbosity directives, max_tokens budgets cap generation, and post-generation distillation trims filler. -- evidence: [README.md#L501-L501](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L501-L501) (`clm_2747031c25e77111c11080a40941f1a18fcaa0f43bf5a181fa5fd0e03855105a`)

## tools-permissions (1 claim(s))

- [observation/documented] The MCP server is configured with environment flags such as ENTROLY_NO_DOCKER, ENTROLY_MCP_PASSIVE, and ENTROLY_MAX_FILES, and the MCP path is provider-neutral across many model vendors. -- evidence: [README.md#L372-L386](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L372-L386), [README.md#L388-L391](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L388-L391) (`clm_3ea9906cd3d23c004b82d33d2d5e2f584774eb0e71cf86a17f410a8cfa6b8b40`)

## evaluation (3 claim(s))

- [observation/documented] Benchmark tables report accuracy retention with gpt-4o-mini and Wilson 95% CIs across NeedleInAHaystack, GSM8K, SQuAD 2.0, MMLU, TruthfulQA, and LongBench, with an average retention of 101.7%. -- evidence: [README.md#L50-L50](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L50-L50), [README.md#L41-L48](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L41-L48), [README.md#L39-L39](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L39-L39) (`clm_551e8021d8b300c19859550e0f6a632af04b9a2db97bebc609283a06d515aea7`)
- [observation/documented] The README candidly notes a regression: SQuAD 2.0 accuracy dropped from 80% to 72% with compression, and points users to entroly simulate for their own numbers. -- evidence: [README.md#L281-L284](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L281-L284), [README.md#L269-L279](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L269-L279) (`clm_a9dd57dcc2fb0b74edb57d8e2b922427260680631f908ecb86042c1e7b8bb5f5`)
- [observation/documented] A WITNESS hallucination detector is reported at 84.92% accuracy and 0.7976 AUROC on 20,000 HaluEval-QA decisions, run locally without an API. -- evidence: [README.md#L286-L286](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L286-L286) (`clm_e5be4c02de8c9ba323c4fb83989fef0aadc87108d36825666249e0be78525ae7`)

## dependencies (1 claim(s))

- [observation/documented] If the native engine is missing, Entroly installs it from PyPI before measuring; this self-heal is the only outbound call of these commands and can be disabled with ENTROLY_NO_SELF_HEAL=1. -- evidence: [README.md#L459-L463](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L459-L463), [README.md#L174-L180](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L174-L180) (`clm_6712bf6b8efbdf9f184a2e304f9097b1f6b969f1075b6a640bead1ab0722c00a`)

## limitations (1 claim(s))

- [observation/documented] The README states savings are not a universal guarantee, that MCP-only integrations remain tools an agent may skip, and that provider-bound savings exist only when requests traverse an Entroly-controlled route. -- evidence: [README.md#L90-L93](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L90-L93), [README.md#L290-L290](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L290-L290), [README.md#L112-L124](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L112-L124) (`clm_e99f0be5ab3cbf2d4c0adff059ffc7308a9a90162d674837e07ef251bb01b3b7`)

## relevance (1 claim(s))

- [observation/documented] Stated good fits are large repos where agents see few files at a time, chatty multi-turn agents, and evidence-checked answers; tiny repos or prompts already within budget are cases to skip. -- evidence: [README.md#L417-L417](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L417-L417), [README.md#L419-L419](https://github.com/juyterman1000/entroly/blob/9bab5850955cff6f1e374fada7227d45c9f2f570/README.md#L419-L419) (`clm_64e412b2c005ef9438889441f89bd7854a1102d5ea15c2b2a9bf018402042fd4`)

