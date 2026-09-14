# 233i/ore-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b36da0c05720 @ f358b98138f19402

## Summary (orientation draft, not independently verified)

Selected evidence records: The product combines a TypeScript agent runtime, a React/Tauri desktop app, and a Rust OS boundary handling local file, shell, process, Git, keychain, artifact, and MCP operations. The workspace includes packages for protocol event schemas, tool specs with approval policy, agent engine with model adapters, JSONL session/artifact state storage, and a scenario-replay harness.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product combines a TypeScript agent runtime, a React/Tauri desktop app, and a Rust OS boundary handling local file, shell, process, Git, keychain, artifact, and MCP operations. -- evidence: [README.md#L36-L36](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L36-L36)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use Node 22 (pinned in .node-version), pnpm 11.x, Rust stable, and Tauri 2 prerequisites; local checks run via pnpm ci:local plus per-package test/typecheck/lint filters. -- evidence: [README.md#L106-L109](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L106-L109), [docs/API_AND_COMPATIBILITY.md#L92-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L92-L95), [README.md#L91-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L91-L95), [docs/API_AND_COMPATIBILITY.md#L97-L97](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L97-L97)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are user-level reusable workflow instructions stored at ~/.ore-code/skills/<skill-id>/SKILL.md; each skill auto-registers a slash command and its content is injected into the current prompt. -- evidence: [docs/06-skill-system.md#L7-L9](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L7-L9), [docs/06-skill-system.md#L24-L24](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L24-L24), [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30)
  - [observation/documented] Skills are documentation-like instructions, not plugin code, and do not execute arbitrary scripts; actual file, shell, and git actions still go through existing tools and the approval system. -- evidence: [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30)
- interfaces (2 claim(s)):
  - [observation/documented] The workspace includes packages for protocol event schemas, tool specs with approval policy, agent engine with model adapters, JSONL session/artifact state storage, and a scenario-replay harness. -- evidence: [docs/API_AND_COMPATIBILITY.md#L7-L14](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L7-L14), [README.md#L76-L85](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L76-L85)
  - [observation/documented] Runtime events are designed to be append-only from a reader's perspective, with new event types added in the protocol package first and older sessions expected to load when optional fields are missing. -- evidence: [docs/API_AND_COMPATIBILITY.md#L36-L39](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L36-L39), [docs/API_AND_COMPATIBILITY.md#L34-L34](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L34-L34)
- memory-state (1 claim(s)):
  - [observation/documented] The agent offers context-control features including history compression, context briefing, checkpoint summaries, usage visibility, and provider-aware request shaping for long conversations. -- evidence: [README.md#L42-L44](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L42-L44)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The runtime can execute local tools such as Git, shell/process commands, tests, diagnostics, code execution, and MCP servers when the user permits them, with an approval system meant to surface higher-risk actions. -- evidence: [PRIVACY.md#L39-L39](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/PRIVACY.md#L39-L39), [PRIVACY.md#L41-L41](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/PRIVACY.md#L41-L41)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](ore-code.detail.md)

Metadata and full claim list: [full detail](ore-code.detail.md)
Human notes ([notes](ore-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
