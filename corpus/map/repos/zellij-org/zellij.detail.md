# zellij-org/zellij -- full detail

[Back to orientation](zellij.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zellij-org/zellij/a162323384dff3fbd9c68a4c0971f4f6efca424a/6985d63e6d540d43.json](../../../wiki/dossiers/zellij-org/zellij/a162323384dff3fbd9c68a4c0971f4f6efca424a/6985d63e6d540d43.json)

## specifications (1 claim(s))

- [observation/documented] Zellij is a workspace aimed at developers, ops-oriented people, and terminal enthusiasts; similar programs are known as terminal multiplexers. -- evidence: [README.md#L44-L44](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L44-L44) (`clm_51e0fd0eb467bf1f3f4704f54a292fdf46d7291ecbb04c59ccaf433981e40c44`)

## components (3 claim(s))

- [observation/documented] The Screen component manages on-screen panes: coordinating pane resizing, creating new panes, and closing panes while filling their space with others. -- evidence: [docs/ARCHITECTURE.md#L4-L8](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ARCHITECTURE.md#L4-L8) (`clm_3d957ab74046ff817da29fd77c0116847b59b4c1ad392572c54919bb9498fcd8`)
- [observation/documented] TerminalPane connects a pane to a single pty (typically running a shell or program), tracks the Scroll line buffer, and interprets ANSI/VT instructions for styling and cursor positioning. -- evidence: [docs/ARCHITECTURE.md#L11-L14](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ARCHITECTURE.md#L11-L14) (`clm_ffdf28cf6513737c54693ff22f21b3569d47ca54f886b0c61a79e00a7778740f`)
- [observation/documented] The PtyBus tracks asynchronous streams reading from pty sockets, parses bytes into ANSI/VT events, and sends them to the Screen for delivery to the relevant TerminalPane. -- evidence: [docs/ARCHITECTURE.md#L41-L41](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ARCHITECTURE.md#L41-L41) (`clm_6cf0d0bb45a5cb5e3150f51a8fbeae0a6953a8d49bd105b0f87e7b10f77ee8fb`)

## design-choices (1 claim(s))

- [observation/documented] The project states a philosophy of not sacrificing simplicity for power, aiming for a strong out-of-the-box experience plus advanced features. -- evidence: [README.md#L46-L46](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L46-L46) (`clm_27c93638f02426190d0ea7446a3a2a91b5f46deffb771b27e3cb567da6ad602f`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: after cloning, debug builds run via `cargo xtask run` and all tests via `cargo xtask test`, with more build commands documented in CONTRIBUTING.md. -- evidence: [README.md#L90-L90](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L90-L90), [README.md#L86-L88](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L86-L88) (`clm_c01ef3753165a9bd7b39f9dcae88b9c0e8db5d41dc6b8b53cd5fd28e4595b0df`)
- [observation/documented] Repository development practice: contributors are asked to eliminate unwrap() where possible in favor of Result-returning functions, using fatal()/non_fatal() helpers and the zellij_utils::errors prelude. -- evidence: [docs/ERROR_HANDLING.md#L35-L37](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L35-L37), [docs/ERROR_HANDLING.md#L81-L88](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L81-L88), [docs/ERROR_HANDLING.md#L90-L93](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L90-L93), [docs/ERROR_HANDLING.md#L11-L15](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L11-L15), [docs/ERROR_HANDLING.md#L3-L9](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L3-L9) (`clm_2ac694dd1225b98b7de4066deb3646ade386177223b8f1bf0999ead17eee5f24`)
- [observation/documented] Repository development practice: governance gives organization members decision-making power, with a BDFL (Aram Drevekenin) holding ultimate say on large decisions and veto power over group decisions. -- evidence: [GOVERNANCE.md#L6-L6](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/GOVERNANCE.md#L6-L6), [GOVERNANCE.md#L9-L9](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/GOVERNANCE.md#L9-L9), [GOVERNANCE.md#L11-L11](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/GOVERNANCE.md#L11-L11) (`clm_dde5b91a949e9ae6b6090451bcde580b2927c469da42ec2df9a46ff3cf73d67d`)
- [observation/documented] Repository development practice: installing from the main branch is not recommended, as it is pre-release code that may be broken and can corrupt the cache for future released versions. -- evidence: [README.md#L80-L80](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L80-L80) (`clm_308f16d5155443471f950fd6c4aeebee3d5e581fcbf6951d3f9623d4e73dc518`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Zellij advertises deep customizability, layout-based personal automation, multiplayer collaboration, floating and stacked panes, and a plugin system for any language compiling to WebAssembly. -- evidence: [README.md#L48-L48](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L48-L48) (`clm_31b40d585f1939d05d6d9c5ce73b4edffca7dca3fac3d25344a93ea3d2c6d800`)
- [observation/documented] Zellij includes a built-in web client, making a terminal optional for using it. -- evidence: [README.md#L50-L50](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L50-L50) (`clm_47fd3457a1cf007496c591329b579ec1618d2cb5318b62399d1869b33cecd1ba`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The error-handling approach uses the anyhow crate to propagate errors with context, the miette crate for panic-message formatting, and thiserror to build the ZellijError type. -- evidence: [docs/ERROR_HANDLING.md#L41-L43](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L41-L43), [docs/ERROR_HANDLING.md#L509-L514](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L509-L514), [docs/ERROR_HANDLING.md#L47-L51](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L47-L51) (`clm_c30fdd179c9eb3b6e3c1257e8627f61bc88df0fe751e13b8b0329a8a0bcc53a2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

