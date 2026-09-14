# razzant/claudexor

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 87f08d28cf33 @ ffa685ceb1e6d91a

## Summary (orientation draft, not independently verified)

Claudexor (v3.11.0) is a local-first control plane that orchestrates vendor coding-agent CLIs (Codex, Claude Code, Cursor, OpenCode, Antigravity) plus raw API adapters behind a daemon with a /v2 loopback control API, typed modes (ask/plan/agent), best-of races, review panels, credential profiles, and file-backed run artifacts. Evidence is README documentation only; development commands are correctly scoped to workflows. Evidence coverage: 91 of 133 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The monorepo splits packages/schema (contracts and generated JSON Schema), harness-* adapters, workspace (Git/directory envelopes), orchestrator (canonical mode pipelines), and review/arbitration/synthesis/budget packages. -- evidence: [README.md#L798-L807](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L798-L807)
- design-choices (2 claim(s)):
  - [observation/documented] The product is local-first: everything runs on the user's machine, files are the source of truth, and the README states there is no telemetry. -- evidence: [README.md#L22-L32](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L22-L32)
  - [observation/documented] Cost accounting is typed: paid budgets are explicit via --max-usd with zero as a real cap, unknown cost is never reported as $0, and runs can end cost_unverifiable or budget_overshoot. -- evidence: [README.md#L549-L562](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L549-L562)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors build with pnpm install --frozen-lockfile and pnpm build, then run typecheck, test, schema:gen with a generated-diff check, docs:check, and knip as gates. -- evidence: [README.md#L827-L836](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L827-L836)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Claudexor exposes a CLI, a loopback HTTP/SSE control API scoped to /v2 with POST /v2/handshake negotiation, MCP, ACP, and a macOS app as thin surfaces over the daemon. -- evidence: [README.md#L690-L693](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L690-L693), [README.md#L798-L807](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L798-L807), [README.md#L615-L623](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L615-L623)
  - [observation/documented] Retired mode ids and verbs (audit, best_of_n, explore, orchestrate, etc.) hard-error with the new spelling rather than silently aliasing; unknown flags and invalid flag values exit with code 2. -- evidence: [README.md#L259-L267](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L259-L267), [README.md#L34-L36](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L34-L36), [README.md#L404-L410](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L404-L410)
- memory-state (1 claim(s)):
  - [observation/documented] Read-only ask/plan turns resume the routed harness's native CLI session in a durable per-lane home; lane switches hydrate with a bounded continuation packet written to context/THREAD.md and disclosed via a typed session.continuity event. -- evidence: [README.md#L427-L439](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L427-L439), [README.md#L412-L425](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L412-L425)
- orchestration (2 claim(s)):
  - [observation/documented] Canonical modes are ask (read-only, with --deep-scan multi-scout research), plan (with --council parallel multi-harness drafting merged into one plan), and agent (with --n best-of races, --attempts repair loops, --until-clean, and --delegate). -- evidence: [README.md#L339-L353](https://github.com/razzant/claudexor/blob/87f08d28cf3366a27e099e05d489cf4631255c65/README.md#L339-L353)
More evidence: [full detail](claudexor.detail.md)

Metadata and full claim list: [full detail](claudexor.detail.md)
Human notes ([notes](claudexor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
