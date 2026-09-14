---
access: public
aliases: []
claim_ids:
- clm_107a38b861461958cba9f3aa17a9dde21b799842df31b40e75f5cc4fc6f6b501
- clm_4d145a2382c6e85acbd2fee2d0cfe35c649fbc5b053123a6b15dc51bb09af396
- clm_9215fdb78259aba7db133f138b162abff61b43d56b8ac1e817e2f0840aca51b3
- clm_a45064f0cf2a7e9b1dc3fa3829cff1c3b33fb0d7f0d68672338cbf300d4a2bb7
- clm_e958c0fbbe5be228c6ca2ed11c36fa5639a2e866096bfc784b7347875f5cce71
maturity: draft
page_id: pg_598be510e71d52cd8a2eb4cf9555ffb8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c04af4a5fae153ada087f2de349c8d33
title: esengine/DeepSeek-Reasonix/README.md @ 8679e1f0b614
updated_at: '2026-09-14T02:00:56Z'
---

# esengine/DeepSeek-Reasonix/README.md @ 8679e1f0b614

<!-- rcw:begin owner=source:src_c04af4a5fae153ada087f2de349c8d33 block=evidence -->
- Building the CLI requires Go 1.26+ with a pinned toolchain directive; the desktop build additionally requires Node 24+ and pnpm 10 for the frontend and Electron shell. [@claim:clm_107a38b861461958cba9f3aa17a9dde21b799842df31b40e75f5cc4fc6f6b501]
- The product ships as a single CGO_ENABLED=0 static Go binary, cross-compilable to six targets (darwin/linux/windows × amd64/arm64) with one command. [@claim:clm_4d145a2382c6e85acbd2fee2d0cfe35c649fbc5b053123a6b15dc51bb09af396]
- MCP servers contribute tools, prompts, and resources, and Extension Protocol v1 sidecars can intercept runtime events and contribute providers and structured UI. [@claim:clm_9215fdb78259aba7db133f138b162abff61b43d56b8ac1e817e2f0840aca51b3]
- Configuration is declared in reasonix.toml covering providers, the agent, enabled tools, and plugins, with no hardcoded models; DeepSeek ships as a preset and any OpenAI-compatible endpoint is a config entry. [@claim:clm_a45064f0cf2a7e9b1dc3fa3829cff1c3b33fb0d7f0d68672338cbf300d4a2bb7]
- Repository development practice: build from source with `make build` (bin/reasonix) and `make cross` (dist/), and build desktop packages via scripts/desktop-build.sh one platform per run. [@claim:clm_e958c0fbbe5be228c6ca2ed11c36fa5639a2e866096bfc784b7347875f5cce71]
<!-- rcw:end owner=source:src_c04af4a5fae153ada087f2de349c8d33 block=evidence -->

## Researcher notes

