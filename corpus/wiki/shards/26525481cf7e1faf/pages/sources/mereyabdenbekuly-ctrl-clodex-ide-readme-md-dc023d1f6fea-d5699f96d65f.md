---
access: public
aliases: []
claim_ids:
- clm_346d9420e567e8df9696228e6c03cd42180b33b0f7400e81d7b8ffb2d79888b5
- clm_3e581500b5fb5d192bc065b594c5679b8a601c00b0de667063969c450efbccfd
- clm_6bc19c26e746317f4a238a0bbdb481969d549899f3d381e9ce6f513852ce9453
- clm_8311affde9b017729b618aabc6c510f0567c0cb2aefd5cd7a35fc7af50aac55b
- clm_876e99da5d5d2bf4d32c96adbaabfd78b0a33d987d6cf49d239801ccca143b63
- clm_87aed4c8803b90ee8a6ac432a2467a45d5f486b7340f891867a783f53e909054
- clm_87c09092df9f604100710dbd86db38a21217a182997f98e206cc284b578ea48b
- clm_91bdf3e14711c46a408005acb36dc4e4b9f6b695ad628d385fa74b12c5798d40
- clm_c8027d7cc54be23e63d3851f161a1a5e1516ceea039ca9ed22d0ff27e7578ac0
- clm_da57e40349fef1459d3346dc5f01fa6800175665a24cdad0f9e952324a7f6cde
- clm_e5c32bb22106681f850eeaf27cd60a2bac5714c6fdecefd4385eb2ff4451a6df
maturity: draft
page_id: pg_78698d91cb2158409773d5699f96d65f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d6e63ab21bcc5228be814dc529003ccd
title: mereyabdenbekuly-ctrl/clodex-ide/README.md @ dc023d1f6fea
updated_at: '2026-09-14T02:17:32Z'
---

# mereyabdenbekuly-ctrl/clodex-ide/README.md @ dc023d1f6fea

<!-- rcw:begin owner=source:src_d6e63ab21bcc5228be814dc529003ccd block=evidence -->
- Repository development practice: local setup involves cloning, enabling corepack pnpm 10.30.3, copying .env.example to .env and .env.dev, then building packages and starting apps/browser, never committing .env files or credentials. [@claim:clm_346d9420e567e8df9696228e6c03cd42180b33b0f7400e81d7b8ffb2d79888b5]
- The Community Observed 21 preview packages are unsigned or ad-hoc signed, not notarized, lack Authenticode on Windows and vendor signatures on Linux, so users are told to verify SHA-256 and keep OS protections enabled. [@claim:clm_3e581500b5fb5d192bc065b594c5679b8a601c00b0de667063969c450efbccfd]
- The project is licensed under GNU Affero General Public License v3.0, with third-party components keeping their original licenses and notices. [@claim:clm_6bc19c26e746317f4a238a0bbdb481969d549899f3d381e9ce6f513852ce9453]
- Building from source requires Node.js 22.23.1, pnpm 10.30.3, and Git, with pnpm activated via corepack and a frozen-lockfile install. [@claim:clm_8311affde9b017729b618aabc6c510f0567c0cb2aefd5cd7a35fc7af50aac55b]
- CLODEx is an open-source, local-first agentic IDE for long-running engineering work that keeps code, Git, terminal, browser, models, and MCP tools in one durable desktop workspace. [@claim:clm_876e99da5d5d2bf4d32c96adbaabfd78b0a33d987d6cf49d239801ccca143b63]
- CLODEx.xyz sign-in uses the system browser with an RFC 8252 loopback callback, state, and PKCE S256, and bearer tokens are not returned in the callback URL. [@claim:clm_87aed4c8803b90ee8a6ac432a2467a45d5f486b7340f891867a783f53e909054]
- The stated product principle is that model output is input, not authority; sensitive operations can require explicit approval and remain reviewable. [@claim:clm_87c09092df9f604100710dbd86db38a21217a182997f98e206cc284b578ea48b]
- CLODEx began as a modified version of the Stagewise codebase, diverging at upstream commit ef9d249f, and documents lineage, attribution obligations, and a reproducible diff against the upstream base. [@claim:clm_91bdf3e14711c46a408005acb36dc4e4b9f6b695ad628d385fa74b12c5798d40]
- Repository development practice: before opening a pull request, contributors run pnpm check, typecheck, test, and security:secrets, and commits must be DCO-signed with focused tests for changed behavior. [@claim:clm_c8027d7cc54be23e63d3851f161a1a5e1516ceea039ca9ed22d0ff27e7578ac0]
- No evidence in the provided slices describes an agent or task performance evaluation harness or benchmark results; the release evidence described covers packaging, checksums, and byte audits rather than agent behavior scoring. [@claim:clm_da57e40349fef1459d3346dc5f01fa6800175665a24cdad0f9e952324a7f6cde]
- The product offers searchable task history, workspace-aware context, restart recovery, and continued work across sessions, with session continuity and workspace snapshot services listed in the architecture. [@claim:clm_e5c32bb22106681f850eeaf27cd60a2bac5714c6fdecefd4385eb2ff4451a6df]
<!-- rcw:end owner=source:src_d6e63ab21bcc5228be814dc529003ccd block=evidence -->

## Researcher notes

