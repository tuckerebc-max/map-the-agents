# fivetaku/kkirikkiri

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 99df0f40feb6 @ 93071784013c9844

## Summary (orientation draft, not independently verified)

kkirikkiri is a Claude Code plugin that turns a natural-language goal into an approved, multi-agent team or Workflow, with session-scoped shared memory, hook-based gates, and optional external CLI providers. Evidence is mostly README and CHANGELOG documentation; no source code slices are present. Evidence coverage: 131 of 134 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] kkirikkiri is a Claude Code plugin that takes a plain-language goal, asks only for missing decisions, scans the environment, and runs an approved agent team or Workflow. -- evidence: [README.md#L9-L9](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L9-L9), [README.md#L11-L11](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L11-L11)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The validation loop runs at most two rounds by default: round 1 is the original team, round 2 an auto-judge choosing keep, full replacement, or partial swap; further rounds need explicit approval. -- evidence: [README.md#L130-L134](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L130-L134)
  - [observation/documented] Five built-in presets (Research, Development, Analysis, Content, Product/PM) are matched by natural-language trigger words and serve only as starting points for the final team. -- evidence: [README.md#L105-L111](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L105-L111), [README.md#L113-L113](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L113-L113), [README.md#L103-L103](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L103-L103)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product is invoked via a /kkirikkiri slash command (e.g. '/kkirikkiri build me a research team') after installing from a plugin marketplace. -- evidence: [README.md#L29-L31](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L29-L31), [README.md#L46-L48](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L46-L48), [README.md#L23-L25](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L23-L25)
- memory-state (1 claim(s)):
  - [observation/documented] Teams write session-scoped files under .kkirikkiri/teams/{team_name}/ (TEAM_PLAN.md, TEAM_PROGRESS.md, TEAM_FINDINGS.md, report.md), while saved teams persist cross-session under .kkirikkiri/shared/saved-teams/. -- evidence: [README.md#L119-L124](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L119-L124), [README.md#L117-L117](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L117-L117), [README.md#L126-L126](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L126-L126)
- orchestration (2 claim(s)):
  - [observation/documented] Execution follows an eight-step pipeline: intent/preset matching, parallel environment scan, interview, team composition, user confirmation, shared-memory init, quality validation, and report collection. -- evidence: [README.md#L69-L79](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L69-L79)
  - [observation/documented] Two execution substrates are offered: a live collaborating Agent Teams mode or a deterministic Workflow pipeline for high-volume fan-out work; the user picks between them. -- evidence: [CHANGELOG.md#L205-L208](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L205-L208), [README.md#L54-L61](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/README.md#L54-L61)
- tools-permissions (1 claim(s)):
  - [observation/documented] Hook-based gates enforce write boundaries at runtime: gate-spawn blocks spawning a member whose write_scope overlaps another member's declared scope, and blocks spawns lacking tool/read-only/write_scope/stop declarations. -- evidence: [CHANGELOG.md#L33-L36](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L33-L36), [CHANGELOG.md#L57-L60](https://github.com/fivetaku/kkirikkiri/blob/99df0f40feb6011b62094677b86260acc9fbb575/CHANGELOG.md#L57-L60)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](kkirikkiri.detail.md)

Metadata and full claim list: [full detail](kkirikkiri.detail.md)
Human notes ([notes](kkirikkiri.notes.md), never overwritten by build)

[Back to map index](../../index.md)
