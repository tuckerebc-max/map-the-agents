---
access: public
aliases: []
claim_ids:
- clm_0bcc419129d27e87ff2979e99634f8aef8cb6c74d7e3d4d28ef3b4d9837b26d0
- clm_20f2dcb8b073e39e03dfea3cd5967653eaeb5aaef156f94d2139a5fea584a27f
- clm_33f2d1659583ddf2381bc63fb576f774a8853987e03230f16968b1ae9a670e51
- clm_3d37ba67b7f4146dd98677d44f7ebdfffdc98277eab73f5a148d3723863acbdf
- clm_44a094a2ff181810d8f487d8c2ecd5ffd28f0fd9c0411e6fefc77714e262c135
- clm_6fd95171d84cb28be7cff5efa13b7c50098d12f6142e3809cf72fb226bde7876
- clm_7bb51eb85d7c77ca6627777e149ed7dd8ced48b99511ea2fef7687fe93b25982
- clm_9800024d7ab05d152206febdf72c2e1ae16bfaba7e0fd4e138a12049706a31ef
- clm_adf0b9118e971e9cc57d7e5480c0497635cd8926d28d18dea801d458be25d7d4
- clm_d95e2692b6e32a30cce8164c78142f2e27290b79468b305ec90a4090ef071293
maturity: draft
page_id: pg_4e5d91154820566fa364cec6fcc7ad97
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e00dfd2542fd5abbb900b598ef04f362
title: cosmtrek/mindwalk/README.md @ 77cd79596a1b
updated_at: '2026-09-14T03:42:57Z'
---

# cosmtrek/mindwalk/README.md @ 77cd79596a1b

<!-- rcw:begin owner=source:src_e00dfd2542fd5abbb900b598ef04f362 block=evidence -->
- mindwalk is a visualization tool that replays coding-agent sessions as light moving through a night-style map of the codebase, showing where the agent searched, read, and edited. [@claim:clm_0bcc419129d27e87ff2979e99634f8aef8cb6c74d7e3d4d28ef3b4d9837b26d0]
- Verdicts are never decided by the model: Go mechanically rolls up dimension and criterion verdicts from finding severities and coverage grades, strips hallucinated citations, and retries once on invalid output. [@claim:clm_20f2dcb8b073e39e03dfea3cd5967653eaeb5aaef156f94d2139a5fea584a27f]
- The judge subprocess runs sealed: it gets no tools, no MCP servers, no user or project settings, and no session persistence, and it only receives the evaluated session's summary. [@claim:clm_33f2d1659583ddf2381bc63fb576f774a8853987e03230f16968b1ae9a670e51]
- Evaluation reports are cached one per session in ~/.mindwalk/reports, go stale without auto-rerun when session content changes, and reuse the drafted rubric when task wording is unchanged. [@claim:clm_3d37ba67b7f4146dd98677d44f7ebdfffdc98277eab73f5a148d3723863acbdf]
- Repository development practice: contributors run make setup, make serve (dev server on :8765), make test before sending a PR, and make build to regenerate embedded assets; Go code must stay gofmt-ed and internal/server/static must never be hand-edited. [@claim:clm_44a094a2ff181810d8f487d8c2ecd5ffd28f0fd9c0411e6fefc77714e262c135]
- Session evaluation uses up to two sealed judge calls via the user's own claude or codex CLI: one drafting task-specific criteria from user messages, one unified scoring pass over four fixed process dimensions plus those criteria. [@claim:clm_6fd95171d84cb28be7cff5efa13b7c50098d12f6142e3809cf72fb226bde7876]
- The system separates three artifacts: a normalized trace (internal/adapter, one adapter per agent format), a deterministic citymap (internal/citymap), and an LLM-judge report (internal/judge), joined by a local Go server serving a React/Three.js frontend. [@claim:clm_7bb51eb85d7c77ca6627777e149ed7dd8ced48b99511ea2fef7687fe93b25982]
- The UI encodes touch state as light on a dark ink-blue map (seen green, read blue, edited amber), with tree and terrain views, a playback histogram where observation stays cool and mutation glows warm, and glow treated strictly as data. [@claim:clm_9800024d7ab05d152206febdf72c2e1ae16bfaba7e0fd4e138a12049706a31ef]
- The CLI offers serve, open, map, build, trace, and analyze subcommands, with flags such as --port, --no-open, per-agent session dirs, --judge, --model, and --no-rubric. [@claim:clm_adf0b9118e971e9cc57d7e5480c0497635cd8926d28d18dea801d458be25d7d4]
- The product is a single Go binary that runs fully locally; viewing sends nothing anywhere, with the only network use being the optional evaluation through the user's own agent CLI. [@claim:clm_d95e2692b6e32a30cce8164c78142f2e27290b79468b305ec90a4090ef071293]
<!-- rcw:end owner=source:src_e00dfd2542fd5abbb900b598ef04f362 block=evidence -->

## Researcher notes

