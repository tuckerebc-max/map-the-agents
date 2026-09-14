---
access: public
aliases: []
claim_ids:
- clm_082fb5b31269dcbddacc35cf9e72974486d72f93a293a063e22a61500756edcd
- clm_3e1b96832e6506e7a62c205732b85f78cc5c21c2022cacc72feb660c4cc14547
- clm_47d4107dfde5c40e1fabdb13267b5f0d6c1f6ee6b7bbfdd9dd4a177f86e0492f
- clm_4fe1ee2828a8dd54ffdc4835c4e6e7d7afec27ab134d46c6778a2f9865f72b90
- clm_58118e66b9cdd82cfe274b076ab84c4f2078146c0307351b4fd3fb416757e0a8
- clm_5b3b5433c2b48c40bfd491696a0965a9ad702eab4ddace943cb84072138d513e
- clm_5f9ce24018cc75edd9deb13c9921776fbd31ff6592b58cd100a1138be9c84fb7
- clm_6abd789d7c4143b4e0caaa939e5f35d6046a9126e0cd0ef2f815090bdba1d4df
- clm_7ed2a853df3eaec0eaf7a08ea589d8face604ff2548673bd6e7d14920ee87c89
- clm_963e359ee9cecdd0a6126206d6b8d4316b952e002d4e41c54a025c89f094dedf
- clm_c020f1519a5e914fc2bece30e49ad0c67463d446fb129949d73266a50f681f14
maturity: draft
page_id: pg_adfb3c0adf1853eca87246252b75eccc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_77f076c532035df782321748248e8689
title: leox255/loopsy/README.md @ 73c165476279
updated_at: '2026-09-14T03:10:02Z'
---

# leox255/loopsy/README.md @ 73c165476279

<!-- rcw:begin owner=source:src_77f076c532035df782321748248e8689 block=evidence -->
- The repository is a pnpm monorepo with packages for shared protocol types, mDNS discovery, a Fastify daemon, a Cloudflare Worker relay, a deploy-relay npx CLI, the loopsy CLI, an MCP server, a dashboard, and a Flutter mobile app. [@claim:clm_082fb5b31269dcbddacc35cf9e72974486d72f93a293a063e22a61500756edcd]
- The daemon binds to 127.0.0.1 by default; LAN exposure for peer-to-peer is opt-in via `loopsy start --lan` or setting server.host to 0.0.0.0 in config. [@claim:clm_3e1b96832e6506e7a62c205732b85f78cc5c21c2022cacc72feb660c4cc14547]
- Phone control works by the daemon opening an outbound WebSocket to a Cloudflare Worker (Durable Object) that the phone also connects to; the Worker splices the two connections, requiring no port forwarding, public IP, or VPN. [@claim:clm_47d4107dfde5c40e1fabdb13267b5f0d6c1f6ee6b7bbfdd9dd4a177f86e0492f]
- Self-hosting the relay uses the @loopsy/deploy-relay npx CLI, which runs wrangler deploy against the user's Cloudflare account; Workers free tier and SQLite-backed Durable Objects are stated to cover personal use. [@claim:clm_4fe1ee2828a8dd54ffdc4835c4e6e7d7afec27ab134d46c6778a2f9865f72b90]
- When wired into an agent, the Loopsy MCP server exposes tools for peer listing, remote command execution, long-lived PTY sessions, file transfer, a shared key/value context store, messaging with ACKs, and read receipts. [@claim:clm_58118e66b9cdd82cfe274b076ab84c4f2078146c0307351b4fd3fb416757e0a8]
- State lives under ~/.loopsy/ in config.yaml, context.json (key-value store), peers.json, logs/audit.jsonl, and relay.json; the messaging protocol stores inbox, outbox, and ack entries as context keys with TTLs. [@claim:clm_5b3b5433c2b48c40bfd491696a0965a9ad702eab4ddace943cb84072138d513e]
- TLS terminates at the relay, so the relay operator can read and modify terminal traffic including passwords; end-to-end phone-daemon encryption is deferred to the v1.1 roadmap, and self-hosting is the recommended mitigation. [@claim:clm_5f9ce24018cc75edd9deb13c9921776fbd31ff6592b58cd100a1138be9c84fb7]
- Repository development practice: contributors build with pnpm install and pnpm build, and releases are tag-driven — pushing a v* tag publishes loopsy and @loopsy/deploy-relay to npm via OIDC Trusted Publisher with provenance attestations. [@claim:clm_6abd789d7c4143b4e0caaa939e5f35d6046a9126e0cd0ef2f815090bdba1d4df]
- Security design includes HMAC-signed pair tokens, SHA-256 hashing of secrets at rest, bearer tokens carried in Sec-WebSocket-Protocol headers rather than query strings, and constant-time bearer comparison. [@claim:clm_7ed2a853df3eaec0eaf7a08ea589d8face604ff2548673bd6e7d14920ee87c89]
- The loopsy CLI includes daemon lifecycle commands (init, start, stop, status, doctor, enable/disable), phone pairing and revocation, relay reconfiguration, log viewing, and API-key show/rotate commands. [@claim:clm_963e359ee9cecdd0a6126206d6b8d4316b952e002d4e41c54a025c89f094dedf]
- Per-session auto-approve lets a user opt in to skipping agent confirmation prompts; it defaults to off and enabling it the first time requires a macOS confirmation dialog (the user's password). [@claim:clm_c020f1519a5e914fc2bece30e49ad0c67463d446fb129949d73266a50f681f14]
<!-- rcw:end owner=source:src_77f076c532035df782321748248e8689 block=evidence -->

## Researcher notes

