# yoanwai/agent-manager

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0f40e31fb1ca @ 39eac2119f1af8d9

## Summary (orientation draft, not independently verified)

agent-manager is a Go terminal (TUI) workspace for running multiple AI coding agent CLIs side by side in persistent tmux sessions, with status detection, diff review, forking, and agent-to-agent spawning. Evidence covers product behavior from README/DESIGN plus contributor workflow instructions in AGENTS.md.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The product is a terminal workspace where Claude Code, Codex, OpenCode, Grok, Gemini CLI, Pi, Command Code, and Hermes Agent run side by side, each in its own persistent tmux session. -- evidence: [README.md#L36-L36](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L36-L36)
- design-choices (2 claim(s)):
  - [observation/documented] The tool is described as a thin layer over the user's installed CLIs: sessions launch the user's own tool with its login, config, and MCP servers intact. -- evidence: [README.md#L38-L38](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L38-L38)
  - [observation/documented] DESIGN.md specifies a terminal-native, keyboard-first, information-dense aesthetic: monospace-only type, semantic theme tokens instead of hard-coded colors, and status color always paired with a glyph or label. -- evidence: [DESIGN.md#L59-L59](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L59-L59), [DESIGN.md#L70-L70](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L70-L70), [DESIGN.md#L61-L64](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L61-L64), [DESIGN.md#L55-L55](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/DESIGN.md#L55-L55)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: tests must run as `env -u TMUX TMUX_TMPDIR=/tmp/amtest go test ./...` because the suite drives a real tmux server and a bare go test could hit the live socket; gofmt and go vet must be clean before finishing. -- evidence: [AGENTS.md#L21-L25](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L21-L25), [AGENTS.md#L34-L34](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L34-L34), [AGENTS.md#L27-L32](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L27-L32)
  - [observation/documented] Repository development practice: releases are cut locally with goreleaser from a clean worktree at the tag, with no release workflow in CI; AUR_KEY is required or the Arch package publish silently skips. -- evidence: [AGENTS.md#L48-L54](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L48-L54), [AGENTS.md#L56-L58](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L56-L58), [AGENTS.md#L45-L46](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/AGENTS.md#L45-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (7 claim(s)):
  - [observation/documented] Sessions show in one list with live status grouped into a foldable project tree; space sends a prompt into a session's pane or spawns a new agent in the selected group. -- evidence: [README.md#L40-L40](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L40-L40)
  - [observation/documented] ctrl+r opens a syntax-highlighted full-file diff of an agent's changes; line comments are sent back to the agent's pane as one review prompt when pressing C. -- evidence: [README.md#L40-L40](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L40-L40)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] An agent can spawn another agent, send it a message, and wait until it is done; every MCP-capable session carries those tools on launch. -- evidence: [README.md#L44-L44](https://github.com/YoanWai/agent-manager/blob/0f40e31fb1cab86e38748f8677cbf58e4029df69/README.md#L44-L44)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](agent-manager.detail.md)

Metadata and full claim list: [full detail](agent-manager.detail.md)
Human notes ([notes](agent-manager.notes.md), never overwritten by build)

[Back to map index](../../index.md)
