# athasdev/athas -- full detail

[Back to orientation](athas.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/athasdev/athas/42ef5d128147eb4c6adf0ce957618ad814345743/f8ffb2c0e80b53b0.json](../../../wiki/dossiers/athasdev/athas/42ef5d128147eb4c6adf0ce957618ad814345743/f8ffb2c0e80b53b0.json)

## specifications (1 claim(s))

- [observation/documented] Athas is described as a lightweight, cross-platform code editor built with Tauri (Rust and React), featuring Git support, AI agents, and vim keybindings. -- evidence: [README.md#L1-L6](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L1-L6) (`clm_f6a6bb6d0a0846b23212350a09a7c521a5e4e2c8c7cb80b3a45d23b0fb487e85`)

## components (1 claim(s))

- [observation/documented] Documented features include AI agents, Git integration, syntax highlighting, LSP support, vim keybindings, an integrated terminal, database viewers, collaboration, and enterprise policy controls. -- evidence: [README.md#L10-L18](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L10-L18) (`clm_d5f18da6bf371f32e26682844338a491a0e17902157eb4f4a800410910623f0a`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: building from source requires Node.js 24, Bun 1.3.14, and Rust, then running git clone, bun setup, and bun dev; bun setup installs dependencies and checks native platform requirements. -- evidence: [README.md#L89-L91](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L89-L91), [README.md#L79-L80](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L79-L80), [README.md#L82-L87](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L82-L87) (`clm_c65313307628752102b90e2ba101a04551b47966dc77b2492f28c32b7cc73a52`)
- [observation/documented] Repository development practice: AGENTS.md specifies Bun 1.3.2, Node.js 22+, and Rust as the required environment, with bun install, bun dev, bun check, bunx vp test run, bun typecheck, and bun check:rust as validation commands. -- evidence: [AGENTS.md#L11-L20](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/AGENTS.md#L11-L20) (`clm_d781957c755dffdd34c4b0d9a353c64d4a4320d35c21e9656e7bebf13ae00e05`)
- [observation/documented] Repository development practice: Rust unit tests live in #[cfg(test)] modules beside the code or in src/<module>/tests.rs, integration tests go in crates/<crate>/tests/, and bun check:rust should run before submitting Rust changes. -- evidence: [CONTRIBUTING.md#L41-L48](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/CONTRIBUTING.md#L41-L48) (`clm_052710bfaca1007b4e2605f8e0c85a5dde8d618ea616e6a7368384c34b74b917`)
- [observation/documented] Repository development practice: release automation is triggered by pushing v* tags, Windows MSI versioning must stay numeric-only, and release changes should be validated with a dry-run before publishing. -- evidence: [AGENTS.md#L118-L122](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/AGENTS.md#L118-L122) (`clm_0a3b1c8c818d9ce1418c18c29d05ab29fb03e2181de0e5ac3ce7817ebe93c9ee`)
- [observation/documented] Repository development practice: contributors must pass bun check, may use bun fix and bun format, rebase on master, squash commits, and agree to the Contributor License and Feedback Agreement before submitting. -- evidence: [CONTRIBUTING.md#L22-L30](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/CONTRIBUTING.md#L22-L30) (`clm_9a15739888bdf3c8f4983074c357c21166122adf3a6b4f40387981422a130d70`)
- [observation/documented] Repository development practice: submitting a pull request, commit, patch, or issue constitutes acceptance of the Contributor License and Feedback Agreement, under which contributions are licensed AGPL-3.0 and feedback is licensed to maintainers without compensation. -- evidence: [CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L63-L64](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L63-L64), [CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L28-L30](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L28-L30), [CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L47-L49](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/CONTRIBUTOR_LICENSE_AND_FEEDBACK_AGREEMENT.md#L47-L49) (`clm_d2fd219f7f81e0050c94207cb81b28cee9b49ed68caf6069519eb04d55a91f5d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Enterprise policy controls are documented as including a managed mode plus an extension allowlist. -- evidence: [README.md#L10-L18](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L10-L18) (`clm_25a1f9e1f3e7d64a0e20f339a89ac24fc80526829811130b40473dcec2f92ba8`)
- [observation/documented] Install scripts for macOS/Linux and Windows are provided, and the scripts detect OS and architecture, download the latest stable release, and verify a SHA256 checksum when available. -- evidence: [README.md#L32-L34](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L32-L34), [README.md#L26-L28](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L26-L28), [README.md#L36-L39](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L36-L39) (`clm_5fc42169e4a5e30d20dbf4412fb6fe91b0ce1ca6f131348dbaa6dc003f2b5585`)
- [observation/documented] A preview release channel exists: passing --preview to the macOS/Linux install script installs the latest preview release. -- evidence: [README.md#L43-L45](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L43-L45), [README.md#L41-L41](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L41-L41) (`clm_0915ad336fa9788d2e17c1ea059939e630eb486229479e1b16f6e441e0086209`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prebuilt packages are distributed for macOS, Windows, and Linux, with Linux releases including .deb, .rpm, and portable .tar.gz bundles. -- evidence: [README.md#L70-L72](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L70-L72) (`clm_2f101b71b47025b77e249e6f50e30a1d8f8e91b0dd2cb858e42eedd00c011ace`)
- [observation/documented] The editor can be installed via Homebrew (cask athas), WinGet (athasdev.Athas), and Scoop from a dedicated bucket. -- evidence: [README.md#L51-L53](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L51-L53), [README.md#L57-L59](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L57-L59), [README.md#L63-L66](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L63-L66) (`clm_ec381a2666fe8ae6c41dcfd1978a2d209ceb2ed5c04799cffb1c40b9a5559d33`)

## limitations (1 claim(s))

- [observation/documented] The project is licensed under AGPL-3.0. -- evidence: [README.md#L109-L109](https://github.com/athasdev/athas/blob/42ef5d128147eb4c6adf0ce957618ad814345743/README.md#L109-L109) (`clm_665f5047232138456d7ceb224abf98bbcd910940b390c8203ac811b2d1d1ec35`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

