---
access: public
aliases: []
claim_ids:
- clm_414f7631e6713b6e127c4c177ce42ce772f96d6e0f9c68ed052f659428faf56f
- clm_5c83388b27e89bed3c1533bf498fb5ca502c4fb975f810dc990e674b496010e5
- clm_5fa01145d448042d5b1e6d53cc05cd02db24926025b16bd674ca2405c0fb0666
- clm_7c8f0dc080f0b5730216a9b8bee7511fe782c97ecff68892721ed228073d1753
- clm_9bdcbe211c84c42942a1f6a9cb86971d33f564fbf9a983ae2d64c0c5d4fc8711
- clm_b1ceb97a8839df933eaa2e9813f147d431c2a3f32e37db5e922738250ae98434
- clm_dd39cf4d5b9324b3e266cc5904641b6b379bc2951c4d219f1d517f03e08ee514
- clm_e09f7fa66afb0e913115a56795f5958808d3298a9a79943f2c0cc936cf70e5c1
- clm_e2aa800e73da93d1f2bbf0763a8970b3e1279af2bb7299f0df078b35fc38d5d3
- clm_e558d7f83a46d596e6e8efbc5b20af221c95d2d6413a304bf040a1da84c4934f
maturity: draft
page_id: pg_4f00ea5538d25eb9b3290e2f14272a67
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf4d289a92335ee7aae24c962c367c78
title: tiann/hapi/README.md @ de6c9dee2032
updated_at: '2026-09-14T03:18:52Z'
---

# tiann/hapi/README.md @ de6c9dee2032

<!-- rcw:begin owner=source:src_bf4d289a92335ee7aae24c962c367c78 block=evidence -->
- The CLI supports starting an agent directly with `hapi <agent> [options]` (e.g. `hapi claude`), and scripts must specify the agent explicitly; `hapi --help` lists commands and supported agents. [@claim:clm_414f7631e6713b6e127c4c177ce42ce772f96d6e0f9c68ed052f659428faf56f]
- The hub displays a URL and two QR codes for opening the web UI or pairing a native companion app. [@claim:clm_5c83388b27e89bed3c1533bf498fb5ca502c4fb975f810dc990e674b496010e5]
- Building from source requires Bun 1.4.0, with `bun install` and `bun run build:single-exe` as the documented build steps. [@claim:clm_5fa01145d448042d5b1e6d53cc05cd02db24926025b16bd674ca2405c0fb0666]
- HAPI positions itself as a local-first alternative to Happy, wrapping the user's existing AI agent rather than replacing it, keeping the same terminal experience. [@claim:clm_7c8f0dc080f0b5730216a9b8bee7511fe782c97ecff68892721ed228073d1753]
- HAPI lets users run sessions of agents such as Claude Code, Codex, Cursor Agent, Grok Build, OpenCode, Kimi, Copilot, Antigravity, Pi, and DeepSeek Harness, controlled remotely via iOS/Android apps, Web/PWA, or a Telegram Mini App. [@claim:clm_9bdcbe211c84c42942a1f6a9cb86971d33f564fbf9a983ae2d64c0c5d4fc8711]
- Shared Codex sessions let users work with Codex from terminal and phone simultaneously, requiring Codex 0.154.0 or newer. [@claim:clm_b1ceb97a8839df933eaa2e9813f147d431c2a3f32e37db5e922738250ae98434]
- The relay uses WireGuard plus TLS for end-to-end encryption, with data encrypted from the user's device to their machine; self-hosted options like Cloudflare Tunnel and Tailscale are documented. [@claim:clm_dd39cf4d5b9324b3e266cc5904641b6b379bc2951c4d219f1d517f03e08ee514]
- A workspace browser feature is opt-in via one or more `hapi runner start --workspace-root <path>` flags, allowing scoped file-tree browsing and session starts in allowed subdirectories. [@claim:clm_e09f7fa66afb0e913115a56795f5958808d3298a9a79943f2c0cc936cf70e5c1]
- The repository includes SwiftUI/UIKit and Kotlin Compose native clients offering chat, approvals, session creation, files, dictation, and push notifications, with a documented client protocol contract. [@claim:clm_e2aa800e73da93d1f2bbf0763a8970b3e1279af2bb7299f0df078b35fc38d5d3]
- Running `npx @twsxtd/hapi hub --relay` starts a hub with an E2E-encrypted relay, and `hapi server` remains supported as an alias for the hub command. [@claim:clm_e558d7f83a46d596e6e8efbc5b20af221c95d2d6413a304bf040a1da84c4934f]
<!-- rcw:end owner=source:src_bf4d289a92335ee7aae24c962c367c78 block=evidence -->

## Researcher notes

