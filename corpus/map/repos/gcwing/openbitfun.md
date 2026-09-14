# gcwing/openbitfun

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: gcwing/bitfun (github id 1147866277).
Latest snapshot: commit 32b20c5b291d @ 8a36a510244d7500

## Summary (orientation draft, not independently verified)

The snapshot is the README, contributor guides (AGENTS-CN.md, CONTRIBUTING_CN.md), and an SDLC-harness design doc for OpenBitFun, an open-source desktop AI-agent workspace built on a Rust runtime with a React/TypeScript frontend. Evidence supports product claims about its harness modes, multi-device/remote architecture, memory/session handling, and a reported DeepSWE benchmark, plus extensive contributor workflow rules. Evidence coverage: 154 of 226 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 146 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 24 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

24 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] OpenBitFun is described as an open-source desktop workspace for AI agents combining a Rust Agent Runtime, an Agent Harness, and a desktop experience. -- evidence: [README.md#L11-L11](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L11-L11)
  - [observation/documented] Mini Apps pair a dedicated interface with an agent conversation, can be built by describing needs to the agent, and can be installed, reused, or shared via a marketplace. -- evidence: [README.md#L65-L65](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L65-L65), [README.md#L61-L61](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L61-L61), [README.md#L63-L63](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L63-L63)
- design-choices (5 claim(s)):
  - [observation/documented] The Agent Harness offers four working modes: Minimal (direct collaboration), Standard (multi-step tasks), Ultimate (delegating work across agents), and Creative (building Mini Apps and extending the interface). -- evidence: [README.md#L29-L29](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L29-L29), [README.md#L33-L38](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L33-L38)
  - [observation/documented] The architecture keeps product logic platform-independent and exposes capabilities through platform adapter layers; shared core must avoid host APIs like Tauri's AppHandle in favor of shared abstractions. -- evidence: [AGENTS-CN.md#L7-L7](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L7-L7), [CONTRIBUTING_CN.md#L84-L90](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L84-L90), [AGENTS-CN.md#L127-L129](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L127-L129)
- workflows (7 claim(s)):
  - [observation/documented] Repository development practice: contributors run `pnpm install` and `pnpm run desktop:dev` for full hot reload (Vite HMR plus automatic Rust rebuild), with a lighter `desktop:preview:debug` mode that reuses a prebuilt binary. -- evidence: [CONTRIBUTING_CN.md#L70-L70](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L70-L70), [AGENTS-CN.md#L52-L53](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/AGENTS-CN.md#L52-L53), [README.md#L125-L128](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L125-L128)
  - [observation/documented] Repository development practice: PRs go directly to the `main` branch, should use Conventional Commits-style titles, stay small and focused, and AI-assisted output must be declared with its testing level. -- evidence: [CONTRIBUTING_CN.md#L124-L129](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L124-L129), [CONTRIBUTING_CN.md#L150-L150](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L150-L150), [CONTRIBUTING_CN.md#L133-L133](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L133-L133), [CONTRIBUTING_CN.md#L146-L146](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L146-L146), [CONTRIBUTING_CN.md#L122-L122](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/CONTRIBUTING_CN.md#L122-L122)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product supports connecting tools via MCP, turning repeatable processes into Skills, customizing task execution with Hooks, and installing skins or modifying UI, tools, and runtime source. -- evidence: [README.md#L71-L73](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L71-L73)
  - [observation/documented] Users can work over SSH on remote hosts, jump hosts, or containers, with files, commands, and agent execution in the target environment; the desktop app and CLI share core execution capabilities. -- evidence: [README.md#L53-L53](https://github.com/GCWing/OpenBitFun/blob/32b20c5b291d0e281b3920c84606e646e0e3524a/README.md#L53-L53)
- memory-state (1 claim(s)):
More evidence: [full detail](openbitfun.detail.md)

Metadata and full claim list: [full detail](openbitfun.detail.md)
Human notes ([notes](openbitfun.notes.md), never overwritten by build)

[Back to map index](../../index.md)
