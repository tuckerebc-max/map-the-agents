# kenn-io/agentsview

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d61382967490 @ 854bb9d72f0e0765

## Summary (orientation draft, not independently verified)

agentsview is a local, single-binary tool that indexes AI coding-agent sessions into SQLite and serves a web UI with usage, cost, and activity analytics, plus optional PostgreSQL and DuckDB/Quack backends. Evidence is README/docs documentation only; no runtime code slices were supplied. Evidence coverage: 142 of 252 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 72 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project layout includes a cmd/agentsview CLI entrypoint, internal Go packages (config, db, parser, server, sync, postgres), a Svelte 5 SPA frontend, and a Tauri desktop wrapper. -- evidence: [README.md#L747-L752](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L747-L752)
- design-choices (3 claim(s)):
  - [observation/documented] The daemon is a single process hosting the web UI, API, session sync, and file watchers; background daemons self-exit after an idle period unless a client request or daemon-owned job is active. -- evidence: [README.md#L86-L90](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L86-L90), [README.md#L56-L61](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L56-L61)
  - [observation/documented] The server binds to loopback by default and validates the request Host header to guard against DNS-rebinding; forwarded access needs --public-url, and exposure beyond loopback should enable --require-auth. -- evidence: [README.md#L141-L143](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L141-L143), [README.md#L99-L103](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L99-L103), [README.md#L116-L122](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L116-L122)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building and testing use make targets (make dev, make build, make test with CGO and fts5 tags, make lint, make e2e for Playwright), with prek-based pre-commit hooks installed via make lint-tools and make install-hooks. -- evidence: [README.md#L725-L731](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L725-L731), [README.md#L741-L743](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L741-L743), [README.md#L718-L723](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L718-L723)
  - [observation/documented] Repository development practice: make bench-backends requires Docker and testcontainers to benchmark SQLite, DuckDB, and PostgreSQL store reads on a default fixture of 1,000 sessions and 64,000 messages, scalable via BENCH_BACKENDS_* env vars. -- evidence: [README.md#L733-L739](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L733-L739)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI offers serve, daemon (start/status/restart/stop), session list, and usage daily subcommands; on first run it discovers sessions, syncs them into local SQLite, and serves a web UI at http://127.0.0.1:8080. -- evidence: [README.md#L42-L50](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L42-L50), [README.md#L52-L54](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L52-L54)
  - [observation/documented] A REST endpoint GET /api/v1/sessions/{id}/usage returns fields such as total_output_tokens, peak_context_tokens, and cost as an integer microdollar object; existing sessions return 200 and missing ones 404. -- evidence: [README.md#L253-L255](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L253-L255), [README.md#L257-L264](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L257-L264)
- memory-state (1 claim(s)):
  - [observation/documented] SQLite is the primary local archive with FTS5 search and a writable UI; PostgreSQL is an optional shared team backend served read-only, and DuckDB is an optional mirror file or Quack endpoint served read-only. -- evidence: [README.md#L669-L672](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L669-L672)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentsview.detail.md)

Metadata and full claim list: [full detail](agentsview.detail.md)
Human notes ([notes](agentsview.notes.md), never overwritten by build)

[Back to map index](../../index.md)
