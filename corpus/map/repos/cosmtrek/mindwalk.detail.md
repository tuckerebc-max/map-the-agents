# cosmtrek/mindwalk -- full detail

[Back to orientation](mindwalk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cosmtrek/mindwalk/77cd79596a1b7f9f62256ea06485e15182a09566/979a5969183bf46b.json](../../../wiki/dossiers/cosmtrek/mindwalk/77cd79596a1b7f9f62256ea06485e15182a09566/979a5969183bf46b.json)

## specifications (1 claim(s))

- [observation/documented] mindwalk is a visualization tool that replays coding-agent sessions as light moving through a night-style map of the codebase, showing where the agent searched, read, and edited. -- evidence: [README.md#L16-L24](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L16-L24), [README.md#L3-L3](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L3-L3) (`clm_0bcc419129d27e87ff2979e99634f8aef8cb6c74d7e3d4d28ef3b4d9837b26d0`)

## components (1 claim(s))

- [observation/documented] The system separates three artifacts: a normalized trace (internal/adapter, one adapter per agent format), a deterministic citymap (internal/citymap), and an LLM-judge report (internal/judge), joined by a local Go server serving a React/Three.js frontend. -- evidence: [README.md#L137-L147](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L137-L147), [README.md#L149-L150](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L149-L150) (`clm_7bb51eb85d7c77ca6627777e149ed7dd8ced48b99511ea2fef7687fe93b25982`)

## design-choices (1 claim(s))

- [observation/documented] The UI encodes touch state as light on a dark ink-blue map (seen green, read blue, edited amber), with tree and terrain views, a playback histogram where observation stays cool and mutation glows warm, and glow treated strictly as data. -- evidence: [.impeccable.md#L44-L54](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/.impeccable.md#L44-L54), [.impeccable.md#L22-L34](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/.impeccable.md#L22-L34), [README.md#L58-L83](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L58-L83) (`clm_9800024d7ab05d152206febdf72c2e1ae16bfaba7e0fd4e138a12049706a31ef`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors run make setup, make serve (dev server on :8765), make test before sending a PR, and make build to regenerate embedded assets; Go code must stay gofmt-ed and internal/server/static must never be hand-edited. -- evidence: [README.md#L165-L171](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L165-L171), [README.md#L156-L161](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L156-L161), [AGENTS.md#L43-L43](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/AGENTS.md#L43-L43), [AGENTS.md#L38-L41](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/AGENTS.md#L38-L41) (`clm_44a094a2ff181810d8f487d8c2ecd5ffd28f0fd9c0411e6fefc77714e262c135`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI offers serve, open, map, build, trace, and analyze subcommands, with flags such as --port, --no-open, per-agent session dirs, --judge, --model, and --no-rubric. -- evidence: [README.md#L46-L54](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L46-L54) (`clm_adf0b9118e971e9cc57d7e5480c0497635cd8926d28d18dea801d458be25d7d4`)

## memory-state (1 claim(s))

- [observation/documented] Evaluation reports are cached one per session in ~/.mindwalk/reports, go stale without auto-rerun when session content changes, and reuse the drafted rubric when task wording is unchanged. -- evidence: [docs/dynamic-rubric-evaluation.md#L79-L83](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L79-L83), [README.md#L128-L131](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L128-L131), [docs/dynamic-rubric-evaluation.md#L85-L86](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L85-L86) (`clm_3d37ba67b7f4146dd98677d44f7ebdfffdc98277eab73f5a148d3723863acbdf`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The judge subprocess runs sealed: it gets no tools, no MCP servers, no user or project settings, and no session persistence, and it only receives the evaluated session's summary. -- evidence: [docs/dynamic-rubric-evaluation.md#L101-L103](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L101-L103), [README.md#L120-L126](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L120-L126) (`clm_33f2d1659583ddf2381bc63fb576f774a8853987e03230f16968b1ae9a670e51`)

## evaluation (2 claim(s))

- [observation/documented] Session evaluation uses up to two sealed judge calls via the user's own claude or codex CLI: one drafting task-specific criteria from user messages, one unified scoring pass over four fixed process dimensions plus those criteria. -- evidence: [docs/dynamic-rubric-evaluation.md#L52-L55](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L52-L55), [docs/dynamic-rubric-evaluation.md#L35-L41](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L35-L41), [README.md#L120-L126](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L120-L126) (`clm_6fd95171d84cb28be7cff5efa13b7c50098d12f6142e3809cf72fb226bde7876`)
- [observation/documented] Verdicts are never decided by the model: Go mechanically rolls up dimension and criterion verdicts from finding severities and coverage grades, strips hallucinated citations, and retries once on invalid output. -- evidence: [docs/dynamic-rubric-evaluation.md#L57-L61](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L57-L61), [README.md#L105-L111](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L105-L111) (`clm_20f2dcb8b073e39e03dfea3cd5967653eaeb5aaef156f94d2139a5fea584a27f`)

## dependencies (1 claim(s))

- [observation/documented] The product is a single Go binary that runs fully locally; viewing sends nothing anywhere, with the only network use being the optional evaluation through the user's own agent CLI. -- evidence: [README.md#L16-L24](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L16-L24), [README.md#L120-L126](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/README.md#L120-L126) (`clm_d95e2692b6e32a30cce8164c78142f2e27290b79468b305ec90a4090ef071293`)

## limitations (1 claim(s))

- [observation/documented] The fixed process dimensions (exploration, scope, wandering, verification) are tuned for code-editing work and can be systematically too harsh on research, debugging, or documentation sessions, per the project's own design doc. -- evidence: [docs/dynamic-rubric-evaluation.md#L12-L16](https://github.com/cosmtrek/mindwalk/blob/77cd79596a1b7f9f62256ea06485e15182a09566/docs/dynamic-rubric-evaluation.md#L12-L16) (`clm_ac9b82cfa8f0e7c9e321440ad868bcf358d1acde8b87332207d98bff3a24385e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

