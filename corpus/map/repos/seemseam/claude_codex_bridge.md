# seemseam/claude_codex_bridge

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 20ac0ec58c17 @ ac7d55089d5c9a56

## Summary (orientation draft, not independently verified)

The evidence is README-only for CCB v8.6.13, a multi-agent TUI that coordinates CLI coding agents (Codex, Claude, Gemini, etc.) with a background daemon, config UI, mobile remote control, and role packs. Claims below are documentation-based; no code or development-practice text is present. Evidence coverage: 147 of 267 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 771 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A background daemon keeps project state alive even after the foreground UI is closed, per the README's feature list. -- evidence: [README.md#L47-L53](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L47-L53)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Supported managed agents receive built-in ask, ccb-clear, ccb-compact, and ccb-diagnose control skills even when optional skill inheritance is disabled. -- evidence: [README.md#L305-L305](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L305-L305)
- interfaces (4 claim(s)):
  - [observation/documented] CCB is described as a lightweight multi-agent TUI that coordinates CLI agents such as Codex, Claude, and Gemini in visible, controllable workflows. -- evidence: [README.md#L5-L6](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L5-L6)
  - [observation/documented] The README badges list version 8.6.13, platforms Linux/macOS/WSL/Windows beta, and 16 CLI provider families. -- evidence: [README.md#L8-L12](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L8-L12)
- memory-state (1 claim(s)):
  - [observation/documented] .ccb/ccb_memory.md serves as the project-wide shared memory document for collaboration rules, constraints, and agent handoff conventions. -- evidence: [README.md#L307-L307](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L307-L307)
- orchestration (1 claim(s)):
  - [observation/documented] Agents can invoke /ask during workflow orchestration to delegate and hand off work, and users can type directly in any agent pane. -- evidence: [README.md#L221-L221](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L221-L221), [README.md#L215-L215](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L215-L215)
- tools-permissions (2 claim(s)):
  - [observation/documented] Project configuration executing tool-window commands or custom provider command templates requires exact external approval via ccb config approve-commands. -- evidence: [README.md#L406-L409](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L406-L409)
  - [observation/documented] The mobile gateway binds to loopback by default; LAN binding requires a specific private interface address, and remote access uses Tailscale Serve rather than Funnel. -- evidence: [README.md#L255-L259](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L255-L259)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The native Windows x64 beta requires Python 3.10+, WezTerm, Git Bash, and Herdr 0.8.0 or newer, with an install-local managed Python runtime. -- evidence: [README.md#L86-L90](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L86-L90)
- limitations (1 claim(s)):
  - [observation/documented] Release notes state that DeepSeek CLI, Z.ai, and DeepSeek Harness remain implemented but are no longer presented as current headline provider support. -- evidence: [README.md#L338-L341](https://github.com/SeemSeam/claude_codex_bridge/blob/20ac0ec58c17375bab2ce3bb75fa2efcc5bd8cf6/README.md#L338-L341)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](claude_codex_bridge.detail.md) for every claim.)

Metadata and full claim list: [full detail](claude_codex_bridge.detail.md)
Human notes ([notes](claude_codex_bridge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
