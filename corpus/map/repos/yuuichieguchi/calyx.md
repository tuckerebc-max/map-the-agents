# yuuichieguchi/calyx

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8415801ce661 @ 8b35c2344eef19d5

## Summary (orientation draft, not independently verified)

Calyx is a native macOS terminal app for running and supervising multiple coding agents in parallel, with an approval inbox, agent status sidebar, MCP-based agent IPC, LSP proxy, browser automation, and persistent sessions. The README documents product features, build steps, and a no-external-PRs contribution policy.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Calyx is a native macOS terminal for running and supervising coding agents (Claude Code, Codex, OpenCode, Hermes, Grok, pi) in parallel, with an approval inbox, live status, persistent sessions, and inline diff review. -- evidence: [README.md#L5-L5](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L5-L5)
- components (3 claim(s)):
  - [observation/documented] An Agents Sidebar shows each connected agent as working, blocked, idle, or done, with unread badges, click-to-focus navigation, and expandable subagent rows for CLIs that report them. -- evidence: [README.md#L34-L34](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L34-L34), [README.md#L52-L58](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L52-L58)
  - [observation/documented] A Git sidebar shows working changes, staging state, commit graph, branch visualization, and inline diffs per repository, including linked worktrees and submodules, with per-line diff comments submittable to agent panes. -- evidence: [README.md#L42-L42](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L42-L42), [README.md#L62-L66](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L62-L66)
- design-choices (1 claim(s)):
  - [observation/documented] Architecture: AppKit handles window/tab/focus management with SwiftUI rendering bridged via NSHostingView; all ghostty C API calls go through a GhosttyFFI enum and @MainActor is enforced on UI and model code. -- evidence: [README.md#L250-L252](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L250-L252), [README.md#L248-L248](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L248-L248)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: external pull requests are not accepted and are closed automatically without review; bug reports and feature ideas go through GitHub Issues. -- evidence: [CONTRIBUTING.md#L5-L5](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/CONTRIBUTING.md#L5-L5), [CONTRIBUTING.md#L3-L3](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/CONTRIBUTING.md#L3-L3), [README.md#L258-L258](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L258-L258)
  - [observation/documented] Repository development practice: building requires macOS 26+, Xcode 26+, Zig matching ghostty's build.zig.zon, and XcodeGen; clone with submodules, build the GhosttyKit xcframework with zig, then generate the Xcode project and build with xcodebuild. -- evidence: [README.md#L221-L224](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L221-L224), [README.md#L242-L244](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L242-L244), [README.md#L234-L236](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L234-L236), [README.md#L230-L231](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L230-L231)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Calyx exposes panes, commands, captured output, browser tabs, language servers, and peer agents to agents through MCP and a bundled CLI. -- evidence: [README.md#L46-L46](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L46-L46)
  - [observation/documented] The AI Agent IPC MCP server offers tools register_peer, list_peers, send_message, broadcast, receive_messages, and get_peer_status; receive_messages deletes messages on delivery so each is delivered once. -- evidence: [README.md#L169-L169](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L169-L169)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The approval inbox is opt-in via Settings; nothing is automatically approved unless the user separately opts in, and cockpit tools like pane_run and pane_send_keys are approval-gated. -- evidence: [README.md#L38-L38](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L38-L38), [README.md#L171-L171](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L171-L171)
More evidence: [full detail](calyx.detail.md)

Metadata and full claim list: [full detail](calyx.detail.md)
Human notes ([notes](calyx.notes.md), never overwritten by build)

[Back to map index](../../index.md)
