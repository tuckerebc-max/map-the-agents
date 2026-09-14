# lucianodiisouza/semaphore

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0632b3147987 @ 2d0f49ea8635d35c

## Summary (orientation draft, not independently verified)

Semaphore is an always-on-top floating traffic-light widget that signals when an AI coding agent is idle, thinking, or writing files, without switching windows. Light states are defined as green for idle/ready, yellow for thinking or running tools, and red for writing or editing files. Evidence coverage: 185 of 201 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Semaphore is an always-on-top floating traffic-light widget that signals when an AI coding agent is idle, thinking, or writing files, without switching windows. -- evidence: [README.md#L11-L11](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L11-L11), [README.md#L3-L3](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L3-L3)
  - [observation/documented] Light states are defined as green for idle/ready, yellow for thinking or running tools, and red for writing or editing files. -- evidence: [README.md#L5-L9](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L5-L9)
- components (3 claim(s)):
  - [observation/documented] The project comprises a sem-core library (state machine, session aggregation, IPC, config), a semctl CLI, a Tauri-based widget app, and a TypeScript/Vite frontend. -- evidence: [README.md#L325-L336](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L325-L336), [README.md#L291-L296](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L291-L296)
  - [observation/documented] sem-hook is a thin wrapper invoked by AI tool hooks that parses optional JSON from stdin for session identifiers and then calls semctl set. -- evidence: [README.md#L205-L205](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L205-L205)
- design-choices (2 claim(s)):
  - [observation/documented] The state machine tracks one entry per session ID and picks the highest-priority color with red over yellow over green; setting green removes the session. -- evidence: [README.md#L277-L281](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L277-L281), [README.md#L283-L283](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L283-L283)
  - [observation/documented] Hooks always exit 0 so they never block the agent, and the installer merges hook entries using a _semaphore marker without overwriting unrelated hooks. -- evidence: [README.md#L156-L156](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L156-L156), [README.md#L205-L205](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L205-L205)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building requires Rust stable, Node.js 20+, and npm (plus WebKit/GTK dev packages on Linux); tests run via cargo test and npm test (Vitest). -- evidence: [README.md#L378-L381](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L378-L381), [README.md#L348-L348](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L348-L348), [README.md#L344-L346](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L344-L346)
  - [observation/documented] Repository development practice: tagging a version (e.g. git tag v0.2.0 and pushing) triggers a GitHub Actions release workflow that builds macOS arm64/x64, Linux x64, and Windows x64 artifacts. -- evidence: [README.md#L387-L390](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L387-L390), [README.md#L385-L385](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L385-L385), [README.md#L392-L392](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L392-L392)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The semctl CLI supports set/status light control, install/uninstall of hooks, doctor diagnostics, and launch, and lives at ~/.semaphore/bin after install. -- evidence: [README.md#L162-L162](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L162-L162), [README.md#L190-L193](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L190-L193), [README.md#L181-L186](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L181-L186), [README.md#L175-L177](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L175-L177), [README.md#L166-L171](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L166-L171)
  - [observation/documented] IPC is newline-delimited JSON over a Unix socket ($XDG_RUNTIME_DIR/semaphore.sock or /tmp/semaphore-<uid>.sock) or the Windows named pipe \\.\pipe\semaphore, with set and status commands. -- evidence: [README.md#L313-L315](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L313-L315), [README.md#L300-L300](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L300-L300), [README.md#L302-L303](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L302-L303), [README.md#L307-L309](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L307-L309), [README.md#L319-L321](https://github.com/lucianodiisouza/semaphore/blob/0632b3147987e9d41cce3aa8145a7a79bddc7b41/README.md#L319-L321)
- memory-state (1 claim(s)):
More evidence: [full detail](semaphore.detail.md)

Metadata and full claim list: [full detail](semaphore.detail.md)
Human notes ([notes](semaphore.notes.md), never overwritten by build)

[Back to map index](../../index.md)
