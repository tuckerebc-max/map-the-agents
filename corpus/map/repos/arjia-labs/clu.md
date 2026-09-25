# arjia-labs/clu

Status: distilled - Freshness: stale
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 90db9ca81b89 @ cee0033f1c0d6e82

## Summary (orientation draft, not independently verified)

clu is a single-binary, pure-Go SQLite-backed issue tracker CLI for coordinating multiple AI coding agents on one machine, with atomic claims, capability routing, bulk graph instantiation, workflow templates, a web dashboard, and an experimental git-ref sync. Evidence is README plus contributor notes (CLAUDE.md); no code slices are present, so behavior claims rest on documentation.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] clu is a SQLite-backed issue tracker CLI intended for coordinating AI coding agents working on a single machine. -- evidence: [README.md#L7-L10](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L7-L10), [README.md#L48-L48](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L48-L48)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] clu is local-first: a single binary over one SQLite file at .clu/data.sqlite, with no daemon, server, account, or network access; config.yaml is committed while the DB is gitignored. -- evidence: [README.md#L48-L48](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L48-L48), [README.md#L52-L69](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L52-L69)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to run go build ./... && go test ./... before every commit, exercise demo.sh and demo-workflow.sh as end-to-end smoke tests, and follow CLAUDE.md conventions such as one file per kong command and entity-specific sentinel errors. -- evidence: [CLAUDE.md#L64-L70](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/CLAUDE.md#L64-L70), [README.md#L395-L398](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L395-L398), [README.md#L400-L400](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L400-L400)
  - [observation/documented] Repository development practice: CLAUDE.md instructs breaking batch work into per-group commits that compile and pass tests, fixing bugs in priority order with separate commits, and running an end-to-end smoke test before declaring multi-file features done. -- evidence: [CLAUDE.md#L156-L164](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/CLAUDE.md#L156-L164)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The core CLI loop is clu init, create (with -p priority and -d dependency wiring), ready, claim --context, and close, with clu brief printing an agent guide plus declared and live agents. -- evidence: [README.md#L106-L110](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L106-L110), [README.md#L120-L122](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L120-L122), [README.md#L124-L124](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L124-L124), [README.md#L112-L116](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L112-L116)
  - [observation/documented] clu batch accepts a JSON array of issues referencing each other by alias, validates the whole graph (acyclic, resolvable references, valid fields), and writes it in one transaction; a key field makes re-runs idempotent with --on-existing skip or update. -- evidence: [README.md#L231-L232](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L231-L232), [README.md#L219-L224](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L219-L224), [README.md#L245-L247](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L245-L247)
- memory-state (1 claim(s)):
  - [observation/documented] Every write is recorded in an append-only event log; clu history shows one issue's timeline and clu log filters the global stream by actor, kind, issue, or time window, with the actor resolved from --agent or $USER. -- evidence: [README.md#L296-L296](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L296-L296), [README.md#L291-L294](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L291-L294), [README.md#L289-L289](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L289-L289)
- orchestration (4 claim(s)):
  - [observation/documented] Claims are atomic via an UPDATE ... RETURNING query with a subquery, so racing agents receive different issues rather than colliding on the same task. -- evidence: [README.md#L52-L69](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L52-L69)
More evidence: [full detail](clu.detail.md)

Metadata and full claim list: [full detail](clu.detail.md)
Human notes ([notes](clu.notes.md), never overwritten by build)

[Back to map index](../../index.md)
