# construct-worlds/construct

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit cf75b7398c78 @ c959755ce3b13c69

## Summary (orientation draft, not independently verified)

The snapshot shows construct, a Rust terminal-native agent fleet manager with a daemon/client split, multi-harness adapters, ACP/MCP interfaces, and contributor workflow rules in AGENTS.md. No evaluation or benchmark evidence is present.

## Source coverage

Source coverage (partial): 3 of 23 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Construct is a single Rust binary that includes a TUI, control CLI, daemon, ACP stdio server, an internal MCP bridge, and harness adapters. -- evidence: [README.md#L1-L11](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L1-L11), [README.md#L197-L200](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L197-L200)
  - [observation/documented] The daemon owns sessions, persists state, and exposes the local IPC socket used by clients; lifecycle helpers include daemon start/stop/restart with session-safe stop variants. -- evidence: [README.md#L143-L149](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L143-L149), [README.md#L140-L141](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L140-L141)
- design-choices (2 claim(s)):
  - [observation/documented] Sessions live in the daemon rather than the terminal, so SSH drops or laptop sleep do not stop agents, and users can reattach with scrollback intact. -- evidence: [README.md#L25-L32](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L25-L32)
  - [observation/documented] Lineage lets sessions branch like ideas: a session can be forked for a parallel attempt, including cross-harness forks, and results merged back. -- evidence: [README.md#L25-L32](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L25-L32)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: all code changes go through a branch, git worktree under .claude/worktrees, and a PR, with no direct pushes to main and no Co-Authored-By: Claude trailers. -- evidence: [AGENTS.md#L5-L5](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L5-L5), [AGENTS.md#L7-L18](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L7-L18)
  - [observation/documented] Repository development practice: durable design decisions are recorded as focused spec files in specs/ named NNNN-title-kebab-case.md with status, date, area, scope, decision, reason, and consequences sections. -- evidence: [AGENTS.md#L117-L120](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L117-L120), [AGENTS.md#L106-L110](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L106-L110), [AGENTS.md#L104-L104](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/AGENTS.md#L104-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The harness adapter protocol uses separate adapter processes speaking JSON-RPC over stdio, so new tools can plug in without changing the daemon. -- evidence: [README.md#L57-L59](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L57-L59)
  - [observation/documented] `construct acp` runs an Agent Client Protocol stdio server that auto-starts the daemon if needed and maps ACP session lifecycle calls onto daemon sessions, with --harness/--model/--cwd defaults. -- evidence: [README.md#L176-L177](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L176-L177), [README.md#L183-L185](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L183-L185)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Construct wraps CLIs already on the machine; users must install and authenticate harnesses such as codex, claude, opencode, agy, grok, muse, and prime-agent, while smith is built in. -- evidence: [README.md#L69-L81](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L69-L81), [README.md#L65-L67](https://github.com/construct-worlds/construct/blob/cf75b7398c784566b7003d7f63253be1b88d9186/README.md#L65-L67)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](construct.detail.md)

Metadata and full claim list: [full detail](construct.detail.md)
Human notes ([notes](construct.notes.md), never overwritten by build)

[Back to map index](../../index.md)
