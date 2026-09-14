# autoresearch-factory/agon

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 594fa079fd35 @ e0afbc882b3308ac

## Summary (orientation draft, not independently verified)

The snapshot contains only README documentation (English and Chinese) describing Agon, a Claude Code plugin that drives autonomous research from topic to experiment via slash commands and multi-agent loops with file-based handoffs. No source code is present in the evidence, so claims are limited to what the README documents.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Every handoff between agents goes through a file on disk, which the README says makes runs recoverable, auditable, and reusable across projects. -- evidence: [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11)
  - [observation/documented] The pipeline is deliberately minimal and explicit: topic → idea → proposal → experiment. -- evidence: [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Agon exposes four Claude Code slash commands: /idea-tick, /proposal-tick, /experiment-tick, and /deep-lit-tick, which advance the research pipeline stages. -- evidence: [README.md#L45-L48](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L45-L48)
  - [observation/documented] Commands accept free-form arguments, e.g. /experiment-tick can be told a run is a debugging run and asked to pause for user approval after each agent call. -- evidence: [README.md#L52-L59](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L52-L59)
- memory-state (2 claim(s)):
  - [observation/documented] The documented setup enables CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS so the main agent can resume background subagents and subagents can message each other, and sets cleanupPeriodDays to 3650 to retain session history. -- evidence: [README.md#L109-L113](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L109-L113)
  - [inference/documented] The data workspace layout (topics/, ideas/, workspace/ directories) appears to be where the file-based artifacts of each pipeline stage are stored. -- evidence: [README.md#L67-L72](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L67-L72)
- orchestration (1 claim(s)):
  - [observation/documented] The experiment stage coordinates scientist, coder, auditor, and reviewer roles for a single workspace, with agents planning, implementing, auditing, and reviewing each other in closed loops. -- evidence: [README.md#L45-L48](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L45-L48), [README.md#L11-L11](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L11-L11)
- tools-permissions (1 claim(s)):
  - [observation/documented] Running Agon requires launching Claude Code with --dangerously-skip-permissions, because unattended subagents write files, launch experiments, and call tools for hours and a permission prompt would stall the run; the README suggests isolating it on its own machine, container, or account. -- evidence: [README.md#L36-L39](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L36-L39), [README.md#L41-L41](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L41-L41)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Agon is a Claude Code plugin intended to run from a separate data workspace repository (agon-artifacts), cloned side by side with the plugin directory. -- evidence: [README.md#L63-L63](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L63-L63), [README.md#L19-L19](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L19-L19), [README.md#L21-L24](https://github.com/AutoResearch-Factory/Agon/blob/594fa079fd35ad51a0ae062668fd859447f5681b/README.md#L21-L24)
More evidence: [full detail](agon.detail.md)

Metadata and full claim list: [full detail](agon.detail.md)
Human notes ([notes](agon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
