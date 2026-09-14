# arch1esun/arcgentic

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 645c345077d7 @ 8f6a77ad6d7d02bc

## Summary (orientation draft, not independently verified)

Arcgentic v2.2.0 is a harness-engineering plugin for Codex and Claude Code that wraps coding work in a gated Orchestrator/Planner/Developer/Test/Auditor workflow, distributed via PyPI, npm, and a Claude Code marketplace. Evidence is mostly README documentation plus a developer handoff file describing contributor workflow rules. Evidence coverage: 149 of 288 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 37 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Arcgentic is described as a harness engineering layer for AI coding agents, turning ad-hoc prompting into a gated engineering workflow for Codex and Claude Code. -- evidence: [README.md#L44-L49](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L44-L49), [README.md#L7-L8](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L7-L8)
  - [observation/documented] The V2 workflow sequence is: idea, brainstorm/planning, round handoff, development, developer self-audit, optional user-test, external audit, pass-or-fix, then next round, next phase, or closeout. -- evidence: [README.md#L229-L239](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L229-L239)
- components (3 claim(s)):
  - [observation/documented] Five fixed roles are defined: Orchestrator (routing/dispatch), Planner (planning and closeout decisions), Developer (building, fixes, self-audit), Test (realistic user testing when needed), and Auditor (independent PASS/NEEDS_FIX/AUDIT_INCOMPLETE review). -- evidence: [README.md#L243-L249](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L243-L249), [README.md#L251-L252](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L251-L252)
  - [observation/documented] Role/state routing is implemented as a Topology module (toolkit/src/arcgentic/topology.py) that projects can override via project.arcgentic_v2.topology in state.yaml; custom topologies are validated at parse time and zero-config projects keep the default 5-role sequence. -- evidence: [README.md#L256-L266](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L256-L266)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the CLAUDE handoff file instructs the contributing dev session to follow a 30-task build contract in order, use TDD for Bash scripts, commit once per task with conventional-commit prefixes directly on main, and never add paid-API integrations or force-push. -- evidence: [CLAUDE-v0.1.0-handoff.md#L232-L243](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L232-L243), [CLAUDE-v0.1.0-handoff.md#L113-L114](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L113-L114), [CLAUDE-v0.1.0-handoff.md#L118-L121](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L118-L121), [CLAUDE-v0.1.0-handoff.md#L72-L72](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L72-L72), [CLAUDE-v0.1.0-handoff.md#L107-L109](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L107-L109)
  - [observation/documented] Repository development practice: the handoff defines six mechanical completion checks (commits count, all test files passing, plugin.json version bump, tag creation, dogfood gate files present, and everything pushed to origin) before reporting done. -- evidence: [CLAUDE-v0.1.0-handoff.md#L191-L191](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L191-L191), [CLAUDE-v0.1.0-handoff.md#L220-L221](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L220-L221), [CLAUDE-v0.1.0-handoff.md#L214-L217](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L214-L217), [CLAUDE-v0.1.0-handoff.md#L208-L208](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L208-L208), [CLAUDE-v0.1.0-handoff.md#L200-L205](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L200-L205), [CLAUDE-v0.1.0-handoff.md#L211-L211](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L211-L211), [CLAUDE-v0.1.0-handoff.md#L197-L197](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/CLAUDE-v0.1.0-handoff.md#L197-L197)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The Auditor role returns one of three verdicts — PASS, NEEDS_FIX, or AUDIT_INCOMPLETE — and the Orchestrator routes the next step based on that outcome. -- evidence: [README.md#L174-L185](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L174-L185), [README.md#L243-L249](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L243-L249), [README.md#L471-L474](https://github.com/Arch1eSUN/Arcgentic/blob/645c345077d78a6525055f641eb677c361ae767a/README.md#L471-L474)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
More evidence: [full detail](arcgentic.detail.md)

Metadata and full claim list: [full detail](arcgentic.detail.md)
Human notes ([notes](arcgentic.notes.md), never overwritten by build)

[Back to map index](../../index.md)
