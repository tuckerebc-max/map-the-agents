---
access: public
aliases: []
claim_ids:
- clm_192b3041acb3db583e0dfc43750e01e6f0cab241bc87c227acf4d3a1da7a4ecd
- clm_1f85cd6e3e400bf943c5b23fdeceee6fb900770b65eef929b4843eade7d10e5d
- clm_2343ef742e1d6c68ce88d6877e3e259127f62289472efa26095c23a25d21b4ab
- clm_4762820a9919a22d7c52360ab82efbd53f0fe613caab24203c3fbe8e388d40cd
- clm_498f544aa4dcb531a2058a78f9a2edb3f03da53645882055a6cb0865be550782
- clm_4dda02683c30cda8b08bbfbf77729daac24860772b04d72f2761c54f407d5e09
- clm_735fb0047d297ebb8d3bbd1f86c0e23ea5441286d6e53dc095c1006df951150a
- clm_7884fc4d50d800e3e258e554857b286bd0602ac6201b56c7652e32126f506422
- clm_807a85aa25ddb22a9c690cc33c372bf030666323ceefe7818e3547b8b515d832
- clm_826168e8357e786653d8b27a1cf61d27287ceb7a263da3bf0bd8f8a0173d0f3d
- clm_8ccb4eea8cd264cd1b115d878078b1594aa9197a8c76e89a00cff7e539a31554
- clm_c5db8606c5a0f94fc1f0054a07dafe0b560d9df5d3d0416d7acf5dc1907edb8a
- clm_c6ec23c91aff3f8c8a8d63669299c86c56b5e8685bb71968ff528addc131e503
- clm_d8f72c3f6bec6017379865c1a7d3abd8dd8e35f6194faae4de0157a34b0ec8dd
maturity: draft
page_id: pg_33a87ebbcf2a5f6495c19ac79002ec43
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0e41427458db5111b4aba1e956ea7046
title: Arjia-Labs/clu/README.md @ 90db9ca81b89
updated_at: '2026-09-14T03:35:02Z'
---

# Arjia-Labs/clu/README.md @ 90db9ca81b89

<!-- rcw:begin owner=source:src_0e41427458db5111b4aba1e956ea7046 block=evidence -->
- Every write is recorded in an append-only event log; clu history shows one issue's timeline and clu log filters the global stream by actor, kind, issue, or time window, with the actor resolved from --agent or $USER. [@claim:clm_192b3041acb3db583e0dfc43750e01e6f0cab241bc87c227acf4d3a1da7a4ecd]
- clu is local-first: a single binary over one SQLite file at .clu/data.sqlite, with no daemon, server, account, or network access; config.yaml is committed while the DB is gitignored. [@claim:clm_1f85cd6e3e400bf943c5b23fdeceee6fb900770b65eef929b4843eade7d10e5d]
- The project is written in Go (badges indicate Go 1.26+) and uses the pure-Go modernc.org/sqlite driver, so it needs no CGo or system SQLite libraries. [@claim:clm_2343ef742e1d6c68ce88d6877e3e259127f62289472efa26095c23a25d21b4ab]
- Repository development practice: contributors are told to run go build ./... && go test ./... before every commit, exercise demo.sh and demo-workflow.sh as end-to-end smoke tests, and follow CLAUDE.md conventions such as one file per kong command and entity-specific sentinel errors. [@claim:clm_4762820a9919a22d7c52360ab82efbd53f0fe613caab24203c3fbe8e388d40cd]
- Agents are declared in .clu/config.yaml with capabilities; capability-tagged issues in the default lane flow to whichever agent advertises that capability, or coordinators can assign directly with -a. [@claim:clm_498f544aa4dcb531a2058a78f9a2edb3f03da53645882055a6cb0865be550782]
- Status semantics: closed issues unblock dependents, cancelled issues leave dependents blocked, and clu cancel cascades cancellation to all transitive descendants; milestone issues auto-close when their dependencies close. [@claim:clm_4dda02683c30cda8b08bbfbf77729daac24860772b04d72f2761c54f407d5e09]
- The project explicitly excludes being a live server-backed sync layer, a generic project-management tool, a live GitHub/Linear/Jira bridge, or an agent runtime; sync across machines is manual push/pull and marked experimental. [@claim:clm_735fb0047d297ebb8d3bbd1f86c0e23ea5441286d6e53dc095c1006df951150a]
- Claims are atomic via an UPDATE ... RETURNING query with a subquery, so racing agents receive different issues rather than colliding on the same task. [@claim:clm_7884fc4d50d800e3e258e554857b286bd0602ac6201b56c7652e32126f506422]
- clu is a SQLite-backed issue tracker CLI intended for coordinating AI coding agents working on a single machine. [@claim:clm_807a85aa25ddb22a9c690cc33c372bf030666323ceefe7818e3547b8b515d832]
- clu batch accepts a JSON array of issues referencing each other by alias, validates the whole graph (acyclic, resolvable references, valid fields), and writes it in one transaction; a key field makes re-runs idempotent with --on-existing skip or update. [@claim:clm_826168e8357e786653d8b27a1cf61d27287ceb7a263da3bf0bd8f8a0173d0f3d]
- clu web serves a local read/write dashboard on port 5757 over the same SQLite file, backed by an in-process REST API that clu http can expose standalone; it includes a kanban board, issue list, dependency graph, and approvals queue. [@claim:clm_8ccb4eea8cd264cd1b115d878078b1594aa9197a8c76e89a00cff7e539a31554]
- clu agent start launches a configured agent command with layered prompts (shared .clu/agents/_shared/ markdown prepended to per-agent prompts) and heartbeats it; the command is runtime-agnostic (e.g. claude or codex). [@claim:clm_c5db8606c5a0f94fc1f0054a07dafe0b560d9df5d3d0416d7acf5dc1907edb8a]
- Coordination primitives include TTL'd named locks (clu lock with auto-release), fire-and-forget inter-agent messaging (clu ping / clu inbox), git worktree bootstrapping, and an experimental clu sync that stores issue state as JSONL on a refs/clu/store git ref. [@claim:clm_c6ec23c91aff3f8c8a8d63669299c86c56b5e8685bb71968ff528addc131e503]
- The core CLI loop is clu init, create (with -p priority and -d dependency wiring), ready, claim --context, and close, with clu brief printing an agent guide plus declared and live agents. [@claim:clm_d8f72c3f6bec6017379865c1a7d3abd8dd8e35f6194faae4de0157a34b0ec8dd]
<!-- rcw:end owner=source:src_0e41427458db5111b4aba1e956ea7046 block=evidence -->

## Researcher notes

