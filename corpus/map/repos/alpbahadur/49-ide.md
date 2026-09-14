# alpbahadur/49-ide

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: alpbahadur/49agents (github id 1168100167).
Latest snapshot: commit c8bfb5c0a355 @ 9e8ea4ce68281998

## Summary (orientation draft, not independently verified)

The repository ships 49 Agents IDE, a self-hosted 2D agentic IDE presenting terminals, agents, and machines on a zoomable canvas via a WSS relay architecture, with a macOS desktop app and BSL 1.1 licensing. Contributor-facing files (CLA, AGENTS.md, CLAUDE.md, CONTRIBUTING.md) document development practice only.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Terminals are real tmux sessions served via ttyd with ANSI color, scrollback, and the user's shell config, plus broadcast input to multiple terminals at once. -- evidence: [README.md#L94-L95](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L94-L95), [README.md#L111-L114](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L111-L114)
  - [observation/documented] A macOS desktop app is distributed as a .dmg on GitHub Releases, runs as a tray icon, is not notarized (requiring an xattr workaround), and offers in-app update checks. -- evidence: [README.md#L79-L79](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L79-L79), [README.md#L71-L71](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L71-L71), [README.md#L69-L69](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L69-L69), [README.md#L77-L77](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L77-L77)
- design-choices (1 claim(s)):
  - [observation/documented] The relay stores no terminal data server-side; terminal I/O is relayed, never persisted, and self-hosting keeps terminals and files on the user's machine. -- evidence: [README.md#L59-L62](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L59-L62), [README.md#L148-L151](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L148-L151), [README.md#L104-L107](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L104-L107)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: contributors must sign a CLA on their first PR by commenting a fixed statement, granting the organization copyright, patent, and relicensing rights, because the project is BSL 1.1 licensed. -- evidence: [CONTRIBUTING.md#L8-L11](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CONTRIBUTING.md#L8-L11), [CLA.md#L22-L26](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L22-L26), [CLA.md#L40-L48](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L40-L48), [CLA.md#L76-L77](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L76-L77), [CONTRIBUTING.md#L18-L19](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CONTRIBUTING.md#L18-L19), [CLA.md#L30-L36](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/CLA.md#L30-L36)
  - [observation/documented] Repository development practice: AGENTS.md mandates using the bd (beads) CLI for all issue tracking (bd ready/claim/close, --json flags, discovered-from links) and forbids markdown TODO lists or external trackers. -- evidence: [AGENTS.md#L166-L171](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L166-L171), [AGENTS.md#L183-L189](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L183-L189), [AGENTS.md#L111-L111](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/AGENTS.md#L111-L111)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is described as a 2D agentic IDE whose workspace is an infinite zoomable canvas of draggable, resizable panes with persistent layout, replacing terminal tabs. -- evidence: [README.md#L87-L90](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L87-L90), [README.md#L7-L7](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L7-L7)
  - [observation/documented] Setup uses a 49ctl CLI: './49ctl setup' for one-time interactive setup and './49ctl start' to launch the cloud server and agent, then the UI is served at localhost:1071 with no account or login. -- evidence: [README.md#L50-L55](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L50-L55), [README.md#L57-L57](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L57-L57)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Architecture: 49-agent processes on machines connect over WSS to a relay (self-hosted or 49agents.com), which browsers on phones, laptops, and tablets also connect to; each agent connects independently via WebSocket. -- evidence: [README.md#L132-L146](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L132-L146), [README.md#L120-L127](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L120-L127), [README.md#L148-L151](https://github.com/alpbahadur/49-IDE/blob/c8bfb5c0a3552264412e39cd9c12ced75627d735/README.md#L148-L151)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](49-ide.detail.md)

Metadata and full claim list: [full detail](49-ide.detail.md)
Human notes ([notes](49-ide.notes.md), never overwritten by build)

[Back to map index](../../index.md)
