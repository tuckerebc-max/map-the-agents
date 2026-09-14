# mbruhler/claude-orchestration -- full detail

[Back to orientation](claude-orchestration.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mbruhler/claude-orchestration/47fd2623a46dde056d3d00884d87373eaa188f19/9303df1c465c0ce0.json](../../../wiki/dossiers/mbruhler/claude-orchestration/47fd2623a46dde056d3d00884d87373eaa188f19/9303df1c465c0ce0.json)

## specifications (1 claim(s))

- [observation/documented] The README describes this as a Claude Code plugin for multi-agent workflow orchestration, comparing it to N8N in Claude Code, that chains AI agents to automate complex tasks using natural language or a declarative flow syntax. -- evidence: [README.md#L9-L10](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L9-L10), [README.md#L3-L3](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L3-L3) (`clm_0d6d783dca5afa1710d2c51d669b192efdc51434fca625a1a8f191e31cbf81d1`)

## components (1 claim(s))

- [observation/documented] Documentation describes the project's own layout: auto-activating skills for creating, executing, and debugging workflows, a permanent agents/ directory, an auto-cleaned temp-agents/ directory, generated temp-scripts/, and example .flow templates. -- evidence: [README.md#L340-L355](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L340-L355) (`clm_2e1faf4ffc3e8345e474523dd32e541e026c337713bf604481962521b76334f5`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Documentation describes an agent-promotion flow: after a workflow completes, temporary agents are analyzed for reusability (generic versus workflow-specific), and selected ones are moved from a temp-agents directory into a permanent agents directory and registered, while unselected ones are deleted. -- evidence: [docs/features/agent-promotion.md#L38-L41](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L38-L41), [docs/features/agent-promotion.md#L32-L36](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L32-L36), [docs/features/agent-promotion.md#L67-L70](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L67-L70), [docs/features/agent-promotion.md#L3-L3](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/features/agent-promotion.md#L3-L3) (`clm_513146c11a32086475aa522951bf64e5edef50dfbb97a574a308fccdb8954b6d`)

## interfaces (3 claim(s))

- [observation/documented] Documentation states the plugin is installed by adding a marketplace to Claude Code and installing it from the plugin menu, then verified by checking for orchestration slash commands such as /orchestration:menu and /orchestration:init. -- evidence: [README.md#L21-L21](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L21-L21), [README.md#L49-L49](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L49-L49) (`clm_079e3646521017641b39e66358a915001837ddc1ee35b9dde2621cf1fccad4bb`)
- [observation/documented] The README documents a flow syntax with sequential (->), parallel (||), and conditional (~>) operators, checkpoint labels (@label), variable capture (:var) and interpolation ({var}), and temporary-agent declaration ($agent). -- evidence: [README.md#L227-L235](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L227-L235) (`clm_be101a1b4d5a32b23b291fb6d0560fcd73fb56b79720ae60c8ba707afbfe690d`)
- [observation/documented] The README documents that workflows can run standalone and headless outside interactive Claude Code, invoked as a claude -p command against a flow file, with an option to request JSON-formatted output. -- evidence: [README.md#L364-L364](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L364-L364), [README.md#L367-L369](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L367-L369), [README.md#L362-L362](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L362-L362) (`clm_7bf7c2b0cad253cef1eddb093b655d65cc11fd9ad3443f541ffda28bfc82fa55`)

## memory-state (1 claim(s))

- [observation/documented] The executor documentation illustrates workflow execution state as a graph of nodes and edges plus per-node status (current, completed, failed, skipped) and outputs, alongside separate steering state tracking whether execution is paused and at which node. -- evidence: [docs/core/executor.md#L23-L51](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/core/executor.md#L23-L51) (`clm_1170d47b3be63776513059ae257346737c6293232890eac6e0d3f43a8a3423cd`)

## orchestration (3 claim(s))

- [observation/documented] Documentation describes a semantic routing step that sends a captured variable through an LLM-evaluated condition tree to select which branch of agents runs next, in place of fixed text-matching conditions. -- evidence: [README.md#L204-L210](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L204-L210), [README.md#L202-L202](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L202-L202) (`clm_3d7aa7afabe036838c49e94856a63101894330ded9547d917a9d19e3e38bc9fa`)
- [observation/documented] Documentation states failed or interrupted workflows are recoverable: node and variable state is saved automatically to a state file, and resuming a workflow reloads that state, skips completed steps, and continues from the point of failure. -- evidence: [README.md#L185-L187](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L185-L187), [README.md#L183-L183](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L183-L183) (`clm_5dbbdc0ad07e4cfe30a4defce918d10226e220c92f47feb4bf2d67df9cb53319`)
- [observation/documented] The steering documentation describes checkpoint types as either explicit (@review markers written into the flow syntax) or automatically inserted before risky operations, after errors, at parallel-branch merge points, and before workflow completion. -- evidence: [docs/core/steering.md#L27-L31](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/core/steering.md#L27-L31), [docs/core/steering.md#L22-L25](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/docs/core/steering.md#L22-L25) (`clm_51ca604f59423c8ddaa49ac1f199af29ad85ba069cda48bc8b3562686f707906`)

## tools-permissions (1 claim(s))

- [observation/documented] The README describes checkpoint directives such as @review that pause a workflow for human approval, with documented fallback behaviors - skip, or log to a file instead of blocking - for unattended, scheduled runs where no one can approve interactively. -- evidence: [README.md#L175-L176](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L175-L176), [README.md#L168-L168](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L168-L168), [README.md#L172-L172](https://github.com/mbruhler/claude-orchestration/blob/47fd2623a46dde056d3d00884d87373eaa188f19/README.md#L172-L172) (`clm_dc90ac4955f0ca3fe96421ac0597bb7f04bc4b7643ad458d06b01eb0241f3883`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

