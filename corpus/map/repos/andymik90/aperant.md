# andymik90/aperant

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 20250db069a8 @ 0c573f086089e8d9

## Summary (orientation draft, not independently verified)

The README describes a three-layer security model: bash commands run inside an OS sandbox, filesystem operations stay confined to the project directory, and a dynamic allowlist admits only commands approved for the detected project stack. The README states the current 2.x desktop app is in maintenance mode while a ground-up 3.0 rebuild happens in a separate repository, and that code pull requests against the present codebase are paused and will be closed.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 4 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

4 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to always target the develop branch rather than main for pull requests, and to avoid console.log in production code in favor of Sentry-based error tracking. -- evidence: [CLAUDE.md#L43-L43](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/CLAUDE.md#L43-L43), [CLAUDE.md#L41-L41](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/CLAUDE.md#L41-L41)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The README describes a three-layer security model: bash commands run inside an OS sandbox, filesystem operations stay confined to the project directory, and a dynamic allowlist admits only commands approved for the detected project stack. -- evidence: [README.md#L157-L159](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md#L157-L159), [README.md#L155-L155](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md#L155-L155)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Documented requirements for using the app are a Claude Pro or Max subscription, the Claude Code CLI, and a project already initialized as a git repository. -- evidence: [README.md#L78-L80](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md#L78-L80)
- limitations (1 claim(s)):
  - [observation/documented] The README states the current 2.x desktop app is in maintenance mode while a ground-up 3.0 rebuild happens in a separate repository, and that code pull requests against the present codebase are paused and will be closed. -- evidence: [README.md#L17-L28](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md#L17-L28), [README.md#L187-L187](https://github.com/AndyMik90/Aperant/blob/20250db069a849ab001ac6ab9e3e9779886ab9e2/README.md#L187-L187)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](aperant.detail.md).

Metadata and full claim list: [full detail](aperant.detail.md)
Human notes ([notes](aperant.notes.md), never overwritten by build)

[Back to map index](../../index.md)
