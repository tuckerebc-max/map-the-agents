# basilisk-labs/agentplane

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ecfccc5ad023 @ f428a157f1df96e8

## Summary (orientation draft, not independently verified)

Agentplane is a Git-native CLI control plane that constrains coding agents with bounded semantic episodes, formal lifecycle transitions, and repository-stored evidence. Evidence is mostly README, roadmap, and contributor policy; no source code slices are present.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The design separates semantic judgment (agents) from mechanically authoritative workflow mechanics (CLI), with the CLI resolving authority, transitions, routing, schemas, and stop conditions in code rather than by model guesses. -- evidence: [README.md#L33-L38](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L33-L38), [README.md#L105-L107](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L105-L107), [README.md#L30-L31](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L30-L31), [README.md#L11-L14](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L11-L14)
  - [observation/documented] Two workflow modes are offered: 'direct' for lighter local routes and 'branch_pr' for worktrees, branches, PR artifacts, and hosted checks; the agent declares a preferred mode but Agentplane can strengthen the route based on observed work. -- evidence: [README.md#L116-L119](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L116-L119), [README.md#L111-L114](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L111-L114)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: POLICY.md requires lint and full tests to pass before merging to main, tests for behavior changes, English-only user-facing strings, no accidental npm releases, and no uncommitted code changes under packages/**. -- evidence: [POLICY.md#L33-L36](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L33-L36), [POLICY.md#L17-L27](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L17-L27)
  - [observation/documented] Repository development practice: contributors work through the agentplane task lifecycle (task new, plan approve, verify, finish), open issues first for architectural or CLI-surface changes, and must keep src/cli, usecases, ports, and adapters layering with OS/git/network access confined to adapters. -- evidence: [CONTRIBUTING.md#L33-L34](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L33-L34), [CONTRIBUTING.md#L51-L59](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L51-L59), [POLICY.md#L51-L59](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/POLICY.md#L51-L59), [CONTRIBUTING.md#L15-L20](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L15-L20), [CONTRIBUTING.md#L38-L41](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/CONTRIBUTING.md#L38-L41)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a CLI (npm package 'agentplane', short alias 'ap') with commands such as init, quickstart, task create/active/advance/run, and evaluator list/show/execute. -- evidence: [README.md#L55-L57](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L55-L57), [README.md#L61-L65](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L61-L65), [README.md#L47-L53](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L47-L53), [ROADMAP.md#L100-L100](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/ROADMAP.md#L100-L100)
  - [observation/documented] task advance returns a bounded episode packet containing the objective, writable scope, context, result schema, an exchange.result_path, and an exact exchange.resume_argv command for returning the typed result. -- evidence: [README.md#L67-L70](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L67-L70)
- memory-state (1 claim(s)):
  - [observation/documented] Operating state lives in the repository: AGENTS.md/CLAUDE.md as policy gateway, .agentplane/WORKFLOW.md, per-task README and acr.json (Agent Change Record), and pr/ artifacts; an optional Local Context layer adds source-backed repository knowledge. -- evidence: [README.md#L125-L131](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L125-L131), [README.md#L133-L136](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L133-L136)
- orchestration (2 claim(s)):
  - [observation/documented] The control loop issues a bounded semantic episode, the agent returns a semantic result, and the CLI observes facts, runs the formal route, records evidence, and stops at approval, recovery, or verified completion. -- evidence: [README.md#L72-L75](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L72-L75), [README.md#L89-L95](https://github.com/basilisk-labs/agentplane/blob/ecfccc5ad0230fc1876a319be0af5cdb530c339f/README.md#L89-L95)
More evidence: [full detail](agentplane.detail.md)

Metadata and full claim list: [full detail](agentplane.detail.md)
Human notes ([notes](agentplane.notes.md), never overwritten by build)

[Back to map index](../../index.md)
