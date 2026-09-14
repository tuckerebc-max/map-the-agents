# kuberwastaken/claurst

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b0637c97ec34 @ c2842a05b173155c

## Summary (orientation draft, not independently verified)

The evidence consists of product documentation (docs/advanced.md, docs/auth.md) describing Claurst's runtime features: effort/thinking controls, auto-compaction, session storage and SDK, plan mode, goal system, managed agents, speech modes, headless mode, permission tiers, LSP tool, worktree isolation, and credential resolution. All prior claims were verified as supported; the worktree feature is now backed by cited slices. Evidence coverage: 177 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 37 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

37 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The max effort level is only supported by models exposing it in the API (currently Opus 4.6 generation); unsupported models fall back to high. -- evidence: [docs/advanced.md#L34-L34](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L34-L34)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (15 claim(s)):
  - [observation/documented] Claurst exposes /thinking to toggle extended thinking and /effort to set a level (low, medium, high, or max) for the session. -- evidence: [docs/advanced.md#L13-L16](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L13-L16)
  - [observation/documented] CLI flags --thinking <tokens> and --effort <level> set a token budget and effort level for the claurst binary. -- evidence: [docs/advanced.md#L20-L23](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L20-L23)
- memory-state (6 claim(s)):
  - [observation/documented] Effort levels low, medium, and high persist to ~/.claude.json across sessions, while max and numeric token budgets are session-scoped. -- evidence: [docs/advanced.md#L36-L36](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L36-L36)
  - [observation/documented] The CLAUDE_CODE_EFFORT_LEVEL environment variable overrides the persisted effort setting for the current process, with a warning shown on conflict with /effort. -- evidence: [docs/advanced.md#L38-L38](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L38-L38)
- orchestration (6 claim(s)):
  - [observation/documented] Auto-compaction summarises conversation history when token usage crosses the effective context window minus a 13,000-token buffer, replacing messages with a compact summary. -- evidence: [docs/advanced.md#L52-L52](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L52-L52)
  - [observation/documented] The goal system lets Claurst work autonomously across turns toward one objective, stopping on GoalCompleteTool with audit, /goal pause or clear, a 200-turn runaway guard, or token budget exhaustion. -- evidence: [docs/advanced.md#L207-L210](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L207-L210), [docs/advanced.md#L196-L196](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L196-L196)
- tools-permissions (6 claim(s)):
  - [observation/documented] Plan mode restricts the model to read-only operations; write and execute operations require explicit permission, and ExitPlanModeTool returns to the normal permission model. -- evidence: [docs/advanced.md#L185-L188](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L185-L188), [docs/advanced.md#L176-L176](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L176-L176)
  - [observation/documented] Budget-control flags --max-budget-usd, --max-turns, and --max-tokens stop the run when limits are reached, exiting with a corresponding error message. -- evidence: [docs/advanced.md#L409-L411](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L409-L411), [docs/advanced.md#L403-L407](https://github.com/Kuberwastaken/claurst/blob/b0637c97ec34144387cbf2f74f65df6d16a6cef1/docs/advanced.md#L403-L407)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](claurst.detail.md)

Metadata and full claim list: [full detail](claurst.detail.md)
Human notes ([notes](claurst.notes.md), never overwritten by build)

[Back to map index](../../index.md)
