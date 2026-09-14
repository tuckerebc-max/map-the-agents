# umacloud/umadev -- full detail

[Back to orientation](umadev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/umacloud/umadev/585262706174ad4a958cd054f0948509e84ad610/cf947f1456377b10.json](../../../wiki/dossiers/umacloud/umadev/585262706174ad4a958cd054f0948509e84ad610/cf947f1456377b10.json)

## specifications (1 claim(s))

- [observation/documented] The project's source of truth is the UMADEV_HOST_SPEC_V1 spec document, described as containing 34 normative clauses backed by 113 governance content checks. -- evidence: [README.md#L9-L12](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L9-L12), [README.md#L461-L461](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L461-L461), [README.md#L169-L172](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L169-L172) (`clm_5ff49b74364933a72382a1933458e46ce7217d19863319d9e41708d86e054449`)

## components (1 claim(s))

- [observation/documented] UmaDev is a single Rust binary distributed via an npm shim; the architecture diagram names internal components umadev-agent, umadev-spec, umadev-knowledge, umadev-governance, umadev-contract, umadev-runtime, and umadev-host. -- evidence: [README.md#L235-L238](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L235-L238), [README.md#L26-L26](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L26-L26), [README.md#L76-L76](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L76-L76), [README.md#L240-L242](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L240-L242), [README.md#L233-L233](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L233-L233) (`clm_1b3d51ea9be8a14243702471800d099f18f8c626489a1d9f00ba8c6624724018`)

## design-choices (2 claim(s))

- [observation/documented] Governance is fail-open by design: an error path in the governor returns pass rather than a block, and at write time only irreversible findings (leaked secrets, sensitive paths, destructive shell) are hard-blocked while craft issues are flagged for post-write repair. -- evidence: [README.md#L475-L475](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L475-L475), [README.md#L344-L344](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L344-L344) (`clm_993ebb77e8a91eeae2fb950504982a6a9134a7d001a83fd63036c40515a3f02b`)
- [observation/documented] Failures are surfaced honestly as degraded, paused, blocked, incompatible, or failed rather than converted into success; a missing required review becomes an operational Unavailable pause, and critic opinions never replace the deterministic acceptance floor. -- evidence: [README.md#L227-L227](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L227-L227), [README.md#L316-L322](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L316-L322) (`clm_be52936ff546d1358282511ef768887912ba12b5540c9088ed034f03392c1aec`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Five backend integrations are supported via --backend: claude-code (stream-json), codex (app-server JSON-RPC), opencode (serve HTTP/SSE), and grok-build and kimi-code over ACP v1 stdio, each with its own session transport, permission mapping, and resume behavior. -- evidence: [README.md#L367-L367](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L367-L367), [README.md#L359-L365](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L359-L365), [README.md#L92-L98](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L92-L98) (`clm_6237aa59e5a11703de00c3897d9cbf216bb554ea75f4e4e60e793eee3952706c`)

## memory-state (2 claim(s))

- [observation/documented] Audit evidence (tool calls, verification runs, critic verdicts) is written as JSONL under .umadev/audit/, and plans are stored in .umadev/plan.json as a dependency plan rendered as a live checklist steerable via /plan. -- evidence: [README.md#L340-L340](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L340-L340), [README.md#L209-L221](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L209-L221), [README.md#L247-L251](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L247-L251) (`clm_cf696fd1ce095f346942e4cb13bf3c392bc7cc8967e15909874b20c79e4f8417`)
- [observation/documented] A curated markdown knowledge corpus is embedded in the binary and extracted to ~/.umadev/knowledge on first launch; retrieval uses BM25 plus optional vector embeddings fused with RRF and HyDE-style expansion, falling back to BM25-only when vectors are unavailable. -- evidence: [README.md#L518-L518](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L518-L518), [README.md#L496-L496](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L496-L496), [README.md#L504-L516](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L504-L516) (`clm_ffd5082257b0b7b9730df80a1a7a071692e363fa9a7de7f5153c66700bbbee96`)

## orchestration (2 claim(s))

- [observation/documented] A nine-seat team model is described: eight specialist roles (product, architecture, UI/UX, frontend, backend, QA, security, DevOps) plus a coordinator that routes intent, owns the plan, schedules roles, and keeps the audit trail; role verdicts are advisory. -- evidence: [README.md#L273-L283](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L273-L283), [README.md#L22-L22](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L22-L22), [README.md#L24-L24](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L24-L24), [README.md#L271-L271](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L271-L271) (`clm_6f75512dcdf1e5ff0b7969397e43ada06d7de53271725b63e37bd72d3eb70f6d`)
- [observation/documented] Writing roles drive the main session serially under a single-writer rule, while reviewing roles run in parallel on fresh Plan-profile child sessions and return typed RoleVerdicts (accepts, blocking, advisory) over shared blackboard artifacts rather than free-form cross-talk. -- evidence: [README.md#L310-L312](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L310-L312), [README.md#L255-L259](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L255-L259), [README.md#L316-L322](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L316-L322) (`clm_9e3128113e7a80c2ce9380ed64731374058f6241c5b8b934a65b5c27e2c1da84`)

## tools-permissions (1 claim(s))

- [observation/documented] Plan intent is mapped to each vendor's real permission surface rather than advertised as a uniform hard sandbox; explicit no-write intent, the single-writer rule, and irreversible-action safeguards are described as hard ceilings. -- evidence: [README.md#L255-L259](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L255-L259) (`clm_fc17fd496d1c62237bb5bda0189754abb5233946b563b3c0c5148fe00c4e7ce1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] UmaDev owns no model endpoint and requires an externally installed, authenticated base CLI (Claude Code, Codex, OpenCode, Grok Build, or Kimi Code); it never stores or silently replaces the base's credentials or model configuration. -- evidence: [README.md#L20-L20](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L20-L20), [README.md#L373-L373](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L373-L373), [README.md#L90-L90](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L90-L90), [README.md#L102-L102](https://github.com/umacloud/umadev/blob/585262706174ad4a958cd054f0948509e84ad610/README.md#L102-L102) (`clm_e582b6fb960e905f2eb96f465b3b540ec8cb2e02347aa603ce4cb784516abd57`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

