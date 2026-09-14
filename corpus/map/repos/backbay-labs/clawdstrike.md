# backbay-labs/clawdstrike

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b01f63ae64fa @ e30732e863637655

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is described as a policy engine, EDR, and signed audit chain in one binary, treating AI agent tool calls in the same event taxonomy as kernel-level file, process, network, dylib, and persistence events. The engine ships in multiple forms: a Rust crate, TypeScript SDK, Python package, Go module, CLI, desktop EDR agent (macOS Endpoint Security/Network Extension; Linux Tetragon/Hubble), and an enterprise control plane.

## Source coverage

Source coverage (partial): 6 of 311 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The product is described as a policy engine, EDR, and signed audit chain in one binary, treating AI agent tool calls in the same event taxonomy as kernel-level file, process, network, dylib, and persistence events. -- evidence: [README.md#L23-L23](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L23-L23)
  - [observation/documented] The engine ships in multiple forms: a Rust crate, TypeScript SDK, Python package, Go module, CLI, desktop EDR agent (macOS Endpoint Security/Network Extension; Linux Tetragon/Hubble), and an enterprise control plane. -- evidence: [README.md#L25-L25](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L25-L25)
- design-choices (2 claim(s)):
  - [observation/documented] Defaults fail closed: the guard report aggregates per-guard results such that any deny produces an overall deny, and denials emit signed receipts. -- evidence: [docs/src/hunt/architecture.md#L336-L343](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/docs/src/hunt/architecture.md#L336-L343), [README.md#L93-L93](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L93-L93), [README.md#L23-L23](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L23-L23)
  - [observation/documented] Policies are versioned deterministic policy-as-code (schema 1.5.0, backward-compatible with 1.1.0+) supporting extends from built-ins, local files, and remote URLs that are host-allowlisted and sha256 integrity-pinned. -- evidence: [README.md#L172-L172](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L172-L172)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI supports commands such as init --keygen, daemon start/status, check with --action-type and --ruleset, verify --policy, run --policy, and policy synth/simulate/diff subcommands. -- evidence: [README.md#L184-L184](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L184-L184), [README.md#L187-L188](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L187-L188), [README.md#L57-L58](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L57-L58), [README.md#L61-L61](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L61-L61), [README.md#L80-L85](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L80-L85), [README.md#L67-L69](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L67-L69), [README.md#L89-L91](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L89-L91), [README.md#L180-L181](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L180-L181)
- memory-state (1 claim(s)):
  - [observation/documented] Past observations are kept on a disk-backed flight recorder so a tightened policy can be simulated against prior state before deployment. -- evidence: [README.md#L140-L140](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L140-L140)
- orchestration (2 claim(s)):
  - [observation/documented] Enterprise deployments use a control plane with Control API, NATS JetStream transport, Spine audit chain, and Control Console; enrollment is over mTLS with posture commands using request/reply acks and signed completion bundles. -- evidence: [README.md#L303-L303](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L303-L303)
  - [observation/documented] A Helm chart deploys hushd, the Spine checkpointer plus witness, and bundled NATS JetStream; hushd and Spine signers are fail-closed and require pre-created Kubernetes Secrets for keys at install time. -- evidence: [README.md#L119-L119](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L119-L119), [README.md#L97-L97](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L97-L97), [README.md#L112-L117](https://github.com/backbay-labs/clawdstrike/blob/b01f63ae64fae2ee6a5c359b9fc8683d44b08073/README.md#L112-L117)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](clawdstrike.detail.md)

Metadata and full claim list: [full detail](clawdstrike.detail.md)
Human notes ([notes](clawdstrike.notes.md), never overwritten by build)

[Back to map index](../../index.md)
