---
access: public
aliases: []
claim_ids:
- clm_109e8e5631ba526bcf34e3775c58f778e8c2d234534ec4604f0d5bd47bb18319
- clm_1da346edfde5449801f23c77c08e4e73ee4dbfe7122e19811a3f2e9ed8c70576
- clm_41a99956f6398e284c6cfef71be3e1e4b15a02d0bc7aa3eed7f252d475ceb0aa
- clm_513665df0e4f00cd3040a50ed51424803870a49ac3f762059ba1eaa21b19be34
- clm_5854007065684055c855d94df624dd9f0a36471a76945da39c1f8f84c88d5f4e
- clm_8cc1bb28d6c871b2542b614e9651fddef5099262425981457c7ffb8d3c5ed9a6
- clm_bff4e20a71f6a5f66d867ee2dca5609610bbbd44a0838e2939f4a5566eb9224a
- clm_ccfaa6b1b30b9bfe894db467e358a64958b1ba94f7988bdf7932aeca4e4677ec
- clm_d47ea68779a889a57e81b8bcbdb0c3ef7b2f3cba52bb6ebe5f0e8757089098b9
maturity: draft
page_id: pg_5faf4d39d6145c23a842397fa825ea79
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_db3f6c8c9d775f33b82f1e4cbb8cae21
title: JayCRL/MobileVC/README.md @ 8f9eb5a13f41
updated_at: '2026-09-14T02:07:05Z'
---

# JayCRL/MobileVC/README.md @ 8f9eb5a13f41

<!-- rcw:begin owner=source:src_db3f6c8c9d775f33b82f1e4cbb8cae21 block=evidence -->
- Flutter Web assets are embedded in the Go backend binary with shared web/mobile UI and state logic; `npm run sync:web` copies build output into `cmd/server/web/`. [@claim:clm_109e8e5631ba526bcf34e3775c58f778e8c2d234534ec4604f0d5bd47bb18319]
- The mobile client surfaces permission requests and Plan Mode handling for Claude/Codex, and recent updates added Codex sandbox mode settings with finer-grained permission control. [@claim:clm_1da346edfde5449801f23c77c08e4e73ee4dbfe7122e19811a3f2e9ed8c70576]
- Relay mode forwards only encrypted packets so the relay server cannot see plaintext; keys are exchanged out-of-band via QR scan, and a relay-only network exposure mode exists. [@claim:clm_41a99956f6398e284c6cfef71be3e1e4b15a02d0bc7aa3eed7f252d475ceb0aa]
- The Go server exposes `/ws`, `/healthz`, `/download`, and `/api/tts/synthesize`, and orchestrates sessions, permissions, files, logs, Skill/Memory, and ADB debugging. [@claim:clm_513665df0e4f00cd3040a50ed51424803870a49ac3f762059ba1eaa21b19be34]
- The product ships a CLI with `mobilevc start`, `status`, `logs` (with --follow), `config`, `stop`, and `public --relay` for relay connectivity. [@claim:clm_5854007065684055c855d94df624dd9f0a36471a76945da39c1f8f84c88d5f4e]
- The Flutter client entry is `mobile_vc/lib/main.dart`; root state is driven by `SessionController` and the home page `SessionHomePage` renders backend events. [@claim:clm_8cc1bb28d6c871b2542b614e9651fddef5099262425981457c7ffb8d3c5ed9a6]
- Badges indicate Go 1.25 and Flutter 3.41; the npm package `@justprove/mobilevc` (version 0.2.10) distributes prebuilt platform backend binaries. [@claim:clm_bff4e20a71f6a5f66d867ee2dca5609610bbbd44a0838e2939f4a5566eb9224a]
- The product lets users manage Skill / Memory / Session Context from the phone, and recent updates optimized the mobile Skill/Memory management entry and display experience. [@claim:clm_ccfaa6b1b30b9bfe894db467e358a64958b1ba94f7988bdf7932aeca4e4677ec]
- Architecture comprises a mobile browser/Flutter app, a Go server with WebSocket event stream, PTY/assistant runtime, ADB + WebRTC bridge, session store, and an optional ChatTTS sidecar. [@claim:clm_d47ea68779a889a57e81b8bcbdb0c3ef7b2f3cba52bb6ebe5f0e8757089098b9]
<!-- rcw:end owner=source:src_db3f6c8c9d775f33b82f1e4cbb8cae21 block=evidence -->

## Researcher notes

