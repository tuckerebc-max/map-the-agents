# athasdev/athas

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 42ef5d128147 @ f8ffb2c0e80b53b0

## Summary (orientation draft, not independently verified)

The snapshot is mostly README and contributor documentation for Athas, a Tauri-based desktop code editor; product claims are limited to documented features, installation channels, and licensing, while build/test instructions are contributor practice only.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Athas is described as a lightweight, cross-platform code editor built with Tauri (Rust and React), featuring Git support, AI agents, and vim keybindings. -- evidence: [README.md#L1-L6](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L1-L6)
- components (1 claim(s)):
  - [observation/documented] Documented features include AI agents, Git integration, syntax highlighting, LSP support, vim keybindings, an integrated terminal, database viewers, collaboration, and enterprise policy controls. -- evidence: [README.md#L10-L18](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L10-L18)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: building from source requires Node.js 24, Bun 1.3.14, and Rust, then running git clone, bun setup, and bun dev; bun setup installs dependencies and checks native platform requirements. -- evidence: [README.md#L89-L91](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L89-L91), [README.md#L79-L80](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L79-L80), [README.md#L82-L87](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L82-L87)
  - [observation/documented] Repository development practice: AGENTS.md specifies Bun 1.3.2, Node.js 22+, and Rust as the required environment, with bun install, bun dev, bun check, bunx vp test run, bun typecheck, and bun check:rust as validation commands. -- evidence: [AGENTS.md#L11-L20](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/AGENTS.md#L11-L20)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Enterprise policy controls are documented as including a managed mode plus an extension allowlist. -- evidence: [README.md#L10-L18](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L10-L18)
  - [observation/documented] Install scripts for macOS/Linux and Windows are provided, and the scripts detect OS and architecture, download the latest stable release, and verify a SHA256 checksum when available. -- evidence: [README.md#L32-L34](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L32-L34), [README.md#L26-L28](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L26-L28), [README.md#L36-L39](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L36-L39)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Prebuilt packages are distributed for macOS, Windows, and Linux, with Linux releases including .deb, .rpm, and portable .tar.gz bundles. -- evidence: [README.md#L70-L72](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L70-L72)
  - [observation/documented] The editor can be installed via Homebrew (cask athas), WinGet (athasdev.Athas), and Scoop from a dedicated bucket. -- evidence: [README.md#L51-L53](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L51-L53), [README.md#L57-L59](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L57-L59), [README.md#L63-L66](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L63-L66)
- limitations (1 claim(s)):
  - [observation/documented] The project is licensed under AGPL-3.0. -- evidence: [README.md#L109-L109](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L109-L109)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](athas.detail.md) for every claim.)

Metadata and full claim list: [full detail](athas.detail.md)
Human notes ([notes](athas.notes.md), never overwritten by build)

[Back to map index](../../index.md)
