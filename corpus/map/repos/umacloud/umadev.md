# umacloud/umadev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 585262706174 @ cf947f1456377b10

## Summary (orientation draft, not independently verified)

Selected evidence records: The project's source of truth is the UMADEV_HOST_SPEC_V1 spec document, described as containing 34 normative clauses backed by 113 governance content checks. UmaDev is a single Rust binary distributed via an npm shim; the architecture diagram names internal components umadev-agent, umadev-spec, umadev-knowledge, umadev-governance, umadev-contract, umadev-runtime, and umadev-host.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project's source of truth is the UMADEV_HOST_SPEC_V1 spec document, described as containing 34 normative clauses backed by 113 governance content checks. -- evidence: [README.md#L9-L12](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L9-L12), [README.md#L461-L461](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L461-L461), [README.md#L169-L172](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L169-L172)
- components (1 claim(s)):
  - [observation/documented] UmaDev is a single Rust binary distributed via an npm shim; the architecture diagram names internal components umadev-agent, umadev-spec, umadev-knowledge, umadev-governance, umadev-contract, umadev-runtime, and umadev-host. -- evidence: [README.md#L235-L238](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L235-L238), [README.md#L26-L26](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L26-L26), [README.md#L76-L76](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L76-L76), [README.md#L240-L242](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L240-L242), [README.md#L233-L233](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L233-L233)
- design-choices (2 claim(s)):
  - [observation/documented] Governance is fail-open by design: an error path in the governor returns pass rather than a block, and at write time only irreversible findings (leaked secrets, sensitive paths, destructive shell) are hard-blocked while craft issues are flagged for post-write repair. -- evidence: [README.md#L475-L475](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L475-L475), [README.md#L344-L344](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L344-L344)
  - [observation/documented] Failures are surfaced honestly as degraded, paused, blocked, incompatible, or failed rather than converted into success; a missing required review becomes an operational Unavailable pause, and critic opinions never replace the deterministic acceptance floor. -- evidence: [README.md#L227-L227](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L227-L227), [README.md#L316-L322](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L316-L322)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Five backend integrations are supported via --backend: claude-code (stream-json), codex (app-server JSON-RPC), opencode (serve HTTP/SSE), and grok-build and kimi-code over ACP v1 stdio, each with its own session transport, permission mapping, and resume behavior. -- evidence: [README.md#L367-L367](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L367-L367), [README.md#L359-L365](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L359-L365), [README.md#L92-L98](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L92-L98)
- memory-state (2 claim(s)):
  - [observation/documented] Audit evidence (tool calls, verification runs, critic verdicts) is written as JSONL under .umadev/audit/, and plans are stored in .umadev/plan.json as a dependency plan rendered as a live checklist steerable via /plan. -- evidence: [README.md#L340-L340](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L340-L340), [README.md#L209-L221](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L209-L221), [README.md#L247-L251](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L247-L251)
  - [observation/documented] A curated markdown knowledge corpus is embedded in the binary and extracted to ~/.umadev/knowledge on first launch; retrieval uses BM25 plus optional vector embeddings fused with RRF and HyDE-style expansion, falling back to BM25-only when vectors are unavailable. -- evidence: [README.md#L518-L518](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L518-L518), [README.md#L496-L496](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L496-L496), [README.md#L504-L516](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L504-L516)
- orchestration (2 claim(s)):
More evidence: [full detail](umadev.detail.md)

Metadata and full claim list: [full detail](umadev.detail.md)
Human notes ([notes](umadev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
