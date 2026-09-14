# aetherstudio-cn/aetherstudio

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f7fcd26149f2 @ 9dbf470b8b2608bc

## Summary (orientation draft, not independently verified)

README documents Aether Studio, a Rust + Win32 native Windows code editor organized as a multi-crate Cargo workspace with AI, LSP/DAP, Tree-sitter, remote, and plugin features; AGENT_SPEC.md describes planned production-grade goals, and CONTRIBUTING.md defines the commit/PR workflow.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] AGENT_SPEC.md sets goals of production-grade Git support, SSH remote connections, Acrylic/glass UI, 60fps rendering with sub-16ms input latency, and configurable LLM API keys (OpenAI, Claude, Kimi). -- evidence: [AGENT_SPEC.md#L5-L11](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L5-L11)
  - [observation/documented] AGENT_SPEC.md lists non-goals: no new LSP/DAP features, no new plugin-system features, no additional localization, and no cloud sync or collaborative editing. -- evidence: [AGENT_SPEC.md#L14-L17](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/AGENT_SPEC.md#L14-L17)
- components (1 claim(s)):
  - [observation/documented] The project is a Cargo workspace split by responsibility into crates including aether-core (text buffer, lexer, search), aether-render (Direct2D rendering/themes), aether-win32 (native UI layer), aether-lsp, aether-dap, aether-remote, aether-ai, aether-tree-sitter, aether-plugin, aether-shared, and aether-cli. -- evidence: [README.md#L166-L178](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L166-L178), [README.md#L339-L351](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L339-L351)
- design-choices (3 claim(s)):
  - [observation/documented] The editor uses a Piece Table text buffer with multi-cursor support, undo/redo history, syntax highlighting, find/replace, and auto-indentation. -- evidence: [README.md#L50-L65](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L50-L65), [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238)
  - [observation/documented] The UI is self-rendered via a Direct2D/DirectWrite pipeline with themes, translucent backgrounds, shadows, animations, and dirty-rectangle optimization, on a Win32 window with DWM immersive dark mode and high-DPI support. -- evidence: [README.md#L50-L65](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L50-L65), [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: CONTRIBUTING.md requires external contributors to use a fork workflow, branch from dev (temp/ or fix/ prefixes), target PRs at dev rather than main, and follow a <type>(<scope>): <description> commit format with types like feat, fix, perf, and refactor. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L9-L9), [CONTRIBUTING.md#L94-L95](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L94-L95), [CONTRIBUTING.md#L134-L143](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L134-L143), [CONTRIBUTING.md#L115-L115](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L115-L115), [CONTRIBUTING.md#L86-L91](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L86-L91)
  - [observation/documented] Repository development practice: a pre-push checklist mandates cargo fmt --check, cargo check -p aether-win32, and cargo test --workspace --lib --no-fail-fast; the README also documents workspace tests run with CARGO_INCREMENTAL=0 to avoid an ICE, clippy with -D warnings, a GUI smoke test script, and a coverage script. -- evidence: [README.md#L141-L142](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L141-L142), [README.md#L131-L132](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L131-L132), [README.md#L145-L146](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L145-L146), [README.md#L135-L135](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L135-L135), [CONTRIBUTING.md#L103-L107](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/CONTRIBUTING.md#L103-L107)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The aether CLI can launch the GUI, open a file path, and navigate to a line:column position such as file.txt:10:5. -- evidence: [README.md#L287-L287](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L287-L287), [README.md#L290-L291](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L290-L291), [README.md#L117-L118](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L117-L118), [README.md#L114-L114](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L114-L114)
  - [observation/documented] Per the Chinese feature list, the aether CLI supports --wait and --new-window flags in addition to opening paths and locating line/column positions. -- evidence: [README.md#L223-L238](https://github.com/aetherstudio-cn/AetherStudio/blob/f7fcd26149f22f88c90354ef297aac400d8c20d4/README.md#L223-L238)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](aetherstudio.detail.md)

Metadata and full claim list: [full detail](aetherstudio.detail.md)
Human notes ([notes](aetherstudio.notes.md), never overwritten by build)

[Back to map index](../../index.md)
