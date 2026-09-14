# zellij-org/zellij

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a162323384df @ 6985d63e6d540d43

## Summary (orientation draft, not independently verified)

Selected evidence records: Zellij is a workspace aimed at developers, ops-oriented people, and terminal enthusiasts; similar programs are known as terminal multiplexers. The project states a philosophy of not sacrificing simplicity for power, aiming for a strong out-of-the-box experience plus advanced features.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Zellij is a workspace aimed at developers, ops-oriented people, and terminal enthusiasts; similar programs are known as terminal multiplexers. -- evidence: [README.md#L44-L44](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L44-L44)
- components (3 claim(s)):
  - [observation/documented] The Screen component manages on-screen panes: coordinating pane resizing, creating new panes, and closing panes while filling their space with others. -- evidence: [docs/ARCHITECTURE.md#L4-L8](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ARCHITECTURE.md#L4-L8)
  - [observation/documented] TerminalPane connects a pane to a single pty (typically running a shell or program), tracks the Scroll line buffer, and interprets ANSI/VT instructions for styling and cursor positioning. -- evidence: [docs/ARCHITECTURE.md#L11-L14](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ARCHITECTURE.md#L11-L14)
- design-choices (1 claim(s)):
  - [observation/documented] The project states a philosophy of not sacrificing simplicity for power, aiming for a strong out-of-the-box experience plus advanced features. -- evidence: [README.md#L46-L46](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L46-L46)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: after cloning, debug builds run via `cargo xtask run` and all tests via `cargo xtask test`, with more build commands documented in CONTRIBUTING.md. -- evidence: [README.md#L90-L90](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L90-L90), [README.md#L86-L88](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L86-L88)
  - [observation/documented] Repository development practice: contributors are asked to eliminate unwrap() where possible in favor of Result-returning functions, using fatal()/non_fatal() helpers and the zellij_utils::errors prelude. -- evidence: [docs/ERROR_HANDLING.md#L35-L37](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L35-L37), [docs/ERROR_HANDLING.md#L81-L88](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L81-L88), [docs/ERROR_HANDLING.md#L90-L93](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L90-L93), [docs/ERROR_HANDLING.md#L11-L15](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L11-L15), [docs/ERROR_HANDLING.md#L3-L9](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L3-L9)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Zellij advertises deep customizability, layout-based personal automation, multiplayer collaboration, floating and stacked panes, and a plugin system for any language compiling to WebAssembly. -- evidence: [README.md#L48-L48](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L48-L48)
  - [observation/documented] Zellij includes a built-in web client, making a terminal optional for using it. -- evidence: [README.md#L50-L50](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/README.md#L50-L50)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The error-handling approach uses the anyhow crate to propagate errors with context, the miette crate for panic-message formatting, and thiserror to build the ZellijError type. -- evidence: [docs/ERROR_HANDLING.md#L41-L43](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L41-L43), [docs/ERROR_HANDLING.md#L509-L514](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L509-L514), [docs/ERROR_HANDLING.md#L47-L51](https://github.com/zellij-org/zellij/blob/a162323384dff3fbd9c68a4c0971f4f6efca424a/docs/ERROR_HANDLING.md#L47-L51)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](zellij.detail.md) for every claim.)

Metadata and full claim list: [full detail](zellij.detail.md)
Human notes ([notes](zellij.notes.md), never overwritten by build)

[Back to map index](../../index.md)
