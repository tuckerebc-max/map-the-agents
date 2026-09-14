# arjia-labs/clu -- full detail

[Back to orientation](clu.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arjia-labs/clu/90db9ca81b89f80cddaf01491f391783c0bbba2e/09fed11b9ad5694a.json](../../../wiki/dossiers/arjia-labs/clu/90db9ca81b89f80cddaf01491f391783c0bbba2e/09fed11b9ad5694a.json)

## specifications (1 claim(s))

- [observation/documented] clu is a SQLite-backed issue tracker CLI intended for coordinating AI coding agents working on a single machine. -- evidence: [README.md#L7-L10](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L7-L10), [README.md#L48-L48](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L48-L48) (`clm_807a85aa25ddb22a9c690cc33c372bf030666323ceefe7818e3547b8b515d832`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] clu is local-first: a single binary over one SQLite file at .clu/data.sqlite, with no daemon, server, account, or network access; config.yaml is committed while the DB is gitignored. -- evidence: [README.md#L48-L48](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L48-L48), [README.md#L52-L69](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L52-L69) (`clm_1f85cd6e3e400bf943c5b23fdeceee6fb900770b65eef929b4843eade7d10e5d`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are told to run go build ./... && go test ./... before every commit, exercise demo.sh and demo-workflow.sh as end-to-end smoke tests, and follow CLAUDE.md conventions such as one file per kong command and entity-specific sentinel errors. -- evidence: [CLAUDE.md#L64-L70](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/CLAUDE.md#L64-L70), [README.md#L395-L398](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L395-L398), [README.md#L400-L400](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L400-L400) (`clm_4762820a9919a22d7c52360ab82efbd53f0fe613caab24203c3fbe8e388d40cd`)
- [observation/documented] Repository development practice: CLAUDE.md instructs breaking batch work into per-group commits that compile and pass tests, fixing bugs in priority order with separate commits, and running an end-to-end smoke test before declaring multi-file features done. -- evidence: [CLAUDE.md#L156-L164](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/CLAUDE.md#L156-L164) (`clm_cb51967f16c338ff97592f8ab3ef5b13c9405b7895c26980574562f28e9c036b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The core CLI loop is clu init, create (with -p priority and -d dependency wiring), ready, claim --context, and close, with clu brief printing an agent guide plus declared and live agents. -- evidence: [README.md#L106-L110](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L106-L110), [README.md#L120-L122](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L120-L122), [README.md#L124-L124](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L124-L124), [README.md#L112-L116](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L112-L116) (`clm_d8f72c3f6bec6017379865c1a7d3abd8dd8e35f6194faae4de0157a34b0ec8dd`)
- [observation/documented] clu batch accepts a JSON array of issues referencing each other by alias, validates the whole graph (acyclic, resolvable references, valid fields), and writes it in one transaction; a key field makes re-runs idempotent with --on-existing skip or update. -- evidence: [README.md#L231-L232](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L231-L232), [README.md#L219-L224](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L219-L224), [README.md#L245-L247](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L245-L247) (`clm_826168e8357e786653d8b27a1cf61d27287ceb7a263da3bf0bd8f8a0173d0f3d`)
- [observation/documented] clu web serves a local read/write dashboard on port 5757 over the same SQLite file, backed by an in-process REST API that clu http can expose standalone; it includes a kanban board, issue list, dependency graph, and approvals queue. -- evidence: [README.md#L73-L73](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L73-L73), [README.md#L304-L304](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L304-L304) (`clm_8ccb4eea8cd264cd1b115d878078b1594aa9197a8c76e89a00cff7e539a31554`)
- [observation/documented] Coordination primitives include TTL'd named locks (clu lock with auto-release), fire-and-forget inter-agent messaging (clu ping / clu inbox), git worktree bootstrapping, and an experimental clu sync that stores issue state as JSONL on a refs/clu/store git ref. -- evidence: [README.md#L310-L316](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L310-L316), [README.md#L318-L321](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L318-L321) (`clm_c6ec23c91aff3f8c8a8d63669299c86c56b5e8685bb71968ff528addc131e503`)

## memory-state (1 claim(s))

- [observation/documented] Every write is recorded in an append-only event log; clu history shows one issue's timeline and clu log filters the global stream by actor, kind, issue, or time window, with the actor resolved from --agent or $USER. -- evidence: [README.md#L296-L296](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L296-L296), [README.md#L291-L294](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L291-L294), [README.md#L289-L289](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L289-L289) (`clm_192b3041acb3db583e0dfc43750e01e6f0cab241bc87c227acf4d3a1da7a4ecd`)

## orchestration (4 claim(s))

- [observation/documented] Claims are atomic via an UPDATE ... RETURNING query with a subquery, so racing agents receive different issues rather than colliding on the same task. -- evidence: [README.md#L52-L69](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L52-L69) (`clm_7884fc4d50d800e3e258e554857b286bd0602ac6201b56c7652e32126f506422`)
- [observation/documented] Agents are declared in .clu/config.yaml with capabilities; capability-tagged issues in the default lane flow to whichever agent advertises that capability, or coordinators can assign directly with -a. -- evidence: [README.md#L176-L176](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L176-L176), [README.md#L157-L166](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L157-L166) (`clm_498f544aa4dcb531a2058a78f9a2edb3f03da53645882055a6cb0865be550782`)
- [observation/documented] clu agent start launches a configured agent command with layered prompts (shared .clu/agents/_shared/ markdown prepended to per-agent prompts) and heartbeats it; the command is runtime-agnostic (e.g. claude or codex). -- evidence: [README.md#L191-L194](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L191-L194), [README.md#L196-L196](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L196-L196), [README.md#L182-L189](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L182-L189) (`clm_c5db8606c5a0f94fc1f0054a07dafe0b560d9df5d3d0416d7acf5dc1907edb8a`)
- [observation/documented] Status semantics: closed issues unblock dependents, cancelled issues leave dependents blocked, and clu cancel cascades cancellation to all transitive descendants; milestone issues auto-close when their dependencies close. -- evidence: [README.md#L128-L133](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L128-L133), [README.md#L151-L151](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L151-L151), [README.md#L135-L135](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L135-L135) (`clm_4dda02683c30cda8b08bbfbf77729daac24860772b04d72f2761c54f407d5e09`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is written in Go (badges indicate Go 1.26+) and uses the pure-Go modernc.org/sqlite driver, so it needs no CGo or system SQLite libraries. -- evidence: [README.md#L12-L21](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L12-L21), [README.md#L52-L69](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L52-L69) (`clm_2343ef742e1d6c68ce88d6877e3e259127f62289472efa26095c23a25d21b4ab`)

## limitations (1 claim(s))

- [observation/documented] The project explicitly excludes being a live server-backed sync layer, a generic project-management tool, a live GitHub/Linear/Jira bridge, or an agent runtime; sync across machines is manual push/pull and marked experimental. -- evidence: [README.md#L386-L389](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L386-L389), [README.md#L318-L321](https://github.com/Arjia-Labs/clu/blob/90db9ca81b89f80cddaf01491f391783c0bbba2e/README.md#L318-L321) (`clm_735fb0047d297ebb8d3bbd1f86c0e23ea5441286d6e53dc095c1006df951150a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

