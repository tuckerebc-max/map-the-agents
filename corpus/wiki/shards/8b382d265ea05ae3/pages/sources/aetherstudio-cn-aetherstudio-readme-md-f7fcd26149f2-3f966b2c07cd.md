---
access: public
aliases: []
claim_ids:
- clm_1df5d36482c628b390891f91bd2c4e42dfacfd1e5b2f3e1cf62d05ae8a7df3e8
- clm_36335f66754aa7540421f29eb5f9a920fb55979496c35d3e9503177854992ac9
- clm_400b79043bcfea23abe44a308a3ebc957910fd32a1a2083d4346b8402ee0a593
- clm_9e9f67a36b6e3a57a448d175052b56300bef5811d39f79bbd4d5bffe22704637
- clm_a2b19b57ba367a9da947395975c931a256bee6881a1685017fa611aa91f89965
- clm_a6d18f4ce77c2fa6edf69eb5426a5fe440bf8fc20586030948f1c4233057af85
- clm_d2c46354b04eeaf6b5ee9790071705c34ef7881be0a1311269792fabdd8d7417
- clm_d40631a4abd79ccd20a4e57fa1415db23824a3cb9f38a55814c4ec5bb84a9f38
- clm_d9479f40a9a351c7e75764f50ed2accd83361ff9eefe7c41f2c0486c05a5967b
- clm_e566c9e832b219f65dc74af7cf2cd5281569e30f38e2a488a3b9d42023ad8bd7
maturity: draft
page_id: pg_d655649eaad659fabc0e3f966b2c07cd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9c71f133e81b550881db667060ce31fc
title: aetherstudio-cn/AetherStudio/README.md @ f7fcd26149f2
updated_at: '2026-09-14T01:29:58Z'
---

# aetherstudio-cn/AetherStudio/README.md @ f7fcd26149f2

<!-- rcw:begin owner=source:src_9c71f133e81b550881db667060ce31fc block=evidence -->
- The UI is self-rendered via a Direct2D/DirectWrite pipeline with themes, translucent backgrounds, shadows, animations, and dirty-rectangle optimization, on a Win32 window with DWM immersive dark mode and high-DPI support. [@claim:clm_1df5d36482c628b390891f91bd2c4e42dfacfd1e5b2f3e1cf62d05ae8a7df3e8]
- AI integration is HTTP-based LLM interaction with DeepSeek and Kimi presets, offering code explanation, rewrite, inline suggestions, agent tool-result feedback, and an API configuration panel. [@claim:clm_36335f66754aa7540421f29eb5f9a920fb55979496c35d3e9503177854992ac9]
- The project is a Cargo workspace split by responsibility into crates including aether-core (text buffer, lexer, search), aether-render (Direct2D rendering/themes), aether-win32 (native UI layer), aether-lsp, aether-dap, aether-remote, aether-ai, aether-tree-sitter, aether-plugin, aether-shared, and aether-cli. [@claim:clm_400b79043bcfea23abe44a308a3ebc957910fd32a1a2083d4346b8402ee0a593]
- Repository development practice: the README reports a test snapshot (dated 2026-07-06) of 793 passing unit tests, coverage of about 47.8% regions / 43.7% lines, a successful GUI smoke test, ~67MB memory, and a lexer benchmark of roughly 500-650 MiB/s. [@claim:clm_9e9f67a36b6e3a57a448d175052b56300bef5811d39f79bbd4d5bffe22704637]
- The aether CLI can launch the GUI, open a file path, and navigate to a line:column position such as file.txt:10:5. [@claim:clm_a2b19b57ba367a9da947395975c931a256bee6881a1685017fa611aa91f89965]
- Repository development practice: a pre-push checklist mandates cargo fmt --check, cargo check -p aether-win32, and cargo test --workspace --lib --no-fail-fast; the README also documents workspace tests run with CARGO_INCREMENTAL=0 to avoid an ICE, clippy with -D warnings, a GUI smoke test script, and a coverage script. [@claim:clm_a6d18f4ce77c2fa6edf69eb5426a5fe440bf8fc20586030948f1c4233057af85]
- The editor uses a Piece Table text buffer with multi-cursor support, undo/redo history, syntax highlighting, find/replace, and auto-indentation. [@claim:clm_d2c46354b04eeaf6b5ee9790071705c34ef7881be0a1311269792fabdd8d7417]
- Building requires Windows 10 1809+ (Windows 11 recommended), a Rust stable toolchain pinned via rust-toolchain.toml, Visual Studio 2022 or Windows SDK build tools, and the x86_64-pc-windows-msvc target. [@claim:clm_d40631a4abd79ccd20a4e57fa1415db23824a3cb9f38a55814c4ec5bb84a9f38]
- Per the Chinese feature list, the aether CLI supports --wait and --new-window flags in addition to opening paths and locating line/column positions. [@claim:clm_d9479f40a9a351c7e75764f50ed2accd83361ff9eefe7c41f2c0486c05a5967b]
- The product currently targets only Windows 10 1809+ and Windows 11; AGENT_SPEC.md also notes the build environment lacked a Rust toolchain, so code correctness had to be ensured without compile verification. [@claim:clm_e566c9e832b219f65dc74af7cf2cd5281569e30f38e2a488a3b9d42023ad8bd7]
<!-- rcw:end owner=source:src_9c71f133e81b550881db667060ce31fc block=evidence -->

## Researcher notes

