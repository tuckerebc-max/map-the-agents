# wecode-ai/runvsagent

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0ffde86ec130 @ 03f5f487b3c9754f

## Summary (orientation draft, not independently verified)

RunVSAgent is a cross-platform tool that runs VSCode-based coding agents (Roo Code, Cline, Kilo Code) inside JetBrains IDEs via a Kotlin plugin and a Node.js extension host communicating over RPC. Evidence is mostly README/BUILD/CONTRIBUTING documentation; no agent-behavior evaluation evidence is present. Evidence coverage: 195 of 320 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] RunVSAgent is a cross-platform tool that lets developers run VSCode-based coding agents and extensions inside JetBrains IDEs such as IntelliJ IDEA, WebStorm, and PyCharm. -- evidence: [README.md#L11-L11](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L11-L11), [README.md#L9-L9](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L9-L9)
  - [observation/documented] Supported agents listed are Roo Code, Cline, and Kilo Code, with Cline described as able to create/edit files, execute commands, and use the browser with user permission. -- evidence: [README.md#L24-L26](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L24-L26)
- components (2 claim(s)):
  - [observation/documented] The architecture comprises a Kotlin JetBrains plugin (UI integration, editor bridge), a Node.js extension host with a VSCode API compatibility layer and agent manager, and the VSCode agents themselves. -- evidence: [README.md#L77-L81](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L77-L81), [README.md#L63-L65](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L63-L65), [README.md#L49-L55](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L49-L55), [README.md#L57-L61](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L57-L61)
  - [observation/documented] The extension host source includes main.ts, extensionManager.ts for extension lifecycle, rpcManager.ts for the RPC layer, and webViewManager.ts for WebView support. -- evidence: [README.md#L157-L175](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L157-L175)
- design-choices (1 claim(s)):
  - [observation/documented] RPC communication runs over Unix Domain Sockets or Named Pipes, per the documented technology stack. -- evidence: [README.md#L179-L182](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L179-L182)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors follow a Git Flow-inspired branch strategy (main, develop, feature/*, bugfix/*, hotfix/*, release/*) and Conventional Commits message format. -- evidence: [CONTRIBUTING.md#L123-L128](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L123-L128), [CONTRIBUTING.md#L121-L121](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L121-L121), [CONTRIBUTING.md#L200-L200](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L200-L200)
  - [observation/documented] Repository development practice: contributors run ./scripts/test.sh (with unit, lint, integration variants), build with ./scripts/build.sh, and submit pull requests with clear descriptions and issue references. -- evidence: [CONTRIBUTING.md#L174-L175](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L174-L175), [CONTRIBUTING.md#L192-L196](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L192-L196), [CONTRIBUTING.md#L166-L166](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L166-L166), [CONTRIBUTING.md#L169-L171](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/CONTRIBUTING.md#L169-L171)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The JetBrains plugin and extension host communicate bidirectionally via RPC, described as high-performance inter-process communication for real-time data exchange. -- evidence: [README.md#L77-L81](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L77-L81), [README.md#L67-L69](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L67-L69)
  - [observation/documented] The plugin can be installed from the JetBrains Marketplace via Settings/Preferences > Plugins, or from a GitHub Releases .zip via 'Install Plugin from Disk', followed by an IDE restart. -- evidence: [README.md#L87-L87](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L87-L87), [README.md#L89-L94](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L89-L94), [README.md#L104-L109](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L104-L109), [README.md#L102-L102](https://github.com/wecode-ai/RunVSAgent/blob/0ffde86ec130cd511d70d2308d697b980ea0e9ca/README.md#L102-L102)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](runvsagent.detail.md)

Metadata and full claim list: [full detail](runvsagent.detail.md)
Human notes ([notes](runvsagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
