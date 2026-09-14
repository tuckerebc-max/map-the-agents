# 2389-research/tracker

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit de156192ce90 @ 573327dee8852ffb

## Summary (orientation draft, not independently verified)

Selected evidence records: Pipelines are defined in .dip files using the Dippin DSL, with workflow headers declaring goal, start, exit, defaults (model/provider), and edges between nodes. Workflows can declare environmental requirements via a requires: header line; as of v0.29.0 only git is checked, and unrecognized entries warn and continue.

## Source coverage

Source coverage (partial): 6 of 220 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Pipelines are defined in .dip files using the Dippin DSL, with workflow headers declaring goal, start, exit, defaults (model/provider), and edges between nodes. -- evidence: [README.md#L136-L140](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L136-L140), [README.md#L116-L118](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L116-L118), [README.md#L110-L114](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L110-L114), [README.md#L108-L108](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L108-L108)
  - [observation/documented] Workflows can declare environmental requirements via a requires: header line; as of v0.29.0 only git is checked, and unrecognized entries warn and continue. -- evidence: [README.md#L144-L144](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L144-L144), [README.md#L154-L154](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L154-L154)
- components (2 claim(s)):
  - [observation/documented] Tracker is a three-layer stack: an LLM client with provider adapters, an agent session with turn loop and context compaction, and a pipeline engine with graph execution, checkpoints, and TUI. -- evidence: [README.md#L355-L355](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L355-L355), [README.md#L357-L376](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L357-L376)
  - [observation/documented] The engine supports eight node types: agent, human gate, tool, parallel, fan_in, subgraph, manager_loop, and conditional. -- evidence: [README.md#L158-L167](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L158-L167)
- design-choices (3 claim(s)):
  - [observation/documented] The core engine is UI-agnostic: TUI, Slack bot, and terminal REPL are peers on one library boundary sharing a transport-neutral transport/chatops core. -- evidence: [README.md#L378-L384](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L378-L384), [README.md#L472-L476](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L472-L476)
  - [observation/documented] Variable expansion is single-pass so resolved values are never re-scanned, preventing recursive expansion; unknown --param keys hard-fail at startup. -- evidence: [README.md#L192-L192](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L192-L192), [README.md#L186-L188](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L186-L188), [README.md#L190-L190](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L190-L190)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Human gates support five modes: choice, freeform, hybrid, yes/no, and interview, with interview answers stored as JSON plus a markdown summary. -- evidence: [README.md#L246-L250](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L246-L250), [README.md#L282-L282](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L282-L282), [README.md#L244-L244](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L244-L244)
  - [observation/documented] Headless operation is supported via --webhook-url: human gates are POSTed as JSON and the pipeline resumes on callback, with flags for timeout, timeout action, and auth header. -- evidence: [README.md#L672-L678](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L672-L678), [README.md#L655-L658](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L655-L658), [README.md#L662-L668](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L662-L668), [README.md#L649-L649](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L649-L649)
- memory-state (2 claim(s)):
  - [observation/documented] Each agent node runs a fresh LLM session; data flows between nodes via context keys (ctx.*, params.*, graph.*), not conversation history, with per-node scoping available. -- evidence: [README.md#L173-L175](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L173-L175), [README.md#L171-L171](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L171-L171), [README.md#L194-L194](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L194-L194)
  - [observation/documented] Agent, tool, and interview nodes can declare writes:/reads: context keys; missing declared writes hard-fail the node, and reads: pins fidelity of upstream keys. -- evidence: [README.md#L215-L215](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L215-L215), [README.md#L227-L227](https://github.com/2389-research/tracker/blob/de156192ce90ec59e00039e0f37f174754a3aeb5/README.md#L227-L227)
- orchestration (1 claim(s)):
More evidence: [full detail](tracker.detail.md)

Metadata and full claim list: [full detail](tracker.detail.md)
Human notes ([notes](tracker.notes.md), never overwritten by build)

[Back to map index](../../index.md)
