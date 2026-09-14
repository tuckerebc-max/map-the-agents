# exqqstar/exagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d9adbbd6f18a @ 7e7049df465467e0

## Summary (orientation draft, not independently verified)

ExAgent is a local desktop agent workbench (Rust runtime, Tauri/React GUI) with durable sessions, approval-gated tools, memory, goals, subagents, MCP tools, and workflows; evidence is documentation-only, with no code slices in the snapshot.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] ExAgent is a desktop-first agent workbench with a Rust runtime and Tauri/React GUI, aimed at long-running coding work in local projects with resumable sessions. -- evidence: [README.md#L21-L24](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L21-L24)
- components (1 claim(s)):
  - [observation/documented] Each thread runs behind an actor-backed ThreadRuntime that serializes turns while streaming snapshots, status, and events back to the GUI. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109)
- design-choices (2 claim(s)):
  - [observation/documented] The desktop UI uses a restrained neutral OKLCH-token palette with a semantic primary accent, a 4px spacing rhythm, and a sidebar/chat/inspector layout that collapses responsively below 1200px. -- evidence: [DESIGN.md#L13-L13](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L13-L13), [DESIGN.md#L92-L94](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L92-L94), [DESIGN.md#L11-L11](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L11-L11), [DESIGN.md#L98-L101](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L98-L101), [DESIGN.md#L86-L88](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L86-L88)
  - [observation/documented] The frontend uses shadcn/ui (new-york style, Radix primitives) as its component source system, with product components kept separate from low-level UI primitives. -- evidence: [DESIGN.md#L107-L110](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L107-L110), [DESIGN.md#L114-L119](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/DESIGN.md#L114-L119)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run npm ci, tauri:dev, test, and build commands, plus cargo test, fmt, clippy, and cargo deny checks for verification. -- evidence: [README.md#L124-L130](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L124-L130), [README.md#L115-L120](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L115-L120)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The model layer normalizes provider-specific APIs into internal conversation, tool-call, multimodal, reasoning, and streaming types. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109)
  - [observation/documented] A typed app-server boundary exposes the local Rust runtime to the desktop; the Tauri shell stays project-aware while the runtime owns thread execution, model calls, tools, state, and live events. -- evidence: [README.md#L86-L88](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L86-L88)
- memory-state (2 claim(s)):
  - [observation/documented] Local durability is append-first: each thread has a rollout.jsonl ledger, and IndexDb stores cross-thread indexes for projects, threads, goals, memory, and review state. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109)
  - [observation/documented] The memory system supports automatic prompt recall, explicit memory tools, candidate saves, local promote/archive/forget flows, and audit state. -- evidence: [README.md#L33-L40](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L33-L40), [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agent policy gates both tool visibility and execution; tool contracts live in src/tools while per-turn orchestration lives in src/runtime/tool. -- evidence: [README.md#L90-L109](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L90-L109)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project is dual-licensed MIT OR Apache-2.0, and Rust dependency license policy is enforced via cargo deny configured in deny.toml. -- evidence: [README.md#L193-L194](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/README.md#L193-L194), [THIRD_PARTY_NOTICES.md#L17-L19](https://github.com/exqqstar/ExAgent/blob/d9adbbd6f18ab53b3761eb7cbdb3cc6560f4b921/THIRD_PARTY_NOTICES.md#L17-L19)
- limitations (1 claim(s)):
More evidence: [full detail](exagent.detail.md)

Metadata and full claim list: [full detail](exagent.detail.md)
Human notes ([notes](exagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
