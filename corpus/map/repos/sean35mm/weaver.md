# sean35mm/weaver

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e5f41572c338 @ f18b9c6d31110a99

## Summary (orientation draft, not independently verified)

Weaver is a local CLI over SQLite that coordinates multiple coding agents via sessions, advisory file claims, revision-safe Markdown scratchpads, and Repository Facts, with an optional loopback web dashboard and OpenCode plugin. Contributor instructions in AGENTS.md describe development practice and are reported only under workflows.

## Source coverage

Source coverage (partial): 3 of 25 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Weaver is a CLI over a local SQLite store with no cloud account, remote sync, coordination daemon, or MCP server; Git stays authoritative for code and the CLI for coordination. -- evidence: [README.md#L29-L31](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L29-L31)
- components (1 claim(s)):
  - [observation/documented] The product provides a status→task→claim→done coordination loop, live sessions, advisory file claims, recent activity, optional Markdown scratchpads, and durable Repository Facts. -- evidence: [README.md#L13-L16](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L13-L16)
- design-choices (2 claim(s)):
  - [observation/documented] Claims are advisory and TTL-bound; a claim exit code 1 means the claim was recorded with an overlap found, and different-worktree overlaps are informational because files are isolated. -- evidence: [README.md#L172-L176](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L172-L176)
  - [observation/documented] Every scratchpad mutation creates a revision, and passing --revision prevents a stale writer from replacing a newer edit. -- evidence: [README.md#L92-L94](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L92-L94)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run tests with npm test (node --test) and npm run test:bun (bun test), both of which must pass, plus npm run typecheck and npm run build. -- evidence: [AGENTS.md#L15-L22](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L15-L22)
  - [observation/documented] Repository development practice: Conventional Commits are mandatory and drive versioning via release-please; releases are cut by merging the release-please PR rather than hand-creating releases. -- evidence: [AGENTS.md#L38-L41](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L38-L41), [AGENTS.md#L26-L34](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/AGENTS.md#L26-L34)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes scratchpad commands (list/create/read/use/edit-section/archive/trash/recover), coordination commands (status, task, claim, preflight, done, fact/forget), and setup commands (init, disable, deinit, upgrade, uninstall). -- evidence: [README.md#L200-L204](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L200-L204), [README.md#L195-L198](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L195-L198), [README.md#L188-L193](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L188-L193)
  - [observation/documented] The scratchpads web UI supports WYSIWYG and Markdown source modes, autosave with revision conflict handling, search, revision history, and shows sessions, claims, activity, and Facts; it binds only to loopback with an unguessable launch capability. -- evidence: [README.md#L114-L118](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L114-L118)
- memory-state (2 claim(s)):
  - [observation/documented] Stores live under ~/.weaver/ with one SQLite database per repository identity; scratchpads, facts, intents, and reasons are plaintext local data, and there is no telemetry. -- evidence: [README.md#L210-L222](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L210-L222)
  - [observation/documented] The first scratchpads invocation owns a foreground server per project store and OS user; later invocations reuse it, and worktrees sharing repo identity and WEAVER_HOME share the instance. -- evidence: [README.md#L120-L125](https://github.com/sean35mm/weaver/blob/e5f41572c338f41e402e9ea309088d74d10a6f68/README.md#L120-L125)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](weaver.detail.md)

Metadata and full claim list: [full detail](weaver.detail.md)
Human notes ([notes](weaver.notes.md), never overwritten by build)

[Back to map index](../../index.md)
