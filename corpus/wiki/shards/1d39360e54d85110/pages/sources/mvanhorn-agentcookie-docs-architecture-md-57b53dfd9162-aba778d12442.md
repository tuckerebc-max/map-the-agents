---
access: public
aliases: []
claim_ids:
- clm_217080b97abe02d053cebc2bc97c0b61f0e170fc479bf358fb0fbb352db7e033
- clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc
- clm_856e0652a55416bf71836e48d841e20d891b59ab0ea81d7d9fa4afa804896462
- clm_883b948f84a528007a60465948774ffebb85547487ba73c9af168c262550a91f
- clm_91834bd6d42db94bc7be4e4c04a3ffd9aa54c988570999df7e25a41d21e6b36b
- clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592
maturity: draft
page_id: pg_323b94f81e9159428ab1aba778d12442
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa0a3da2a74b5c549a74b52329b95a00
title: mvanhorn/agentcookie/docs/architecture.md @ 57b53dfd9162
updated_at: '2026-09-14T04:10:49Z'
---

# mvanhorn/agentcookie/docs/architecture.md @ 57b53dfd9162

<!-- rcw:begin owner=source:src_aa0a3da2a74b5c549a74b52329b95a00 block=evidence -->
- The architecture doc lays out Go packages including cmd/agentcookie (cobra CLI), internal/cli, internal/chrome, internal/transport, internal/config, internal/pairing, internal/keystore, internal/protocol, and internal/cdp. [@claim:clm_217080b97abe02d053cebc2bc97c0b61f0e170fc479bf358fb0fbb352db7e033]
- The product requires Tailscale and Chrome on both machines, and the Linux sink must bind a Tailscale 100.x address, refusing to start without the tailnet. [@claim:clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc]
- The sync protocol carries a versioned SyncEnvelope with a monotonic Sequence; the sink rejects wrong keys with 401, version mismatches with 400, and replays via an in-memory SequenceTracker with 409. [@claim:clm_856e0652a55416bf71836e48d841e20d891b59ab0ea81d7d9fa4afa804896462]
- On Linux the sink injects cookies directly into Chrome's in-memory store via the Chrome DevTools Protocol (Storage.setCookies) instead of rewriting Chrome's SQLite, and Chrome must be started with a remote-debugging port such as 9223. [@claim:clm_883b948f84a528007a60465948774ffebb85547487ba73c9af168c262550a91f]
- Cookies are sealed with AES-GCM using per-peer keys derived from an X25519 + HKDF pairing handshake in which the pairing code is mixed into the HKDF salt; key files are stored mode 0600. [@claim:clm_91834bd6d42db94bc7be4e4c04a3ffd9aa54c988570999df7e25a41d21e6b36b]
- On Linux, a missing blocklist.yaml or omitted policy field means the sink ships nothing (allowlist-empty) as a security default; sync-all requires an explicit blocklist policy with an empty domains list, described as an operator choice rather than the code default. [@claim:clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592]
<!-- rcw:end owner=source:src_aa0a3da2a74b5c549a74b52329b95a00 block=evidence -->

## Researcher notes

