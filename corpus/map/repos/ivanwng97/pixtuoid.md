# ivanwng97/pixtuoid

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 61fa3012895f @ d6a2848ae934438e

## Summary (orientation draft, not independently verified)

pixtuoid is a Rust terminal TUI that visualizes multiple AI coding-agent sessions as animated pixel-art characters in an office, fed by hook shims and JSONL transcript watching. Evidence covers product behavior, architecture, configuration, supported tools, and contributor workflow.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] pixtuoid is a terminal-based tool that visualizes AI coding agents as pixel-art coworkers in an office, with each session shown as a character at a desk. -- evidence: [README.md#L41-L41](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L41-L41), [README.md#L7-L9](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L7-L9)
- components (2 claim(s)):
  - [observation/documented] Agent events arrive via two transports — a hook shim writing to a Unix socket (named pipe on Windows) with a 200ms fire-and-forget bound, and JSONL transcript watching — feeding one channel whose reducer folds events into office state for a half-block pixel-art renderer. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138)
  - [observation/documented] The project is a Rust workspace of five crates, with the core having no terminal dependencies. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138), [CLAUDE.md#L28-L30](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L28-L30)
- design-choices (3 claim(s)):
  - [observation/documented] The hook shim is designed to never block the agent: it performs a 200ms fire-and-forget write and can be invoked without blocking the agent CLI. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138)
  - [observation/documented] Character shirt and pants colors derive from the working directory so same-repo agents share colors; hair and skin vary per agent across 16 curated outfits. -- evidence: [README.md#L77-L95](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L77-L95)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: non-trivial work follows an arc (pick, design gate, spec, TDD build, self-review, merge gate) where the merge gate is a two-lens-review skill requiring 2+ differentiated lenses, green CI, and dispositioned bot findings, and a human performs the merge. -- evidence: [CLAUDE.md#L71-L76](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L71-L76)
  - [observation/documented] Repository development practice: contributors use `just build`, `just test` (nextest), and `just preflight` as the pre-push gate running lint, clippy, hack, and test in CI order. -- evidence: [CLAUDE.md#L50-L55](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L50-L55)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The TUI exposes keyboard shortcuts: q quit, p pause, s sources panel, t themes, m sound, Tab agent dashboard, ? help, and arrow/jk/PgUp/PgDn floor navigation. -- evidence: [README.md#L71-L71](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L71-L71)
  - [observation/documented] Pressing s opens a Sources panel to connect an agent CLI without a separate install step; disconnecting there removes the character, and broken hooks are flagged, with `pixtuoid doctor` providing a health report. -- evidence: [README.md#L69-L69](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L69-L69)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](pixtuoid.detail.md)

Metadata and full claim list: [full detail](pixtuoid.detail.md)
Human notes ([notes](pixtuoid.notes.md), never overwritten by build)

[Back to map index](../../index.md)
