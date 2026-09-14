# jaycrl/mobilevc

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8f9eb5a13f41 @ 3de314f7245aeedf

## Summary (orientation draft, not independently verified)

MobileVC is a Go backend plus Flutter client that lets a phone control local Claude/Codex CLI sessions over LAN or an encrypted relay, distributed via npm with prebuilt binaries. Evidence covers architecture, CLI/HTTP interfaces, relay security design, session history handling, and dependencies; contributor-instruction-only claims were omitted per correction scope.

## Source coverage

Source coverage (partial): 3 of 41 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Architecture comprises a mobile browser/Flutter app, a Go server with WebSocket event stream, PTY/assistant runtime, ADB + WebRTC bridge, session store, and an optional ChatTTS sidecar. -- evidence: [README.md#L140-L151](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L140-L151)
  - [observation/documented] The Flutter client entry is `mobile_vc/lib/main.dart`; root state is driven by `SessionController` and the home page `SessionHomePage` renders backend events. -- evidence: [README.md#L161-L164](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L161-L164)
- design-choices (2 claim(s)):
  - [observation/documented] Relay mode forwards only encrypted packets so the relay server cannot see plaintext; keys are exchanged out-of-band via QR scan, and a relay-only network exposure mode exists. -- evidence: [README.md#L95-L95](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L95-L95), [README.md#L91-L93](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L91-L93)
  - [observation/documented] Flutter Web assets are embedded in the Go backend binary with shared web/mobile UI and state logic; `npm run sync:web` copies build output into `cmd/server/web/`. -- evidence: [CHANGELOG.md#L100-L101](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L100-L101), [README.md#L224-L234](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L224-L234), [CHANGELOG.md#L107-L108](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L107-L108)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The product lets users manage Skill / Memory / Session Context from the phone, and recent updates optimized the mobile Skill/Memory management entry and display experience. -- evidence: [README.md#L114-L122](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L114-L122), [CHANGELOG.md#L35-L37](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L35-L37), [README.md#L40-L45](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L40-L45)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships a CLI with `mobilevc start`, `status`, `logs` (with --follow), `config`, `stop`, and `public --relay` for relay connectivity. -- evidence: [README.md#L85-L87](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L85-L87), [README.md#L73-L79](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L73-L79), [README.md#L53-L56](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L53-L56)
  - [observation/documented] The Go server exposes `/ws`, `/healthz`, `/download`, and `/api/tts/synthesize`, and orchestrates sessions, permissions, files, logs, Skill/Memory, and ADB debugging. -- evidence: [README.md#L155-L157](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L155-L157)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions can be restored from native Claude CLI history mirrored from `~/.claude/projects/<cwd>/*.jsonl`, with missing assistant replies backfilled from that JSONL. -- evidence: [CHANGELOG.md#L95-L96](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L95-L96)
  - [observation/documented] Session history length is configurable with resumed history converged to that window; reconnect can resume a selected session via `session_resume` with client cursor/runtime state. -- evidence: [CHANGELOG.md#L13-L15](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L13-L15), [CHANGELOG.md#L75-L76](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L75-L76)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The mobile client surfaces permission requests and Plan Mode handling for Claude/Codex, and recent updates added Codex sandbox mode settings with finer-grained permission control. -- evidence: [CHANGELOG.md#L13-L15](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L13-L15), [README.md#L103-L108](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L103-L108), [README.md#L114-L122](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L114-L122), [README.md#L40-L45](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L40-L45)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](mobilevc.detail.md)

Metadata and full claim list: [full detail](mobilevc.detail.md)
Human notes ([notes](mobilevc.notes.md), never overwritten by build)

[Back to map index](../../index.md)
