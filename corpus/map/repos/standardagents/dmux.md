# standardagents/dmux

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8cb3d926631a @ 68485dfe5f603c6d

## Summary (orientation draft, not independently verified)

dmux manages multiple AI coding agents in parallel, giving each task a tmux pane backed by its own isolated git worktree and branch, with merge or GitHub PR actions to bring work back. The TUI exposes single-key shortcuts: n for a new worktree pane, t for a terminal pane, m for the pane menu, f for file browsing, s for settings, and q to quit, among others.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] dmux manages multiple AI coding agents in parallel, giving each task a tmux pane backed by its own isolated git worktree and branch, with merge or GitHub PR actions to bring work back. -- evidence: [README.md#L7-L10](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L7-L10), [README.md#L47-L47](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L47-L47)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Each pane is a full working copy in its own worktree so agents do not conflict; merging auto-commits, merges, and cleans up in one step. -- evidence: [README.md#L49-L60](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L49-L60), [README.md#L47-L47](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L47-L47)
  - [observation/documented] Branch handling defaults to automatic worktree/branch naming, but users can optionally pick a different base branch per pane or supply an explicit name, with agent-specific suffixes for multi-agent launches. -- evidence: [README.md#L66-L69](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L66-L69), [README.md#L64-L64](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L64-L64)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: maintainers use a 'dmux-on-dmux' loop via pnpm dev, and the recommended PR workflow runs pnpm run typecheck and pnpm run test before submitting. -- evidence: [AGENTS.md#L169-L172](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L169-L172), [AGENTS.md#L109-L109](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L109-L109), [AGENTS.md#L174-L177](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/AGENTS.md#L174-L177)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The TUI exposes single-key shortcuts: n for a new worktree pane, t for a terminal pane, m for the pane menu, f for file browsing, s for settings, and q to quit, among others. -- evidence: [README.md#L73-L86](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L73-L86)
  - [observation/documented] dmux supports launching many agent CLIs, including Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, pi, Cursor, Copilot, and Crush, with multi-select of several agents per prompt. -- evidence: [README.md#L49-L60](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L49-L60)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Runtime requirements are tmux 3.0+, Node.js 18+, Git 2.20+, at least one supported agent CLI, and optionally an inference provider key or Codex/Grok Build login for AI naming and analysis. -- evidence: [README.md#L90-L94](https://github.com/standardagents/dmux/blob/8cb3d926631a9349ab67f7ece41d218427ac7e24/README.md#L90-L94)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](dmux.detail.md)

Metadata and full claim list: [full detail](dmux.detail.md)
Human notes ([notes](dmux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
