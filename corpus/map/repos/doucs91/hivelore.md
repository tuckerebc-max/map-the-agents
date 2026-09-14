# doucs91/hivelore

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f6ddcc78c4fe @ 84c09b59240bf4ba

## Summary (orientation draft, not independently verified)

Hivelore is a repo-native context-policy tool for coding agents: team knowledge lives as anchored Markdown records under .ai/, and deterministic gates (MCP tools, Git hooks, CI) block changes that repeat captured mistakes. The README documents its CLI/MCP interfaces, packages, sensor validation doctrine, enforcement postures, and explicit scope limits. Evidence coverage: 124 of 388 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The monorepo contains @hivelore/cli (main product), @hivelore/mcp (bundled MCP server), @hivelore/core (types, schema, anchors, token budgets), @hivelore/embeddings (optional offline semantic ranking), plus a VS Code extension and a GitHub Action. -- evidence: [README.md#L590-L592](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L590-L592), [README.md#L583-L588](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L583-L588)
- design-choices (3 claim(s)):
  - [observation/documented] Enforcement is governed by a single posture knob (advisory, balanced default, strict); process gates never refuse a local commit at any posture, and strict adds process gates at pre-push and CI. -- evidence: [README.md#L340-L344](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L340-L344), [README.md#L350-L353](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L350-L353)
  - [observation/documented] Only deterministic, code-bound evidence can block a commit (validated sensors, anchored anti-patterns, stale anchors on touched files); anchor, literal-token, and semantic matches are surfaced for review, never blocked. -- evidence: [README.md#L432-L445](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L432-L445)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product ships an MCP server exposing tools including get_briefing, mem_save, mem_tried, mem_search, mem_get, mem_update, propose_sensor, code_map, code_search, mem_verify, scaffold_test, and pre_commit_check. -- evidence: [README.md#L544-L560](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L544-L560)
  - [observation/documented] MCP tool exposure is controlled by a profile variable: enforcement (default), maintenance, and experimental/full as legacy aliases for maintenance after the experimental diagnostics were removed in v0.32.0. -- evidence: [README.md#L564-L567](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L564-L567)
- memory-state (2 claim(s)):
  - [observation/documented] Knowledge lives as Git-native Markdown records (decision, gotcha, convention, attempt, architecture) under .ai/, anchored to file paths and symbols; team memories are committed to git while personal memories and runtime/cache state are gitignored. -- evidence: [README.md#L538-L538](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L538-L538), [README.md#L530-L536](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L530-L536), [README.md#L67-L72](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L67-L72), [README.md#L481-L502](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L481-L502)
  - [observation/documented] Since v0.57.0 anchor matches are weighted by path rarity (IDF): anchors touched by over 35% of recent commits need corroboration to outrank others, and too-small samples are reported as unknown and rank as before. -- evidence: [README.md#L632-L633](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L632-L633), [README.md#L627-L630](https://github.com/Doucs91/hivelore/blob/f6ddcc78c4fee972631ad7c23adaf53a971e3566/README.md#L627-L630)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](hivelore.detail.md)

Metadata and full claim list: [full detail](hivelore.detail.md)
Human notes ([notes](hivelore.notes.md), never overwritten by build)

[Back to map index](../../index.md)
