# wrongstack/wrongstack

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fdbf2c0268c6 @ c8dee8173236ea4b

## Summary (orientation draft, not independently verified)

README and architecture docs describe WrongStack as a from-scratch, MIT-licensed TypeScript AI coding agent with a four-primitive kernel, six UI surfaces, SAGE SQLite/FTS5 memory, a Director-led multi-agent fleet, per-tool permission policy, and a benchmark harness package. Evidence is documentation-based; no source code slices are present. Evidence coverage: 123 of 367 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 382 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The pnpm workspace reportedly contains 29 packages and two applications, with foundation packages persistence, kanban, and core, plus runtime, providers, tools, and user-surface packages. -- evidence: [docs/architecture.md#L50-L52](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L50-L52), [docs/architecture.md#L54-L62](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L54-L62)
- design-choices (1 claim(s)):
  - [observation/documented] The kernel is described as four primitives — Container, Pipeline, EventBus, RunController — with extension points in registries and services bound through the Container. -- evidence: [docs/architecture.md#L88-L92](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L88-L92), [README.md#L524-L527](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L524-L527), [README.md#L510-L520](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L510-L520), [README.md#L155-L165](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L155-L165)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: release verification uses pnpm release:check with 18 gates, root Vitest coverage thresholds are set (>=76% lines, >=75% functions, >=66% branches), and package-boundary rules are enforced by a dedicated architecture test. -- evidence: [README.md#L563-L568](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L563-L568), [docs/architecture.md#L64-L70](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L64-L70)
  - [observation/documented] Repository development practice: pnpm release:fast skips only the audit and instrumented-coverage gates that CI covers, and the release matrix verifies the packed providers package installs with npm 10. -- evidence: [README.md#L50-L66](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L50-L66)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product offers six launch surfaces: a readline REPL, an Ink TUI behind --tui, a WebUI, SimpleUI, an Electron Desktop shell, and a cross-machine HQ dashboard. -- evidence: [README.md#L285-L289](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L285-L289), [README.md#L273-L280](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L273-L280), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144)
- memory-state (1 claim(s)):
  - [observation/documented] SAGE is project-local long-term memory backed by SQLite/FTS5 under .wrongstack/memories/, with typed knowledge, anchors to files/symbols/commands/commits, a knowledge graph, and auto-injection into context each turn. -- evidence: [README.md#L355-L362](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L355-L362), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144), [README.md#L364-L368](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L364-L368)
- orchestration (1 claim(s)):
  - [observation/documented] A Director-led specialist fleet fans out subagents, each isolated with its own budget and JSONL transcript, coordinated over a project-wide mailbox with typed messages and live presence. -- evidence: [README.md#L322-L325](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L322-L325), [README.md#L343-L351](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L343-L351), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144)
- tools-permissions (2 claim(s)):
  - [observation/documented] Every tool call passes a permission policy; project-root containment cannot be overridden by YOLO, absolute denies remain enforced, and destructive shell actions stay confirmable unless destructive YOLO is explicitly enabled. -- evidence: [docs/architecture.md#L140-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L140-L144), [README.md#L481-L483](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L481-L483), [README.md#L155-L165](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L155-L165)
More evidence: [full detail](wrongstack.detail.md)

Metadata and full claim list: [full detail](wrongstack.detail.md)
Human notes ([notes](wrongstack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
