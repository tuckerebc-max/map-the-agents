# tlbx-ai/tlbx

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f4e926504190 @ 85ca0d4d0e4cf7cf

## Summary (orientation draft, not independently verified)

The snapshot is the README of tlbx (formerly MidTerm), a browser-based terminal multiplexer for running shells and coding agents persistently on a host, plus AGENTS.md/CLAUDE.md contributor instructions covering release workflows and design constraints. Product claims come from README documentation; contributor-facing rules are reported only as repository development practice.

## Source coverage

Source coverage (partial): 3 of 41 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture splits roles: the host runs tlbx and the user's tools, mthost runs terminals, mtagenthost runs Agent Controller sessions, and a browser client connects over HTTPS/WebSocket. -- evidence: [README.md#L123-L129](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L123-L129), [README.md#L145-L149](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L145-L149)
- design-choices (1 claim(s)):
  - [observation/documented] Sessions persist when the browser disconnects or the user switches devices, as long as the host stays awake and online; shutting down the host stops its processes. -- evidence: [README.md#L131-L131](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L131-L131), [README.md#L29-L29](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L29-L29)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md and CLAUDE.md instruct contributors that development happens on the dev branch, with main reserved for stable integration, and that release scripts (release-dev.ps1, promote.ps1, release.ps1) may only be run for the explicitly requested release path. -- evidence: [AGENTS.md#L19-L19](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L19-L19), [AGENTS.md#L30-L43](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L30-L43)
  - [observation/documented] Repository development practice: every release invocation must explicitly pass -TestCategories from a fixed set (assets, frontend, server, runtime, installers, dependencies, build, or all), and stable releases require all. -- evidence: [AGENTS.md#L8-L15](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L8-L15)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] tlbx offers two session types: a Terminal Session rendering the user's terminal with output retained on the host, and an Agent Controller Session rendering a conversation view with tool calls, code changes, questions and approval buttons. -- evidence: [README.md#L57-L60](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L57-L60)
  - [observation/documented] Agent Controller has built-in launch options for Codex, Grok Build, OpenCode, Gemini CLI and GitHub Copilot CLI, and compatible ACP agents can be added via acp-agents.json; Claude Code runs in a normal terminal session. -- evidence: [README.md#L84-L84](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L84-L84)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The mt helpers let agents send prompts, read terminal output, and inspect or control the app preview within the workspace. -- evidence: [README.md#L76-L82](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L76-L82)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] tlbx is built with .NET 10 Native AOT, TypeScript and xterm.js. -- evidence: [README.md#L151-L151](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L151-L151)
More evidence: [full detail](tlbx.detail.md)

Metadata and full claim list: [full detail](tlbx.detail.md)
Human notes ([notes](tlbx.notes.md), never overwritten by build)

[Back to map index](../../index.md)
