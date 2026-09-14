# haleclipse/codex-jetbrains -- full detail

[Back to orientation](codex-jetbrains.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/haleclipse/codex-jetbrains/e2db6655d78da0f9ec3dd67c155fb30c59037959/50cc8f371d9c5902.json](../../../wiki/dossiers/haleclipse/codex-jetbrains/e2db6655d78da0f9ec3dd67c155fb30c59037959/50cc8f371d9c5902.json)

## specifications (3 claim(s))

- [observation/documented] RunVSAgent is a cross-platform tool that runs VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. -- evidence: [README.md#L11-L11](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L11-L11) (`clm_3633d7f61e8835fe4fe91d08f02bd59f87c15b38b4321459ee6de6f7381fb702`)
- [observation/documented] The project lists Roo Code, Cline, and Kilo Code as supported VSCode-based coding agents. -- evidence: [README.md#L24-L26](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L24-L26) (`clm_ba3ba25d7f6c283a3b91fab993e0a81e6e06ea4e92c19fa0311d3abaaf1e77dd`)
- [observation/documented] Supported JetBrains IDEs include IntelliJ IDEA, WebStorm, PyCharm, PhpStorm, RubyMine, CLion, GoLand, DataGrip, Rider, and Android Studio. -- evidence: [README.md#L33-L42](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L33-L42) (`clm_871331dfaa31e7413383f270e258bc4acda592dd9e72f18db80e3c9dbe9216d8`)

## components (2 claim(s))

- [observation/documented] The architecture comprises a Kotlin JetBrains plugin (with UI integration and editor bridge), a Node.js extension host providing a VSCode API compatibility layer, and VSCode agents, connected via RPC. -- evidence: [README.md#L49-L55](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L49-L55), [README.md#L63-L65](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L63-L65), [README.md#L67-L69](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L67-L69), [README.md#L57-L61](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L57-L61), [README.md#L77-L81](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L77-L81) (`clm_ce81d6370238dce250a3764cda026766875d5677096be78227601e99bcba6f1a`)
- [observation/documented] The extension host's TypeScript source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for RPC, and webViewManager.ts for WebView support. -- evidence: [README.md#L157-L175](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L157-L175) (`clm_3fe1934c00857f8fccca2a2f7f4c49fa92746f5dfcf3c1ca1cf169128bf582b9`)

## design-choices (1 claim(s))

- [observation/documented] Communication between the plugin and extension host uses RPC over Unix Domain Sockets or Named Pipes, per the technology stack description. -- evidence: [README.md#L179-L182](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L179-L182) (`clm_d37e3c623d5b5729a4c01c3c3afcf2a16ce54d2abdb1f861711a2730bca864d9`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors initialize the environment with scripts/setup.sh, build with scripts/build.sh, and run tests with scripts/test.sh; development mode uses npm run dev for the extension host and ./gradlew runIde for the plugin. -- evidence: [CONTRIBUTING.md#L80-L81](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L80-L81), [CONTRIBUTING.md#L89-L90](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L89-L90), [README.md#L130-L130](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L130-L130), [README.md#L144-L146](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L144-L146), [CONTRIBUTING.md#L93-L95](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L93-L95), [README.md#L133-L133](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L133-L133), [README.md#L149-L151](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L149-L151) (`clm_14ccaef5b309de6e4fa5864b849687ba9671328c743ff61ad983da17f32811b9`)
- [observation/documented] Repository development practice: the project follows Conventional Commits (feat, fix, docs, etc.) and a Git Flow-inspired branch strategy with main, develop, feature/*, bugfix/*, hotfix/*, and release/* branches. -- evidence: [CONTRIBUTING.md#L210-L219](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L210-L219), [CONTRIBUTING.md#L200-L200](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L200-L200), [CONTRIBUTING.md#L121-L121](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L121-L121), [CONTRIBUTING.md#L123-L128](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L123-L128) (`clm_00e7ccc40e51b91ddcac71a8cac423d31bf5251c73b1a367056be014cd6f27b1`)
- [observation/documented] Repository development practice: TypeScript code should follow ESLint/Prettier configs with camelCase variables, and Kotlin code should follow Kotlin conventions with ktlint formatting; .editorconfig sets 2-space TS and 4-space Kotlin indentation. -- evidence: [CONTRIBUTING.md#L403-L405](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L403-L405), [CONTRIBUTING.md#L235-L239](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L235-L239), [CONTRIBUTING.md#L304-L308](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L304-L308), [CONTRIBUTING.md#L407-L409](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/CONTRIBUTING.md#L407-L409) (`clm_8b13d67d1f8c5a0207565cdede51eb2aa47b7b5c33e28f7946be11a95de0e550`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The plugin can be installed from the JetBrains Marketplace via Settings/Preferences → Plugins, or from a downloaded .zip via 'Install Plugin from Disk', followed by an IDE restart. -- evidence: [README.md#L89-L94](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L89-L94), [README.md#L104-L109](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L104-L109) (`clm_b4e982a2640e2b82baebac088f99e65e7f198f9c996c9432683d761323b593c4`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running/building the project requires Node.js 18+, a JetBrains IDE 2023.1+, Git, and JDK 17+. -- evidence: [README.md#L117-L120](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L117-L120) (`clm_5c48edafaef4a3ea2044db77e8bc5d12df60e408416eeb92f63e0e00bf10cbdb`)

## limitations (1 claim(s))

- [observation/documented] The README notes that JetBrains IDE version 2023.1 or later is required for optimal compatibility. -- evidence: [README.md#L44-L44](https://github.com/Haleclipse/Codex-JetBrains/blob/e2db6655d78da0f9ec3dd67c155fb30c59037959/README.md#L44-L44) (`clm_c9ccf96dec331fcde3725d4b08ce585abb3951bffefd054e2ee9c0648a26e611`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

