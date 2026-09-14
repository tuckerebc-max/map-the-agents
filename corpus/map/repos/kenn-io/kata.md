# kenn-io/kata

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f41a33383aba @ f7283538f30a32a1

## Summary (orientation draft, not independently verified)

kata is a durable task ledger for coding agents and humans: agents create, claim, relate, and close issues with evidence via CLI, while humans supervise in a terminal UI. The product ships as one Go binary with a CLI, a long-lived daemon, a TUI, and a browser UI served by the daemon with no separate backend. Evidence coverage: 122 of 232 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 49 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 22 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

22 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] kata is a durable task ledger for coding agents and humans: agents create, claim, relate, and close issues with evidence via CLI, while humans supervise in a terminal UI. -- evidence: [README.md#L3-L3](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L3-L3), [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20)
- components (2 claim(s)):
  - [observation/documented] The product ships as one Go binary with a CLI, a long-lived daemon, a TUI, and a browser UI served by the daemon with no separate backend. -- evidence: [docs/design/architecture.md#L11-L13](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L11-L13), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120)
  - [observation/documented] By default issue state lives in a local SQLite database under KATA_HOME; teams can opt into a remote daemon or federation, and a shared daemon can use Postgres via KATA_DSN. -- evidence: [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120)
- design-choices (4 claim(s)):
  - [observation/documented] Projects are bound to workspaces explicitly via a committed .kata.toml, never inferred from the current directory; outside a bound workspace every command except kata init fails with project_not_initialized. -- evidence: [docs/design/architecture.md#L89-L100](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L89-L100), [docs/design/architecture.md#L86-L87](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L86-L87)
  - [observation/documented] Workspace identity derives from the normalized git remote URL rather than the filesystem path, so clones resolve to the same project; one git repository attaches to exactly one project. -- evidence: [docs/design/architecture.md#L104-L112](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L104-L112)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors should see docs/development/contributing.md for repository layout and local checks including make test, make lint, make vet, and make nilaway. -- evidence: [README.md#L228-L230](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L228-L230)
  - [observation/documented] kata quickstart (alias kata agent-instructions) prints an operating contract for coding agents: search before creating, pass idempotency keys, prefer --agent output, claim work, and close only verified work with evidence. -- evidence: [README.md#L178-L183](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L178-L183)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] All reads and writes go through kata's HTTP API; no client opens SQLite or Postgres directly, and a Go app can mount the listener-free service in-process. -- evidence: [docs/design/architecture.md#L47-L53](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L47-L53), [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20)
  - [observation/documented] The CLI offers agent-oriented ergonomics: stable short refs, --json and --agent output, idempotent creates, semantic-aware search, a claim flow, and predictable failure modes. -- evidence: [docs/design/architecture.md#L15-L18](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L15-L18), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120)
More evidence: [full detail](kata.detail.md)

Metadata and full claim list: [full detail](kata.detail.md)
Human notes ([notes](kata.notes.md), never overwritten by build)

[Back to map index](../../index.md)
