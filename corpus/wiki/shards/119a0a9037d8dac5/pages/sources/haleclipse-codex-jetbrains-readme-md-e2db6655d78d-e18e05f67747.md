---
access: public
aliases: []
claim_ids:
- clm_14ccaef5b309de6e4fa5864b849687ba9671328c743ff61ad983da17f32811b9
- clm_3633d7f61e8835fe4fe91d08f02bd59f87c15b38b4321459ee6de6f7381fb702
- clm_3fe1934c00857f8fccca2a2f7f4c49fa92746f5dfcf3c1ca1cf169128bf582b9
- clm_5c48edafaef4a3ea2044db77e8bc5d12df60e408416eeb92f63e0e00bf10cbdb
- clm_871331dfaa31e7413383f270e258bc4acda592dd9e72f18db80e3c9dbe9216d8
- clm_b4e982a2640e2b82baebac088f99e65e7f198f9c996c9432683d761323b593c4
- clm_ba3ba25d7f6c283a3b91fab993e0a81e6e06ea4e92c19fa0311d3abaaf1e77dd
- clm_c9ccf96dec331fcde3725d4b08ce585abb3951bffefd054e2ee9c0648a26e611
- clm_ce81d6370238dce250a3764cda026766875d5677096be78227601e99bcba6f1a
- clm_d37e3c623d5b5729a4c01c3c3afcf2a16ce54d2abdb1f861711a2730bca864d9
maturity: draft
page_id: pg_5d02e83d503c5098b8a0e18e05f67747
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0dce8ec969e75b75a02b79148afa1a00
title: Haleclipse/Codex-JetBrains/README.md @ e2db6655d78d
updated_at: '2026-09-14T01:53:11Z'
---

# Haleclipse/Codex-JetBrains/README.md @ e2db6655d78d

<!-- rcw:begin owner=source:src_0dce8ec969e75b75a02b79148afa1a00 block=evidence -->
- Repository development practice: contributors initialize the environment with scripts/setup.sh, build with scripts/build.sh, and run tests with scripts/test.sh; development mode uses npm run dev for the extension host and ./gradlew runIde for the plugin. [@claim:clm_14ccaef5b309de6e4fa5864b849687ba9671328c743ff61ad983da17f32811b9]
- RunVSAgent is a cross-platform tool that runs VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. [@claim:clm_3633d7f61e8835fe4fe91d08f02bd59f87c15b38b4321459ee6de6f7381fb702]
- The extension host's TypeScript source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for RPC, and webViewManager.ts for WebView support. [@claim:clm_3fe1934c00857f8fccca2a2f7f4c49fa92746f5dfcf3c1ca1cf169128bf582b9]
- Running/building the project requires Node.js 18+, a JetBrains IDE 2023.1+, Git, and JDK 17+. [@claim:clm_5c48edafaef4a3ea2044db77e8bc5d12df60e408416eeb92f63e0e00bf10cbdb]
- Supported JetBrains IDEs include IntelliJ IDEA, WebStorm, PyCharm, PhpStorm, RubyMine, CLion, GoLand, DataGrip, Rider, and Android Studio. [@claim:clm_871331dfaa31e7413383f270e258bc4acda592dd9e72f18db80e3c9dbe9216d8]
- The plugin can be installed from the JetBrains Marketplace via Settings/Preferences → Plugins, or from a downloaded .zip via 'Install Plugin from Disk', followed by an IDE restart. [@claim:clm_b4e982a2640e2b82baebac088f99e65e7f198f9c996c9432683d761323b593c4]
- The project lists Roo Code, Cline, and Kilo Code as supported VSCode-based coding agents. [@claim:clm_ba3ba25d7f6c283a3b91fab993e0a81e6e06ea4e92c19fa0311d3abaaf1e77dd]
- The README notes that JetBrains IDE version 2023.1 or later is required for optimal compatibility. [@claim:clm_c9ccf96dec331fcde3725d4b08ce585abb3951bffefd054e2ee9c0648a26e611]
- The architecture comprises a Kotlin JetBrains plugin (with UI integration and editor bridge), a Node.js extension host providing a VSCode API compatibility layer, and VSCode agents, connected via RPC. [@claim:clm_ce81d6370238dce250a3764cda026766875d5677096be78227601e99bcba6f1a]
- Communication between the plugin and extension host uses RPC over Unix Domain Sockets or Named Pipes, per the technology stack description. [@claim:clm_d37e3c623d5b5729a4c01c3c3afcf2a16ce54d2abdb1f861711a2730bca864d9]
<!-- rcw:end owner=source:src_0dce8ec969e75b75a02b79148afa1a00 block=evidence -->

## Researcher notes

