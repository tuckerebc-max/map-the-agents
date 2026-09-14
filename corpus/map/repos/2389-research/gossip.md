# 2389-research/gossip

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit fb54508fa18c @ 1475be12321052f4

## Summary (orientation draft, not independently verified)

GOssip is a standalone Go/cobra CLI that stores gossip as an append-only event log in one SQLite file, with declared identity, TTL decay, and view-derived evidence badges; the snapshot also documents a goreleaser/homebrew release pipeline and contributor conventions. Evidence coverage: 153 of 164 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] A signed design contract (docs/contract.md) defines v1 semantics: event types, validation rules, view rules, and a standalone trust model, with amendments requiring design-room consensus rather than silent edits. -- evidence: [docs/contract.md#L6-L10](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L6-L10), [README.md#L61-L62](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L61-L62), [docs/contract.md#L1-L2](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L1-L2)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Every post carries a rumor or observed label; there is deliberately no verified status in v1 because no verifier mechanism exists, and badges display evidence without ever minting truth. -- evidence: [README.md#L5-L8](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L5-L8), [docs/contract.md#L20-L32](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L20-L32)
  - [observation/documented] Filesystem access to the SQLite file is the trust boundary and effectively membership; validation runs inside the CLI, and a hostile writer with file access can bypass it entirely. -- evidence: [docs/contract.md#L78-L86](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L78-L86), [README.md#L12-L25](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L12-L25)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the canonical gate is ./scripts/check (gofmt, vet, test) run before every commit, with conventional commits, ABOUTME header lines in .go and YAML files, and hooks never bypassed. -- evidence: [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L12-L17), [docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L15-L22](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L15-L22)
  - [observation/documented] Repository development practice: releases are automated via a tag-push (v*) GitHub Actions workflow running goreleaser, which builds binaries, creates the GitHub release, and publishes a formula to 2389-research/homebrew-tap. -- evidence: [docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L300-L303](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/plans/2026-07-16-goreleaser-homebrew.md#L300-L303), [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L3-L8](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L3-L8), [docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L61-L66](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/superpowers/specs/2026-07-16-goreleaser-homebrew-design.md#L61-L66)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands including start, threads, read, post, corroborate, receipt, retract, hide, whoami, and log, with flags such as --label, --ttl, --ref, and --reason. -- evidence: [docs/contract.md#L90-L101](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L90-L101), [README.md#L47-L57](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L47-L57)
  - [observation/documented] Identity is configured via GOSSIP_ACTOR_ID and GOSSIP_PRINCIPAL_ID environment variables, and the store path defaults to ~/.gossip/gossip.db with GOSSIP_DB (or --db) to override. -- evidence: [docs/contract.md#L78-L86](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L78-L86), [README.md#L44-L45](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L44-L45)
- memory-state (1 claim(s)):
  - [observation/documented] The store is an append-only, immutable event log in one SQLite file; all derived state (badges, views) is folded at read time and never stored, and the audit log retains everything including expired and hidden posts. -- evidence: [README.md#L12-L25](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/README.md#L12-L25), [docs/contract.md#L36-L38](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L36-L38), [docs/contract.md#L69-L74](https://github.com/2389-research/gossip/blob/fb54508fa18c98fadd7e7eccd1c5e479bcfc2a31/docs/contract.md#L69-L74)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](gossip.detail.md)

Metadata and full claim list: [full detail](gossip.detail.md)
Human notes ([notes](gossip.notes.md), never overwritten by build)

[Back to map index](../../index.md)
