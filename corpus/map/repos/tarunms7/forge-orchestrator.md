# tarunms7/forge-orchestrator

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0ac78e8eddf5 @ 25cc550ed3447ada

## Summary (orientation draft, not independently verified)

Forge-orchestrator is a Python 3.12+ orchestration engine built on Claude Code that plans tasks into a DAG, runs parallel agents in isolated git worktrees, applies a multi-gate review, and opens PRs, with optional OpenAI routing. Evidence is mostly README product documentation plus an implementation plan describing a proposed unified planner. Evidence coverage: 155 of 255 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 67 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Before coding, a Contract Builder generates binding API and type specs naming producer and consumer tasks, so parallel agents agree on interfaces; the reviewer checks compliance. -- evidence: [README.md#L204-L204](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L204-L204), [README.md#L213-L213](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L213-L213), [README.md#L206-L211](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L206-L211)
  - [inference/documented] An implementation plan proposes replacing the Scout→Architect→Detailer→Validator planning pipeline with a single Unified Planner having read-only tool access (Edit/Write disallowed) and a deterministic validator; this appears to be a planned change, not necessarily shipped behavior. -- evidence: [IMPLEMENTATION_PLAN.md#L177-L189](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L177-L189), [IMPLEMENTATION_PLAN.md#L5-L5](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L5-L5), [IMPLEMENTATION_PLAN.md#L17-L29](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L17-L29), [IMPLEMENTATION_PLAN.md#L287-L287](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/IMPLEMENTATION_PLAN.md#L287-L287)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors set up a venv, pip install -e '.[dev,web]', and run python -m pytest forge/ -q; CI runs ruff lint and format plus 2200+ tests on every PR. -- evidence: [README.md#L543-L543](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L543-L543), [README.md#L535-L541](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L535-L541)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a Click-based CLI with 14 commands including forge tui, run, fix, status, stats, logs, lessons, doctor, clean, init, serve, upgrade, and ping. -- evidence: [README.md#L500-L514](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L500-L514), [README.md#L467-L482](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L467-L482)
  - [observation/documented] A terminal UI (forge tui) and a web dashboard (forge serve, backend on port 8000 and frontend on 3000) provide live pipeline progress, plan editing, contract viewing, and cost tracking. -- evidence: [README.md#L492-L492](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L492-L492), [README.md#L488-L490](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L488-L490)
- memory-state (2 claim(s)):
  - [observation/documented] Forge stores lessons learned from failed-then-retried tasks, filters transient errors like 503s, persists lessons across projects, and adapts timeouts after slow failures; lessons are viewable and addable via forge lessons. -- evidence: [README.md#L219-L222](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L219-L222), [README.md#L224-L227](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L224-L227)
  - [observation/documented] The resolved provider configuration is persisted in pipelines.provider_config at pipeline creation, and restarts, retries, and webhook resumptions reuse that snapshot rather than current settings. -- evidence: [README.md#L403-L403](https://github.com/tarunms7/forge-orchestrator/blob/0ac78e8eddf570c11f01e5cb500a74ba148a6477/README.md#L403-L403)
- orchestration (2 claim(s)):
More evidence: [full detail](forge-orchestrator.detail.md)

Metadata and full claim list: [full detail](forge-orchestrator.detail.md)
Human notes ([notes](forge-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
