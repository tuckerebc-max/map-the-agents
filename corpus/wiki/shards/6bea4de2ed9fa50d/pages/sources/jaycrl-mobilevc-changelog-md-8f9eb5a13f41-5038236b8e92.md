---
access: public
aliases: []
claim_ids:
- clm_109e8e5631ba526bcf34e3775c58f778e8c2d234534ec4604f0d5bd47bb18319
- clm_1da346edfde5449801f23c77c08e4e73ee4dbfe7122e19811a3f2e9ed8c70576
- clm_60b605fa4e6a0de5dc4a5d6c568b7658afaed093fcd53cd03698c64c4017590d
- clm_61de1120ae6753d4517c66f1a20d8b122b42e8a2a2855a8a42728d6cc71f54f0
- clm_bff4e20a71f6a5f66d867ee2dca5609610bbbd44a0838e2939f4a5566eb9224a
- clm_cc90637298acc50e9bd0367b221f2ecceac8272720a7eb1a4f01416c20a8d323
- clm_ccfaa6b1b30b9bfe894db467e358a64958b1ba94f7988bdf7932aeca4e4677ec
maturity: draft
page_id: pg_f946c66e89d657f2be945038236b8e92
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cee28cc954ad5197a0b1851936c2fd32
title: JayCRL/MobileVC/CHANGELOG.md @ 8f9eb5a13f41
updated_at: '2026-09-14T02:07:05Z'
---

# JayCRL/MobileVC/CHANGELOG.md @ 8f9eb5a13f41

<!-- rcw:begin owner=source:src_cee28cc954ad5197a0b1851936c2fd32 block=evidence -->
- Flutter Web assets are embedded in the Go backend binary with shared web/mobile UI and state logic; `npm run sync:web` copies build output into `cmd/server/web/`. [@claim:clm_109e8e5631ba526bcf34e3775c58f778e8c2d234534ec4604f0d5bd47bb18319]
- The mobile client surfaces permission requests and Plan Mode handling for Claude/Codex, and recent updates added Codex sandbox mode settings with finer-grained permission control. [@claim:clm_1da346edfde5449801f23c77c08e4e73ee4dbfe7122e19811a3f2e9ed8c70576]
- Sessions can be restored from native Claude CLI history mirrored from `~/.claude/projects/<cwd>/*.jsonl`, with missing assistant replies backfilled from that JSONL. [@claim:clm_60b605fa4e6a0de5dc4a5d6c568b7658afaed093fcd53cd03698c64c4017590d]
- Firebase was removed as a dependency from the Web build while mobile push support, including iOS APNs, was retained. [@claim:clm_61de1120ae6753d4517c66f1a20d8b122b42e8a2a2855a8a42728d6cc71f54f0]
- Badges indicate Go 1.25 and Flutter 3.41; the npm package `@justprove/mobilevc` (version 0.2.10) distributes prebuilt platform backend binaries. [@claim:clm_bff4e20a71f6a5f66d867ee2dca5609610bbbd44a0838e2939f4a5566eb9224a]
- Session history length is configurable with resumed history converged to that window; reconnect can resume a selected session via `session_resume` with client cursor/runtime state. [@claim:clm_cc90637298acc50e9bd0367b221f2ecceac8272720a7eb1a4f01416c20a8d323]
- The product lets users manage Skill / Memory / Session Context from the phone, and recent updates optimized the mobile Skill/Memory management entry and display experience. [@claim:clm_ccfaa6b1b30b9bfe894db467e358a64958b1ba94f7988bdf7932aeca4e4677ec]
<!-- rcw:end owner=source:src_cee28cc954ad5197a0b1851936c2fd32 block=evidence -->

## Researcher notes

