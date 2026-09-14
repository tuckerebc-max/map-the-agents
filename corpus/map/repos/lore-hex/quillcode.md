# lore-hex/quillcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9f412834f0d6 @ c9647230348e1d7f

## Summary (orientation draft, not independently verified)

Selected evidence records: The desktop app targets macOS 14 or later and runs natively on both Apple silicon and Intel Macs via a universal installer. The project is built with Swift 6 and Swift Package Manager, with commands like swift test and swift run quill-code-desktop.

## Source coverage

Source coverage (partial): 6 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The desktop app targets macOS 14 or later and runs natively on both Apple silicon and Intel Macs via a universal installer. -- evidence: [README.md#L47-L47](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L47-L47), [README.md#L49-L54](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L49-L54)
  - [observation/documented] The project is built with Swift 6 and Swift Package Manager, with commands like swift test and swift run quill-code-desktop. -- evidence: [README.md#L117-L117](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L117-L117), [README.md#L119-L124](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L119-L124)
- components (2 claim(s)):
  - [observation/documented] Quill Cowork is a SwiftUI desktop app combining project-aware chat, local tools, Git workflows, Computer Use, automations, plugins, and a workspace terminal, with no Electron or web shell. -- evidence: [README.md#L12-L16](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L12-L16)
  - [observation/documented] Distributions include macOS universal/arm64/x86_64 desktop apps plus CLI tarballs for macOS arm64, x86_64, and Linux x86_64, all labeled tester preview. -- evidence: [README.md#L88-L95](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L88-L95)
- design-choices (2 claim(s)):
  - [observation/documented] Confidential Cowork defaults to trustedrouter/confidential, requires Confidential-tier providers for every model-backed request, supports US/EU processing policy, and fails closed rather than using a standard route. -- evidence: [README.md#L20-L24](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L20-L24)
  - [observation/documented] The confidential policy also covers safety review, summaries, compaction, code review, fallback, and model-assisted search, and settings cannot disable it or replace the official endpoint. -- evidence: [README.md#L26-L28](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L26-L28)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: agent changes merge through a serialized Merge Train that reruns CI and publishes an exact-main tester build after each successful merge; smoke tests run via scripts/smoke.sh. -- evidence: [README.md#L132-L134](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L132-L134), [README.md#L136-L137](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L136-L137)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The quill-code CLI defaults to live TrustedRouter when a model is needed, supports --mock for deterministic local runs, and offers auth set-key for developer keys. -- evidence: [README.md#L126-L128](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L126-L128)
- memory-state (1 claim(s)):
  - [observation/documented] Unsent composer text is checkpointed after a typing pause or on app inactivity/quit and restored after unexpected exit; checkpoints are bounded, per-chat, and never store confidential-chat text. -- evidence: [README.md#L72-L75](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/README.md#L72-L75)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] A documented safety limitation: background desktop clicks via the opt-in cua-driver backend can actuate unapproved background apps because the Approved-Apps gate checks only the frontmost app. -- evidence: [docs/CUA_COMPUTER_USE_TEST_PLAN.md#L82-L91](https://github.com/Lore-Hex/QuillCode/blob/9f412834f0d6487d59619669d56198fcb872d374/docs/CUA_COMPUTER_USE_TEST_PLAN.md#L82-L91)
More evidence: [full detail](quillcode.detail.md)

Metadata and full claim list: [full detail](quillcode.detail.md)
Human notes ([notes](quillcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
