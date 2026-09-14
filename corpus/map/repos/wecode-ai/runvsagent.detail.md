# wecode-ai/runvsagent -- full detail

[Back to orientation](runvsagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wecode-ai/runvsagent/0ffde86ec130cd511d70d2308d697b980ea0e9ca/03f5f487b3c9754f.json](../../../wiki/dossiers/wecode-ai/runvsagent/0ffde86ec130cd511d70d2308d697b980ea0e9ca/03f5f487b3c9754f.json)

## specifications (3 claim(s))

- [observation/documented] RunVSAgent is a cross-platform tool that lets developers run VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. -- evidence: [README.md#L11-L11](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L11-L11), [README.md#L9-L9](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L9-L9) (`clm_bf949f48eb313105470f7a19e477dc133fad8123e74b16f998832ed6932bbd70`)
- [observation/documented] Supported agents listed are Roo Code, Cline, and Kilo Code, with Cline described as able to create/edit files, execute commands, and use the browser with user permission. -- evidence: [README.md#L24-L26](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L24-L26) (`clm_09c45aaf3d1a772bf51cdaf1f747c1f6ea6fe9c1937baf2f4ebf629e0934e2c7`)
- [observation/documented] Supported JetBrains IDEs include IntelliJ IDEA, WebStorm, PyCharm, PhpStorm, RubyMine, CLion, GoLand, DataGrip, Rider, and Android Studio. -- evidence: [README.md#L33-L42](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L33-L42) (`clm_6859bb1535713b4163716b2419b52e1681474eedfda3f5b75b542935c005b743`)

## components (2 claim(s))

- [observation/documented] The architecture comprises a Kotlin JetBrains plugin (UI integration, editor bridge), a Node.js extension host with a VSCode API compatibility layer and agent manager, and the VSCode agents themselves. -- evidence: [README.md#L77-L81](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L77-L81), [README.md#L63-L65](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L63-L65), [README.md#L49-L55](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L49-L55), [README.md#L57-L61](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L57-L61) (`clm_db2ab1d18f439268aca9bbf70c6ee872d1259837e3da2404ab398fc08456d8b2`)
- [observation/documented] The extension host source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for the RPC layer, and webViewManager.ts for WebView support. -- evidence: [README.md#L157-L175](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L157-L175) (`clm_cdcbfae34b72386ba213117d0cf287bc8e0796b7bc21a443edc3d4dfceb056b6`)

## design-choices (1 claim(s))

- [observation/documented] RPC communication runs over Unix Domain Sockets or Named Pipes, per the documented technology stack. -- evidence: [README.md#L179-L182](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L179-L182) (`clm_2947817d82dd5b5cce85b93176f68aca8fbc4d5cfd265c0cbc573d86d80266f0`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors follow a Git Flow-inspired branch strategy (main, develop, feature/*, bugfix/*, hotfix/*, release/*) and Conventional Commits message format. -- evidence: [CONTRIBUTING.md#L123-L128](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L123-L128), [CONTRIBUTING.md#L121-L121](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L121-L121), [CONTRIBUTING.md#L200-L200](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L200-L200) (`clm_e47e6bbdba9fea2453b37c6e96898bac2fb762a2fedf7612c2861ebc69ea2f5e`)
- [observation/documented] Repository development practice: contributors run ./scripts/test.sh (with unit, lint, integration variants), build with ./scripts/build.sh, and submit pull requests with clear descriptions and issue references. -- evidence: [CONTRIBUTING.md#L174-L175](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L174-L175), [CONTRIBUTING.md#L192-L196](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L192-L196), [CONTRIBUTING.md#L166-L166](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L166-L166), [CONTRIBUTING.md#L169-L171](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L169-L171) (`clm_abddc91fab28f8ac15e1415f059df675af9cffab03be4d670d925eaf8d5c73bb`)
- [observation/documented] Repository development practice: TypeScript code should follow ESLint/Prettier configs with camelCase/PascalCase naming, and Kotlin code should follow Kotlin conventions with ktlint formatting. -- evidence: [CONTRIBUTING.md#L304-L308](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L304-L308), [CONTRIBUTING.md#L235-L239](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L235-L239) (`clm_247b457aab99f4b75432b12f06054294ad86c1dd4896227c33b64ab3bde8e3a8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The JetBrains plugin and extension host communicate bidirectionally via RPC, described as high-performance inter-process communication for real-time data exchange. -- evidence: [README.md#L77-L81](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L77-L81), [README.md#L67-L69](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L67-L69) (`clm_8468c6b325b07f2faf74cc6a56bea0320a0b21b2edbf1dbf9a9d20238a80cec5`)
- [observation/documented] The plugin can be installed from the JetBrains Marketplace via Settings/Preferences > Plugins, or from a GitHub Releases .zip via 'Install Plugin from Disk', followed by an IDE restart. -- evidence: [README.md#L87-L87](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L87-L87), [README.md#L89-L94](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L89-L94), [README.md#L104-L109](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L104-L109), [README.md#L102-L102](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L102-L102) (`clm_6c6378ad04d7f703e15e7c2a7749ddcdc4dc905398ca9aecf2d122bd3a6dd050`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running the product requires JetBrains IDE 2023.1 or later for optimal compatibility, and the build prerequisites include Node.js 18+, Git, and JDK 17+. -- evidence: [README.md#L44-L44](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L44-L44), [README.md#L117-L120](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L117-L120) (`clm_b7d402438206cba92193ba59578920f75710a926ed1b0502006c0f91ce05521d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

