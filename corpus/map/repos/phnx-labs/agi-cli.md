# phnx-labs/agi-cli

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: phnx-labs/agents-cli (github id 1215855441).
Latest snapshot: commit 148a9795a4cd @ ac41ecdac71c4c24

## Summary (orientation draft, not independently verified)

The snapshot is README-only evidence for agi-cli (@phnx-labs/agents-cli), a CLI framework for dispatching multiple agent harnesses across machines with sessions, fleet control, insights, and routines. Claims below are documentation-based; no code inspection is available. Evidence coverage: 124 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] `agents insights perf` reads a disposable SQLite warehouse at ~/.agents/.cache/perf/perf.db containing hook, command, and run timing rollups, which is deletable at any time. -- evidence: [README.md#L141-L141](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L141-L141)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is installed as @phnx-labs/agents-cli via npm (or bun, or a curl one-liner) and every command works under both the `agents` and `ag` aliases. -- evidence: [README.md#L81-L81](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L81-L81), [README.md#L49-L54](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L49-L54), [README.md#L56-L56](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L56-L56)
  - [observation/documented] `agents run <harness> "task"` dispatches work to harnesses such as claude, codex, and antigravity, with modes (plan/edit/auto/skip), JSON output, timeouts, and Unix-pipeline chaining of agents. -- evidence: [README.md#L177-L181](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L177-L181), [README.md#L235-L238](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L235-L238), [README.md#L240-L240](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L240-L240)
- memory-state (2 claim(s)):
  - [observation/documented] Session search is backed by a SQLite + FTS5 index at ~/.agents/.history/sessions/sessions.db with incremental scanning; tool queries read SQLite only, with no embeddings, vector database, or model calls. -- evidence: [README.md#L359-L359](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L359-L359)
  - [observation/documented] Live sessions resolve to states such as working, waiting_input, idle, orphaned, crashed, closed, abandoned, queued, or unknown, with matching filter flags that imply --active; orphan/crashed detection reads tmux attached-client counts and editor registry heartbeats. -- evidence: [README.md#L395-L395](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L395-L395), [README.md#L403-L403](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L403-L403)
- orchestration (3 claim(s)):
  - [observation/documented] `agents run` supports a rate-limit fallback chain (--fallback codex,antigravity) and account-selection strategies such as --strategy balanced that spread work across accounts and exclude session-limited accounts until their stated reset time. -- evidence: [README.md#L203-L203](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L203-L203), [README.md#L216-L216](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L216-L216), [README.md#L196-L197](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L196-L197)
  - [observation/documented] `agents run auto` picks across device, harness, and account layers, excluding harnesses whose accounts are all rate-limited or signed out, and exits nonzero naming the earliest reset when nothing is healthy. -- evidence: [README.md#L227-L227](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L227-L227), [README.md#L223-L225](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L223-L225)
- tools-permissions (2 claim(s)):
More evidence: [full detail](agi-cli.detail.md)

Metadata and full claim list: [full detail](agi-cli.detail.md)
Human notes ([notes](agi-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
