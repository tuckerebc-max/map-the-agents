# carloluisito/omnidesk

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 95f0b96dc802 @ 65711062c53336a3

## Summary (orientation draft, not independently verified)

README and CHANGELOG evidence describes OmniDesk, an Electron desktop terminal wrapper for AI coding CLIs (Claude Code, Codex) with multi-session, worktree, remote-access, and notification features; development/build instructions appear in the Development section. Evidence coverage: 127 of 221 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 2 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] OmniDesk is an Electron 28 desktop app using React 18 + TypeScript, xterm.js with node-pty for terminals, Tailwind CSS styling, and Vite with electron-builder for building. -- evidence: [README.md#L9-L9](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L9-L9), [README.md#L231-L238](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L231-L238)
  - [observation/documented] The architecture is a three-layer pattern per domain: managers in the Electron main process, hooks in the renderer, and shell components, connected via roughly 115 IPC methods through an auto-derived preload bridge. -- evidence: [README.md#L244-L244](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L244-L244), [README.md#L246-L260](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L246-L260)
- design-choices (2 claim(s)):
  - [observation/documented] The IPC contract file is treated as the single source of truth, auto-deriving channels, preload bridge methods, and TypeScript types; a provider abstraction (IProvider) decouples CLI specifics from session management. -- evidence: [README.md#L262-L262](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L262-L262)
  - [observation/documented] The project is local-first and telemetry-free: session data stays on the machine, and network calls are limited to Anthropic's quota API, GitHub update checks, configured git remotes, and a one-time consented Hugging Face voice-model download. -- evidence: [README.md#L300-L304](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L300-L304)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: development uses npm run electron:dev for hot-reload dev mode, npm test for the 1418-test Vitest suite, npm run test:e2e for Playwright E2E tests requiring a built app, and npm run test:coverage for coverage. -- evidence: [README.md#L292-L292](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L292-L292), [README.md#L283-L290](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L283-L290)
  - [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines and a Code of Conduct, with bug reports and feature requests via GitHub issue templates; the repo workflow requires worktree-per-task branching from an up-to-date main. -- evidence: [CHANGELOG.md#L90-L90](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/CHANGELOG.md#L90-L90), [README.md#L324-L324](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L324-L324), [README.md#L320-L322](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L320-L322)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The app exposes keyboard-driven interfaces: Ctrl/Cmd+K command palette, Ctrl/Cmd+J attention cockpit, Ctrl/Cmd+Shift+K repo switcher, Ctrl/Cmd+1/2 for Focus/Grid views, and Ctrl+Shift+Space for voice dictation. -- evidence: [README.md#L211-L225](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L211-L225)
  - [observation/documented] Remote access serves the same UI from a browser over a one-click managed Cloudflare tunnel, bound to 127.0.0.1 only with its own access token (cookie plus WebSocket check), off by default, with a QR sign-in and installable PWA. -- evidence: [README.md#L113-L119](https://github.com/carloluisito/omnidesk/blob/95f0b96dc8024677b02ca8ca7d4e92b2d66db788/README.md#L113-L119)
- memory-state (1 claim(s)):
More evidence: [full detail](omnidesk.detail.md)

Metadata and full claim list: [full detail](omnidesk.detail.md)
Human notes ([notes](omnidesk.notes.md), never overwritten by build)

[Back to map index](../../index.md)
