# lore-hex/quillcode -- full detail

[Back to orientation](quillcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lore-hex/quillcode/9f412834f0d6487d59619669d56198fcb872d374/c9647230348e1d7f.json](../../../wiki/dossiers/lore-hex/quillcode/9f412834f0d6487d59619669d56198fcb872d374/c9647230348e1d7f.json)

## specifications (2 claim(s))

- [observation/documented] The desktop app targets macOS 14 or later and runs natively on both Apple silicon and Intel Macs via a universal installer. -- evidence: [README.md#L47-L47](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L47-L47), [README.md#L49-L54](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L49-L54) (`clm_1c08599e19dab5c09359cb36172520a8b591780824fe29408f473e9dc24ffb4c`)
- [observation/documented] The project is built with Swift 6 and Swift Package Manager, with commands like swift test and swift run quill-code-desktop. -- evidence: [README.md#L117-L117](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L117-L117), [README.md#L119-L124](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L119-L124) (`clm_1977ebd04f9d79c81ae045800bb8e80824ce234f3d68c1bc9c49ebe05db53b2b`)

## components (2 claim(s))

- [observation/documented] Quill Cowork is a SwiftUI desktop app combining project-aware chat, local tools, Git workflows, Computer Use, automations, plugins, and a workspace terminal, with no Electron or web shell. -- evidence: [README.md#L12-L16](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L12-L16) (`clm_0e117b7e2e51a642b20c8773e4732cd395cfdd6364c1e6b83c6e9420391f1cc7`)
- [observation/documented] Distributions include macOS universal/arm64/x86_64 desktop apps plus CLI tarballs for macOS arm64, x86_64, and Linux x86_64, all labeled tester preview. -- evidence: [README.md#L88-L95](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L88-L95) (`clm_d6365c50d34313c2244ea444f2742b5819820c5db0bb93dfa430db60c2a78c6a`)

## design-choices (2 claim(s))

- [observation/documented] Confidential Cowork defaults to trustedrouter/confidential, requires Confidential-tier providers for every model-backed request, supports US/EU processing policy, and fails closed rather than using a standard route. -- evidence: [README.md#L20-L24](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L20-L24) (`clm_8912bb102544e7a90cd257560faf738801c5480bc278e803d8a2ec7fbeac0bab`)
- [observation/documented] The confidential policy also covers safety review, summaries, compaction, code review, fallback, and model-assisted search, and settings cannot disable it or replace the official endpoint. -- evidence: [README.md#L26-L28](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L26-L28) (`clm_bb5663d9a97f452f05c9cf6d90018229805a96162537fb0fc6ddee83f3979c5c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: agent changes merge through a serialized Merge Train that reruns CI and publishes an exact-main tester build after each successful merge; smoke tests run via scripts/smoke.sh. -- evidence: [README.md#L132-L134](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L132-L134), [README.md#L136-L137](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L136-L137) (`clm_0b49d70a979635ab7617f8b9478327ba5d91e6e82fed034d81feacf1b38fb784`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The quill-code CLI defaults to live TrustedRouter when a model is needed, supports --mock for deterministic local runs, and offers auth set-key for developer keys. -- evidence: [README.md#L126-L128](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L126-L128) (`clm_d786b7c8a53a22b511699399716225e99c8e5bc39899761cada3a2cc9a0cfdbe`)

## memory-state (1 claim(s))

- [observation/documented] Unsent composer text is checkpointed after a typing pause or on app inactivity/quit and restored after unexpected exit; checkpoints are bounded, per-chat, and never store confidential-chat text. -- evidence: [README.md#L72-L75](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L72-L75) (`clm_311fe3a2f484095df7083680726f48e865df8eab678d55dc9fe112d096aeaf42`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] A documented safety limitation: background desktop clicks via the opt-in cua-driver backend can actuate unapproved background apps because the Approved-Apps gate checks only the frontmost app. -- evidence: [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L82-L91](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L82-L91) (`clm_27c081171bad06164eb93a426a4566c05ca9d3c6223a164dd499a368d6236e0f`)
- [observation/documented] The cua-driver computer-use backend is off by default and enabled via QUILLCODE_USE_CUA_DRIVER=1, with an optional path override; the agent-facing tools and approval gate are unchanged. -- evidence: [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L19-L21](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L19-L21), [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L3-L7](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L3-L7) (`clm_f40285223b5560d9e448ea6dc191593959ffc864c6f687d4383bbfac80190330`)

## evaluation (1 claim(s))

- [observation/documented] A cheap-agentic-eval analysis reports a baseline passing 10/12 and 11/12 cases across two trials, with a targeted rerun passing all affected cases; root causes included a missing line-semantic grader. -- evidence: [docs/cheap-agentic-eval-root-causes.md#L26-L27](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/cheap-agentic-eval-root-causes.md#L26-L27), [docs/cheap-agentic-eval-root-causes.md#L7-L11](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/cheap-agentic-eval-root-causes.md#L7-L11), [docs/cheap-agentic-eval-root-causes.md#L13-L14](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/cheap-agentic-eval-root-causes.md#L13-L14), [docs/cheap-agentic-eval-root-causes.md#L18-L24](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/cheap-agentic-eval-root-causes.md#L18-L24) (`clm_dd66221235b5c71ac82a003dc3fa939228c9cabf9a1d8a6d77f75c43d5c1f58e`)

## dependencies (1 claim(s))

- [observation/documented] The computer-use backend adopts TryCua's MIT-licensed cua-driver behind the existing ComputerUseBackend seam, verified live against cua-driver 0.8.3. -- evidence: [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L52-L52](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L52-L52), [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L3-L7](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L3-L7) (`clm_be3265a7dcc14ed8a7573a171401d3b9d450c535f19de110ca5c163967454220`)

## limitations (2 claim(s))

- [observation/documented] Tester builds are ad-hoc code-signed but not Apple-notarized, so macOS blocks first launch and users must use Open Anyway in Privacy & Security. -- evidence: [README.md#L49-L54](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L49-L54) (`clm_5a6b9466e09cf43c56c303feeb128030ea7dc42b3e55e487c2188dd38df4b56c`)
- [observation/documented] A merge/extraction data-loss gate (F21) was attempted twice and deliberately not shipped after reviews found both designs' premises false; merge verification remains with the human or an explicit per-task check. -- evidence: [docs/CLINE_TOOL_LEARNINGS.md#L94-L97](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CLINE_TOOL_LEARNINGS.md#L94-L97), [docs/CLINE_TOOL_LEARNINGS.md#L125-L128](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CLINE_TOOL_LEARNINGS.md#L125-L128) (`clm_59937a725569c012f463e3acb5982ce2722d93cf6e2c94aeec187b09ab69c0b2`)

## relevance (1 claim(s))

- [observation/documented] The project is an independent open-source Apache-2.0 coding agent inspired by Codex, Claude Code, and Cline, and tracks Codex workflow parity in its research docs. -- evidence: [README.md#L152-L154](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L152-L154), [docs/CODEX_RESEARCH.md#L3-L3](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CODEX_RESEARCH.md#L3-L3) (`clm_bc0f098256d4111009222633167ad99f36d71a4f937c5e12d8edae2510a8acae`)

