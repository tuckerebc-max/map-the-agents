# CodeAlmanac Architecture Audit

This folder captures the ongoing architecture audit requested on 2026-06-08.
The audit is intentionally critical: existing code shape is treated as
provisional until it earns its place.

## Goal

Determine the clean target architecture for the current CodeAlmanac codebase,
including which current boundaries are correct, which are accidental
special-case architecture, which features may not justify their cost, and which
refactor slices should happen before future feature work.

## Constraints

- Do not modify source code during this investigation.
- Write findings frequently so the work survives context compaction.
- Use the repo wiki before inspecting related subsystems.
- Trust code over wiki if they disagree, but record disagreements.
- Use subagents or external research for independent critiques and prior-art
  checks where helpful.

## Working Files

- `worklog.md`: running notes, decisions, open questions, and next steps.
- `source-map.md`: current repo map built from inspection.
- `smells.md`: suspected code smells and architectural debt.
- `subagent-briefs.md`: prompts sent to research/critique agents and returned summaries.
- `target-architecture.md`: emerging recommended shape and refactor roadmap.
- `refactor-roadmap.md`: proposed future implementation slices.
- `research-notes.md`: outside architecture research notes and takeaways.
- `completion-audit.md`: evidence that this read-only audit satisfied the request.
- `reports/`: full independent subagent reports.

## Current Verdict

The codebase does not need an enterprise-style folder rewrite. It does need a
major cleanup of accumulated exceptions: sqlite-free CLI duplication, typed
lifecycle start APIs, capture discovery consolidation, provider identity and
runtime contract cleanup, shared query read models, viewer scope clarification,
and a product decision on GitHub source access.
