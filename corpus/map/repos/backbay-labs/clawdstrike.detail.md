# backbay-labs/clawdstrike -- full detail

[Back to orientation](clawdstrike.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/backbay-labs/clawdstrike/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/e30732e863637655.json](../../../wiki/dossiers/backbay-labs/clawdstrike/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/e30732e863637655.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The product is described as a policy engine, EDR, and signed audit chain in one binary, treating AI agent tool calls in the same event taxonomy as kernel-level file, process, network, dylib, and persistence events. -- evidence: [README.md#L23-L23](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L23-L23) (`clm_193fbf7ee05d51232b0aa73ef4d749ce092feb37ad3d0b1a26427f4b9b9f3632`)
- [observation/documented] The engine ships in multiple forms: a Rust crate, TypeScript SDK, Python package, Go module, CLI, desktop EDR agent (macOS Endpoint Security/Network Extension; Linux Tetragon/Hubble), and an enterprise control plane. -- evidence: [README.md#L25-L25](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L25-L25) (`clm_26ed14ccac4508a679ab965259c4f4e5dfca63d846fe88f5590b1179dca94bd4`)
- [observation/documented] A documented guard stack includes ForbiddenPathGuard, EgressAllowlistGuard, SecretLeakGuard, ShellCommandGuard, McpToolGuard, PromptInjectionGuard, JailbreakGuard, ComputerUseGuard, and SpiderSenseGuard, each returning a verdict with evidence. -- evidence: [README.md#L150-L164](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L150-L164), [README.md#L148-L148](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L148-L148) (`clm_a36f56bdd137e004d038c255e4d613a0127d0581309e73c96cac012dbab50f96`)

## design-choices (2 claim(s))

- [observation/documented] Defaults fail closed: the guard report aggregates per-guard results such that any deny produces an overall deny, and denials emit signed receipts. -- evidence: [docs/src/hunt/architecture.md#L336-L343](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/docs/src/hunt/architecture.md#L336-L343), [README.md#L93-L93](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L93-L93), [README.md#L23-L23](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L23-L23) (`clm_f04c576ef81938f8218e1f4cb0f176c3d697e099fa34e111e96f767af570d276`)
- [observation/documented] Policies are versioned deterministic policy-as-code (schema 1.5.0, backward-compatible with 1.1.0+) supporting extends from built-ins, local files, and remote URLs that are host-allowlisted and sha256 integrity-pinned. -- evidence: [README.md#L172-L172](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L172-L172) (`clm_67b0d569ec11835e904c8774f7a3d2666dca18575c1f2edf4705718353cca01f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI supports commands such as init --keygen, daemon start/status, check with --action-type and --ruleset, verify --policy, run --policy, and policy synth/simulate/diff subcommands. -- evidence: [README.md#L184-L184](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L184-L184), [README.md#L187-L188](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L187-L188), [README.md#L57-L58](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L57-L58), [README.md#L61-L61](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L61-L61), [README.md#L80-L85](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L80-L85), [README.md#L67-L69](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L67-L69), [README.md#L89-L91](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L89-L91), [README.md#L180-L181](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L180-L181) (`clm_3d9a824d8b4980770542ddc8baf525956dc12717e7c1578e515fa305fda71380`)

## memory-state (1 claim(s))

- [observation/documented] Past observations are kept on a disk-backed flight recorder so a tightened policy can be simulated against prior state before deployment. -- evidence: [README.md#L140-L140](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L140-L140) (`clm_a190c4ae9401c60564a74e5342fc9699679ee794cac646d1159c73a029a00486`)

## orchestration (2 claim(s))

- [observation/documented] Enterprise deployments use a control plane with Control API, NATS JetStream transport, Spine audit chain, and Control Console; enrollment is over mTLS with posture commands using request/reply acks and signed completion bundles. -- evidence: [README.md#L303-L303](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L303-L303) (`clm_983d56618f10d67da132177d25248de32e249b4fc035066041848f5dde2d16a6`)
- [observation/documented] A Helm chart deploys hushd, the Spine checkpointer plus witness, and bundled NATS JetStream; hushd and Spine signers are fail-closed and require pre-created Kubernetes Secrets for keys at install time. -- evidence: [README.md#L119-L119](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L119-L119), [README.md#L97-L97](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L97-L97), [README.md#L112-L117](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L112-L117) (`clm_0c2db57e325c9a21a213d9b55b185fabee168b8ec728cca52ecaa8c733d22185`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The system depends on Ed25519 signing (ed25519-dalek for Rust primitives), RFC 8785 JSON canonicalization for cross-language signature verification, and NATS JetStream for telemetry transport. -- evidence: [README.md#L220-L220](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L220-L220), [README.md#L206-L206](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L206-L206), [docs/src/hunt/architecture.md#L72-L73](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/docs/src/hunt/architecture.md#L72-L73) (`clm_4392c4644d8683d5d0350bdd0585546465ee72cc562a65966b19cd4a403242fe`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

