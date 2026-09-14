# yusifeng/formax

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1b0c3f32eb20 @ d2824f0bf33bfc75

## Summary (orientation draft, not independently verified)

Formax is an open-source, Claude Code-inspired AI coding assistant in beta, offering TUI, Web/Electron GUI, and a JSON-RPC app-server over a shared semantics core. Evidence covers its CLI surface, architecture, permissions/hooks, env configuration, and documented gaps; review/test notes are development practice. Evidence coverage: 101 of 131 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 197 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Formax is an open-source implementation of a Claude Code-style AI assistant for software engineering tasks, offering both TUI and GUI workflows. -- evidence: [README.md#L5-L5](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L5-L5)
  - [observation/documented] The project is in Beta and is positioned as better suited for learning, experimentation, and architecture study than for stable production daily use. -- evidence: [README.md#L116-L116](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L116-L116), [README.md#L9-L9](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L9-L9)
- components (1 claim(s)):
  - [observation/documented] The codebase includes a hooks system (PreToolUse, PermissionRequest, PostToolUse) configured via `.formax/settings.local.json` with scripts under `.formax/hooks/*`, plus audit fields and a debug env flag. -- evidence: [CODEMAP.md#L179-L197](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/CODEMAP.md#L179-L197)
- design-choices (2 claim(s)):
  - [observation/documented] The architecture follows a single shared semantic core (packages/core semantics) consumed by three entry points — TUI, app-server, and Web — with renderers forbidden from forking semantic state. -- evidence: [ARCHITECTURE.md#L12-L12](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L12-L12), [ARCHITECTURE.md#L7-L10](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L7-L10), [ARCHITECTURE.md#L94-L95](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L94-L95)
  - [observation/documented] Architectural invariants include transcript truth from semantics projection, single-writer discipline, replay parity, `replaySeq` as ordering authority, and input lifecycle closure. -- evidence: [ARCHITECTURE.md#L111-L115](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L111-L115)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the project is built 100% with Codex, keeping `.codex/skills`, `docs/`, and `plans/` as traces of AI-assisted development, and semantic changes follow a contract-first change workflow. -- evidence: [README.md#L108-L110](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L108-L110), [ARCHITECTURE.md#L126-L130](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L126-L130)
  - [observation/documented] Repository development practice: a review-findings log records code-review rounds (e.g. `codex review --uncommitted`) with P1–P3 findings, fixes verified by targeted test runs and type-checks. -- evidence: [docs/anthropic-thinking-effort-review-findings-log.md#L5-L7](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/anthropic-thinking-effort-review-findings-log.md#L5-L7), [docs/anthropic-thinking-effort-review-findings-log.md#L13-L19](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/anthropic-thinking-effort-review-findings-log.md#L13-L19)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands including bare `formax` (REPL in a project directory), `formax setup`, `formax web`, `formax app-server`, and `formax serve`. -- evidence: [README.md#L70-L72](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L70-L72), [README.md#L89-L91](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L89-L91), [README.md#L62-L64](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L62-L64), [README.md#L83-L85](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L83-L85), [README.md#L46-L48](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L46-L48), [README.md#L54-L57](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L54-L57)
  - [observation/documented] `formax app-server` provides a JSON-RPC backend over stdio for GUI/IDE clients, and `formax serve` starts only the WebSocket bridge for advanced debugging or split deployments. -- evidence: [ARCHITECTURE.md#L7-L10](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/ARCHITECTURE.md#L7-L10), [README.md#L87-L87](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L87-L87), [README.md#L93-L93](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/README.md#L93-L93)
- memory-state (1 claim(s)):
  - [observation/documented] Session save/replay is supported with writer/reader modules and durable transcript turn snapshots; session saving is enabled by default and can be disabled via `FORMAX_SESSION_SAVE`. -- evidence: [docs/environment-variables.md#L33-L36](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/docs/environment-variables.md#L33-L36), [CODEMAP.md#L49-L62](https://github.com/yusifeng/formax/blob/1b0c3f32eb20c7d1ad042e01a1ce6e2adee7ad61/CODEMAP.md#L49-L62)
More evidence: [full detail](formax.detail.md)

Metadata and full claim list: [full detail](formax.detail.md)
Human notes ([notes](formax.notes.md), never overwritten by build)

[Back to map index](../../index.md)
