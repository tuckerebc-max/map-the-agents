---
access: public
aliases: []
claim_ids:
- clm_6c84ee8add798f08a7ed95ba56f65344fd49176ca2362cb12c366dbcadea80c4
- clm_c70c1ca32d78f554c24a1a2ad80cb4101849d6686668fe0a8ad47c9895a27d56
- clm_f7c23209a3ab0f22735ca3e247b046d219f653cb2cd8c0dadf75f4ba8787cd7d
maturity: draft
page_id: pg_bbc4f99d2d82532483696205a64ea783
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f26e4333dde05645a1d409ce68f0408b
title: sudoprivacy/sudocode/README.md @ a67bb90f5c4b
updated_at: '2026-09-14T04:40:28Z'
---

# sudoprivacy/sudocode/README.md @ a67bb90f5c4b

<!-- rcw:begin owner=source:src_f26e4333dde05645a1d409ce68f0408b block=evidence -->
- Sudo Code positions itself as an agent unit, not an orchestrator: it plugs into a nexus-VFS `chat-with-me` mailbox primitive so humans, orchestrators, or peer agents over ACP can drive it. [@claim:clm_6c84ee8add798f08a7ed95ba56f65344fd49176ca2362cb12c366dbcadea80c4]
- One scode binary serves copilot, worker, or standalone roles depending on the FsBackend implementation: StdFsBackend (host std::fs), NexusVfsFsBackend (gRPC to remote kernel), or KernelFsBackend (in-process syscalls). [@claim:clm_c70c1ca32d78f554c24a1a2ad80cb4101849d6686668fe0a8ad47c9895a27d56]
- The project commits to inline-only terminal output (no alternate-screen TUI, no ratatui), local-first operation with zero telemetry by default, and semver stability with no forced auto-updates. [@claim:clm_f7c23209a3ab0f22735ca3e247b046d219f653cb2cd8c0dadf75f4ba8787cd7d]
<!-- rcw:end owner=source:src_f26e4333dde05645a1d409ce68f0408b block=evidence -->

## Researcher notes

