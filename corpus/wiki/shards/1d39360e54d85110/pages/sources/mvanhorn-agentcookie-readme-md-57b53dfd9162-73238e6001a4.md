---
access: public
aliases: []
claim_ids:
- clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc
- clm_6e5b51b9f28b3198359239f7bf0607ffac6d2ad00667c36b734e911c0270ef58
- clm_7256e87791e180d626c0c934abb3abb1ec3b4dc5357f284109e1efaad611ee31
- clm_883b948f84a528007a60465948774ffebb85547487ba73c9af168c262550a91f
- clm_8d6fc2d31418ac32fc0e08e547f64d2584594935ea06f01db111b7b5f0cddc09
- clm_91834bd6d42db94bc7be4e4c04a3ffd9aa54c988570999df7e25a41d21e6b36b
- clm_a4ebb241bef483db16875c3200ded1bc1161a8e5fda6c40278524e8292397151
- clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592
maturity: draft
page_id: pg_8f5381998bfc542ab3de73238e6001a4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e274ec2eb4135ca694d54c11b952f1f9
title: mvanhorn/agentcookie/README.md @ 57b53dfd9162
updated_at: '2026-09-14T04:10:49Z'
---

# mvanhorn/agentcookie/README.md @ 57b53dfd9162

<!-- rcw:begin owner=source:src_e274ec2eb4135ca694d54c11b952f1f9 block=evidence -->
- The product requires Tailscale and Chrome on both machines, and the Linux sink must bind a Tailscale 100.x address, refusing to start without the tailnet. [@claim:clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc]
- Chrome's DBSC binds Google/Workspace sessions to device keys, so copied cookies for such sites stop working within minutes; the documented workaround is signing the sink's Chrome into the same Google account locally. [@claim:clm_6e5b51b9f28b3198359239f7bf0607ffac6d2ad00667c36b734e911c0270ef58]
- Documented limits include a plaintext-at-rest sidecar at ~/.agentcookie/cookies-plain.db, a loopback-only CDP port that same-user processes can read, no live key rotation (wizard re-run required), and unread Linux extra-profile Chrome SQLite. [@claim:clm_7256e87791e180d626c0c934abb3abb1ec3b4dc5357f284109e1efaad611ee31]
- On Linux the sink injects cookies directly into Chrome's in-memory store via the Chrome DevTools Protocol (Storage.setCookies) instead of rewriting Chrome's SQLite, and Chrome must be started with a remote-debugging port such as 9223. [@claim:clm_883b948f84a528007a60465948774ffebb85547487ba73c9af168c262550a91f]
- Repository development practice: the README's working-today list cites 520+ unit tests across 26 packages, a repository test-suite figure rather than any agent-performance evaluation. [@claim:clm_8d6fc2d31418ac32fc0e08e547f64d2584594935ea06f01db111b7b5f0cddc09]
- Cookies are sealed with AES-GCM using per-peer keys derived from an X25519 + HKDF pairing handshake in which the pairing code is mixed into the HKDF salt; key files are stored mode 0600. [@claim:clm_91834bd6d42db94bc7be4e4c04a3ffd9aa54c988570999df7e25a41d21e6b36b]
- One source can fan out to multiple sinks, reading and filtering cookies once then sealing and POSTing to each sink with that sink's own paired key; an unreachable sink fails in isolation, and every sink receives the full cookie and secret set. [@claim:clm_a4ebb241bef483db16875c3200ded1bc1161a8e5fda6c40278524e8292397151]
- On Linux, a missing blocklist.yaml or omitted policy field means the sink ships nothing (allowlist-empty) as a security default; sync-all requires an explicit blocklist policy with an empty domains list, described as an operator choice rather than the code default. [@claim:clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592]
<!-- rcw:end owner=source:src_e274ec2eb4135ca694d54c11b952f1f9 block=evidence -->

## Researcher notes

