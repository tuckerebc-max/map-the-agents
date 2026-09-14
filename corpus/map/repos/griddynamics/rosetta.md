# griddynamics/rosetta

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 785054e925aa @ 785672389caeb1f9

## Summary (orientation draft, not independently verified)

Rosetta is an open-source engineering-governance system for AI coding agents, delivered as IDE plugins or an optional MCP server, layering core/organization/project instructions with workflows, guardrails, and subagent orchestration. The snapshot documents its architecture, command-alias interface, rosettify CLI/MCP tooling, and eval harnesses (curiocity, rosettify-prompts). Evidence coverage: 106 of 288 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 210 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Rosettify is a local CLI/MCP utility providing deterministic workflow execution with zero network calls; it includes plan management, specs management, an atomic write cycle with a backup chain, and sequential phase enforcement. -- evidence: [docs/ARCHITECTURE.md#L151-L158](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L151-L158), [docs/ARCHITECTURE.md#L143-L143](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L143-L143)
- design-choices (2 claim(s)):
  - [observation/documented] Rosetta layers instructions at runtime — core, then organization, then project — with higher layers propagating to every project automatically, all authored in markdown and versioned in Git. -- evidence: [README.md#L102-L102](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L102-L102), [README.md#L123-L123](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L123-L123)
  - [observation/documented] The architecture follows inversion of control: Rosetta does not see or process source code; it exposes guardrails and a menu of instructions, and the coding agent selects only what it needs. -- evidence: [docs/ARCHITECTURE.md#L72-L72](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L72-L72)
- workflows (2 claim(s)):
  - [observation/documented] Rosetta ships named workflows including coding-flow, requirements-authoring-flow, security-flow, testgen/api-aqa/ui-aqa flows, and code-analysis-flow, each with defined phases, subagents, and HITL gates. -- evidence: [README.md#L49-L55](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L49-L55), [README.md#L191-L191](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L191-L191)
  - [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md for workflow and expectations, and the README notes Rosetta plugins are used to develop Rosetta itself. -- evidence: [README.md#L211-L211](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L211-L211), [README.md#L213-L213](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L213-L213)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Rosetta defines typed command aliases (e.g. USE SKILL, APPLY PHASE, INVOKE SUBAGENT) that work across IDEs instead of calling MCP tools directly, for portability, decoupling, and authoring. -- evidence: [docs/ARCHITECTURE.md#L80-L80](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L80-L80), [docs/ARCHITECTURE.md#L82-L84](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L82-L84), [docs/ARCHITECTURE.md#L86-L100](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L86-L100)
  - [observation/documented] The rosettify tool is published on npm and invoked via npx, or run as a local MCP server over stdio with a --mcp flag; it offers plan and specs subcommands operating on local JSON files. -- evidence: [docs/ARCHITECTURE.md#L151-L158](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L151-L158), [docs/ARCHITECTURE.md#L145-L145](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L145-L145)
- memory-state (1 claim(s)):
  - [observation/documented] Rosetta instructs agents to maintain agents/MEMORY.md with root causes, actions tried, and lessons learned, and to write execution state (plans, specs, phase progress) to disk so failed sessions resume from checkpoints. -- evidence: [README.md#L199-L199](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L199-L199), [README.md#L195-L195](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L195-L195)
- orchestration (1 claim(s)):
More evidence: [full detail](rosetta.detail.md)

Metadata and full claim list: [full detail](rosetta.detail.md)
Human notes ([notes](rosetta.notes.md), never overwritten by build)

[Back to map index](../../index.md)
