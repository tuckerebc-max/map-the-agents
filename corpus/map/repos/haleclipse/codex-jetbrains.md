# haleclipse/codex-jetbrains

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e2db6655d78d @ 50cc8f371d9c5902

## Summary (orientation draft, not independently verified)

RunVSAgent is a JetBrains plugin plus Node.js extension host that lets VSCode-based coding agents (Roo Code, Cline, Kilo Code) run inside JetBrains IDEs, communicating over RPC. Evidence is mostly README/BUILD/CONTRIBUTING documentation covering architecture, supported IDEs, installation, and contributor workflows. Evidence coverage: 195 of 320 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] RunVSAgent is a cross-platform tool that runs VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. -- evidence: [README.md#L11-L11](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L11-L11)
  - [observation/documented] The project lists Roo Code, Cline, and Kilo Code as supported VSCode-based coding agents. -- evidence: [README.md#L24-L26](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L24-L26)
- components (2 claim(s)):
  - [observation/documented] The architecture comprises a Kotlin JetBrains plugin (with UI integration and editor bridge), a Node.js extension host providing a VSCode API compatibility layer, and VSCode agents, connected via RPC. -- evidence: [README.md#L49-L55](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L49-L55), [README.md#L63-L65](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L63-L65), [README.md#L67-L69](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L67-L69), [README.md#L57-L61](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L57-L61), [README.md#L77-L81](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L77-L81)
  - [observation/documented] The extension host's TypeScript source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for RPC, and webViewManager.ts for WebView support. -- evidence: [README.md#L157-L175](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L157-L175)
- design-choices (1 claim(s)):
  - [observation/documented] Communication between the plugin and extension host uses RPC over Unix Domain Sockets or Named Pipes, per the technology stack description. -- evidence: [README.md#L179-L182](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L179-L182)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors initialize the environment with scripts/setup.sh, build with scripts/build.sh, and run tests with scripts/test.sh; development mode uses npm run dev for the extension host and ./gradlew runIde for the plugin. -- evidence: [CONTRIBUTING.md#L80-L81](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L80-L81), [CONTRIBUTING.md#L89-L90](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L89-L90), [README.md#L130-L130](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L130-L130), [README.md#L144-L146](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L144-L146), [CONTRIBUTING.md#L93-L95](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L93-L95), [README.md#L133-L133](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L133-L133), [README.md#L149-L151](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L149-L151)
  - [observation/documented] Repository development practice: the project follows Conventional Commits (feat, fix, docs, etc.) and a Git Flow-inspired branch strategy with main, develop, feature/*, bugfix/*, hotfix/*, and release/* branches. -- evidence: [CONTRIBUTING.md#L210-L219](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L210-L219), [CONTRIBUTING.md#L200-L200](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L200-L200), [CONTRIBUTING.md#L121-L121](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L121-L121), [CONTRIBUTING.md#L123-L128](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L123-L128)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The plugin can be installed from the JetBrains Marketplace via Settings/Preferences → Plugins, or from a downloaded .zip via 'Install Plugin from Disk', followed by an IDE restart. -- evidence: [README.md#L89-L94](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L89-L94), [README.md#L104-L109](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L104-L109)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Running/building the project requires Node.js 18+, a JetBrains IDE 2023.1+, Git, and JDK 17+. -- evidence: [README.md#L117-L120](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L117-L120)
- limitations (1 claim(s)):
More evidence: [full detail](codex-jetbrains.detail.md)

Metadata and full claim list: [full detail](codex-jetbrains.detail.md)
Human notes ([notes](codex-jetbrains.notes.md), never overwritten by build)

[Back to map index](../../index.md)
