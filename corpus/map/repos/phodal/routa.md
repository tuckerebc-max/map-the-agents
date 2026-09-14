# phodal/routa

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e48861ab81e2 @ 53e7bdcd26858588

## Summary (orientation draft, not independently verified)

Routa is a workspace-first multi-agent coordination platform with a dual-backend architecture (Next.js web, Tauri desktop backed by a Rust/Axum server), a Kanban-based specialist pipeline with review gates, and documented contributor workflows. Evidence is mostly README/AGENTS documentation; no code slices are present.

## Source coverage

Source coverage (partial): 3 of 307 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Routa is described as a workspace-first multi-agent coordination platform for software delivery, keeping goals, tasks, sessions, traces, evidence, and review state visible on a board rather than in one chat thread. -- evidence: [README.md#L23-L23](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L23-L23), [README.md#L7-L7](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L7-L7)
- components (2 claim(s)):
  - [observation/documented] The implementation is intentionally dual-backend: a Next.js web app in src/, a Tauri desktop shell backed by an Axum server in crates/routa-server, sharing semantics defined by api-contract.yaml. -- evidence: [README.md#L47-L47](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L47-L47), [README.md#L49-L52](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L49-L52)
  - [observation/documented] Repository map includes crates/routa-core (shared Rust runtime foundation), crates/routa-cli (CLI entrypoints and ACP serving), and crates/harness-monitor (run observation and operator-facing harness monitor). -- evidence: [README.md#L231-L244](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L231-L244)
- design-choices (2 claim(s)):
  - [observation/documented] Each downstream lane is deliberately stricter than the previous one; cards accumulate artifacts (story YAML, execution brief, dev evidence, review verdict, completion summary) as they move forward. -- evidence: [README.md#L108-L108](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L108-L108), [README.md#L110-L114](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L110-L114), [README.md#L116-L116](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L116-L116), [README.md#L77-L77](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L77-L77)
  - [observation/documented] The review gate is a stacked decision path with three layers: Harness Monitor (what happened), Entrix Fitness (what should be true, hard gates and evidence requirements), and Gate Specialist (whether the card can move). -- evidence: [README.md#L60-L62](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L60-L62), [README.md#L58-L58](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L58-L58)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors must run entrix validation before PR using docs/fitness/README.md as the canonical rulebook, with tiers fast and normal, and build via cargo build -p entrix. -- evidence: [AGENTS.md#L41-L41](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L41-L41), [AGENTS.md#L43-L47](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L43-L47), [AGENTS.md#L49-L51](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L49-L51)
  - [observation/documented] Repository development practice: commits must follow Conventional Commits with one concern per commit, under 10 files and 1000 changed lines, exactly one co-author line, and UI PRs should include screenshots or recordings. -- evidence: [AGENTS.md#L64-L66](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L64-L66), [AGENTS.md#L82-L83](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L82-L83), [AGENTS.md#L57-L60](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L57-L60)
- skills-patterns (1 claim(s)):
  - [observation/documented] Built-in lane prompts live under resources/specialists/workflows/kanban/*.yaml, and core role prompts (routa, crafter, gate) under resources/specialists/core/. -- evidence: [README.md#L124-L124](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L124-L124)
- interfaces (2 claim(s)):
  - [observation/documented] Integration surfaces listed include ACP, MCP, A2A, AG-UI, A2UI, REST, and SSE. -- evidence: [README.md#L49-L52](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L49-L52)
  - [observation/documented] The CLI is distributed as routa-cli on npm and crates.io, with commands such as routa --help, routa acp list, and routa workspace list. -- evidence: [README.md#L173-L177](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L173-L177), [README.md#L9-L15](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L9-L15)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](routa.detail.md)

Metadata and full claim list: [full detail](routa.detail.md)
Human notes ([notes](routa.notes.md), never overwritten by build)

[Back to map index](../../index.md)
