# adshao/flounder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6a5ee2313e0d @ 353ad75ef581bff8

## Summary (orientation draft, not independently verified)

Flounder is documented as a thin-agent security-audit framework whose model decides audit strategy while the framework supplies sandboxing, command policy, durable state, execution gates, a daemon control plane, and reporting. Claims below rest on README and docs/ARCHITECTURE slices; the snapshot shows 113 of 268 slices. Evidence coverage: 113 of 268 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Flounder is described as an autonomous white-hat security auditor providing security automation for target prep, audit, exploit construction, and execution proof. -- evidence: [README.md#L5-L5](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The framework is deliberately stack-agnostic: it encodes no Solidity, ZK, Rust, Go, or crypto-specific audit strategy; the model decides strategy while Flounder supplies sandbox, command policy, durable state, and reporting. -- evidence: [docs/ARCHITECTURE.md#L24-L24](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/docs/ARCHITECTURE.md#L24-L24), [README.md#L18-L18](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L18-L18)
  - [observation/documented] Findings must be execution-grounded: a finding is upgraded only when a cited local command exercises the vulnerable path, with statuses like confirmed-differential, confirmed-executable, suspected, and refuted. -- evidence: [README.md#L47-L59](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L47-L59), [README.md#L390-L397](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L390-L397)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product exposes a CLI with workflow verbs (prepare, run, map, audit, verify, confirm, report), a dashboard via `flounder ui`, a REST API where GET /api returns a self-describing catalog, and pi extension tools like flounder_prepare and flounder_run. -- evidence: [README.md#L338-L341](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L338-L341)
- memory-state (1 claim(s)):
  - [observation/documented] Local state lives under ~/.flounder: a SQLite tracking database (flounder.db), per-run artifact directories, durable history/memory per target, a daemon workspace, and daemon-local provider auth. -- evidence: [README.md#L412-L416](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L412-L416)
- orchestration (2 claim(s)):
  - [observation/documented] The tracked workflow runs prepare -> map -> dig -> synthesize -> verify -> confirm -> report, with each phase's purpose documented (e.g. Map enumerates and scores the audit surface without producing findings). -- evidence: [README.md#L47-L59](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L47-L59), [README.md#L347-L353](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L347-L353)
  - [observation/documented] A daemon/control-plane split exists: remote daemons connect with minted tokens (`flounder server daemon-token mint`), providers are authenticated per executor machine, and projects pin to a daemon and provider profile. -- evidence: [README.md#L149-L151](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L149-L151), [README.md#L434-L434](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L434-L434)
- tools-permissions (2 claim(s)):
  - [observation/documented] Model-generated commands execute in a sandbox; the default `--sandbox-backend auto` prefers Apple's container runtime on Apple silicon, falls back to Docker-backed OCI, and fails closed if no sandbox engine is ready rather than running on the host. -- evidence: [README.md#L309-L309](https://github.com/adshao/flounder/blob/6a5ee2313e0dbedcdc0d5f808ce584aa94c3cd60/README.md#L309-L309)
More evidence: [full detail](flounder.detail.md)

Metadata and full claim list: [full detail](flounder.detail.md)
Human notes ([notes](flounder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
