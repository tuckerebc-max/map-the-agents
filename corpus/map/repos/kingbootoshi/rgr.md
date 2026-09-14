# kingbootoshi/rgr

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 45ffc907a54b @ 608a715aaa98a9c8

## Summary (orientation draft, not independently verified)

rgr is described as a no-dependency Red-Green-Refactor gate for coding agents that records the failing test first, freezes it with hashes and snapshots, and refuses Green or Refactor if the Red test was edited. The CLI exposes subcommands including init, red, green, refactor, verify, revise-test, status, doctor, inspect-test, prompt, and lock-intent, invoked via Bun with flags like --goal-id, --test, --protect, --ci, --replay.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] rgr is described as a no-dependency Red-Green-Refactor gate for coding agents that records the failing test first, freezes it with hashes and snapshots, and refuses Green or Refactor if the Red test was edited. -- evidence: [README.md#L5-L5](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] The intent-lock feature adds core files intent.ts, scope-audit.ts, glob.ts, and stable-json.ts, with the scope audit composed inside verifyCommand rather than as a standalone authoritative command. -- evidence: [docs/prds/intent-lock-scope-audit.intent-boundary.md#L117-L117](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L117-L117), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L34-L42), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L24-L31](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L24-L31)
  - [observation/documented] RGR ships two skills as Claude Code and Codex plugins: the rgr skill and intent-contract, which compiles a signed Locked Intent Boundary into an IntentLock that `rgr verify --intent-lock` enforces. -- evidence: [README.md#L40-L40](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L40-L40), [README.md#L42-L43](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L42-L43)
- design-choices (1 claim(s)):
  - [observation/documented] Enforcement rules include: Red must fail, Red defaults to test-surface changes only, protected Red files are hashed with SHA-256 and snapshotted, Green runs the exact Red command, and strict Red protects imported helpers, fixtures, snapshots, test config, and lockfiles. -- evidence: [README.md#L116-L131](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L116-L131)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to write the failing test first, capture Red via `bun run rgr -- red --strict`, change production code only after Red, then run green, refactor, and `verify --ci --replay` before handoff, and to use `rgr revise-test` rather than editing protected Red tests. -- evidence: [AGENTS.md#L3-L3](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L3-L3), [AGENTS.md#L14-L14](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L14-L14), [AGENTS.md#L5-L5](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L5-L5), [AGENTS.md#L7-L12](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/AGENTS.md#L7-L12)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes subcommands including init, red, green, refactor, verify, revise-test, status, doctor, inspect-test, prompt, and lock-intent, invoked via Bun with flags like --goal-id, --test, --protect, --ci, --replay. -- evidence: [docs/TEST-DISCIPLINE.md#L28-L31](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/TEST-DISCIPLINE.md#L28-L31), [README.md#L96-L96](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L96-L96), [README.md#L147-L149](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L147-L149), [README.md#L93-L93](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L93-L93), [README.md#L99-L100](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L99-L100), [README.md#L87-L87](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L87-L87), [docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/docs/prds/intent-lock-scope-audit.intent-boundary.md#L45-L51), [README.md#L84-L84](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L84-L84)
  - [observation/documented] Every command proof uses the argv after the -- separator, and per the enforcement list this is currently direct `bun test` only. -- evidence: [README.md#L116-L131](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L116-L131)
- memory-state (1 claim(s)):
  - [observation/documented] Every rgr run writes .rgr/manifest.json, .rgr/events.jsonl, snapshots, diffs, and command output logs as an audit trail. -- evidence: [README.md#L102-L102](https://github.com/kingbootoshi/rgr/blob/45ffc907a54b0e4d69424c7caa5f88ddff558f37/README.md#L102-L102)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](rgr.detail.md)

Metadata and full claim list: [full detail](rgr.detail.md)
Human notes ([notes](rgr.notes.md), never overwritten by build)

[Back to map index](../../index.md)
