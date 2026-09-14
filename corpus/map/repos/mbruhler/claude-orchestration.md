# mbruhler/claude-orchestration

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 47fd2623a46d @ 9303df1c465c0ce0

## Summary (orientation draft, not independently verified)

claude-orchestration is a Claude Code plugin for multi-agent workflow orchestration: a declarative flow syntax (sequential/parallel/conditional operators, checkpoints, variable capture), semantic LLM-based routing, human-approval checkpoints with unattended fallbacks, state-file recovery of interrupted workflows, and an agent-promotion flow that turns reusable temporary agents into permanent ones. Code examples in its docs are illustrative, not inspected source. Evidence: 6 of 30 candidate files stored (README.md, docs/core/executor.md, parser.md, steering.md, visualizer.md, docs/features/agent-promotion.md); 24 omitted by file budget, and the packet itself further capped visualizer.md at zero delivered slices; selection incomplete.

## Source coverage

Source coverage (partial): 6 of 30 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes this as a Claude Code plugin for multi-agent workflow orchestration, comparing it to N8N in Claude Code, that chains AI agents to automate complex tasks using natural language or a declarative flow syntax. -- evidence: [README.md#L9-L10](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L9-L10), [README.md#L3-L3](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] Documentation describes the project's own layout: auto-activating skills for creating, executing, and debugging workflows, a permanent agents/ directory, an auto-cleaned temp-agents/ directory, generated temp-scripts/, and example .flow templates. -- evidence: [README.md#L340-L355](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L340-L355)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Documentation describes an agent-promotion flow: after a workflow completes, temporary agents are analyzed for reusability (generic versus workflow-specific), and selected ones are moved from a temp-agents directory into a permanent agents directory and registered, while unselected ones are deleted. -- evidence: [docs/features/agent-promotion.md#L38-L41](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L38-L41), [docs/features/agent-promotion.md#L32-L36](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L32-L36), [docs/features/agent-promotion.md#L67-L70](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L67-L70), [docs/features/agent-promotion.md#L3-L3](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L3-L3)
- interfaces (3 claim(s)):
  - [observation/documented] Documentation states the plugin is installed by adding a marketplace to Claude Code and installing it from the plugin menu, then verified by checking for orchestration slash commands such as /orchestration:menu and /orchestration:init. -- evidence: [README.md#L21-L21](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L21-L21), [README.md#L49-L49](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L49-L49)
  - [observation/documented] The README documents a flow syntax with sequential (->), parallel (||), and conditional (~>) operators, checkpoint labels (@label), variable capture (:var) and interpolation ({var}), and temporary-agent declaration ($agent). -- evidence: [README.md#L227-L235](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L227-L235)
- memory-state (1 claim(s)):
  - [observation/documented] The executor documentation illustrates workflow execution state as a graph of nodes and edges plus per-node status (current, completed, failed, skipped) and outputs, alongside separate steering state tracking whether execution is paused and at which node. -- evidence: [docs/core/executor.md#L23-L51](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/core/executor.md#L23-L51)
- orchestration (3 claim(s)):
  - [observation/documented] Documentation describes a semantic routing step that sends a captured variable through an LLM-evaluated condition tree to select which branch of agents runs next, in place of fixed text-matching conditions. -- evidence: [README.md#L204-L210](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L204-L210), [README.md#L202-L202](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L202-L202)
More evidence: [full detail](claude-orchestration.detail.md)

Metadata and full claim list: [full detail](claude-orchestration.detail.md)
Human notes ([notes](claude-orchestration.notes.md), never overwritten by build)

[Back to map index](../../index.md)
