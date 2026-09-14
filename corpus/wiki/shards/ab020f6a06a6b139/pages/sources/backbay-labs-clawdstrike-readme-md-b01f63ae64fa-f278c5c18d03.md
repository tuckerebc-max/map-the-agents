---
access: public
aliases: []
claim_ids:
- clm_0c2db57e325c9a21a213d9b55b185fabee168b8ec728cca52ecaa8c733d22185
- clm_193fbf7ee05d51232b0aa73ef4d749ce092feb37ad3d0b1a26427f4b9b9f3632
- clm_26ed14ccac4508a679ab965259c4f4e5dfca63d846fe88f5590b1179dca94bd4
- clm_3d9a824d8b4980770542ddc8baf525956dc12717e7c1578e515fa305fda71380
- clm_4392c4644d8683d5d0350bdd0585546465ee72cc562a65966b19cd4a403242fe
- clm_67b0d569ec11835e904c8774f7a3d2666dca18575c1f2edf4705718353cca01f
- clm_983d56618f10d67da132177d25248de32e249b4fc035066041848f5dde2d16a6
- clm_a190c4ae9401c60564a74e5342fc9699679ee794cac646d1159c73a029a00486
- clm_a36f56bdd137e004d038c255e4d613a0127d0581309e73c96cac012dbab50f96
- clm_f04c576ef81938f8218e1f4cb0f176c3d697e099fa34e111e96f767af570d276
maturity: draft
page_id: pg_5f446ff504a655d288c4f278c5c18d03
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7904ef33d485509399d778d8e838d94e
title: backbay-labs/clawdstrike/README.md @ b01f63ae64fa
updated_at: '2026-09-14T03:37:35Z'
---

# backbay-labs/clawdstrike/README.md @ b01f63ae64fa

<!-- rcw:begin owner=source:src_7904ef33d485509399d778d8e838d94e block=evidence -->
- A Helm chart deploys hushd, the Spine checkpointer plus witness, and bundled NATS JetStream; hushd and Spine signers are fail-closed and require pre-created Kubernetes Secrets for keys at install time. [@claim:clm_0c2db57e325c9a21a213d9b55b185fabee168b8ec728cca52ecaa8c733d22185]
- The product is described as a policy engine, EDR, and signed audit chain in one binary, treating AI agent tool calls in the same event taxonomy as kernel-level file, process, network, dylib, and persistence events. [@claim:clm_193fbf7ee05d51232b0aa73ef4d749ce092feb37ad3d0b1a26427f4b9b9f3632]
- The engine ships in multiple forms: a Rust crate, TypeScript SDK, Python package, Go module, CLI, desktop EDR agent (macOS Endpoint Security/Network Extension; Linux Tetragon/Hubble), and an enterprise control plane. [@claim:clm_26ed14ccac4508a679ab965259c4f4e5dfca63d846fe88f5590b1179dca94bd4]
- The CLI supports commands such as init --keygen, daemon start/status, check with --action-type and --ruleset, verify --policy, run --policy, and policy synth/simulate/diff subcommands. [@claim:clm_3d9a824d8b4980770542ddc8baf525956dc12717e7c1578e515fa305fda71380]
- The system depends on Ed25519 signing (ed25519-dalek for Rust primitives), RFC 8785 JSON canonicalization for cross-language signature verification, and NATS JetStream for telemetry transport. [@claim:clm_4392c4644d8683d5d0350bdd0585546465ee72cc562a65966b19cd4a403242fe]
- Policies are versioned deterministic policy-as-code (schema 1.5.0, backward-compatible with 1.1.0+) supporting extends from built-ins, local files, and remote URLs that are host-allowlisted and sha256 integrity-pinned. [@claim:clm_67b0d569ec11835e904c8774f7a3d2666dca18575c1f2edf4705718353cca01f]
- Enterprise deployments use a control plane with Control API, NATS JetStream transport, Spine audit chain, and Control Console; enrollment is over mTLS with posture commands using request/reply acks and signed completion bundles. [@claim:clm_983d56618f10d67da132177d25248de32e249b4fc035066041848f5dde2d16a6]
- Past observations are kept on a disk-backed flight recorder so a tightened policy can be simulated against prior state before deployment. [@claim:clm_a190c4ae9401c60564a74e5342fc9699679ee794cac646d1159c73a029a00486]
- A documented guard stack includes ForbiddenPathGuard, EgressAllowlistGuard, SecretLeakGuard, ShellCommandGuard, McpToolGuard, PromptInjectionGuard, JailbreakGuard, ComputerUseGuard, and SpiderSenseGuard, each returning a verdict with evidence. [@claim:clm_a36f56bdd137e004d038c255e4d613a0127d0581309e73c96cac012dbab50f96]
- Defaults fail closed: the guard report aggregates per-guard results such that any deny produces an overall deny, and denials emit signed receipts. [@claim:clm_f04c576ef81938f8218e1f4cb0f176c3d697e099fa34e111e96f767af570d276]
<!-- rcw:end owner=source:src_7904ef33d485509399d778d8e838d94e block=evidence -->

## Researcher notes

