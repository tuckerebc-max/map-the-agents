# jaycrl/mobilevc -- full detail

[Back to orientation](mobilevc.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jaycrl/mobilevc/8f9eb5a13f41bee177383776a50db8b868c5b989/3de314f7245aeedf.json](../../../wiki/dossiers/jaycrl/mobilevc/8f9eb5a13f41bee177383776a50db8b868c5b989/3de314f7245aeedf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Architecture comprises a mobile browser/Flutter app, a Go server with WebSocket event stream, PTY/assistant runtime, ADB + WebRTC bridge, session store, and an optional ChatTTS sidecar. -- evidence: [README.md#L140-L151](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L140-L151) (`clm_d47ea68779a889a57e81b8bcbdb0c3ef7b2f3cba52bb6ebe5f0e8757089098b9`)
- [observation/documented] The Flutter client entry is `mobile_vc/lib/main.dart`; root state is driven by `SessionController` and the home page `SessionHomePage` renders backend events. -- evidence: [README.md#L161-L164](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L161-L164) (`clm_8cc1bb28d6c871b2542b614e9651fddef5099262425981457c7ffb8d3c5ed9a6`)

## design-choices (2 claim(s))

- [observation/documented] Relay mode forwards only encrypted packets so the relay server cannot see plaintext; keys are exchanged out-of-band via QR scan, and a relay-only network exposure mode exists. -- evidence: [README.md#L95-L95](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L95-L95), [README.md#L91-L93](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L91-L93) (`clm_41a99956f6398e284c6cfef71be3e1e4b15a02d0bc7aa3eed7f252d475ceb0aa`)
- [observation/documented] Flutter Web assets are embedded in the Go backend binary with shared web/mobile UI and state logic; `npm run sync:web` copies build output into `cmd/server/web/`. -- evidence: [CHANGELOG.md#L100-L101](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L100-L101), [README.md#L224-L234](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L224-L234), [CHANGELOG.md#L107-L108](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L107-L108) (`clm_109e8e5631ba526bcf34e3775c58f778e8c2d234534ec4604f0d5bd47bb18319`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The product lets users manage Skill / Memory / Session Context from the phone, and recent updates optimized the mobile Skill/Memory management entry and display experience. -- evidence: [README.md#L114-L122](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L114-L122), [CHANGELOG.md#L35-L37](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L35-L37), [README.md#L40-L45](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L40-L45) (`clm_ccfaa6b1b30b9bfe894db467e358a64958b1ba94f7988bdf7932aeca4e4677ec`)

## interfaces (2 claim(s))

- [observation/documented] The product ships a CLI with `mobilevc start`, `status`, `logs` (with --follow), `config`, `stop`, and `public --relay` for relay connectivity. -- evidence: [README.md#L85-L87](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L85-L87), [README.md#L73-L79](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L73-L79), [README.md#L53-L56](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L53-L56) (`clm_5854007065684055c855d94df624dd9f0a36471a76945da39c1f8f84c88d5f4e`)
- [observation/documented] The Go server exposes `/ws`, `/healthz`, `/download`, and `/api/tts/synthesize`, and orchestrates sessions, permissions, files, logs, Skill/Memory, and ADB debugging. -- evidence: [README.md#L155-L157](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L155-L157) (`clm_513665df0e4f00cd3040a50ed51424803870a49ac3f762059ba1eaa21b19be34`)

## memory-state (2 claim(s))

- [observation/documented] Sessions can be restored from native Claude CLI history mirrored from `~/.claude/projects/<cwd>/*.jsonl`, with missing assistant replies backfilled from that JSONL. -- evidence: [CHANGELOG.md#L95-L96](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L95-L96) (`clm_60b605fa4e6a0de5dc4a5d6c568b7658afaed093fcd53cd03698c64c4017590d`)
- [observation/documented] Session history length is configurable with resumed history converged to that window; reconnect can resume a selected session via `session_resume` with client cursor/runtime state. -- evidence: [CHANGELOG.md#L13-L15](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L13-L15), [CHANGELOG.md#L75-L76](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L75-L76) (`clm_cc90637298acc50e9bd0367b221f2ecceac8272720a7eb1a4f01416c20a8d323`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The mobile client surfaces permission requests and Plan Mode handling for Claude/Codex, and recent updates added Codex sandbox mode settings with finer-grained permission control. -- evidence: [CHANGELOG.md#L13-L15](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L13-L15), [README.md#L103-L108](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L103-L108), [README.md#L114-L122](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L114-L122), [README.md#L40-L45](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L40-L45) (`clm_1da346edfde5449801f23c77c08e4e73ee4dbfe7122e19811a3f2e9ed8c70576`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Badges indicate Go 1.25 and Flutter 3.41; the npm package `@justprove/mobilevc` (version 0.2.10) distributes prebuilt platform backend binaries. -- evidence: [README.md#L224-L234](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L224-L234), [README.md#L15-L20](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/README.md#L15-L20), [CHANGELOG.md#L3-L3](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L3-L3) (`clm_bff4e20a71f6a5f66d867ee2dca5609610bbbd44a0838e2939f4a5566eb9224a`)
- [observation/documented] Firebase was removed as a dependency from the Web build while mobile push support, including iOS APNs, was retained. -- evidence: [CHANGELOG.md#L112-L113](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L112-L113), [CHANGELOG.md#L119-L120](https://github.com/JayCRL/MobileVC/blob/8f9eb5a13f41bee177383776a50db8b868c5b989/CHANGELOG.md#L119-L120) (`clm_61de1120ae6753d4517c66f1a20d8b122b42e8a2a2855a8a42728d6cc71f54f0`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

