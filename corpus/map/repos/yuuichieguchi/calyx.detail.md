# yuuichieguchi/calyx -- full detail

[Back to orientation](calyx.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yuuichieguchi/calyx/8415801ce661a7bb5af4968d2955613523d47b00/8b35c2344eef19d5.json](../../../wiki/dossiers/yuuichieguchi/calyx/8415801ce661a7bb5af4968d2955613523d47b00/8b35c2344eef19d5.json)

## specifications (1 claim(s))

- [observation/documented] Calyx is a native macOS terminal for running and supervising coding agents (Claude Code, Codex, OpenCode, Hermes, Grok, pi) in parallel, with an approval inbox, live status, persistent sessions, and inline diff review. -- evidence: [README.md#L5-L5](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L5-L5) (`clm_515bd0b95a78a485af9831c2786c43ec469ce0d2fe948138d2e20b4ea4be9ca4`)

## components (3 claim(s))

- [observation/documented] An Agents Sidebar shows each connected agent as working, blocked, idle, or done, with unread badges, click-to-focus navigation, and expandable subagent rows for CLIs that report them. -- evidence: [README.md#L34-L34](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L34-L34), [README.md#L52-L58](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L52-L58) (`clm_a6adac92bb100e80c0cecd74afdb9c4815726681bc2c0ffe49ed96aba91dceca`)
- [observation/documented] A Git sidebar shows working changes, staging state, commit graph, branch visualization, and inline diffs per repository, including linked worktrees and submodules, with per-line diff comments submittable to agent panes. -- evidence: [README.md#L42-L42](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L42-L42), [README.md#L62-L66](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L62-L66) (`clm_3707a80a926d79d111432cea4a0d548748f1f2479d2259cd61fe8eb2c37c1857`)
- [observation/documented] Persistent sessions are opt-in daemon-backed terminals that survive app quit and crashes, with a Session Browser, recovery flow, optional on-disk history, and remote sessions via calyx-session on SSH hosts. -- evidence: [README.md#L70-L74](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L70-L74) (`clm_8375d983b76f6c5fa66d12525c2bda557e96bf1f37d1fd5d673c5bed26f0b949`)

## design-choices (1 claim(s))

- [observation/documented] Architecture: AppKit handles window/tab/focus management with SwiftUI rendering bridged via NSHostingView; all ghostty C API calls go through a GhosttyFFI enum and @MainActor is enforced on UI and model code. -- evidence: [README.md#L250-L252](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L250-L252), [README.md#L248-L248](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L248-L248) (`clm_87f3d6bbdd32bfd42319db95dbd2c5a5051ed6a753d86fa84c4ad664cd103c37`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: external pull requests are not accepted and are closed automatically without review; bug reports and feature ideas go through GitHub Issues. -- evidence: [CONTRIBUTING.md#L5-L5](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/CONTRIBUTING.md#L5-L5), [CONTRIBUTING.md#L3-L3](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/CONTRIBUTING.md#L3-L3), [README.md#L258-L258](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L258-L258) (`clm_3906595df4649609478cdaea6a2e18c09a5e745a0193766b0b5a87a248e4ac89`)
- [observation/documented] Repository development practice: building requires macOS 26+, Xcode 26+, Zig matching ghostty's build.zig.zon, and XcodeGen; clone with submodules, build the GhosttyKit xcframework with zig, then generate the Xcode project and build with xcodebuild. -- evidence: [README.md#L221-L224](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L221-L224), [README.md#L242-L244](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L242-L244), [README.md#L234-L236](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L234-L236), [README.md#L230-L231](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L230-L231) (`clm_bb467ffddfbafe29774fbd87ccb2c473f2145693f01bdc30fd6d5295159d5f89`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Calyx exposes panes, commands, captured output, browser tabs, language servers, and peer agents to agents through MCP and a bundled CLI. -- evidence: [README.md#L46-L46](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L46-L46) (`clm_64a38775f0715bcaf3d5eb04efb7b66ea0474a330a057e2c962b174bffdd3a45`)
- [observation/documented] The AI Agent IPC MCP server offers tools register_peer, list_peers, send_message, broadcast, receive_messages, and get_peer_status; receive_messages deletes messages on delivery so each is delivered once. -- evidence: [README.md#L169-L169](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L169-L169) (`clm_0110bf258516e4d42e4af88354022f4d07f5a2ef858b8a0bc70135370788740b`)
- [observation/documented] Browser tabs are non-persistent WKWebViews limited to http/https with popups blocked, scriptable via 25 bundled 'calyx browser' commands; the browser server listens on localhost:41840. -- evidence: [README.md#L215-L215](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L215-L215), [README.md#L189-L189](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L189-L189), [README.md#L90-L91](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L90-L91) (`clm_e969e6673a9218637c2eeec15c521fcb1bc36ad1811c20c2ce86aa5452fcf244`)
- [observation/documented] An LSP proxy MCP exposes lsp_hover, lsp_definition, lsp_references, lsp_rename, and lsp_diagnostics to agents, keeping servers running in the background and starting the right one per workspace. -- evidence: [README.md#L177-L177](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L177-L177), [README.md#L185-L185](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L185-L185) (`clm_815345e43a540db8fac1b5438599769c0530bbc3084ac1b746c99d9930dcbfd6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The approval inbox is opt-in via Settings; nothing is automatically approved unless the user separately opts in, and cockpit tools like pane_run and pane_send_keys are approval-gated. -- evidence: [README.md#L38-L38](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L38-L38), [README.md#L171-L171](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L171-L171) (`clm_dd19ee519dca136680f34a22e6e25f2c8d49aae1a051ed1ffcae7e3afdf09775`)
- [observation/documented] Command text and output are redacted for known secret patterns (tokens, passwords, API keys, JWTs) before agents can read them, with pending redaction reported via output_pending. -- evidence: [README.md#L171-L171](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L171-L171) (`clm_c3cb31e0e293324857fa7297c12039d754bd3e17199ff051e3e05d71b7fdaf67`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The terminal engine is libghostty (Ghostty v1.3.1) providing Metal GPU-accelerated rendering; the tech stack is Swift 6.2, AppKit, SwiftUI, and XcodeGen. -- evidence: [README.md#L78-L86](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L78-L86), [README.md#L254-L254](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L254-L254) (`clm_3ac6a5dfd3e6bad357a2ddc1415902add787b8fadb954c56eac1cbdc96ff8ae5`)

## limitations (1 claim(s))

- [observation/documented] Cursor click-to-move may be offset on Japanese/full-width text because Ghostty translates clicks into arrow-key steps over terminal cells; Calyx also overrides certain Ghostty config keys for Glass UI. -- evidence: [README.md#L262-L263](https://github.com/yuuichieguchi/Calyx/blob/8415801ce661a7bb5af4968d2955613523d47b00/README.md#L262-L263) (`clm_97fdb7978ff94349707562434b5b3406db85e507a49709c3e308fa05c16094e8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

