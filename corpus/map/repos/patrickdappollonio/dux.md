# patrickdappollonio/dux

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 14e044d616d2 @ 9cf959f4d95c8dad

## Summary (orientation draft, not independently verified)

dux is a Rust terminal UI for running multiple AI coding agents in parallel, each in its own git worktree, with companion terminals, macros, git staging, and a command palette. Evidence is mostly README product documentation plus contributor instructions in CLAUDE.md.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] dux is a terminal UI that runs multiple AI coding agents side by side, each in its own git worktree, with companion terminals, macros, commit generation, and a command palette. -- evidence: [README.md#L7-L7](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L7-L7)
- components (2 claim(s)):
  - [observation/documented] The interface has three panes: projects and agent sessions on the left, the agent's live terminal output or diff in the center, and changed files, staging, and diffs on the right. -- evidence: [README.md#L81-L83](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L81-L83)
  - [observation/documented] Each agent gets companion terminal shells in the same worktree, and multiple companion terminals per agent are supported. -- evidence: [README.md#L179-L179](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L179-L179)
- design-choices (1 claim(s)):
  - [observation/documented] Agents run through a PTY like a normal shell, so CLIs such as Claude, Codex, or OpenCode behave as they would in a regular terminal, including MCP servers, hooks, and permission dialogs. -- evidence: [README.md#L19-L19](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L19-L19)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors verify changes with cargo fmt, cargo clippy --all-targets --all-features -- -D warnings (a CI gate on every PR), and cargo test, and every change should include unit tests. -- evidence: [CLAUDE.md#L155-L155](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L155-L155), [CLAUDE.md#L48-L49](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L48-L49), [CLAUDE.md#L149-L153](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L149-L153)
  - [observation/documented] Repository development practice: the src/app/ TUI is split into focused submodules (mod.rs, input.rs, render.rs, sessions.rs, workers.rs), and changes should stay scoped to the relevant submodule. -- evidence: [CLAUDE.md#L78-L78](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L78-L78), [CLAUDE.md#L80-L84](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L80-L84), [CLAUDE.md#L86-L86](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L86-L86), [CLAUDE.md#L136-L143](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L136-L143)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Any terminal command can be a provider via a TOML config entry with command, args, and optional resume_args; built-in defaults include Claude, Codex, and OpenCode, and adding a provider is config-only. -- evidence: [README.md#L91-L96](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L91-L96), [README.md#L89-L89](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L89-L89)
  - [observation/documented] Palette commands include change-agent-provider, change-default-provider, and change-project-default-provider for switching providers per worktree, globally, or per project, with resume_args reused when available. -- evidence: [README.md#L102-L102](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L102-L102), [README.md#L104-L106](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L104-L106)
- memory-state (1 claim(s)):
  - [observation/documented] Session state persists in sessions.sqlite3 alongside the config, and logs go to dux.log in the config directory with a configurable level and path. -- evidence: [CLAUDE.md#L57-L63](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L57-L63), [README.md#L283-L283](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L283-L283), [README.md#L285-L289](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L285-L289)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](dux.detail.md)

Metadata and full claim list: [full detail](dux.detail.md)
Human notes ([notes](dux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
