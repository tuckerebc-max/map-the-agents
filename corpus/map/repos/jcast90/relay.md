# jcast90/relay

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7bd5a2f6a13c @ eb9f73091bfb91b5

## Summary (orientation draft, not independently verified)

Selected evidence records: Relay converts a sentence, GitHub issue URL, or Linear ticket into a running plan: classify, plan, decompose into a ticket DAG, dispatch to Claude or Codex agents, verify, open a PR, and track until merged. The project is explicitly beta, pre-v1: APIs, CLI flags, ~/.relay file layouts, and GUI surfaces may change between releases, and users are asked to file issues with reproductions.

## Source coverage

Source coverage (partial): 3 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Relay converts a sentence, GitHub issue URL, or Linear ticket into a running plan: classify, plan, decompose into a ticket DAG, dispatch to Claude or Codex agents, verify, open a PR, and track until merged. -- evidence: [README.md#L46-L46](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L46-L46)
  - [observation/documented] The project is explicitly beta, pre-v1: APIs, CLI flags, ~/.relay file layouts, and GUI surfaces may change between releases, and users are asked to file issues with reproductions. -- evidence: [README.md#L32-L32](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L32-L32)
- components (2 claim(s)):
  - [observation/documented] The repo ships a TypeScript CLI/orchestrator core, a Rust ratatui TUI, a Tauri desktop GUI (React + Vite frontend, Rust backend), and a shared Rust crate harness-data that reads ~/.relay/ for both dashboards. -- evidence: [README.md#L558-L560](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L558-L560), [README.md#L541-L556](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L541-L556)
  - [observation/documented] Verification runs through an Executor abstraction whose only shipping implementation is LocalChildProcessExecutor; a pod-based executor was prototyped and removed, and a Postgres HarnessStore backend is stubbed but not wired (HARNESS_STORE=postgres falls back to files). -- evidence: [README.md#L475-L475](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L475-L475), [README.md#L471-L471](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L471-L471)
- design-choices (2 claim(s)):
  - [observation/documented] Cross-repo work is designed to go through the primary repo's tools rather than file reads: quick questions use crosslink_send, longer tasks are tickets with assignedAlias routing, and the primary agent is told not to grep or edit associated repos directly. -- evidence: [README.md#L250-L252](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L250-L252), [README.md#L246-L246](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L246-L246), [README.md#L248-L248](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L248-L248)
  - [observation/documented] Autonomous runs are bounded by wall-clock hours, a token budget, and a STOP-file kill switch, and verification commands run against an allowlist rather than being shelled blindly. -- evidence: [README.md#L62-L62](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L62-L62), [README.md#L60-L60](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L60-L60), [README.md#L268-L272](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L268-L272)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to keep PR scope tight, run pnpm test && pnpm typecheck && pnpm build before pushing, add tests for new behavior (no snapshot tests of orchestrator output), and follow two-space indent/double-quote formatting; Vitest tests live in test/ mirroring src/. -- evidence: [README.md#L610-L613](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L610-L613), [README.md#L593-L594](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L593-L594), [README.md#L572-L580](https://github.com/jcast90/relay/blob/7bd5a2f6a13ce62db53ca3c55f2a7ef89e36e710/README.md#L572-L580)
More evidence: [full detail](relay.detail.md)

Metadata and full claim list: [full detail](relay.detail.md)
Human notes ([notes](relay.notes.md), never overwritten by build)

[Back to map index](../../index.md)
