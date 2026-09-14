# minghinmatthewlam/pi-gui

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit eb9a7380705d @ 337c0a03359906f9

## Summary (orientation draft, not independently verified)

pi-gui is an Electron desktop UI shell around the pi coding agent, offering threaded session timelines, git worktrees, an integrated terminal, diff viewing, and multi-agent orchestration, with pi's JSONL session files as the source of truth. Evidence is README plus contributor instructions; no code slices are present.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] pi-gui is a Codex-style desktop app for the pi coding agent, in public beta for macOS (Apple Silicon) and Linux (AppImage). -- evidence: [README.md#L52-L52](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L52-L52), [README.md#L3-L3](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] The Electron app is split into a React renderer, a narrow preload IPC bridge, and a Node main process handling windowing, session supervision, worktrees, PTYs, notifications, and persistence. -- evidence: [README.md#L90-L91](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L90-L91), [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104)
  - [observation/documented] Supporting packages include pi-sdk-driver (a thin adapter to the pi coding agent), session-driver (shared session driver types), and catalogs (workspace/session catalog state). -- evidence: [README.md#L145-L149](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L145-L149), [README.md#L106-L107](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L106-L107), [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104)
- design-choices (1 claim(s)):
  - [observation/documented] The app is a UI shell around @earendil-works/pi-coding-agent rather than a separate agent runtime; session management, auth setup, and agent execution run through upstream pi. -- evidence: [README.md#L9-L14](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L9-L14)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors use Node 20+ with pnpm via corepack, and run pnpm dev/build/typecheck/lint/test from the repo root; desktop E2E tests use a Playwright+Electron harness split into lanes, with the core lane run by default. -- evidence: [README.md#L132-L134](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L132-L134), [README.md#L111-L112](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L111-L112), [README.md#L129-L130](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L129-L130), [README.md#L121-L127](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L121-L127)
  - [observation/documented] Repository development practice: AGENTS.md instructs defining success criteria before coding, planning verification with the self-test skill, committing in small focused checkpoints, and running simplify before closing non-trivial work. -- evidence: [AGENTS.md#L6-L10](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/AGENTS.md#L6-L10)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The renderer communicates with the main process only through a typed IPC surface exposed by the preload bridge, with no broad Node access granted to the renderer. -- evidence: [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104)
  - [observation/documented] Features include a threaded timeline with collapsible tool calls, an integrated node-pty terminal, an inline diff viewer toggled with Cmd/Ctrl+D, @-file mentions, image attachments, themes, and OS notifications when runs finish. -- evidence: [README.md#L32-L48](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L32-L48)
- memory-state (1 claim(s)):
  - [observation/documented] pi persists each session as a JSONL transcript on disk, and pi-gui reads those files as the authoritative record for closed sessions instead of keeping a divergent copy. -- evidence: [README.md#L93-L104](https://github.com/minghinmatthewlam/pi-gui/blob/eb9a7380705dffad36db3efa771ee825aafbef6f/README.md#L93-L104)
- orchestration (1 claim(s)):
More evidence: [full detail](pi-gui.detail.md)

Metadata and full claim list: [full detail](pi-gui.detail.md)
Human notes ([notes](pi-gui.notes.md), never overwritten by build)

[Back to map index](../../index.md)
