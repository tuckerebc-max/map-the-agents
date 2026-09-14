# 2389-research/gossip -- full detail

[Back to orientation](gossip.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/gossip/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/1475be12321052f4.json](../../../wiki/dossiers/2389-research/gossip/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/1475be12321052f4.json)

## specifications (1 claim(s))

- [observation/documented] A signed design contract (docs/contract.md) defines v1 semantics: event types, validation rules, view rules, and a standalone trust model, with amendments requiring design-room consensus rather than silent edits. -- evidence: [docs/contract.md#L6-L10](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L6-L10), [README.md#L61-L62](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L61-L62), [docs/contract.md#L1-L2](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L1-L2) (`clm_2adce312392441e935479965283adcba53dec710902699c2701ba25d37ff8e55`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Every post carries a rumor or observed label; there is deliberately no verified status in v1 because no verifier mechanism exists, and badges display evidence without ever minting truth. -- evidence: [README.md#L5-L8](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L5-L8), [docs/contract.md#L20-L32](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L20-L32) (`clm_990c63672b8e8bdfff528f43d83c29a4ac66a98ca8fa59e544aa4f5eff58e5df`)
- [observation/documented] Filesystem access to the SQLite file is the trust boundary and effectively membership; validation runs inside the CLI, and a hostile writer with file access can bypass it entirely. -- evidence: [docs/contract.md#L78-L86](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L78-L86), [README.md#L12-L25](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L12-L25) (`clm_2dd6e649c21b8a74b3929645d7afb4a083db9d2d3ffafc3a3e3a00a530d13d96`)
- [observation/documented] TTLs are speaker-chosen within store-configured default_ttl/max_ttl bounds, persisted as absolute expires_at at append; out-of-bounds TTLs are validation errors, not silent clamps. -- evidence: [docs/contract.md#L49-L65](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L49-L65), [docs/contract.md#L20-L32](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L20-L32) (`clm_0abc3ca6f661346f62ca77c940aeb462692a36d12a06d4bc08f3ae9ef1514018`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the canonical gate is ./scripts/check (gofmt, vet, test) run before every commit, with conventional commits, ABOUTME header lines in .go and YAML files, and hooks never bypassed. -- evidence: [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17), [docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L15-L22](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L15-L22) (`clm_15c53c9fc340f6900e9c6d34946a26da746e5f464497cb1696034e7833bdd610`)
- [observation/documented] Repository development practice: releases are automated via a tag-push (v*) GitHub Actions workflow running goreleaser, which builds binaries, creates the GitHub release, and publishes a formula to 2389-research/homebrew-tap. -- evidence: [docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L300-L303](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L300-L303), [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L3-L8](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L3-L8), [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L61-L66](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L61-L66) (`clm_b7b13fb3d0d804bd0640fddcb0311a5f070a31fd13f2023920c83bbb4c3621bb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands including start, threads, read, post, corroborate, receipt, retract, hide, whoami, and log, with flags such as --label, --ttl, --ref, and --reason. -- evidence: [docs/contract.md#L90-L101](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L90-L101), [README.md#L47-L57](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L47-L57) (`clm_d411149fb8119d5c8d888c4404f30a1d13ec506f1aaa129daa657c70d8853794`)
- [observation/documented] Identity is configured via GOSSIP_ACTOR_ID and GOSSIP_PRINCIPAL_ID environment variables, and the store path defaults to ~/.gossip/gossip.db with GOSSIP_DB (or --db) to override. -- evidence: [docs/contract.md#L78-L86](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L78-L86), [README.md#L44-L45](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L44-L45) (`clm_952497d2acafad3c4d45cde7311ee58b7a5bf2a4e4aa8cd7fe66fcbf4175da2e`)

## memory-state (1 claim(s))

- [observation/documented] The store is an append-only, immutable event log in one SQLite file; all derived state (badges, views) is folded at read time and never stored, and the audit log retains everything including expired and hidden posts. -- evidence: [README.md#L12-L25](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L12-L25), [docs/contract.md#L36-L38](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L36-L38), [docs/contract.md#L69-L74](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L69-L74) (`clm_1e730d26242fefe98aff50f4d37fbfb23471e6fd9c5952914decb3c82688c6f2`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is a single Go binary built with cobra, using pure-Go SQLite via modernc.org/sqlite so CGO_ENABLED=0 cross-compiles cleanly for darwin/linux on amd64 and arm64. -- evidence: [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17), [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L43-L57](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L43-L57), [docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L9-L9](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L9-L9) (`clm_aee5553be45bc74727ad77b37f6ec40a44e5129bcfa1b498654373cdf76c8bd4`)

## limitations (2 claim(s))

- [observation/documented] Documented v1 cuts include no verifier or verified status, no cross-store sharing, no per-thread ACLs, no rooms, no SSE/watch, no cryptographic identity, and no publish/live subscribers. -- evidence: [docs/contract.md#L78-L86](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L78-L86), [docs/contract.md#L105-L106](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L105-L106) (`clm_ea24042fc64980ae1a7c6d85f4945a91fcfd62feccdaff7844caede7d446b6c9`)
- [observation/documented] The CLI mints a fresh command key per invocation, so it offers no retry semantics in v1; re-running a command like retract is a distinct later command that is correctly rejected. -- evidence: [README.md#L29-L32](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L29-L32) (`clm_9b7ec6d7ed190398b6266c15d18e01076085f4d22c17b0aa09cd75241811a642`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

