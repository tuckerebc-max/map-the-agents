---
access: public
aliases: []
claim_ids:
- clm_18a7e7f62eecae052005e8ee7f6437bae63aca2c6beb93a38d4d6027c83440fd
- clm_1b0ca20ffdf79af0f570cfc76422ddf2c23e0b5f74647cd3983fd9de50ad20b7
- clm_38ba189317864945afe8c1d41cb03d4d03fa179bae3ce0d11de810b9b754496d
- clm_3ab328624b2f95a74a76b5c6f16456314774aac88a2ede622f236c238d2f2cc6
- clm_45dd7056130d09882cca1838a55ae14d96c23f2d76aad537f1fab23caa36cba0
- clm_4a6b5bcd7d94345e631ed06921e78a771c7af6fa484985289b04469997fc6340
- clm_54d1a8c542f6fc1c53662bb895bfdc1d229de4e5a4068bcffb3f5b2a8b86eaf2
- clm_6d00511d06a0790e4de2617a462177f4d28cd89472f34b6e6c1092f4f66bc45c
- clm_70494c6b379bdb0bd2eb145eeb4e30c2d4330a0c548f4f72b530f2eeb593eab0
- clm_874bc843f28ba695dcd5feb2c491b275a844395f747185bb0650c700608c102f
- clm_8ce1c36a01b02366afdc324ae26bd0a02a9424c21a966f7670075322b204ee98
maturity: draft
page_id: pg_49e3c68e636955a28dd16faa1505a955
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_113d32534a8d5bd295d4a96cbb95e77b
title: h5i-dev/h5i/MANUAL.md @ ec1a18cd4f2d
updated_at: '2026-09-14T03:56:26Z'
---

# h5i-dev/h5i/MANUAL.md @ ec1a18cd4f2d

<!-- rcw:begin owner=source:src_113d32534a8d5bd295d4a96cbb95e77b block=evidence -->
- Boxes are disposable environments holding code, agent, toolchain and optionally the browser session; box export produces a patch, report, receipt and timelines, and the agent has no direct host write path. [@claim:clm_18a7e7f62eecae052005e8ee7f6437bae63aca2c6beb93a38d4d6027c83440fd]
- Resident sessions in a box on Linux require a tier that keeps the engine alive; the supervised tier cannot hold a resident process because its seccomp-notify gate dies with the starting command. [@claim:clm_1b0ca20ffdf79af0f570cfc76422ddf2c23e0b5f74647cd3983fd9de50ad20b7]
- A session grants only the origin it was opened on; --allow adds named origins, loopback is reachable by default unless --no-loopback, and off-origin subresources are refused and logged. [@claim:clm_38ba189317864945afe8c1d41cb03d4d03fa179bae3ce0d11de810b9b754496d]
- By default a session runs unsandboxed on the host machine; --in places it in a box whose egress allowlist is enforced at a network boundary outside the engine. [@claim:clm_3ab328624b2f95a74a76b5c6f16456314774aac88a2ede622f236c238d2f2cc6]
- The manual states the browser is incomplete: Canvas, WebSockets, Workers and IndexedDB are absent, and of twenty SPAs measured, eighteen read usefully and one not at all. [@claim:clm_45dd7056130d09882cca1838a55ae14d96c23f2d76aad537f1fab23caa36cba0]
- The manual's command table lists groups including browser, box, box share, ui, runner, skill, plugin, websec, recon, join, and shell completions. [@claim:clm_4a6b5bcd7d94345e631ed06921e78a771c7af6fa484985289b04469997fc6340]
- Browser sessions are driven by verbs such as open, snapshot, click, type, extract, markdown, requests, audit, screenshot, reload, and close, with @ref handles identifying page elements. [@claim:clm_54d1a8c542f6fc1c53662bb895bfdc1d229de4e5a4068bcffb3f5b2a8b86eaf2]
- The engine is the HTTP client: every request is policy-checked and recorded before bytes move, and a fetch that cannot be recorded is refused, so the log is a decision record. [@claim:clm_6d00511d06a0790e4de2617a462177f4d28cd89472f34b6e6c1092f4f66bc45c]
- Verbs resolve a session via --session name or id, the H5I_BROWSER_SESSION variable, or the last-opened session; there is deliberately no single-live-session default. [@claim:clm_70494c6b379bdb0bd2eb145eeb4e30c2d4330a0c548f4f72b530f2eeb593eab0]
- Only the firefox-143-linux identity is currently supported; Chrome identities need client hints and WebGL capabilities the engine lacks, and identity consistency is explicitly not anonymity. [@claim:clm_874bc843f28ba695dcd5feb2c491b275a844395f747185bb0650c700608c102f]
- h5i is one Rust binary with no server, daemon, or SaaS; websec and recon are optional plugins shipped as separate archives and registered via h5i plugin install. [@claim:clm_8ce1c36a01b02366afdc324ae26bd0a02a9424c21a966f7670075322b204ee98]
<!-- rcw:end owner=source:src_113d32534a8d5bd295d4a96cbb95e77b block=evidence -->

## Researcher notes

