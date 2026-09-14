---
access: public
aliases: []
claim_ids:
- clm_0b49d70a979635ab7617f8b9478327ba5d91e6e82fed034d81feacf1b38fb784
- clm_0e117b7e2e51a642b20c8773e4732cd395cfdd6364c1e6b83c6e9420391f1cc7
- clm_1977ebd04f9d79c81ae045800bb8e80824ce234f3d68c1bc9c49ebe05db53b2b
- clm_1c08599e19dab5c09359cb36172520a8b591780824fe29408f473e9dc24ffb4c
- clm_311fe3a2f484095df7083680726f48e865df8eab678d55dc9fe112d096aeaf42
- clm_5a6b9466e09cf43c56c303feeb128030ea7dc42b3e55e487c2188dd38df4b56c
- clm_8912bb102544e7a90cd257560faf738801c5480bc278e803d8a2ec7fbeac0bab
- clm_bb5663d9a97f452f05c9cf6d90018229805a96162537fb0fc6ddee83f3979c5c
- clm_bc0f098256d4111009222633167ad99f36d71a4f937c5e12d8edae2510a8acae
- clm_d6365c50d34313c2244ea444f2742b5819820c5db0bb93dfa430db60c2a78c6a
- clm_d786b7c8a53a22b511699399716225e99c8e5bc39899761cada3a2cc9a0cfdbe
maturity: draft
page_id: pg_9511eceeba78570981ff868be3882445
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1b54b60d2dde5d41b8a085963dd020b8
title: Lore-Hex/QuillCode/README.md @ 9f412834f0d6
updated_at: '2026-09-14T02:14:03Z'
---

# Lore-Hex/QuillCode/README.md @ 9f412834f0d6

<!-- rcw:begin owner=source:src_1b54b60d2dde5d41b8a085963dd020b8 block=evidence -->
- Repository development practice: agent changes merge through a serialized Merge Train that reruns CI and publishes an exact-main tester build after each successful merge; smoke tests run via scripts/smoke.sh. [@claim:clm_0b49d70a979635ab7617f8b9478327ba5d91e6e82fed034d81feacf1b38fb784]
- Quill Cowork is a SwiftUI desktop app combining project-aware chat, local tools, Git workflows, Computer Use, automations, plugins, and a workspace terminal, with no Electron or web shell. [@claim:clm_0e117b7e2e51a642b20c8773e4732cd395cfdd6364c1e6b83c6e9420391f1cc7]
- The project is built with Swift 6 and Swift Package Manager, with commands like swift test and swift run quill-code-desktop. [@claim:clm_1977ebd04f9d79c81ae045800bb8e80824ce234f3d68c1bc9c49ebe05db53b2b]
- The desktop app targets macOS 14 or later and runs natively on both Apple silicon and Intel Macs via a universal installer. [@claim:clm_1c08599e19dab5c09359cb36172520a8b591780824fe29408f473e9dc24ffb4c]
- Unsent composer text is checkpointed after a typing pause or on app inactivity/quit and restored after unexpected exit; checkpoints are bounded, per-chat, and never store confidential-chat text. [@claim:clm_311fe3a2f484095df7083680726f48e865df8eab678d55dc9fe112d096aeaf42]
- Tester builds are ad-hoc code-signed but not Apple-notarized, so macOS blocks first launch and users must use Open Anyway in Privacy & Security. [@claim:clm_5a6b9466e09cf43c56c303feeb128030ea7dc42b3e55e487c2188dd38df4b56c]
- Confidential Cowork defaults to trustedrouter/confidential, requires Confidential-tier providers for every model-backed request, supports US/EU processing policy, and fails closed rather than using a standard route. [@claim:clm_8912bb102544e7a90cd257560faf738801c5480bc278e803d8a2ec7fbeac0bab]
- The confidential policy also covers safety review, summaries, compaction, code review, fallback, and model-assisted search, and settings cannot disable it or replace the official endpoint. [@claim:clm_bb5663d9a97f452f05c9cf6d90018229805a96162537fb0fc6ddee83f3979c5c]
- The project is an independent open-source Apache-2.0 coding agent inspired by Codex, Claude Code, and Cline, and tracks Codex workflow parity in its research docs. [@claim:clm_bc0f098256d4111009222633167ad99f36d71a4f937c5e12d8edae2510a8acae]
- Distributions include macOS universal/arm64/x86_64 desktop apps plus CLI tarballs for macOS arm64, x86_64, and Linux x86_64, all labeled tester preview. [@claim:clm_d6365c50d34313c2244ea444f2742b5819820c5db0bb93dfa430db60c2a78c6a]
- The quill-code CLI defaults to live TrustedRouter when a model is needed, supports --mock for deterministic local runs, and offers auth set-key for developer keys. [@claim:clm_d786b7c8a53a22b511699399716225e99c8e5bc39899761cada3a2cc9a0cfdbe]
<!-- rcw:end owner=source:src_1b54b60d2dde5d41b8a085963dd020b8 block=evidence -->

## Researcher notes

