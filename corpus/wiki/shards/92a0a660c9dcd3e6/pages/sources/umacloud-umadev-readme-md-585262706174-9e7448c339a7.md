---
access: public
aliases: []
claim_ids:
- clm_1b3d51ea9be8a14243702471800d099f18f8c626489a1d9f00ba8c6624724018
- clm_5ff49b74364933a72382a1933458e46ce7217d19863319d9e41708d86e054449
- clm_6237aa59e5a11703de00c3897d9cbf216bb554ea75f4e4e60e793eee3952706c
- clm_6f75512dcdf1e5ff0b7969397e43ada06d7de53271725b63e37bd72d3eb70f6d
- clm_993ebb77e8a91eeae2fb950504982a6a9134a7d001a83fd63036c40515a3f02b
- clm_9e3128113e7a80c2ce9380ed64731374058f6241c5b8b934a65b5c27e2c1da84
- clm_be52936ff546d1358282511ef768887912ba12b5540c9088ed034f03392c1aec
- clm_cf696fd1ce095f346942e4cb13bf3c392bc7cc8967e15909874b20c79e4f8417
- clm_e582b6fb960e905f2eb96f465b3b540ec8cb2e02347aa603ce4cb784516abd57
- clm_fc17fd496d1c62237bb5bda0189754abb5233946b563b3c0c5148fe00c4e7ce1
- clm_ffd5082257b0b7b9730df80a1a7a071692e363fa9a7de7f5153c66700bbbee96
maturity: draft
page_id: pg_bfef0def7a3059f6be949e7448c339a7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3fc2b08febc65004b1663af5ef6b3a85
title: umacloud/umadev/README.md @ 585262706174
updated_at: '2026-09-14T03:21:03Z'
---

# umacloud/umadev/README.md @ 585262706174

<!-- rcw:begin owner=source:src_3fc2b08febc65004b1663af5ef6b3a85 block=evidence -->
- UmaDev is a single Rust binary distributed via an npm shim; the architecture diagram names internal components umadev-agent, umadev-spec, umadev-knowledge, umadev-governance, umadev-contract, umadev-runtime, and umadev-host. [@claim:clm_1b3d51ea9be8a14243702471800d099f18f8c626489a1d9f00ba8c6624724018]
- The project's source of truth is the UMADEV_HOST_SPEC_V1 spec document, described as containing 34 normative clauses backed by 113 governance content checks. [@claim:clm_5ff49b74364933a72382a1933458e46ce7217d19863319d9e41708d86e054449]
- Five backend integrations are supported via --backend: claude-code (stream-json), codex (app-server JSON-RPC), opencode (serve HTTP/SSE), and grok-build and kimi-code over ACP v1 stdio, each with its own session transport, permission mapping, and resume behavior. [@claim:clm_6237aa59e5a11703de00c3897d9cbf216bb554ea75f4e4e60e793eee3952706c]
- A nine-seat team model is described: eight specialist roles (product, architecture, UI/UX, frontend, backend, QA, security, DevOps) plus a coordinator that routes intent, owns the plan, schedules roles, and keeps the audit trail; role verdicts are advisory. [@claim:clm_6f75512dcdf1e5ff0b7969397e43ada06d7de53271725b63e37bd72d3eb70f6d]
- Governance is fail-open by design: an error path in the governor returns pass rather than a block, and at write time only irreversible findings (leaked secrets, sensitive paths, destructive shell) are hard-blocked while craft issues are flagged for post-write repair. [@claim:clm_993ebb77e8a91eeae2fb950504982a6a9134a7d001a83fd63036c40515a3f02b]
- Writing roles drive the main session serially under a single-writer rule, while reviewing roles run in parallel on fresh Plan-profile child sessions and return typed RoleVerdicts (accepts, blocking, advisory) over shared blackboard artifacts rather than free-form cross-talk. [@claim:clm_9e3128113e7a80c2ce9380ed64731374058f6241c5b8b934a65b5c27e2c1da84]
- Failures are surfaced honestly as degraded, paused, blocked, incompatible, or failed rather than converted into success; a missing required review becomes an operational Unavailable pause, and critic opinions never replace the deterministic acceptance floor. [@claim:clm_be52936ff546d1358282511ef768887912ba12b5540c9088ed034f03392c1aec]
- Audit evidence (tool calls, verification runs, critic verdicts) is written as JSONL under .umadev/audit/, and plans are stored in .umadev/plan.json as a dependency plan rendered as a live checklist steerable via /plan. [@claim:clm_cf696fd1ce095f346942e4cb13bf3c392bc7cc8967e15909874b20c79e4f8417]
- UmaDev owns no model endpoint and requires an externally installed, authenticated base CLI (Claude Code, Codex, OpenCode, Grok Build, or Kimi Code); it never stores or silently replaces the base's credentials or model configuration. [@claim:clm_e582b6fb960e905f2eb96f465b3b540ec8cb2e02347aa603ce4cb784516abd57]
- Plan intent is mapped to each vendor's real permission surface rather than advertised as a uniform hard sandbox; explicit no-write intent, the single-writer rule, and irreversible-action safeguards are described as hard ceilings. [@claim:clm_fc17fd496d1c62237bb5bda0189754abb5233946b563b3c0c5148fe00c4e7ce1]
- A curated markdown knowledge corpus is embedded in the binary and extracted to ~/.umadev/knowledge on first launch; retrieval uses BM25 plus optional vector embeddings fused with RRF and HyDE-style expansion, falling back to BM25-only when vectors are unavailable. [@claim:clm_ffd5082257b0b7b9730df80a1a7a071692e363fa9a7de7f5153c66700bbbee96]
<!-- rcw:end owner=source:src_3fc2b08febc65004b1663af5ef6b3a85 block=evidence -->

## Researcher notes

