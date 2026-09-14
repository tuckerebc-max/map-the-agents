---
access: public
aliases: []
claim_ids:
- clm_0da90645688a2c6f8504c2e70291f396a64f27611b8ef244ca39fad98edd45e8
- clm_1e74c304ac2110b700908e69626b45591ca5c1a006512933036848e27edb3089
- clm_2f2773f26d08e34e262f0d3434ecbec45f9935d7062db3db2d26352c4c952617
- clm_3c10d6eaaee86fbbda28baaa1681eba4d70f346116c3c7a158fdd55d20d18704
- clm_6b3f9b46ef5566b57d4377427437e04fae0ad0d94d7f583d46718e31fd918972
- clm_6dcd2c09f9c1eb2009aedb09c19ecdfeec2b0d2e90b02e1ad27b300f61f9acd1
- clm_82c87afa9521263bb3701c48ee167b8b5dfc3e5c011e9e0ffed63ba21c83b78f
- clm_85803b6453668e8b195ef7066087fc45c7b6214dbf206533cc85434269d31cae
- clm_ae5e5b6893353475db1f3081cdcb2499787b570194f2521bdec857567c7809f1
- clm_cc436b4776af489152359ab539d738eeea1f043809d93d9df8a352bb742f9397
- clm_f4b7670ca95cce1abe3efa3233b723ea86ce31bfd36fb29070e79caac5e0f4c5
- clm_f8eec5c95f482c380c95364d0f3cf607f2cc23fe37990d718d3cd206b8f6d34e
maturity: draft
page_id: pg_09d8c444b8b056d29aab29c42ba59112
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ecf1b03491fc51628421166c6a7d0a35
title: SeemSeam/claude_codex_bridge/README.md @ 20ac0ec58c17
updated_at: '2026-09-14T02:38:49Z'
---

# SeemSeam/claude_codex_bridge/README.md @ 20ac0ec58c17

<!-- rcw:begin owner=source:src_ecf1b03491fc51628421166c6a7d0a35 block=evidence -->
- .ccb/ccb_memory.md serves as the project-wide shared memory document for collaboration rules, constraints, and agent handoff conventions. [@claim:clm_0da90645688a2c6f8504c2e70291f396a64f27611b8ef244ca39fad98edd45e8]
- The mobile gateway binds to loopback by default; LAN binding requires a specific private interface address, and remote access uses Tailscale Serve rather than Funnel. [@claim:clm_1e74c304ac2110b700908e69626b45591ca5c1a006512933036848e27edb3089]
- Version-2 config uses [windows] entries where commas and semicolons denote vertical stacking and horizontal splits, e.g. A,B;C,D as a four-pane layout. [@claim:clm_2f2773f26d08e34e262f0d3434ecbec45f9935d7062db3db2d26352c4c952617]
- Agents can invoke /ask during workflow orchestration to delegate and hand off work, and users can type directly in any agent pane. [@claim:clm_3c10d6eaaee86fbbda28baaa1681eba4d70f346116c3c7a158fdd55d20d18704]
- Release notes state that DeepSeek CLI, Z.ai, and DeepSeek Harness remain implemented but are no longer presented as current headline provider support. [@claim:clm_6b3f9b46ef5566b57d4377427437e04fae0ad0d94d7f583d46718e31fd918972]
- A background daemon keeps project state alive even after the foreground UI is closed, per the README's feature list. [@claim:clm_6dcd2c09f9c1eb2009aedb09c19ecdfeec2b0d2e90b02e1ad27b300f61f9acd1]
- Project configuration executing tool-window commands or custom provider command templates requires exact external approval via ccb config approve-commands. [@claim:clm_82c87afa9521263bb3701c48ee167b8b5dfc3e5c011e9e0ffed63ba21c83b78f]
- The native Windows x64 beta requires Python 3.10+, WezTerm, Git Bash, and Herdr 0.8.0 or newer, with an install-local managed Python runtime. [@claim:clm_85803b6453668e8b195ef7066087fc45c7b6214dbf206533cc85434269d31cae]
- The README badges list version 8.6.13, platforms Linux/macOS/WSL/Windows beta, and 16 CLI provider families. [@claim:clm_ae5e5b6893353475db1f3081cdcb2499787b570194f2521bdec857567c7809f1]
- The Config UI binds to loopback only; a token source is configured in .ccb/ccb.config, and the CLI prints the URL and token source but never the token value. [@claim:clm_cc436b4776af489152359ab539d738eeea1f043809d93d9df8a352bb742f9397]
- Supported managed agents receive built-in ask, ccb-clear, ccb-compact, and ccb-diagnose control skills even when optional skill inheritance is disabled. [@claim:clm_f4b7670ca95cce1abe3efa3233b723ea86ce31bfd36fb29070e79caac5e0f4c5]
- CCB is described as a lightweight multi-agent TUI that coordinates CLI agents such as Codex, Claude, and Gemini in visible, controllable workflows. [@claim:clm_f8eec5c95f482c380c95364d0f3cf607f2cc23fe37990d718d3cd206b8f6d34e]
<!-- rcw:end owner=source:src_ecf1b03491fc51628421166c6a7d0a35 block=evidence -->

## Researcher notes

